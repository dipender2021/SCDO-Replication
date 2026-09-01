# SCDO

Structure-Constrained Diffusion Oversampling for Imbalanced Software Defect Prediction

## Overview

This repository provides the replication package for our work on **Structure-Constrained Diffusion Oversampling (SCDO)** for imbalanced software defect prediction.

Software defect datasets are often highly imbalanced, with defective modules forming only a small fraction of the available training data. Existing oversampling methods can increase minority-class representation, but they may not adequately preserve the statistical relationships among software metrics observed in real defective modules. SCDO addresses this problem by combining class-conditional diffusion-based generation with explicit minority-structure preservation.

SCDO is designed to:
- generate synthetic defective samples through class-conditional diffusion,
- model cross-metric interactions using a feature-token Transformer denoiser,
- preserve defective-class covariance and correlation structure,
- align projected multivariate distributions using sliced-Wasserstein regularization,
- support both within-project defect prediction (WPDP) and cross-project defect prediction (CPDP).

This repository contains the implementation, experiment configurations, datasets, evaluation scripts, and results required to reproduce the experiments reported in the paper.


# Details of the Datasets
1. Yatish, S., Jiarpakdee, J., Thongtanunam, P., & Tantithamthavorn, C. (2019). Mining software defects: Should we consider affected releases? In: 2019 IEEE/ACM 41st International Conference on Software Engineering (ICSE), pp. 654–665. IEEE.

2. Menzies, T., Krishna, R., & Pryor, D. (2015). The PROMISE repository of empirical software engineering data. Available at: http://promisedata.googlecode.com

# Metrics Details of JIRA 
| **Abbreviation**          | **Description**                                                            |
| ------------------------- | -------------------------------------------------------------------------- |
| AvgCyclomatic             | Average cyclomatic complexity for all nested functions or methods          |
| SumCyclomatic             | Sum of cyclomatic complexity of all nested functions or methods            |
| AvgCyclomaticModified     | Average modified cyclomatic complexity for all nested functions or methods |
| SumCyclomaticModified     | Sum of modified cyclomatic complexity of all nested functions              |
| AvgCyclomaticStrict       | Average strict cyclomatic complexity for all nested functions or methods   |
| SumCyclomaticStrict       | Sum of strict cyclomatic complexity of all nested functions or methods     |
| AvgEssential              | Average essential complexity for all nested functions or methods           |
| SumEssential              | Sum of essential complexity of all nested functions or methods             |
| AvgLine                   | Average number of lines for all nested functions or methods                |
| AvgLineBlank              | Average number of blank lines for all nested functions or methods          |
| AvgLineCode               | Average number of lines containing source code for all nested functions    |
| AvgLineComment            | Average number of comment lines for all nested functions or methods        |
| CountClassBase            | Number of immediate base classes                                           |
| CountClassCoupled         | Number of other classes coupled to                                         |
| CountClassDerived         | Number of immediate subclasses                                             |
| MaxInheritanceTree        | Maximum depth of class in inheritance tree                                 |
| PercentLackOfCohesion     | 100% minus the average cohesion for package entities                       |
| CountDeclClass            | Number of classes                                                          |
| CountDeclClassMethod      | Number of class methods                                                    |
| CountDeclClassVariable    | Number of class variables                                                  |
| CountDeclFunction         | Number of functions                                                        |
| CountDeclInstanceMethod   | Number of instance methods                                                 |
| CountDeclInstanceVariable | Number of instance variables                                               |
| CountDeclMethod           | Number of local (non-inherited) methods                                    |
| CountDeclMethodDefault    | Number of local default methods                                            |
| CountDeclMethodPrivate    | Number of local (non-inherited) private methods                            |
| CountDeclMethodProtected  | Number of local protected methods                                          |
| CountDeclMethodPublic     | Number of local (non-inherited) public methods                             |
| CountLine                 | Number of physical lines                                                   |
| CountLineBlank            | Number of blank lines                                                      |
| CountLineCode             | Number of lines containing source code                                     |
| CountLineCodeDecl         | Number of lines containing declarative source code                         |
| CountLineCodeExe          | Number of lines containing executable source code                          |
| CountLineComment          | Number of lines containing comment                                         |
| CountSemicolon            | Number of semicolons                                                       |
| CountStmt                 | Number of statements                                                       |
| CountStmtDecl             | Number of declarative statements                                           |
| CountStmtExe              | Number of executable statements                                            |
| MaxCyclomatic             | Maximum cyclomatic complexity of all nested functions or methods           |
| MaxCyclomaticModified     | Maximum modified cyclomatic complexity of nested functions or methods      |
| MaxCyclomaticStrict       | Maximum strict cyclomatic complexity of nested functions or methods        |
| RatioCommentToCode        | Ratio of comment lines to code lines                                       |
| CountInput\_Min           | Min number of calling subprograms plus global variables read               |
| CountInput\_Mean          | Mean number of calling subprograms plus global variables read              |
| CountInput\_Max           | Max number of calling subprograms plus global variables read               |
| CountOutput\_Min          | Min number of called subprograms plus global variables set                 |
| CountOutput\_Mean         | Mean number of called subprograms plus global variables set                |
| CountOutput\_Max          | Max number of called subprograms plus global variables set                 |
| CountPath\_Min            | Min number of unique paths through a body of code                          |
| CountPath\_Mean           | Mean number of unique paths through a body of code                         |
| CountPath\_Max            | Max number of unique paths through a body of code                          |
| MaxNesting\_Min           | Min of maximum nesting level of control constructs in the function         |
| MaxNesting\_Mean          | Mean of maximum nesting level of control constructs in the function        |
| MaxNesting\_Max           | Max of maximum nesting level of control constructs in the function         |
| COMM                      | Number of Git commits                                                      |
| ADDED\_LINES              | Normalized number of lines added to the module                             |
| DEL\_LINES                | Normalized number of lines deleted from the module                         |
| ADEV                      | Number of active developers                                                |
| DDEV                      | Number of distinct developers                                              |
| MINOR\_COMMIT             | Developers contributing <5% of total code changes                          |
| MINOR\_LINE               | Developers contributing <5% of total LOC                                   |
| MAJOR\_COMMIT             | Developers contributing >5% of total code changes                          |
| MAJOR\_LINES              | Developers contributing >5% of total LOC                                   |
| OWN\_COMMIT               | Proportion of code changes by top contributor                              |
| OWN\_LINE                 | Proportion of lines of code by top contributor                             |

# Metrics Details of PROMISE
| **Abbreviation** | **Description** |
|------------------|-----------------|
| WMC              | Weighted Methods per Class |
| DIT              | Depth of Inheritance Tree |
| NOC              | Number of Children |
| CBO              | Coupling Between Object Classes |
| RFC              | Response for a Class |
| LCOM             | Lack of Cohesion in Methods |
| CA               | Afferent Couplings |
| CE               | Efferent Couplings |
| NPM              | Number of Public Methods |
| LCOM3            | Lack of Cohesion in Methods (variant of LCOM) |
| LOC              | Lines of Code |
| DAM              | Data Access Metric |
| MOA              | Measure of Aggregation |
| MFA              | Measure of Functional Abstraction |
| CAM              | Cohesion Among Methods of a Class |
| IC               | Inheritance Coupling |
| CBM              | Coupling Between Methods |
| AMC              | Average Method Complexity |
| CC               | McCabe’s Cyclomatic Complexity |
| MAX_CC           | Maximum Value of CC Among Methods in the Class |
| AVG_CC           | Average (Arithmetic Mean) CC of Methods in the Class |


## RQ1: Project-Level F1 Results for WPDP

The following tables report the complete project-level F1-score results for
the five WPDP frameworks. The **Average** row corresponds to the mean across
the 11 evaluated projects.

### CGCN

| Project | Default | SMOTE | SMOTE-ENN | CTGAN | CTAB-GAN+ | TabDDPM | TabSyn | SCDO |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|
| Activemq-5.3.0 | 0.41 | 0.41 | 0.41 | 0.43 | 0.42 | 0.37 | 0.39 | **0.46** |
| Camel-2.11.0 | 0.24 | 0.24 | 0.29 | 0.15 | 0.14 | 0.14 | 0.14 | 0.19 |
| Derby-10.3.1.4 | 0.61 | 0.61 | 0.64 | 0.64 | 0.65 | 0.65 | 0.65 | **0.69** |
| Hbase-0.95.0 | 0.57 | 0.57 | 0.56 | 0.57 | 0.59 | 0.55 | 0.56 | **0.61** |
| Hive-0.12.0 | 0.46 | 0.46 | 0.39 | 0.34 | 0.34 | 0.32 | 0.32 | 0.34 |
| Lucene-3.1 | 0.11 | 0.11 | **0.23** | 0.14 | 0.14 | 0.17 | 0.08 | 0.18 |
| Ant-1.7 | 0.56 | 0.56 | 0.56 | 0.61 | 0.60 | 0.55 | 0.55 | **0.64** |
| Jedit-4.2 | 0.40 | 0.40 | 0.44 | 0.45 | 0.44 | 0.40 | 0.35 | **0.51** |
| Prop-4 | 0.33 | 0.33 | **0.37** | 0.29 | 0.29 | 0.30 | 0.29 | 0.34 |
| Xalan-2.6 | 0.62 | 0.62 | 0.61 | 0.68 | 0.67 | 0.67 | 0.67 | **0.74** |
| Xerces-1.3 | 0.51 | 0.51 | 0.46 | 0.48 | 0.49 | 0.47 | 0.48 | **0.55** |
| **Average** | **0.44** | **0.44** | **0.45** | **0.44** | **0.44** | **0.42** | **0.41** | **0.48** |

### TCLP

| Project | Default | SMOTE | SMOTE-ENN | CTGAN | CTAB-GAN+ | TabDDPM | TabSyn | SCDO |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|
| Activemq-5.3.0 | 0.37 | 0.37 | 0.37 | 0.37 | 0.38 | 0.36 | 0.39 | **0.40** |
| Camel-2.11.0 | 0.09 | 0.09 | 0.15 | 0.15 | 0.16 | 0.15 | **0.18** | 0.17 |
| Derby-10.3.1.4 | 0.43 | 0.43 | 0.43 | 0.42 | 0.43 | 0.45 | 0.44 | **0.46** |
| Hbase-0.95.0 | 0.31 | 0.31 | 0.32 | 0.30 | 0.31 | 0.33 | 0.32 | **0.37** |
| Hive-0.12.0 | 0.04 | 0.04 | **0.08** | 0.04 | 0.04 | 0.05 | 0.06 | 0.06 |
| Lucene-3.1 | 0.18 | 0.18 | 0.18 | 0.17 | 0.17 | 0.14 | 0.16 | **0.20** |
| Ant-1.7 | 0.35 | 0.35 | 0.39 | 0.38 | 0.39 | **0.52** | 0.50 | 0.47 |
| Jedit-4.2 | 0.40 | 0.40 | 0.44 | 0.44 | 0.45 | 0.46 | 0.51 | **0.53** |
| Prop-4 | 0.11 | 0.11 | **0.21** | 0.13 | 0.13 | 0.17 | 0.17 | 0.20 |
| Xalan-2.6 | 0.06 | 0.06 | 0.20 | 0.08 | 0.08 | **0.22** | 0.16 | 0.17 |
| Xerces-1.3 | 0.32 | 0.32 | 0.33 | 0.32 | 0.33 | 0.38 | 0.32 | **0.39** |
| **Average** | **0.24** | **0.24** | **0.28** | **0.25** | **0.26** | **0.29** | **0.29** | **0.31** |

### ME-SFP

| Project | Default | SMOTE | SMOTE-ENN | CTGAN | CTAB-GAN+ | TabDDPM | TabSyn | SCDO |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|
| Activemq-5.3.0 | 0.33 | 0.33 | **0.36** | 0.35 | 0.35 | **0.36** | **0.36** | **0.36** |
| Camel-2.11.0 | 0.19 | 0.19 | 0.16 | 0.19 | 0.20 | 0.24 | 0.24 | **0.27** |
| Derby-10.3.1.4 | 0.56 | 0.56 | 0.61 | 0.55 | 0.56 | 0.59 | 0.57 | **0.63** |
| Hbase-0.95.0 | 0.51 | 0.51 | 0.54 | 0.47 | 0.48 | 0.48 | 0.46 | **0.56** |
| Hive-0.12.0 | 0.35 | 0.35 | 0.33 | 0.32 | 0.33 | 0.34 | **0.37** | **0.37** |
| Lucene-3.1 | 0.18 | 0.18 | 0.17 | 0.15 | 0.16 | 0.17 | 0.16 | **0.23** |
| Ant-1.7 | 0.45 | 0.45 | 0.53 | 0.49 | 0.50 | 0.46 | 0.49 | **0.56** |
| Jedit-4.2 | 0.27 | 0.27 | 0.31 | 0.37 | 0.38 | 0.46 | 0.35 | **0.47** |
| Prop-4 | **0.34** | **0.34** | **0.36** | 0.31 | 0.32 | 0.33 | 0.32 | 0.34 |
| Xalan-2.6 | 0.63 | 0.63 | 0.57 | 0.60 | 0.62 | **0.64** | 0.62 | **0.64** |
| Xerces-1.3 | 0.40 | 0.40 | 0.43 | 0.43 | 0.44 | 0.43 | **0.49** | 0.48 |
| **Average** | **0.38** | **0.38** | **0.40** | **0.38** | **0.39** | **0.41** | **0.40** | **0.45** |

### SS-WDRN

| Project | Default | SMOTE | SMOTE-ENN | CTGAN | CTAB-GAN+ | TabDDPM | TabSyn | SCDO |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|
| Activemq-5.3.0 | 0.34 | 0.24 | 0.33 | 0.34 | 0.29 | 0.20 | 0.30 | **0.49** |
| Camel-2.11.0 | 0.06 | 0.01 | 0.01 | 0.06 | 0.07 | 0.15 | **0.18** | **0.18** |
| Derby-10.3.1.4 | 0.57 | 0.57 | 0.55 | 0.55 | **0.59** | 0.42 | 0.44 | 0.47 |
| Hbase-0.95.0 | 0.48 | **0.51** | 0.47 | 0.48 | 0.50 | 0.30 | 0.32 | 0.39 |
| Hive-0.12.0 | 0.24 | **0.39** | 0.30 | 0.25 | 0.25 | 0.04 | 0.06 | 0.07 |
| Lucene-3.1 | 0.00 | 0.08 | 0.14 | 0.05 | 0.09 | 0.17 | 0.16 | **0.21** |
| Ant-1.7 | 0.47 | 0.49 | 0.47 | 0.52 | **0.54** | 0.38 | 0.50 | 0.49 |
| Jedit-4.2 | 0.27 | 0.36 | 0.35 | 0.36 | 0.39 | 0.44 | 0.51 | **0.54** |
| Prop-4 | 0.21 | 0.27 | **0.28** | 0.20 | 0.23 | 0.13 | 0.17 | 0.21 |
| Xalan-2.6 | 0.59 | 0.58 | 0.52 | 0.59 | **0.61** | 0.08 | 0.16 | 0.18 |
| Xerces-1.3 | 0.40 | **0.44** | 0.37 | 0.39 | 0.43 | 0.32 | 0.32 | 0.40 |
| **Average** | **0.33** | **0.35** | **0.34** | **0.34** | **0.36** | **0.24** | **0.28** | **0.33** |

### MA

| Project | Default | SMOTE | SMOTE-ENN | CTGAN | CTAB-GAN+ | TabDDPM | TabSyn | SCDO |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|
| Activemq-5.3.0 | 0.36 | 0.39 | 0.41 | **0.44** | 0.38 | 0.41 | 0.40 | 0.43 |
| Camel-2.11.0 | 0.19 | **0.32** | 0.29 | 0.30 | 0.21 | 0.25 | 0.18 | 0.28 |
| Derby-10.3.1.4 | 0.65 | 0.62 | 0.61 | 0.61 | 0.66 | 0.65 | 0.65 | **0.69** |
| Hbase-0.95.0 | 0.57 | 0.55 | 0.54 | 0.58 | 0.58 | 0.57 | 0.57 | **0.60** |
| Hive-0.12.0 | 0.34 | **0.40** | 0.35 | 0.38 | 0.31 | 0.34 | 0.34 | **0.40** |
| Lucene-3.1 | 0.06 | 0.18 | 0.18 | **0.20** | 0.14 | 0.11 | 0.13 | 0.12 |
| Ant-1.7 | 0.54 | 0.53 | 0.48 | 0.48 | 0.57 | 0.56 | 0.55 | **0.64** |
| Jedit-4.2 | 0.37 | 0.41 | 0.35 | 0.36 | 0.39 | 0.40 | 0.41 | **0.53** |
| Prop-4 | 0.22 | 0.30 | 0.29 | **0.32** | 0.23 | 0.23 | 0.23 | 0.26 |
| Xalan-2.6 | 0.65 | 0.62 | 0.59 | 0.59 | 0.66 | 0.67 | 0.65 | **0.72** |
| Xerces-1.3 | 0.47 | 0.41 | 0.44 | 0.47 | 0.47 | 0.49 | 0.49 | **0.51** |
| **Average** | **0.40** | **0.43** | **0.41** | **0.43** | **0.42** | **0.43** | **0.42** | **0.47** |




