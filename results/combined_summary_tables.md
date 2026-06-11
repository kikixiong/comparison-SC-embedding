# Combined Results Summary Tables

This file is rebuilt from generated Markdown exports under `results/`.
It collects only aggregate/summary tables so reviewers can inspect cross-dataset results in one place.

Last rebuilt: 2026-06-11 13:33:46

## Annotation

Source: `annotation/annotation_conference_tables.md`

#### Accuracy: aggregate mean across datasets

| Classifier | cl_v6_tau03 | baseline | cl_scratch_v5 | cl_v6_fair | cl_v6_tau01 | cl_v6_tau02 | cl_v7_fair | minus | scGPT_human | scconcept | scconcept_encoded | v4_bias_rec_best | v4_plain_best | v4_type_pe_best |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| LR | **0.8382** | 0.8382 | **0.8386** | 0.8376 | **0.8387** | **0.8387** | **0.8388** | <span style="color:red"><strong>0.8413</strong></span> | 0.8342 | 0.8018 | 0.8066 | 0.8352 | 0.8373 | 0.8375 |
| MLP | 0.8493 | 0.8508 | **0.8515** | 0.8505 | 0.8498 | 0.8498 | 0.8505 | **0.8522** | <span style="color:red"><strong>0.8574</strong></span> | 0.8273 | 0.7652 | 0.8419 | **0.8509** | 0.8476 |

#### F1-macro: aggregate mean across datasets

| Classifier | cl_v6_tau03 | baseline | cl_scratch_v5 | cl_v6_fair | cl_v6_tau01 | cl_v6_tau02 | cl_v7_fair | minus | scGPT_human | scconcept | scconcept_encoded | v4_bias_rec_best | v4_plain_best | v4_type_pe_best |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| LR | 0.7639 | 0.7677 | **0.7682** | 0.7654 | 0.7646 | 0.7618 | 0.7675 | <span style="color:red"><strong>0.7711</strong></span> | 0.7621 | 0.7197 | 0.7196 | 0.7676 | 0.7638 | 0.7649 |
| MLP | **0.7751** | 0.7730 | **0.7832** | **0.7744** | **0.7771** | **0.7766** | **0.7782** | **0.7774** | <span style="color:red"><strong>0.7856</strong></span> | 0.7327 | 0.6586 | 0.7591 | **0.7748** | 0.7702 |

#### F1-weighted: aggregate mean across datasets

| Classifier | cl_v6_tau03 | baseline | cl_scratch_v5 | cl_v6_fair | cl_v6_tau01 | cl_v6_tau02 | cl_v7_fair | minus | scGPT_human | scconcept | scconcept_encoded | v4_bias_rec_best | v4_plain_best | v4_type_pe_best |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| LR | 0.8361 | 0.8361 | **0.8366** | 0.8356 | **0.8367** | **0.8367** | **0.8367** | <span style="color:red"><strong>0.8392</strong></span> | 0.8335 | 0.8016 | 0.8041 | 0.8327 | 0.8351 | 0.8355 |
| MLP | 0.8462 | 0.8476 | **0.8482** | 0.8465 | 0.8466 | 0.8467 | 0.8465 | **0.8491** | <span style="color:red"><strong>0.8549</strong></span> | 0.8234 | 0.7605 | 0.8380 | **0.8477** | 0.8437 |

## Perturbation regression

Source: `perturbation_regression/conference_embedding_aggregate.md`

### Table A. Aggregated average rank across datasets (lower is better)

| Embedding | Frozen Linear Rank | Backbone+Head Rank | Overall Rank |
|---|---:|---:|---:|
| baseline | 5.333 | 6.500 | 5.917 |
| scGPT_human | 7.667 | 10.500 | 9.083 |
| minus | 9.000 | 9.000 | 9.000 |
| v4_bias_rec_best | <span style="color:red"><strong>4.333</strong></span> | 4.500 | 4.417 |
| v4_plain_best | 7.333 | 10.500 | 8.917 |
| v4_type_pe_best | 10.667 | 8.500 | 9.583 |
| scconcept | 10.333 | 12.000 | 11.167 |
| scconcept_encoded | 12.333 | 13.500 | 12.917 |
| <span style="color:red"><strong>cl_scratch_v5</strong></span> | 4.667 | <span style="color:red"><strong>1.500</strong></span> | <span style="color:red"><strong>3.083</strong></span> |
| cl_v6_fair | 6.667 | 6.000 | 6.333 |
| cl_v7_fair | 9.667 | 9.000 | 9.333 |
| cl_v6_tau01 | 6.000 | 4.000 | 5.000 |
| cl_v6_tau02 | 4.667 | 3.500 | 4.083 |
| cl_v6_tau03 | 6.333 | 6.000 | 6.167 |

### Table C. Mean aggregation across datasets by method/setting

| Method | Embedding | Mean Pearson r | Mean MSE | Mean Sign Acc |
|---|---|---:|---:|---:|
| frozen_linear | baseline | 0.2328 | 1.3233 | 0.6117 |
| frozen_backbone_trainable_head | baseline | 0.1483 | 1.1856 | 0.5612 |
| frozen_linear | scGPT_human | 0.2084 | <span style="color:red"><strong>1.1104</strong></span> | 0.5941 |
| frozen_backbone_trainable_head | scGPT_human | 0.1214 | <span style="color:red"><strong>1.1589</strong></span> | 0.5435 |
| frozen_linear | minus | 0.1815 | 1.3429 | 0.5848 |
| frozen_backbone_trainable_head | minus | 0.1039 | 1.2027 | 0.5449 |
| frozen_linear | v4_bias_rec_best | <span style="color:red"><strong>0.3037</strong></span> | 1.4256 | <span style="color:red"><strong>0.6495</strong></span> |
| frozen_backbone_trainable_head | v4_bias_rec_best | **0.1680** | 1.2387 | <span style="color:red"><strong>0.5698</strong></span> |
| frozen_linear | v4_plain_best | 0.2193 | 1.3553 | 0.6034 |
| frozen_backbone_trainable_head | v4_plain_best | 0.1184 | 1.2324 | 0.5449 |
| frozen_linear | v4_type_pe_best | 0.1720 | 1.4360 | 0.5838 |
| frozen_backbone_trainable_head | v4_type_pe_best | 0.1275 | 1.2313 | 0.5524 |
| frozen_linear | scconcept | 0.1471 | **1.1849** | 0.5727 |
| frozen_backbone_trainable_head | scconcept | 0.0421 | 1.1994 | 0.5149 |
| frozen_linear | scconcept_encoded | 0.1501 | 1.7581 | 0.5835 |
| frozen_backbone_trainable_head | scconcept_encoded | 0.0069 | 1.5840 | 0.5061 |
| frozen_linear | cl_scratch_v5 | 0.2249 | **1.2743** | 0.5967 |
| frozen_backbone_trainable_head | cl_scratch_v5 | <span style="color:red"><strong>0.1783</strong></span> | **1.1648** | **0.5680** |
| frozen_linear | cl_v6_fair | 0.2234 | 1.3530 | 0.6020 |
| frozen_backbone_trainable_head | cl_v6_fair | **0.1587** | 1.1980 | 0.5573 |
| frozen_linear | cl_v7_fair | 0.2057 | 1.3885 | 0.5967 |
| frozen_backbone_trainable_head | cl_v7_fair | 0.1381 | 1.2334 | 0.5498 |
| frozen_linear | cl_v6_tau01 | 0.2236 | 1.3636 | 0.6026 |
| frozen_backbone_trainable_head | cl_v6_tau01 | **0.1690** | **1.1741** | **0.5644** |
| frozen_linear | cl_v6_tau02 | **0.2333** | 1.3577 | 0.6069 |
| frozen_backbone_trainable_head | cl_v6_tau02 | **0.1688** | **1.1689** | **0.5627** |
| frozen_linear | cl_v6_tau03 | 0.2280 | 1.3526 | 0.6050 |
| frozen_backbone_trainable_head | cl_v6_tau03 | **0.1561** | **1.1794** | 0.5596 |

注：当同一张表内同时出现多个 method 时，embedding 名称后会添加括号用于区分 latent variable；MSE 越低越好，其余指标越高越好。

## GRN embedding-only

Source: `grn_embedding_only/conference_table.md`

#### Aggregate mean across datasets | AUROC | Classifier=lr

Latent variables: metric=AUROC, classifier=lr, aggregation=mean_across_datasets, dataset_size=500

| Embedding | Mean 500 |
|---|---:|
| minus | 0.5479 |
| baseline | 0.7293 |
| scGPT_human | 0.6176 |
| v4_bias_rec_best | 0.7182 |
| v4_plain_best | 0.5980 |
| v4_type_pe_best | 0.5389 |
| scconcept | 0.5928 |
| scconcept_encoded | 0.5887 |
| cl_scratch_v5 | 0.6646 |
| cl_v6_fair | 0.6668 |
| cl_v7_fair | 0.6734 |
| random_256 | <span style="color:red"><strong>0.7341</strong></span> |

#### Aggregate mean across datasets | AUROC | Classifier=mlp

Latent variables: metric=AUROC, classifier=mlp, aggregation=mean_across_datasets, dataset_size=500

| Embedding | Mean 500 |
|---|---:|
| minus | 0.7138 |
| baseline | <span style="color:red"><strong>0.8106</strong></span> |
| scGPT_human | 0.6501 |
| v4_bias_rec_best | 0.8041 |
| v4_plain_best | 0.7152 |
| v4_type_pe_best | 0.8099 |
| scconcept | 0.5391 |
| scconcept_encoded | 0.4981 |
| cl_scratch_v5 | 0.6442 |
| cl_v6_fair | 0.6388 |
| cl_v7_fair | 0.6382 |
| random_256 | 0.6592 |

#### Aggregate mean across datasets | AUPRC | Classifier=lr

Latent variables: metric=AUPRC, classifier=lr, aggregation=mean_across_datasets, dataset_size=500

| Embedding | Mean 500 |
|---|---:|
| minus | 0.7035 |
| baseline | 0.8016 |
| scGPT_human | 0.7455 |
| v4_bias_rec_best | 0.7875 |
| v4_plain_best | 0.7233 |
| v4_type_pe_best | 0.7003 |
| scconcept | 0.7170 |
| scconcept_encoded | 0.7180 |
| cl_scratch_v5 | 0.7658 |
| cl_v6_fair | 0.7684 |
| cl_v7_fair | 0.7699 |
| random_256 | <span style="color:red"><strong>0.8128</strong></span> |

#### Aggregate mean across datasets | AUPRC | Classifier=mlp

Latent variables: metric=AUPRC, classifier=mlp, aggregation=mean_across_datasets, dataset_size=500

| Embedding | Mean 500 |
|---|---:|
| minus | 0.8182 |
| baseline | <span style="color:red"><strong>0.8722</strong></span> |
| scGPT_human | 0.7908 |
| v4_bias_rec_best | 0.8664 |
| v4_plain_best | 0.8200 |
| v4_type_pe_best | 0.8722 |
| scconcept | 0.7244 |
| scconcept_encoded | 0.7026 |
| cl_scratch_v5 | 0.7871 |
| cl_v6_fair | 0.7868 |
| cl_v7_fair | 0.7844 |
| random_256 | 0.7726 |

## GRN BEELINE full

Source: `grn_beeline_full/conference_table.md`

###### Aggregate mean across datasets

Latent variables: metric=AUROC, negative_protocol=full_candidate, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets, network_group=Specific/Non-Specific/STRING, dataset_size=500/1000

| Embedding | Specific 500 | Specific 1000 | Non-Specific 500 | Non-Specific 1000 | STRING 500 | STRING 1000 |
|---|---:|---:|---:|---:|---:|---:|
| minus | 0.7777 | 0.8652 | **0.7984** | 0.8570 | **0.8635** | **0.8793** |
| baseline | <span style="color:red"><strong>0.8113</strong></span> | 0.8687 | 0.7720 | 0.8578 | 0.8579 | 0.8791 |
| scGPT_human | 0.7851 | 0.8640 | <span style="color:red"><strong>0.8203</strong></span> | 0.8497 | <span style="color:red"><strong>0.8671</strong></span> | 0.8758 |
| v4_bias_rec_best | 0.7765 | 0.8650 | **0.8076** | 0.8494 | **0.8598** | 0.8718 |
| v4_plain_best | 0.8072 | 0.8657 | **0.8048** | **0.8607** | **0.8600** | 0.8734 |
| v4_type_pe_best | 0.7944 | 0.8675 | **0.7943** | **0.8634** | **0.8665** | <span style="color:red"><strong>0.8888</strong></span> |
| scconcept | 0.7406 | 0.8343 | 0.7353 | 0.8004 | 0.7537 | 0.8168 |
| scconcept_encoded | 0.7302 | 0.8439 | 0.7272 | 0.7870 | 0.7447 | 0.7795 |
| cl_scratch_v5 | 0.7771 | 0.8663 | **0.7832** | **0.8596** | **0.8601** | 0.8781 |
| cl_v6_fair | 0.7672 | <span style="color:red"><strong>0.8735</strong></span> | **0.7905** | <span style="color:red"><strong>0.8639</strong></span> | **0.8587** | 0.8777 |
| cl_v6_tau01 | 0.7663 | **0.8726** | **0.7942** | **0.8598** | 0.8575 | 0.8760 |
| cl_v6_tau02 | 0.7685 | **0.8712** | **0.7953** | **0.8637** | 0.8570 | 0.8752 |
| cl_v6_tau03 | 0.7611 | **0.8713** | **0.7966** | **0.8611** | **0.8587** | **0.8793** |
| cl_v7_fair | 0.7750 | **0.8710** | **0.7874** | **0.8606** | **0.8594** | **0.8791** |

###### Aggregate mean across datasets

Latent variables: metric=AUPRC, negative_protocol=full_candidate, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets, network_group=Specific/Non-Specific/STRING, dataset_size=500/1000

| Embedding | Specific 500 | Specific 1000 | Non-Specific 500 | Non-Specific 1000 | STRING 500 | STRING 1000 |
|---|---:|---:|---:|---:|---:|---:|
| minus | 0.5801 | 0.7021 | **0.1712** | **0.2091** | **0.3521** | **0.3931** |
| baseline | <span style="color:red"><strong>0.6024</strong></span> | 0.7048 | 0.1587 | 0.1856 | 0.3381 | 0.3845 |
| scGPT_human | 0.5894 | 0.6961 | <span style="color:red"><strong>0.2011</strong></span> | <span style="color:red"><strong>0.2193</strong></span> | <span style="color:red"><strong>0.4094</strong></span> | **0.3877** |
| v4_bias_rec_best | 0.5891 | 0.6994 | **0.1797** | 0.1772 | **0.3613** | 0.3531 |
| v4_plain_best | 0.5944 | **0.7049** | **0.1680** | **0.2032** | **0.3661** | **0.3904** |
| v4_type_pe_best | 0.5980 | 0.7037 | **0.1868** | **0.2005** | **0.3669** | **0.3922** |
| scconcept | 0.5565 | 0.6471 | 0.0886 | 0.0985 | 0.1214 | 0.1423 |
| scconcept_encoded | 0.5390 | 0.6549 | 0.0677 | 0.0789 | 0.0957 | 0.0997 |
| cl_scratch_v5 | 0.5877 | 0.7030 | **0.1823** | **0.2114** | **0.3584** | **0.3868** |
| cl_v6_fair | 0.5856 | **0.7121** | **0.1953** | **0.1884** | **0.3510** | **0.3895** |
| cl_v6_tau01 | 0.5915 | <span style="color:red"><strong>0.7135</strong></span> | **0.1870** | **0.1996** | **0.3639** | **0.3928** |
| cl_v6_tau02 | 0.5888 | **0.7082** | **0.1993** | **0.2020** | **0.3611** | <span style="color:red"><strong>0.3956</strong></span> |
| cl_v6_tau03 | 0.5818 | **0.7075** | **0.1923** | **0.2039** | **0.3656** | **0.3885** |
| cl_v7_fair | 0.5811 | **0.7091** | **0.1821** | **0.1912** | **0.3558** | **0.3884** |

###### Aggregate mean across datasets

Latent variables: metric=AUPRC_LIFT, negative_protocol=full_candidate, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets, network_group=Specific/Non-Specific/STRING, dataset_size=500/1000

| Embedding | Specific 500 | Specific 1000 | Non-Specific 500 | Non-Specific 1000 | STRING 500 | STRING 1000 |
|---|---:|---:|---:|---:|---:|---:|
| minus | 2.1145 | 2.6684 | **8.1332** | **15.2045** | **18.7156** | <span style="color:red"><strong>29.6619</strong></span> |
| baseline | <span style="color:red"><strong>2.5838</strong></span> | 2.7200 | 7.5316 | 13.3797 | 17.5231 | 28.6159 |
| scGPT_human | 2.4423 | 2.6585 | **9.0951** | <span style="color:red"><strong>16.1193</strong></span> | <span style="color:red"><strong>22.4905</strong></span> | **29.1850** |
| v4_bias_rec_best | 2.2128 | 2.6342 | **8.4213** | 12.8058 | **19.1021** | 25.9502 |
| v4_plain_best | 2.4141 | 2.6554 | **7.7457** | **14.7530** | **19.1878** | **29.3648** |
| v4_type_pe_best | 2.2498 | 2.6385 | **8.6616** | **14.5743** | **19.4348** | **29.2591** |
| scconcept | 2.4315 | 2.2818 | 4.2979 | 7.0979 | 7.2090 | 9.7100 |
| scconcept_encoded | 1.7170 | 2.3720 | 3.0756 | 5.6576 | 5.3460 | 6.5517 |
| cl_scratch_v5 | 2.0966 | 2.6768 | **8.5069** | **15.3298** | **18.6356** | **28.9183** |
| cl_v6_fair | 2.0428 | <span style="color:red"><strong>2.7713</strong></span> | <span style="color:red"><strong>9.4608</strong></span> | **13.6557** | **18.3307** | **29.1258** |
| cl_v6_tau01 | 2.2033 | **2.7658** | **8.9948** | **14.5418** | **18.9613** | **29.3453** |
| cl_v6_tau02 | 2.1934 | **2.7244** | **9.3617** | **14.6376** | **19.0490** | **29.6309** |
| cl_v6_tau03 | 1.9748 | 2.6861 | **9.0834** | **14.8092** | **19.3146** | **29.1314** |
| cl_v7_fair | 1.9298 | 2.7148 | **8.4813** | **13.8527** | **18.5253** | **29.0412** |

###### Aggregate mean across datasets

Latent variables: metric=PRECISION_AT_K, negative_protocol=full_candidate, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets, network_group=Specific/Non-Specific/STRING, dataset_size=500/1000

| Embedding | Specific 500 | Specific 1000 | Non-Specific 500 | Non-Specific 1000 | STRING 500 | STRING 1000 |
|---|---:|---:|---:|---:|---:|---:|
| minus | 0.5537 | 0.6606 | **0.2085** | **0.2561** | **0.3853** | **0.4184** |
| baseline | 0.5560 | <span style="color:red"><strong>0.6613</strong></span> | 0.1956 | 0.2330 | 0.3678 | 0.4037 |
| scGPT_human | 0.5550 | 0.6547 | **0.2216** | <span style="color:red"><strong>0.2661</strong></span> | <span style="color:red"><strong>0.4302</strong></span> | **0.4088** |
| v4_bias_rec_best | 0.5350 | 0.6497 | **0.2171** | **0.2434** | **0.3938** | 0.3918 |
| v4_plain_best | 0.5474 | 0.6510 | **0.2207** | **0.2517** | **0.3873** | 0.4003 |
| v4_type_pe_best | <span style="color:red"><strong>0.5670</strong></span> | 0.6539 | **0.2210** | **0.2561** | **0.3969** | **0.4120** |
| scconcept | 0.5435 | 0.6193 | 0.1069 | 0.1515 | 0.1545 | 0.1930 |
| scconcept_encoded | 0.5008 | 0.6248 | 0.0717 | 0.1180 | 0.1394 | 0.1535 |
| cl_scratch_v5 | **0.5576** | 0.6560 | <span style="color:red"><strong>0.2280</strong></span> | **0.2592** | **0.3937** | **0.4114** |
| cl_v6_fair | **0.5605** | 0.6565 | **0.2230** | **0.2349** | **0.3865** | **0.4139** |
| cl_v6_tau01 | 0.5434 | 0.6579 | **0.2204** | **0.2425** | **0.4109** | **0.4159** |
| cl_v6_tau02 | 0.5405 | 0.6599 | **0.2279** | **0.2658** | **0.4029** | <span style="color:red"><strong>0.4204</strong></span> |
| cl_v6_tau03 | 0.5410 | 0.6557 | **0.2142** | **0.2570** | **0.3982** | **0.4106** |
| cl_v7_fair | 0.5481 | 0.6554 | **0.2159** | **0.2379** | **0.3879** | **0.4119** |

###### Aggregate mean across datasets

Latent variables: metric=RECALL_AT_K, negative_protocol=full_candidate, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets, network_group=Specific/Non-Specific/STRING, dataset_size=500/1000

| Embedding | Specific 500 | Specific 1000 | Non-Specific 500 | Non-Specific 1000 | STRING 500 | STRING 1000 |
|---|---:|---:|---:|---:|---:|---:|
| minus | 0.5537 | 0.6606 | **0.2085** | **0.2561** | **0.3853** | **0.4184** |
| baseline | 0.5560 | <span style="color:red"><strong>0.6613</strong></span> | 0.1956 | 0.2330 | 0.3678 | 0.4037 |
| scGPT_human | 0.5550 | 0.6547 | **0.2216** | <span style="color:red"><strong>0.2661</strong></span> | <span style="color:red"><strong>0.4302</strong></span> | **0.4088** |
| v4_bias_rec_best | 0.5350 | 0.6497 | **0.2171** | **0.2434** | **0.3938** | 0.3918 |
| v4_plain_best | 0.5474 | 0.6510 | **0.2207** | **0.2517** | **0.3873** | 0.4003 |
| v4_type_pe_best | <span style="color:red"><strong>0.5670</strong></span> | 0.6539 | **0.2210** | **0.2561** | **0.3969** | **0.4120** |
| scconcept | 0.5435 | 0.6193 | 0.1069 | 0.1515 | 0.1545 | 0.1930 |
| scconcept_encoded | 0.5008 | 0.6248 | 0.0717 | 0.1180 | 0.1394 | 0.1535 |
| cl_scratch_v5 | **0.5576** | 0.6560 | <span style="color:red"><strong>0.2280</strong></span> | **0.2592** | **0.3937** | **0.4114** |
| cl_v6_fair | **0.5605** | 0.6565 | **0.2230** | **0.2349** | **0.3865** | **0.4139** |
| cl_v6_tau01 | 0.5434 | 0.6579 | **0.2204** | **0.2425** | **0.4109** | **0.4159** |
| cl_v6_tau02 | 0.5405 | 0.6599 | **0.2279** | **0.2658** | **0.4029** | <span style="color:red"><strong>0.4204</strong></span> |
| cl_v6_tau03 | 0.5410 | 0.6557 | **0.2142** | **0.2570** | **0.3982** | **0.4106** |
| cl_v7_fair | 0.5481 | 0.6554 | **0.2159** | **0.2379** | **0.3879** | **0.4119** |

###### Aggregate mean across datasets

Latent variables: metric=F1, negative_protocol=full_candidate, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets, network_group=Specific/Non-Specific/STRING, dataset_size=500/1000

| Embedding | Specific 500 | Specific 1000 | Non-Specific 500 | Non-Specific 1000 | STRING 500 | STRING 1000 |
|---|---:|---:|---:|---:|---:|---:|
| minus | 0.5135 | **0.6393** | **0.1295** | **0.1905** | 0.3298 | **0.4111** |
| baseline | 0.5229 | 0.6302 | 0.1172 | 0.1615 | 0.3469 | 0.3836 |
| scGPT_human | <span style="color:red"><strong>0.5399</strong></span> | 0.6254 | **0.1541** | <span style="color:red"><strong>0.2133</strong></span> | <span style="color:red"><strong>0.3698</strong></span> | <span style="color:red"><strong>0.4152</strong></span> |
| v4_bias_rec_best | **0.5380** | **0.6379** | **0.1361** | 0.1407 | 0.3311 | 0.3516 |
| v4_plain_best | **0.5314** | **0.6444** | **0.1418** | **0.1925** | **0.3595** | **0.3953** |
| v4_type_pe_best | 0.5162 | **0.6403** | **0.1370** | 0.1612 | **0.3504** | **0.3974** |
| scconcept | 0.5205 | 0.5864 | 0.0586 | 0.0774 | 0.0952 | 0.1291 |
| scconcept_encoded | 0.4990 | 0.6064 | 0.0474 | 0.0457 | 0.0836 | 0.0641 |
| cl_scratch_v5 | **0.5336** | **0.6417** | **0.1455** | **0.2033** | 0.3378 | **0.3985** |
| cl_v6_fair | 0.5124 | **0.6446** | **0.1392** | 0.1483 | 0.3343 | **0.3978** |
| cl_v6_tau01 | **0.5253** | <span style="color:red"><strong>0.6552</strong></span> | **0.1598** | **0.1755** | 0.3431 | **0.4055** |
| cl_v6_tau02 | 0.5122 | **0.6457** | <span style="color:red"><strong>0.1685</strong></span> | **0.1878** | **0.3619** | **0.4097** |
| cl_v6_tau03 | 0.5116 | **0.6400** | **0.1509** | **0.1900** | **0.3496** | **0.3966** |
| cl_v7_fair | 0.5147 | **0.6453** | **0.1416** | **0.1710** | **0.3506** | **0.3952** |

## Transfer v2 AUROC

Source: `transfer_v2/auroc_embedding_x_train_all_settings.md`

### Aggregate mean across train datasets

Latent variables: metric=AUROC, task=transfer_v2, aggregation=mean_across_train_dataset_means, settings=coverage_matched + lr/coverage_matched + mlp/native + lr/native + mlp/strict + lr/strict + mlp/topology_matched + lr/topology_matched + mlp, train_dataset_count=7/7/7/7/7/7/7/7

Each cell is the mean of that embedding's per-train-dataset means from the setting-specific matrix above.

| Embedding | coverage_matched + lr | coverage_matched + mlp | native + lr | native + mlp | strict + lr | strict + mlp | topology_matched + lr | topology_matched + mlp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| baseline | **0.592388** | 0.598909 | 0.566524 | 0.594150 | 0.602783 | 0.606156 | 0.600095 | 0.602248 |
| cl_scratch_v5 | 0.591561 | **<span style="color:red">0.605642</span>** | <span style="color:red">0.569422</span> | 0.588911 | **<span style="color:red">0.606641</span>** | <span style="color:red">0.610030</span> | **<span style="color:red">0.606924</span>** | <span style="color:red">0.606408</span> |
| cl_v6_fair | 0.575606 | 0.584201 | **<span style="color:red">0.573700</span>** | 0.593141 | 0.598169 | <span style="color:red">0.611316</span> | 0.592066 | <span style="color:red">0.602387</span> |
| cl_v6_tau01 | 0.569475 | 0.581571 | <span style="color:red">0.572361</span> | **<span style="color:red">0.595453</span>** | 0.599194 | **<span style="color:red">0.613506</span>** | 0.585812 | 0.591536 |
| cl_v6_tau02 | 0.572397 | <span style="color:red">0.601468</span> | <span style="color:red">0.568363</span> | 0.591053 | 0.595317 | <span style="color:red">0.611104</span> | 0.576827 | 0.592057 |
| cl_v6_tau03 | 0.570855 | 0.592764 | <span style="color:red">0.569982</span> | 0.591706 | 0.585090 | <span style="color:red">0.609051</span> | 0.593018 | **<span style="color:red">0.614753</span>** |
| cl_v7_fair | 0.558702 | 0.571152 | <span style="color:red">0.568390</span> | 0.592348 | 0.594997 | <span style="color:red">0.610661</span> | 0.595330 | <span style="color:red">0.603338</span> |
| minus | 0.549884 | 0.565133 | 0.555924 | 0.577247 | 0.577195 | 0.589083 | 0.578466 | 0.586531 |
| scGPT_human | 0.583374 | 0.589032 | <span style="color:red">0.567752</span> | 0.589698 | 0.595844 | 0.600142 | <span style="color:red">0.602918</span> | 0.589016 |
| scconcept | 0.513491 | 0.516416 | 0.518305 | 0.521747 | 0.517669 | 0.524064 | 0.514107 | 0.523414 |
| scconcept_encoded | 0.515992 | 0.529192 | 0.516575 | 0.526032 | 0.525731 | 0.537919 | 0.525051 | 0.526650 |
| v4_bias_rec_best | 0.567777 | 0.588799 | 0.548391 | 0.579826 | 0.548625 | 0.597267 | 0.563224 | 0.597002 |
| v4_plain_best | 0.557666 | 0.572275 | 0.558329 | 0.586329 | <span style="color:red">0.605548</span> | <span style="color:red">0.607116</span> | 0.593335 | 0.586092 |
| v4_type_pe_best | 0.571477 | 0.584766 | 0.558697 | 0.593046 | 0.589838 | <span style="color:red">0.606811</span> | 0.585163 | 0.595815 |

## Transfer v2 AUPRC

Source: `transfer_v2/auprc_embedding_x_train_all_settings.md`

### Aggregate mean across train datasets

Latent variables: metric=AUPRC, task=transfer_v2, aggregation=mean_across_train_dataset_means, settings=coverage_matched + lr/coverage_matched + mlp/native + lr/native + mlp/strict + lr/strict + mlp/topology_matched + lr/topology_matched + mlp, train_dataset_count=7/7/7/7/7/7/7/7

Each cell is the mean of that embedding's per-train-dataset means from the setting-specific matrix above.

| Embedding | coverage_matched + lr | coverage_matched + mlp | native + lr | native + mlp | strict + lr | strict + mlp | topology_matched + lr | topology_matched + mlp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| baseline | **0.619306** | **0.625390** | 0.579060 | **0.601418** | 0.572757 | 0.607198 | 0.571226 | 0.605813 |
| cl_scratch_v5 | 0.598874 | 0.605657 | <span style="color:red">0.579900</span> | 0.593719 | 0.571186 | 0.590328 | <span style="color:red">0.573246</span> | 0.580086 |
| cl_v6_fair | 0.590021 | 0.593411 | <span style="color:red">0.587066</span> | 0.597406 | 0.567257 | 0.591824 | 0.563756 | 0.595669 |
| cl_v6_tau01 | 0.615376 | 0.614578 | **<span style="color:red">0.587460</span>** | 0.600567 | 0.570972 | 0.592946 | 0.556757 | 0.574629 |
| cl_v6_tau02 | 0.574701 | 0.600926 | <span style="color:red">0.583758</span> | 0.595859 | 0.565705 | 0.591101 | 0.542888 | 0.572660 |
| cl_v6_tau03 | 0.595427 | 0.614808 | <span style="color:red">0.585084</span> | 0.596852 | 0.559656 | 0.588440 | **<span style="color:red">0.579172</span>** | 0.592780 |
| cl_v7_fair | 0.599952 | 0.603945 | <span style="color:red">0.582672</span> | 0.596842 | 0.568544 | 0.587329 | 0.561916 | 0.587027 |
| minus | 0.588855 | 0.577265 | 0.572096 | 0.587808 | 0.548202 | 0.600984 | 0.570384 | <span style="color:red">0.622377</span> |
| scGPT_human | 0.616233 | 0.609953 | <span style="color:red">0.580588</span> | 0.598603 | 0.563497 | 0.602535 | <span style="color:red">0.577671</span> | <span style="color:red">0.610649</span> |
| scconcept | 0.544878 | 0.540629 | 0.528730 | 0.534178 | 0.487650 | 0.535994 | 0.496011 | 0.561949 |
| scconcept_encoded | 0.546644 | 0.549184 | 0.526312 | 0.537724 | 0.491557 | 0.544311 | 0.498705 | 0.522595 |
| v4_bias_rec_best | 0.588615 | 0.588797 | 0.564965 | 0.591524 | 0.528991 | 0.606782 | 0.542088 | **<span style="color:red">0.627673</span>** |
| v4_plain_best | 0.559575 | 0.572861 | 0.573162 | 0.595488 | **<span style="color:red">0.575590</span>** | **<span style="color:red">0.615907</span>** | 0.561069 | <span style="color:red">0.621008</span> |
| v4_type_pe_best | 0.595181 | 0.592247 | 0.571618 | 0.597866 | 0.555390 | <span style="color:red">0.613174</span> | 0.548393 | <span style="color:red">0.620136</span> |
