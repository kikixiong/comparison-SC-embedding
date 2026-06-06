# Conference-style Aggregated Embedding Comparison

抹除数据集差异后，对多个 embedding 做聚合对比（常用指标：Pearson r、MSE）。

## Table A. Aggregated average rank across datasets (lower is better)

| Embedding | Frozen Linear Rank | Backbone+Head Rank | Overall Rank |
|---|---:|---:|---:|
| baseline | 3.667 | 4.000 | 3.833 |
| scGPT_human | 5.333 | 7.500 | 6.417 |
| minus | 6.333 | 6.000 | 6.167 |
| v4_bias_rec_best | **3.000** | 2.500 | 2.750 |
| v4_plain_best | 5.667 | 6.500 | 6.083 |
| v4_type_pe_best | 7.333 | 5.500 | 6.417 |
| scconcept | 7.000 | 8.000 | 7.500 |
| scconcept_encoded | 8.333 | 9.500 | 8.917 |
| **cl_scratch_v5** | 3.333 | **1.500** | **2.417** |
| cl_v6_fair | 5.000 | 4.000 | 4.500 |

## Table B. Dataset-wise regression metrics

| Embedding | adamson | adamson | dixit | dixit | norman | norman | Overall | Overall | Overall | Overall |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|  | Pearson r | MSE | Pearson r | MSE | Pearson r | MSE | Mean Pearson r | Mean MSE | Mean Acc | Mean F1 |
| baseline(frozen_linear) | 0.1096 | 1.4094 | 0.4898 | 0.9619 | 0.0989 | 1.5986 | 0.2328 | 1.3233 | 0.6117 | - |
| baseline(frozen_head) | 0.1716 | 1.1637 | - | - | 0.1249 | 1.2076 | 0.1483 | 1.1856 | 0.5612 | - |
| scGPT_human(frozen_linear) | 0.1703 | 1.1517 | 0.3574 | 0.9146 | 0.0975 | 1.2648 | 0.2084 | 1.1104 | 0.5941 | - |
| scGPT_human(frozen_head) | 0.1683 | 1.1323 | - | - | 0.0745 | 1.1856 | 0.1214 | 1.1589 | 0.5435 | - |
| minus(frozen_linear) | 0.1291 | 1.3427 | 0.3691 | 0.9052 | 0.0464 | 1.7808 | 0.1815 | 1.3429 | 0.5848 | - |
| minus(frozen_head) | 0.1754 | 1.0913 | - | - | 0.0325 | 1.3141 | 0.1039 | 1.2027 | 0.5449 | - |
| v4_bias_rec_best(frozen_linear) | 0.1852 | 1.6062 | **0.6705** | 0.6748 | 0.0554 | 1.9956 | **0.3037** | 1.4256 | **0.6495** | - |
| v4_bias_rec_best(frozen_head) | **0.2282** | 1.1833 | - | - | 0.1078 | 1.2940 | 0.1680 | 1.2387 | 0.5698 | - |
| v4_plain_best(frozen_linear) | 0.1088 | 1.5070 | 0.4674 | 0.9339 | 0.0817 | 1.6249 | 0.2193 | 1.3553 | 0.6034 | - |
| v4_plain_best(frozen_head) | 0.1356 | 1.2170 | - | - | 0.1011 | 1.2478 | 0.1184 | 1.2324 | 0.5449 | - |
| v4_type_pe_best(frozen_linear) | 0.1181 | 1.4307 | 0.3584 | **1.0788** | 0.0394 | 1.7985 | 0.1720 | 1.4360 | 0.5838 | - |
| v4_type_pe_best(frozen_head) | 0.1721 | 1.1583 | - | - | 0.0828 | 1.3043 | 0.1275 | 1.2313 | 0.5524 | - |
| scconcept(frozen_linear) | 0.0066 | 1.3468 | 0.3225 | 1.0418 | 0.1123 | 1.1662 | 0.1471 | 1.1849 | 0.5727 | - |
| scconcept(frozen_head) | -0.0113 | 1.2503 | - | - | 0.0956 | 1.1484 | 0.0421 | 1.1994 | 0.5149 | - |
| scconcept_encoded(frozen_linear) | -0.0069 | **2.1525** | 0.4321 | 0.9441 | 0.0250 | **2.1778** | 0.1501 | **1.7581** | 0.5835 | - |
| scconcept_encoded(frozen_head) | 0.0024 | 1.5755 | - | - | 0.0114 | 1.5925 | 0.0069 | 1.5840 | 0.5061 | - |
| cl_scratch_v5(frozen_linear) | 0.1575 | 1.3575 | 0.3881 | 0.9273 | 0.1292 | 1.5379 | 0.2249 | 1.2743 | 0.5967 | - |
| cl_scratch_v5(frozen_head) | 0.1948 | 1.1385 | - | - | **0.1617** | 1.1911 | 0.1783 | 1.1648 | 0.5680 | - |
| cl_v6_fair(frozen_linear) | 0.1088 | 1.4654 | 0.4632 | 0.9412 | 0.0984 | 1.6524 | 0.2234 | 1.3530 | 0.6020 | - |
| cl_v6_fair(frozen_head) | 0.1693 | 1.1728 | - | - | 0.1480 | 1.2233 | 0.1587 | 1.1980 | 0.5573 | - |

注：当同一张表内同时出现多个 method 时，embedding 名称后会添加括号用于区分 latent variable。
