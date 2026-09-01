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




## RQ2: Target-Level F1 Results for CPDP

The following tables report the complete target-level F1-score results for
the five CPDP frameworks. The **Average** row corresponds to the final
framework-level results reported in the paper.

### BurakMHD

| Target Project | Default | SMOTE | SMOTE-ENN | CTGAN | CTAB-GAN+ | TabDDPM | TabSyn | SCDO |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|
| Activemq-5.3.0 | 0.02 | 0.20 | 0.35 | 0.30 | 0.08 | **0.36** | 0.09 | 0.22 |
| Camel-2.11.0 | 0.01 | 0.02 | **0.11** | 0.08 | 0.02 | 0.05 | 0.02 | 0.05 |
| Derby-10.3.1.4 | 0.07 | 0.26 | **0.41** | 0.36 | 0.17 | 0.24 | 0.23 | 0.34 |
| Hbase-0.95.0 | 0.17 | 0.38 | 0.37 | 0.32 | 0.33 | 0.36 | 0.27 | **0.43** |
| Hive-0.12.0 | 0.14 | 0.15 | 0.17 | 0.13 | 0.21 | 0.17 | 0.20 | **0.26** |
| Lucene-3.1 | 0.08 | 0.06 | 0.09 | 0.05 | 0.07 | 0.06 | 0.03 | **0.12** |
| Ant-1.7 | 0.18 | 0.42 | **0.58** | 0.52 | 0.50 | 0.49 | 0.31 | 0.54 |
| Jedit-4.2 | 0.43 | 0.36 | 0.33 | 0.28 | 0.39 | 0.38 | 0.24 | **0.44** |
| Prop-4 | 0.31 | 0.33 | 0.32 | 0.27 | 0.34 | 0.37 | 0.23 | **0.39** |
| Xalan-2.6 | 0.21 | 0.50 | **0.59** | 0.53 | 0.47 | 0.53 | 0.49 | 0.41 |
| Xerces-1.3 | 0.33 | 0.30 | 0.33 | 0.29 | 0.30 | 0.31 | 0.40 | **0.41** |
| **Average** | 0.18 | 0.27 | **0.33** | 0.28 | 0.26 | 0.30 | 0.23 | **0.33** |

### DANN

| Target Project | Default | SMOTE | SMOTE-ENN | CTGAN | CTAB-GAN+ | TabDDPM | TabSyn | SCDO |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|
| Activemq-5.3.0 | 0.41 | 0.40 | 0.28 | 0.06 | 0.06 | 0.00 | 0.06 | **0.49** |
| Camel-2.11.0 | 0.16 | 0.14 | 0.04 | 0.12 | 0.12 | 0.01 | 0.11 | **0.17** |
| Derby-10.3.1.4 | 0.52 | 0.51 | 0.52 | 0.50 | 0.51 | 0.01 | 0.37 | **0.60** |
| Hbase-0.95.0 | 0.44 | 0.43 | 0.39 | 0.45 | 0.46 | 0.02 | 0.46 | **0.49** |
| Hive-0.12.0 | 0.22 | 0.21 | 0.17 | 0.23 | 0.23 | 0.00 | 0.17 | **0.26** |
| Lucene-3.1 | 0.11 | 0.09 | 0.09 | 0.13 | 0.13 | 0.02 | **0.15** | 0.14 |
| Ant-1.7 | 0.40 | 0.40 | 0.41 | 0.38 | 0.39 | **0.44** | 0.41 | 0.39 |
| Jedit-4.2 | 0.27 | 0.26 | 0.29 | 0.23 | 0.24 | 0.32 | 0.25 | **0.42** |
| Prop-4 | **0.32** | 0.31 | **0.32** | 0.23 | 0.23 | 0.27 | 0.28 | 0.25 |
| Xalan-2.6 | 0.62 | 0.61 | **0.63** | 0.61 | **0.63** | 0.60 | 0.61 | 0.59 |
| Xerces-1.3 | 0.35 | 0.34 | 0.38 | 0.31 | 0.32 | **0.47** | 0.29 | 0.34 |
| **Average** | 0.35 | 0.34 | 0.32 | 0.30 | 0.30 | 0.20 | 0.29 | **0.38** |

### CORAL

| Target Project | Default | SMOTE | SMOTE-ENN | CTGAN | CTAB-GAN+ | TabDDPM | TabSyn | SCDO |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|
| Activemq-5.3.0 | 0.40 | 0.40 | 0.40 | 0.37 | 0.39 | 0.00 | 0.28 | **0.44** |
| Camel-2.11.0 | 0.09 | 0.08 | 0.08 | 0.05 | 0.06 | 0.01 | 0.11 | **0.17** |
| Derby-10.3.1.4 | **0.56** | 0.55 | 0.55 | 0.54 | **0.56** | 0.04 | 0.52 | 0.52 |
| Hbase-0.95.0 | 0.41 | 0.40 | 0.41 | 0.39 | 0.42 | 0.05 | 0.44 | **0.49** |
| Hive-0.12.0 | 0.21 | 0.22 | 0.19 | 0.20 | 0.21 | 0.01 | 0.17 | **0.28** |
| Lucene-3.1 | 0.08 | 0.08 | 0.07 | 0.08 | 0.09 | 0.03 | 0.14 | **0.18** |
| Ant-1.7 | 0.51 | 0.50 | 0.45 | 0.46 | 0.48 | **0.56** | 0.36 | 0.42 |
| Jedit-4.2 | 0.38 | 0.36 | 0.33 | 0.35 | 0.38 | 0.43 | 0.34 | **0.52** |
| Prop-4 | 0.32 | 0.31 | 0.30 | 0.32 | 0.34 | 0.33 | 0.32 | **0.38** |
| Xalan-2.6 | 0.55 | 0.55 | 0.57 | 0.56 | 0.59 | 0.54 | 0.40 | **0.61** |
| Xerces-1.3 | 0.35 | 0.35 | 0.35 | 0.30 | 0.32 | **0.47** | 0.36 | 0.36 |
| **Average** | 0.35 | 0.35 | 0.34 | 0.33 | 0.35 | 0.22 | 0.31 | **0.40** |

### MASTER

| Target Project | Default | SMOTE | SMOTE-ENN | CTGAN | CTAB-GAN+ | TabDDPM | TabSyn | SCDO |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|
| Activemq-5.3.0 | 0.34 | 0.34 | **0.44** | 0.37 | 0.38 | 0.38 | 0.38 | 0.41 |
| Camel-2.11.0 | 0.21 | 0.21 | **0.23** | 0.13 | 0.13 | 0.13 | 0.12 | 0.16 |
| Derby-10.3.1.4 | 0.18 | 0.18 | 0.39 | 0.60 | 0.61 | 0.61 | 0.61 | **0.65** |
| Hbase-0.95.0 | 0.04 | 0.04 | 0.06 | 0.48 | 0.49 | 0.49 | 0.49 | **0.53** |
| Hive-0.12.0 | 0.01 | 0.01 | 0.03 | 0.31 | 0.31 | 0.31 | 0.31 | **0.34** |
| Lucene-3.1 | **0.22** | **0.22** | 0.18 | 0.15 | 0.16 | 0.16 | 0.16 | 0.18 |
| Ant-1.7 | 0.50 | 0.50 | 0.58 | 0.58 | 0.59 | 0.59 | 0.59 | **0.63** |
| Jedit-4.2 | 0.43 | 0.43 | 0.47 | 0.47 | 0.48 | 0.08 | 0.47 | **0.51** |
| Prop-4 | 0.14 | 0.14 | 0.26 | 0.34 | 0.35 | 0.35 | 0.35 | **0.39** |
| Xalan-2.6 | 0.25 | 0.25 | 0.48 | 0.52 | 0.53 | **0.56** | **0.56** | 0.54 |
| Xerces-1.3 | 0.31 | 0.31 | 0.37 | 0.41 | 0.42 | 0.42 | 0.42 | **0.46** |
| **Average** | 0.24 | 0.24 | 0.32 | 0.40 | 0.40 | 0.37 | 0.40 | **0.44** |

### FEDL

| Target Project | Default | SMOTE | SMOTE-ENN | CTGAN | CTAB-GAN+ | TabDDPM | TabSyn | SCDO |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|
| Activemq-5.3.0 | 0.26 | 0.27 | 0.27 | 0.30 | 0.32 | 0.31 | 0.33 | **0.35** |
| Camel-2.11.0 | 0.25 | 0.27 | 0.28 | 0.29 | 0.30 | 0.32 | 0.33 | **0.36** |
| Derby-10.3.1.4 | 0.25 | 0.27 | 0.28 | 0.30 | 0.30 | 0.31 | 0.34 | **0.37** |
| Hbase-0.95.0 | 0.26 | 0.26 | 0.29 | 0.29 | 0.31 | 0.32 | **0.33** | 0.32 |
| Hive-0.12.0 | 0.27 | 0.28 | 0.29 | 0.28 | 0.30 | 0.31 | 0.34 | **0.36** |
| Lucene-3.1 | 0.27 | 0.26 | 0.27 | 0.29 | 0.30 | 0.31 | 0.31 | **0.35** |
| Ant-1.7 | 0.26 | 0.26 | 0.28 | 0.29 | 0.31 | 0.31 | 0.32 | **0.36** |
| Jedit-4.2 | 0.26 | 0.28 | 0.29 | 0.28 | 0.30 | 0.30 | 0.34 | **0.35** |
| Prop-4 | 0.25 | 0.26 | 0.28 | 0.29 | 0.31 | 0.33 | 0.32 | **0.37** |
| Xalan-2.6 | 0.25 | 0.26 | 0.27 | 0.29 | 0.30 | 0.31 | 0.33 | **0.34** |
| Xerces-1.3 | 0.27 | 0.28 | 0.27 | 0.30 | 0.29 | 0.32 | 0.32 | **0.35** |
| **Average** | 0.27 | 0.28 | 0.29 | 0.30 | 0.32 | 0.33 | 0.35 | **0.37** |


## RQ3: Ablation and Structural-Fidelity Results

RQ3 evaluates the contribution of the main SCDO components and examines how
well the generated defective samples preserve minority-class structure.

### Ablation Study

The following table reports the aggregate AUC, MCC, and F1-score obtained after
removing individual SCDO components.

| Variant | WPDP AUC | WPDP MCC | WPDP F1 | CPDP AUC | CPDP MCC | CPDP F1 |
|:--|--:|--:|--:|--:|--:|--:|
| **Full SCDO** | **0.85** | **0.33** | **0.41** | **0.76** | **0.25** | **0.38** |
| w/o Self-Conditioning | 0.83 | 0.31 | 0.39 | 0.73 | 0.23 | 0.36 |
| w/o CFG | 0.82 | 0.30 | 0.38 | 0.72 | 0.22 | 0.35 |
| w/o Covariance | 0.80 | 0.28 | 0.37 | 0.70 | 0.21 | 0.34 |
| w/o Correlation | 0.81 | 0.29 | 0.37 | 0.69 | 0.20 | 0.33 |
| w/o Sliced-Wasserstein | 0.79 | 0.27 | 0.36 | 0.71 | 0.21 | 0.34 |
| w/o All Structural Terms | 0.77 | 0.25 | 0.34 | 0.66 | 0.19 | 0.31 |

Removing all structural regularizers produces the largest overall degradation.
Among the individual structural terms, removing sliced-Wasserstein
regularization causes the largest observed WPDP degradation, while removing
correlation regularization causes the largest observed CPDP degradation.

### Structural Fidelity

Structural fidelity is evaluated using correlation structure error and centroid
shift. Lower values indicate better preservation of the real defective-class
structure.

| Oversampler | WPDP Correlation Error ↓ | WPDP Centroid Shift ↓ | CPDP Correlation Error ↓ | CPDP Centroid Shift ↓ |
|:--|--:|--:|--:|--:|
| SMOTE | **0.0838** | 0.0718 | 0.0873 | 0.0561 |
| SMOTE-ENN | 0.0906 | 0.0801 | 0.0974 | 0.0784 |
| CTGAN | 0.4958 | 0.6047 | 0.2772 | 0.0460 |
| CTAB-GAN+ | 0.5012 | 0.6129 | 0.1786 | 0.0467 |
| TabDDPM | 0.0920 | 0.0593 | 0.1277 | 0.0441 |
| TabSyn | 0.0907 | 0.0593 | 0.0869 | 0.0490 |
| **SCDO** | 0.0851 | **0.0507** | **0.0715** | **0.0401** |

SCDO obtains the best result in three of the four structural-fidelity
comparisons. SMOTE achieves the lowest WPDP correlation error, while SCDO
achieves the lowest WPDP centroid shift and the lowest CPDP correlation error
and centroid shift.

## RQ4: Computational Cost

RQ4 evaluates the computational cost of SCDO and the competing oversampling
methods. Runtime is measured from method-specific data preparation until the
augmented training set is ready for the downstream prediction framework.

### Oversampling Runtime

| Oversampler | WPDP Time (s) | CPDP Time (s) |
|:--|--:|--:|
| SMOTE | 0.0047 | 0.0607 |
| SMOTE-ENN | 0.0407 | 0.1268 |
| CTGAN | 113.82 | 431.27 |
| CTAB-GAN+ | 148.02 | 438.38 |
| TabDDPM | 8.88 | 30.21 |
| TabSyn | 12.94 | 55.29 |
| **SCDO** | **252.89** | **973.84** |

SCDO requires approximately **4.2 minutes** for WPDP and **16.2 minutes** for
CPDP on average. Its denoiser training accounts for approximately **96%** of
the total SCDO runtime.

The additional computational cost occurs during offline training-data
augmentation. SCDO does not modify the architecture or computational cost of
the downstream predictor at inference time.


## Implementation Details and Hyperparameters

The following configuration is used for SCDO across all datasets and prediction
frameworks. The configuration is fixed and is not tuned separately for
individual projects.

| Category | Hyperparameter / Setting | Value |
|:--|:--|:--|
| **Architecture** | Input representation | Feature-token representation |
|  | Denoiser | Transformer |
|  | Hidden dimension | 256 |
|  | Noise-embedding dimension | 128 |
|  | Transformer layers | 6 |
|  | Attention heads | 8 |
|  | Dropout | 0.10 |
|  | Activation | GELU |
|  | Global token | Enabled |
| **Training** | Optimizer | AdamW |
|  | Learning rate | $2\times10^{-4}$ |
|  | Weight decay | $1\times10^{-4}$ |
|  | Batch size | 256 |
|  | Training epochs | 400 |
|  | Gradient clipping | 1.0 |
|  | Self-conditioning probability $p_{\mathrm{sc}}$ | 0.50 |
|  | Label-drop probability $p_{\mathrm{drop}}$ | 0.15 |
| **EDM / Noise** | $\sigma_{\mathrm{data}}$ | 1.0 |
|  | Training noise mean $P_{\mathrm{mean}}$ | `<fill from implementation>` |
|  | Training noise std. $P_{\mathrm{std}}$ | `<fill from implementation>` |
|  | Numerical stabilization $\delta$ | `<fill from implementation>` |
| **Sampling** | Sampler | Heun predictor--corrector |
|  | Final step | Euler step to $\sigma=0$ |
|  | Noise schedule | Karras |
|  | $\sigma_{\min}$ | 0.002 |
|  | $\sigma_{\max}$ | 80.0 |
|  | Schedule exponent $\rho_{\mathrm{s}}$ | 7.0 |
|  | Reverse transitions $T$ | 40 |
|  | Classifier-free guidance scale $s_{\mathrm{cfg}}$ | 2.0 |
|  | Generation class | Defective class ($y=1$) |
|  | Sampling-time self-conditioning | Enabled |
| **Structural Regularization** | Covariance weight $\lambda_{\mathrm{cov}}$ | 0.05 |
|  | Correlation weight $\lambda_{\mathrm{corr}}$ | 0.05 |
|  | Sliced-Wasserstein weight $\lambda_{\mathrm{swd}}$ | 0.02 |
|  | SWD projection directions $K$ | 32 |
|  | Structural batch limit $m_0$ | `<fill from implementation>` |
|  | Structural batch size | $m_s=\min(m_0,n_+)$ |
|  | Covariance shrinkage $\alpha$ | `<fill from implementation>` |
|  | Covariance stabilization $\delta_C$ | `<fill from implementation>` |
|  | Maximum structural noise $\sigma_{\mathrm{struct}}$ | `<fill from implementation>` |
|  | Structural reference set | All real defective training samples |
|  | Structural label | Defective class ($y=1$) |
|  | Label dropping in structural path | Disabled |
| **Pre/Post-processing** | Standardization | Training-set mean and standard deviation |
|  | Output range handling | Clip to training-set feature ranges |
|  | Count-valued metrics | Rounded after inverse standardization |
|  | Cross-feature hard constraints | None |
| **Oversampling** | Target class | Defective/minority class |
|  | Oversampling target | Minority class balanced to majority class |
|  | Synthetic sample label | 1 (defective) |
| **Reproducibility** | Random seeds | Controlled for data partitioning and model training |
|  | Neural implementation | PyTorch |
| **Hardware** | CPU | AMD Ryzen 9 9950X |
|  | GPU | 12 GB GPU |
|  | RAM | 64 GB |
|  | Operating system | Windows 11 |
