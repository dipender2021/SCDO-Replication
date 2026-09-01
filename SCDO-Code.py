from pathlib import Path
from typing import Optional, Sequence

import math
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset


@dataclass
class SCDOConfig:
    p_mean: float
    p_std: float
    m0: int
    alpha: float
    delta_c: float
    sigma_struct: float
    delta: float
    hidden_dim: int = 256
    noise_embed_dim: int = 128
    layers: int = 6
    heads: int = 8
    dropout: float = 0.1
    ff_mult: int = 4
    epochs: int = 400
    batch_size: int = 256
    learning_rate: float = 2e-4
    weight_decay: float = 1e-4
    grad_clip: float = 1.0
    p_sc: float = 0.5
    p_drop: float = 0.15
    cfg_scale: float = 2.0
    steps: int = 40
    sigma_min: float = 0.002
    sigma_max: float = 80.0
    rho_s: float = 7.0
    sigma_data: float = 1.0
    lambda_cov: float = 0.05
    lambda_corr: float = 0.05
    lambda_swd: float = 0.02
    swd_projections: int = 32


class SinusoidalEmbedding(nn.Module):
    def __init__(self, dim: int):
        super().__init__()
        self.dim = dim

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        half = self.dim // 2
        if half == 0:
            return x.unsqueeze(-1)
        freq = torch.exp(
            -math.log(10000.0)
            * torch.arange(half, device=x.device, dtype=x.dtype)
            / max(half - 1, 1)
        )
        phase = x.unsqueeze(-1) * freq.unsqueeze(0)
        emb = torch.cat([phase.sin(), phase.cos()], dim=-1)
        if self.dim % 2:
            emb = torch.cat([emb, torch.zeros_like(emb[:, :1])], dim=-1)
        return emb


class AdaptiveTransformerBlock(nn.Module):
    def __init__(self, hidden_dim: int, heads: int, dropout: float, ff_mult: int):
        super().__init__()
        self.norm1 = nn.LayerNorm(hidden_dim)
        self.norm2 = nn.LayerNorm(hidden_dim)
        self.adapt = nn.Linear(hidden_dim, 4 * hidden_dim)
        self.attn = nn.MultiheadAttention(
            hidden_dim,
            heads,
            dropout=dropout,
            batch_first=True,
        )
        self.ff = nn.Sequential(
            nn.Linear(hidden_dim, ff_mult * hidden_dim),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(ff_mult * hidden_dim, hidden_dim),
            nn.Dropout(dropout),
        )

    def forward(self, x: torch.Tensor, cond: torch.Tensor) -> torch.Tensor:
        g1, b1, g2, b2 = self.adapt(cond).chunk(4, dim=-1)
        h = self.norm1(x)
        h = h * (1.0 + g1.unsqueeze(1)) + b1.unsqueeze(1)
        h, _ = self.attn(h, h, h, need_weights=False)
        x = x + h
        h = self.norm2(x)
        h = h * (1.0 + g2.unsqueeze(1)) + b2.unsqueeze(1)
        return x + self.ff(h)


class FeatureTokenDenoiser(nn.Module):
    def __init__(self, n_features: int, cfg: SCDOConfig):
        super().__init__()
        self.n_features = n_features
        self.cfg = cfg
        h = cfg.hidden_dim
        self.token_proj = nn.Linear(2, h)
        self.feature_embed = nn.Parameter(torch.randn(n_features, h) * 0.02)
        self.global_token = nn.Parameter(torch.randn(1, 1, h) * 0.02)
        self.noise_fourier = SinusoidalEmbedding(cfg.noise_embed_dim)
        self.noise_mlp = nn.Sequential(
            nn.Linear(cfg.noise_embed_dim, h),
            nn.SiLU(),
            nn.Linear(h, h),
        )
        self.label_embed = nn.Embedding(3, h)
        self.blocks = nn.ModuleList(
            [
                AdaptiveTransformerBlock(
                    h,
                    cfg.heads,
                    cfg.dropout,
                    cfg.ff_mult,
                )
                for _ in range(cfg.layers)
            ]
        )
        self.out_norm = nn.LayerNorm(h)
        self.out = nn.Linear(h, 1)

    def forward(
        self,
        r_sigma: torch.Tensor,
        sigma: torch.Tensor,
        label: torch.Tensor,
        self_cond: torch.Tensor,
    ) -> torch.Tensor:
        local = torch.stack([r_sigma, self_cond], dim=-1)
        local = self.token_proj(local) + self.feature_embed.unsqueeze(0)
        global_token = self.global_token.expand(r_sigma.shape[0], -1, -1)
        x = torch.cat([global_token, local], dim=1)
        c_noise = 0.25 * sigma.clamp_min(1e-12).log()
        cond = self.noise_mlp(self.noise_fourier(c_noise)) + self.label_embed(label)
        for block in self.blocks:
            x = block(x, cond)
        x = self.out_norm(x[:, 1:])
        return self.out(x).squeeze(-1)


class SCDO(nn.Module):
    def __init__(
        self,
        config: SCDOConfig,
        count_indices: Optional[Sequence[int]] = None,
        device: Optional[str] = None,
    ):
        super().__init__()
        self.cfg = config
        self.count_indices = tuple(count_indices or ())
        self.device_name = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.net: Optional[FeatureTokenDenoiser] = None
        self.mu: Optional[torch.Tensor] = None
        self.scale: Optional[torch.Tensor] = None
        self.lower: Optional[torch.Tensor] = None
        self.upper: Optional[torch.Tensor] = None
        self.cov_ref: Optional[torch.Tensor] = None
        self.corr_ref: Optional[torch.Tensor] = None
        self.x_pos: Optional[torch.Tensor] = None

    @property
    def device(self) -> torch.device:
        return torch.device(self.device_name)

    def _validate_config(self) -> None:
        c = self.cfg
        if c.m0 < 2:
            raise ValueError("m0 must be at least 2.")
        if not 0.0 < c.alpha < 1.0:
            raise ValueError("alpha must be in (0, 1).")
        if c.delta_c <= 0.0 or c.delta <= 0.0:
            raise ValueError("delta_c and delta must be positive.")
        if c.sigma_struct <= 0.0:
            raise ValueError("sigma_struct must be positive.")
        if c.sigma_min <= 0.0 or c.sigma_max <= c.sigma_min:
            raise ValueError("Invalid sampling noise range.")
        if c.steps < 2:
            raise ValueError("steps must be at least 2.")
        if c.hidden_dim % c.heads != 0:
            raise ValueError("hidden_dim must be divisible by heads.")

    def _standardize(self, x: torch.Tensor) -> torch.Tensor:
        return (x - self.mu) / (self.scale + self.cfg.delta)

    def _inverse(self, x: torch.Tensor) -> torch.Tensor:
        return x * (self.scale + self.cfg.delta) + self.mu

    def _covariance(self, x: torch.Tensor) -> torch.Tensor:
        centered = x - x.mean(dim=0, keepdim=True)
        return centered.T @ centered / (x.shape[0] - 1)

    def _shrunk_covariance(self, x: torch.Tensor) -> torch.Tensor:
        cov = self._covariance(x)
        diag = torch.diag(torch.diag(cov))
        eye = torch.eye(cov.shape[0], device=x.device, dtype=x.dtype)
        return (
            (1.0 - self.cfg.alpha) * cov
            + self.cfg.alpha * diag
            + self.cfg.delta_c * eye
        )

    def _shrunk_correlation(self, x: torch.Tensor) -> torch.Tensor:
        cov = self._shrunk_covariance(x)
        inv_std = torch.diag(cov).clamp_min(self.cfg.delta_c).rsqrt()
        return inv_std[:, None] * cov * inv_std[None, :]

    def _edm_coefficients(self, sigma: torch.Tensor):
        sd = self.cfg.sigma_data
        denom = torch.sqrt(sigma.square() + sd * sd)
        c_in = 1.0 / denom
        c_skip = (sd * sd) / (sigma.square() + sd * sd)
        c_out = sigma * sd / denom
        return c_in, c_skip, c_out

    def denoise(
        self,
        x_noisy: torch.Tensor,
        sigma: torch.Tensor,
        label: torch.Tensor,
        self_cond: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        if self.net is None:
            raise RuntimeError("SCDO is not initialized.")
        if sigma.ndim == 0:
            sigma = sigma.expand(x_noisy.shape[0])
        if sigma.ndim == 1:
            sigma_col = sigma[:, None]
        else:
            sigma_col = sigma
            sigma = sigma_col[:, 0]
        if self_cond is None:
            self_cond = torch.zeros_like(x_noisy)
        c_in, c_skip, c_out = self._edm_coefficients(sigma_col)
        residual = self.net(c_in * x_noisy, sigma, label, self_cond)
        return c_skip * x_noisy + c_out * residual

    def _effective_labels(self, y: torch.Tensor) -> torch.Tensor:
        labels = y.long().clone()
        drop = torch.rand(labels.shape[0], device=labels.device) < self.cfg.p_drop
        labels[drop] = 2
        return labels

    def _reconstruct(
        self,
        x_noisy: torch.Tensor,
        sigma: torch.Tensor,
        label: torch.Tensor,
        allow_self_conditioning: bool = True,
    ) -> torch.Tensor:
        if allow_self_conditioning and torch.rand((), device=x_noisy.device) < self.cfg.p_sc:
            with torch.no_grad():
                provisional = self.denoise(
                    x_noisy,
                    sigma,
                    label,
                    torch.zeros_like(x_noisy),
                )
            return self.denoise(x_noisy, sigma, label, provisional.detach())
        return self.denoise(
            x_noisy,
            sigma,
            label,
            torch.zeros_like(x_noisy),
        )

    def _sample_training_sigma(self, n: int) -> torch.Tensor:
        z = torch.randn(n, device=self.device)
        return torch.exp(self.cfg.p_mean + self.cfg.p_std * z)

    def _sample_structural_sigma(self) -> torch.Tensor:
        threshold = math.log(self.cfg.sigma_struct)
        while True:
            z = torch.randn((), device=self.device)
            log_sigma = self.cfg.p_mean + self.cfg.p_std * z
            if log_sigma <= threshold:
                return log_sigma.exp()

    def _edm_loss(
        self,
        clean: torch.Tensor,
        noisy: torch.Tensor,
        sigma: torch.Tensor,
        labels: torch.Tensor,
    ) -> torch.Tensor:
        recon = self._reconstruct(noisy, sigma, labels, True)
        sd = self.cfg.sigma_data
        weight = (sigma.square() + sd * sd) / (sigma * sd).square()
        per_sample = (recon - clean).square().sum(dim=1)
        return (weight * per_sample).mean() / clean.shape[1]

    def _structural_losses(self):
        if self.x_pos is None or self.x_pos.shape[0] < 2:
            zero = torch.zeros((), device=self.device)
            return zero, zero, zero
        m_s = min(self.cfg.m0, self.x_pos.shape[0])
        idx = torch.randperm(self.x_pos.shape[0], device=self.device)[:m_s]
        clean = self.x_pos[idx]
        sigma_s = self._sample_structural_sigma()
        noisy = clean + sigma_s * torch.randn_like(clean)
        labels = torch.ones(m_s, dtype=torch.long, device=self.device)
        sigma = sigma_s.expand(m_s)
        recon = self._reconstruct(noisy, sigma, labels, True)
        cov_hat = self._shrunk_covariance(recon)
        corr_hat = self._shrunk_correlation(recon)
        d = clean.shape[1]
        cov_loss = torch.linalg.matrix_norm(cov_hat - self.cov_ref, ord="fro") / d
        mask = torch.ones((d, d), device=self.device, dtype=clean.dtype)
        mask.fill_diagonal_(0.0)
        corr_loss = (
            torch.linalg.matrix_norm(
                mask * (corr_hat - self.corr_ref),
                ord="fro",
            )
            / math.sqrt(d * (d - 1))
        )
        directions = torch.randn(
            d,
            self.cfg.swd_projections,
            device=self.device,
            dtype=clean.dtype,
        )
        directions = directions / directions.norm(dim=0, keepdim=True).clamp_min(1e-12)
        proj_clean = clean @ directions
        proj_recon = recon @ directions
        swd_loss = (
            proj_clean.sort(dim=0).values - proj_recon.sort(dim=0).values
        ).abs().mean()
        return cov_loss, corr_loss, swd_loss

    def fit(self, x, y):
        self._validate_config()
        x = torch.as_tensor(x, dtype=torch.float32)
        y = torch.as_tensor(y, dtype=torch.long)
        if x.ndim != 2:
            raise ValueError("x must be a 2D feature matrix.")
        if y.ndim != 1 or y.shape[0] != x.shape[0]:
            raise ValueError("y must be a 1D label vector aligned with x.")
        if not torch.all((y == 0) | (y == 1)):
            raise ValueError("y must contain binary labels 0 and 1.")
        if (y == 1).sum() == 0:
            raise ValueError("At least one defective sample is required.")
        self.mu = x.mean(dim=0).to(self.device)
        self.scale = x.std(dim=0, unbiased=False).to(self.device)
        self.lower = x.min(dim=0).values.to(self.device)
        self.upper = x.max(dim=0).values.to(self.device)
        x_std = self._standardize(x.to(self.device))
        y_dev = y.to(self.device)
        self.x_pos = x_std[y_dev == 1]
        if self.x_pos.shape[0] >= 2:
            self.cov_ref = self._shrunk_covariance(self.x_pos).detach()
            self.corr_ref = self._shrunk_correlation(self.x_pos).detach()
        self.net = FeatureTokenDenoiser(x.shape[1], self.cfg).to(self.device)
        optimizer = torch.optim.AdamW(
            self.net.parameters(),
            lr=self.cfg.learning_rate,
            weight_decay=self.cfg.weight_decay,
        )
        loader = DataLoader(
            TensorDataset(x_std.detach().cpu(), y.cpu()),
            batch_size=self.cfg.batch_size,
            shuffle=True,
            drop_last=False,
        )
        self.train()
        for _ in range(self.cfg.epochs):
            for xb, yb in loader:
                xb = xb.to(self.device)
                yb = yb.to(self.device)
                sigma = self._sample_training_sigma(xb.shape[0])
                noisy = xb + sigma[:, None] * torch.randn_like(xb)
                labels = self._effective_labels(yb)
                edm = self._edm_loss(xb, noisy, sigma, labels)
                cov, corr, swd = self._structural_losses()
                loss = (
                    edm
                    + self.cfg.lambda_cov * cov
                    + self.cfg.lambda_corr * corr
                    + self.cfg.lambda_swd * swd
                )
                optimizer.zero_grad(set_to_none=True)
                loss.backward()
                torch.nn.utils.clip_grad_norm_(
                    self.net.parameters(),
                    self.cfg.grad_clip,
                )
                optimizer.step()
        return self

    def _schedule(self) -> torch.Tensor:
        i = torch.arange(self.cfg.steps, device=self.device, dtype=torch.float32)
        inv_rho = 1.0 / self.cfg.rho_s
        sigmas = (
            self.cfg.sigma_max ** inv_rho
            + i / (self.cfg.steps - 1)
            * (
                self.cfg.sigma_min ** inv_rho
                - self.cfg.sigma_max ** inv_rho
            )
        ) ** self.cfg.rho_s
        return torch.cat([sigmas, torch.zeros(1, device=self.device)])

    def _guided_denoise(
        self,
        x: torch.Tensor,
        sigma: torch.Tensor,
        self_cond: torch.Tensor,
    ) -> torch.Tensor:
        n = x.shape[0]
        sigma_batch = sigma.expand(n)
        cond_label = torch.ones(n, dtype=torch.long, device=self.device)
        null_label = torch.full((n,), 2, dtype=torch.long, device=self.device)
        cond = self.denoise(x, sigma_batch, cond_label, self_cond)
        uncond = self.denoise(x, sigma_batch, null_label, self_cond)
        return uncond + self.cfg.cfg_scale * (cond - uncond)

    @torch.no_grad()
    def sample(self, n: int, batch_size: Optional[int] = None) -> np.ndarray:
        if self.net is None or self.mu is None:
            raise RuntimeError("Call fit before sample.")
        if n <= 0:
            return np.empty((0, self.mu.shape[0]), dtype=np.float32)
        batch_size = batch_size or self.cfg.batch_size
        self.eval()
        sigmas = self._schedule()
        generated = []
        remaining = n
        while remaining > 0:
            b = min(batch_size, remaining)
            x = torch.randn(
                b,
                self.mu.shape[0],
                device=self.device,
            ) * self.cfg.sigma_max
            self_cond = torch.zeros_like(x)
            for t in range(self.cfg.steps):
                sigma = sigmas[t]
                sigma_next = sigmas[t + 1]
                clean = self._guided_denoise(x, sigma, self_cond)
                velocity = (x - clean) / sigma
                dt = sigma_next - sigma
                proposal = x + dt * velocity
                if sigma_next > 0:
                    clean_next = self._guided_denoise(
                        proposal,
                        sigma_next,
                        self_cond,
                    )
                    velocity_next = (proposal - clean_next) / sigma_next
                    x = x + 0.5 * dt * (velocity + velocity_next)
                    self_cond = clean_next
                else:
                    x = proposal
            x = self._inverse(x)
            x = torch.maximum(torch.minimum(x, self.upper), self.lower)
            if self.count_indices:
                idx = torch.as_tensor(
                    self.count_indices,
                    device=self.device,
                    dtype=torch.long,
                )
                x[:, idx] = x[:, idx].round()
            generated.append(x.cpu())
            remaining -= b
        return torch.cat(generated, dim=0).numpy()

    def fit_resample(self, x, y):
        x_np = np.asarray(x, dtype=np.float32)
        y_np = np.asarray(y, dtype=np.int64)
        n_pos = int((y_np == 1).sum())
        n_neg = int((y_np == 0).sum())
        self.fit(x_np, y_np)
        n_syn = max(0, n_neg - n_pos)
        if n_syn == 0:
            return x_np.copy(), y_np.copy()
        x_syn = self.sample(n_syn)
        y_syn = np.ones(n_syn, dtype=np.int64)
        return (
            np.concatenate([x_np, x_syn], axis=0),
            np.concatenate([y_np, y_syn], axis=0),
        )

