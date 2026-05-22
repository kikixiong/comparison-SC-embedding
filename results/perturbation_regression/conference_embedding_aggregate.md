# Conference-style Aggregated Embedding Comparison

抹除数据集差异后，对多个 embedding 做聚合对比（常用指标：Pearson r、MSE）。

## Table A. Aggregated average rank across datasets (lower is better)

| Embedding | Frozen Linear Rank | Backbone+Head Rank | Overall Rank |
|---|---:|---:|---:|
| baseline | 3.000 | **1.500** | 2.250 |
| scGPT_human | 4.000 | 5.000 | 4.500 |
| minus | 4.667 | 5.000 | 4.833 |
| **v4_bias_rec_best** | **2.333** | **1.500** | **1.917** |
| v4_plain_best | 4.333 | 4.500 | 4.417 |
| v4_type_pe_best | 5.667 | 4.000 | 4.833 |
| scconcept | 5.333 | 7.000 | 6.167 |
| scconcept_encoded | 6.667 | 7.500 | 7.083 |

## Table B. Dataset-wise regression metrics

| Embedding | adamson | adamson | dixit | dixit | norman | norman | Overall | Overall | Overall | Overall |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|  | Pearson r | MSE | Pearson r | MSE | Pearson r | MSE | Mean Pearson r | Mean MSE | Mean Acc | Mean F1 |
| baseline(frozen_linear) | 0.1096 | 1.4094 | 0.4898 | 0.9619 | 0.0989 | 1.5986 | 0.2328 | 1.3233 | 0.6117 | - |
| baseline(frozen_head) | 0.1823 | 1.1555 | - | - | **0.1211** | 1.2053 | 0.1517 | 1.1804 | 0.5636 | - |
| scGPT_human(frozen_linear) | 0.1703 | 1.1517 | 0.3574 | 0.9146 | 0.0975 | 1.2648 | 0.2084 | 1.1104 | 0.5941 | - |
| scGPT_human(frozen_head) | 0.1661 | 1.1432 | - | - | 0.0763 | 1.1876 | 0.1212 | 1.1654 | 0.5442 | - |
| minus(frozen_linear) | 0.1291 | 1.3427 | 0.3691 | 0.9052 | 0.0464 | 1.7808 | 0.1815 | 1.3429 | 0.5848 | - |
| minus(frozen_head) | 0.1759 | 1.0997 | - | - | 0.0323 | 1.3232 | 0.1041 | 1.2115 | 0.5444 | - |
| v4_bias_rec_best(frozen_linear) | 0.1852 | 1.6062 | **0.6705** | 0.6748 | 0.0554 | 1.9956 | **0.3037** | 1.4256 | **0.6495** | - |
| v4_bias_rec_best(frozen_head) | **0.2235** | 1.1723 | - | - | 0.1061 | 1.2899 | 0.1648 | 1.2311 | 0.5690 | - |
| v4_plain_best(frozen_linear) | 0.1088 | 1.5070 | 0.4674 | 0.9339 | 0.0817 | 1.6249 | 0.2193 | 1.3553 | 0.6034 | - |
| v4_plain_best(frozen_head) | 0.1450 | 1.2167 | - | - | 0.1040 | 1.2430 | 0.1245 | 1.2299 | 0.5488 | - |
| v4_type_pe_best(frozen_linear) | 0.1181 | 1.4307 | 0.3584 | **1.0788** | 0.0394 | 1.7985 | 0.1720 | 1.4360 | 0.5838 | - |
| v4_type_pe_best(frozen_head) | 0.1716 | 1.1643 | - | - | 0.0806 | 1.3012 | 0.1261 | 1.2327 | 0.5523 | - |
| scconcept(frozen_linear) | 0.0066 | 1.3468 | 0.3225 | 1.0418 | 0.1123 | 1.1662 | 0.1471 | 1.1849 | 0.5727 | - |
| scconcept(frozen_head) | -0.0177 | 1.2467 | - | - | 0.0587 | 1.1584 | 0.0205 | 1.2025 | 0.5021 | - |
| scconcept_encoded(frozen_linear) | -0.0069 | **2.1525** | 0.4321 | 0.9441 | 0.0250 | **2.1778** | 0.1501 | **1.7581** | 0.5835 | - |
| scconcept_encoded(frozen_head) | -0.0143 | 1.5902 | - | - | 0.0114 | 1.5751 | -0.0015 | 1.5827 | 0.5055 | - |

注：当同一张表内同时出现多个 method 时，embedding 名称后会添加括号用于区分 latent variable。
