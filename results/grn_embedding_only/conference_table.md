# GRN Embedding Only (Conference-style Tables)

说明：`-`表示该组合无结果；按列（同一dataset）比较：**加粗**表示优于baseline；<span style="color:red"><strong>红色加粗</strong></span>表示该列最优。
仅将`dataset`与`embedding`作为显式变量；其余设置作为表上方 latent variables 展示。

## AUROC | Classifier=lr

Latent variables: metric=AUROC, classifier=lr, aggregation=mean, dataset_split=1/1

| Embedding | hHep500 | mHSC-E500 | mHSC-GM500 | mHSC-L500 |
|---|---:|---:|---:|---:|
| minus | 0.3986 | <span style="color:red"><strong>0.7195</strong></span> | 0.5291 | 0.5444 |
| baseline | 0.6249 | 0.7166 | 0.7798 | <span style="color:red"><strong>0.7960</strong></span> |
| scGPT_human | **0.6605** | 0.4967 | 0.7666 | 0.5466 |
| v4_bias_rec_best | **0.6282** | 0.6871 | 0.7708 | 0.7867 |
| v4_plain_best | 0.6060 | 0.4714 | **0.7847** | 0.5298 |
| v4_type_pe_best | 0.3874 | 0.4716 | 0.5167 | 0.7799 |
| scconcept | 0.4057 | 0.4299 | 0.7684 | 0.7672 |
| scconcept_encoded | **0.6343** | 0.4359 | 0.7632 | 0.5211 |
| cl_scratch_v5 | 0.6231 | 0.4779 | 0.7784 | 0.7790 |
| cl_v6_fair | **0.6308** | 0.4694 | <span style="color:red"><strong>0.7854</strong></span> | 0.7816 |
| random_256 | <span style="color:red"><strong>1.0000</strong></span> | 0.5594 | 0.6790 | 0.6978 |

### Aggregate mean across 500-gene datasets | AUROC | Classifier=lr

Latent variables: metric=AUROC, classifier=lr, dataset_size=500, aggregation=mean_across_datasets

| Embedding | Mean |
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
| random_256 | <span style="color:red"><strong>0.7341</strong></span> |

## AUROC | Classifier=mlp

Latent variables: metric=AUROC, classifier=mlp, aggregation=mean, dataset_split=1/1

| Embedding | mHSC-E500 | mHSC-GM500 | mHSC-L500 |
|---|---:|---:|---:|
| minus | 0.7320 | 0.5713 | 0.8380 |
| baseline | <span style="color:red"><strong>0.7745</strong></span> | 0.8171 | 0.8402 |
| scGPT_human | 0.5248 | **0.8268** | 0.5987 |
| v4_bias_rec_best | 0.7508 | <span style="color:red"><strong>0.8283</strong></span> | 0.8332 |
| v4_plain_best | 0.4920 | 0.8097 | **0.8441** |
| v4_type_pe_best | 0.7695 | **0.8178** | **0.8423** |
| scconcept | 0.4843 | 0.5641 | 0.5687 |
| scconcept_encoded | 0.4505 | 0.5004 | 0.5433 |
| cl_scratch_v5 | 0.5158 | 0.5672 | <span style="color:red"><strong>0.8497</strong></span> |
| cl_v6_fair | 0.5089 | 0.5682 | 0.8393 |
| random_256 | 0.6146 | 0.6510 | 0.7120 |

### Aggregate mean across 500-gene datasets | AUROC | Classifier=mlp

Latent variables: metric=AUROC, classifier=mlp, dataset_size=500, aggregation=mean_across_datasets

| Embedding | Mean |
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
| random_256 | 0.6592 |

## AUPRC | Classifier=lr

Latent variables: metric=AUPRC, classifier=lr, aggregation=mean, dataset_split=1/1

| Embedding | hHep500 | mHSC-E500 | mHSC-GM500 | mHSC-L500 |
|---|---:|---:|---:|---:|
| minus | 0.6051 | 0.7800 | 0.7083 | 0.7205 |
| baseline | 0.7309 | <span style="color:red"><strong>0.7905</strong></span> | 0.8333 | <span style="color:red"><strong>0.8517</strong></span> |
| scGPT_human | **0.7597** | 0.6898 | 0.8105 | 0.7221 |
| v4_bias_rec_best | 0.7207 | 0.7628 | 0.8285 | 0.8381 |
| v4_plain_best | 0.7014 | 0.6581 | 0.8310 | 0.7027 |
| v4_type_pe_best | 0.6162 | 0.6586 | 0.6915 | 0.8350 |
| scconcept | 0.6078 | 0.6319 | 0.8119 | 0.8162 |
| scconcept_encoded | 0.7180 | 0.6404 | 0.8122 | 0.7015 |
| cl_scratch_v5 | 0.7267 | 0.6704 | 0.8301 | 0.8361 |
| cl_v6_fair | 0.7279 | 0.6661 | <span style="color:red"><strong>0.8392</strong></span> | 0.8402 |
| random_256 | <span style="color:red"><strong>1.0000</strong></span> | 0.6928 | 0.7619 | 0.7965 |

### Aggregate mean across 500-gene datasets | AUPRC | Classifier=lr

Latent variables: metric=AUPRC, classifier=lr, dataset_size=500, aggregation=mean_across_datasets

| Embedding | Mean |
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
| random_256 | <span style="color:red"><strong>0.8128</strong></span> |

## AUPRC | Classifier=mlp

Latent variables: metric=AUPRC, classifier=mlp, aggregation=mean, dataset_split=1/1

| Embedding | mHSC-E500 | mHSC-GM500 | mHSC-L500 |
|---|---:|---:|---:|
| minus | 0.8180 | 0.7525 | 0.8840 |
| baseline | <span style="color:red"><strong>0.8548</strong></span> | 0.8735 | 0.8884 |
| scGPT_human | 0.7238 | **0.8792** | 0.7694 |
| v4_bias_rec_best | 0.8407 | <span style="color:red"><strong>0.8806</strong></span> | 0.8779 |
| v4_plain_best | 0.7058 | 0.8672 | 0.8871 |
| v4_type_pe_best | 0.8468 | **0.8796** | **0.8901** |
| scconcept | 0.6962 | 0.7336 | 0.7433 |
| scconcept_encoded | 0.6763 | 0.7075 | 0.7240 |
| cl_scratch_v5 | 0.7143 | 0.7538 | <span style="color:red"><strong>0.8932</strong></span> |
| cl_v6_fair | 0.7200 | 0.7499 | **0.8904** |
| random_256 | 0.7526 | 0.7617 | 0.8035 |

### Aggregate mean across 500-gene datasets | AUPRC | Classifier=mlp

Latent variables: metric=AUPRC, classifier=mlp, dataset_size=500, aggregation=mean_across_datasets

| Embedding | Mean |
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
| random_256 | 0.7726 |

