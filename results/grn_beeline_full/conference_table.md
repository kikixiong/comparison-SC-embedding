# GRN BEELINE Full (Conference-style Tables)

说明：`-`表示该组合无结果；按列（同一dataset）比较：**加粗**表示优于baseline；<span style="color:red"><strong>红色加粗</strong></span>表示该列最优。
仅将`dataset`与`embedding`作为显式变量；其余设置作为表上方 latent variables 展示；`dataset_split`与`classifier`已聚合，不再展示拆分明细。

## AUROC (Main)

### Negative protocol: tf_stratified_1to10

Latent variables: metric=AUROC, negative_protocol=tf_stratified_1to10, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.7004 | 0.6687 | 0.8490 | 0.6981 | 0.5172 | <span style="color:red"><strong>0.8352</strong></span> | **0.7881** | <span style="color:red"><strong>0.8248</strong></span> | **0.7770** | **0.8265** | <span style="color:red"><strong>0.8020</strong></span> |
| baseline | <span style="color:red"><strong>0.7217</strong></span> | 0.6884 | <span style="color:red"><strong>0.8645</strong></span> | 0.7041 | <span style="color:red"><strong>0.6492</strong></span> | 0.8327 | 0.7802 | 0.8135 | 0.7479 | 0.8154 | 0.7720 |
| scGPT_human | 0.7086 | 0.6812 | 0.8379 | 0.6972 | 0.5750 | 0.8254 | 0.7571 | 0.8116 | **0.7670** | <span style="color:red"><strong>0.8275</strong></span> | 0.7698 |
| v4_bias_rec_best | 0.7042 | 0.6717 | 0.8591 | 0.6940 | 0.3836 | **0.8333** | 0.7745 | **0.8163** | <span style="color:red"><strong>0.7883</strong></span> | **0.8217** | **0.7779** |
| v4_plain_best | 0.7120 | 0.6567 | 0.8580 | **0.7180** | 0.6016 | 0.8305 | 0.7528 | **0.8176** | **0.7522** | **0.8193** | **0.7916** |
| v4_type_pe_best | 0.7116 | <span style="color:red"><strong>0.7099</strong></span> | 0.8596 | 0.6987 | 0.5125 | 0.8325 | <span style="color:red"><strong>0.7957</strong></span> | **0.8163** | **0.7601** | **0.8248** | **0.7855** |
| scconcept | 0.6249 | 0.6441 | 0.7970 | 0.6512 | 0.4531 | 0.8021 | 0.7257 | 0.7707 | 0.7090 | 0.8121 | 0.7066 |
| scconcept_encoded | 0.6572 | 0.6381 | 0.7945 | 0.6816 | 0.4297 | 0.7990 | 0.7435 | 0.7700 | 0.7272 | 0.7935 | 0.7046 |
| cl_scratch_v5 | 0.6992 | **0.6986** | 0.8587 | <span style="color:red"><strong>0.7196</strong></span> | 0.5398 | 0.8291 | **0.7890** | **0.8167** | **0.7752** | **0.8192** | **0.7727** |
| cl_v6_fair | 0.6857 | 0.6422 | 0.8591 | **0.7175** | 0.5547 | 0.8322 | 0.7744 | **0.8198** | **0.7791** | **0.8198** | **0.7767** |

##### Aggregate mean across Specific 500-gene datasets

Latent variables: metric=AUROC, negative_protocol=tf_stratified_1to10, network_group=Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.7106 |
| baseline | <span style="color:red"><strong>0.7276</strong></span> |
| scGPT_human | 0.7100 |
| v4_bias_rec_best | 0.6792 |
| v4_plain_best | 0.7109 |
| v4_type_pe_best | 0.7127 |
| scconcept | 0.6477 |
| scconcept_encoded | 0.6486 |
| cl_scratch_v5 | 0.7151 |
| cl_v6_fair | 0.7054 |

##### Aggregate mean across Specific 1000-gene datasets

Latent variables: metric=AUROC, negative_protocol=tf_stratified_1to10, network_group=Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.7890 |
| baseline | 0.7920 |
| scGPT_human | 0.7847 |
| v4_bias_rec_best | 0.7881 |
| v4_plain_best | <span style="color:red"><strong>0.7926</strong></span> |
| v4_type_pe_best | 0.7906 |
| scconcept | 0.7430 |
| scconcept_encoded | 0.7493 |
| cl_scratch_v5 | 0.7904 |
| cl_v6_fair | 0.7890 |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.6678 | 0.6145 | **0.6785** | **0.7065** | **0.7966** | 0.6132 | 0.7799 | 0.7200 | **0.7364** | 0.6205 | **0.7315** | 0.6830 |
| baseline | 0.6683 | 0.6235 | 0.6782 | 0.6607 | 0.7864 | 0.7388 | <span style="color:red"><strong>0.7976</strong></span> | 0.7327 | 0.7245 | 0.6547 | 0.7229 | 0.6925 |
| scGPT_human | 0.6394 | **0.6331** | <span style="color:red"><strong>0.7047</strong></span> | <span style="color:red"><strong>0.7178</strong></span> | 0.7677 | 0.6963 | 0.7678 | <span style="color:red"><strong>0.7780</strong></span> | **0.7425** | <span style="color:red"><strong>0.7107</strong></span> | **0.7426** | **0.7174** |
| v4_bias_rec_best | 0.6350 | 0.5756 | 0.6679 | **0.6845** | 0.7839 | 0.7190 | 0.7726 | **0.7568** | **0.7541** | **0.6702** | **0.7297** | **0.6998** |
| v4_plain_best | 0.6640 | <span style="color:red"><strong>0.6442</strong></span> | **0.6991** | **0.6951** | <span style="color:red"><strong>0.8062</strong></span> | 0.7326 | 0.7749 | **0.7599** | 0.6902 | 0.6280 | 0.7005 | **0.7219** |
| v4_type_pe_best | <span style="color:red"><strong>0.6829</strong></span> | 0.5817 | 0.6591 | 0.5546 | **0.7981** | 0.7190 | 0.7825 | 0.7305 | **0.7491** | 0.6281 | <span style="color:red"><strong>0.7483</strong></span> | <span style="color:red"><strong>0.7597</strong></span> |
| scconcept | 0.5374 | 0.5681 | 0.5923 | 0.5559 | 0.6508 | 0.5157 | 0.6326 | 0.5130 | 0.6633 | **0.6696** | 0.6536 | 0.5894 |
| scconcept_encoded | 0.5441 | 0.5226 | 0.6119 | 0.5181 | 0.6020 | 0.6260 | 0.6527 | 0.5934 | 0.6461 | 0.5951 | 0.6946 | 0.5888 |
| cl_scratch_v5 | 0.6626 | 0.5998 | **0.6847** | **0.6853** | **0.7973** | 0.6744 | 0.7851 | 0.7154 | **0.7558** | 0.6334 | **0.7442** | **0.7309** |
| cl_v6_fair | 0.6609 | 0.5781 | 0.6679 | 0.5647 | **0.8042** | <span style="color:red"><strong>0.7475</strong></span> | 0.7810 | **0.7458** | <span style="color:red"><strong>0.7587</strong></span> | 0.6300 | **0.7397** | **0.6989** |

##### Aggregate mean across Non-Specific 500-gene datasets

Latent variables: metric=AUROC, negative_protocol=tf_stratified_1to10, network_group=Non-Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.6596 |
| baseline | 0.6838 |
| scGPT_human | <span style="color:red"><strong>0.7089</strong></span> |
| v4_bias_rec_best | **0.6843** |
| v4_plain_best | **0.6969** |
| v4_type_pe_best | 0.6623 |
| scconcept | 0.5686 |
| scconcept_encoded | 0.5740 |
| cl_scratch_v5 | 0.6732 |
| cl_v6_fair | 0.6608 |

##### Aggregate mean across Non-Specific 1000-gene datasets

Latent variables: metric=AUROC, negative_protocol=tf_stratified_1to10, network_group=Non-Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.7318** |
| baseline | 0.7297 |
| scGPT_human | 0.7274 |
| v4_bias_rec_best | 0.7239 |
| v4_plain_best | 0.7225 |
| v4_type_pe_best | **0.7367** |
| scconcept | 0.6217 |
| scconcept_encoded | 0.6252 |
| cl_scratch_v5 | <span style="color:red"><strong>0.7383</strong></span> |
| cl_v6_fair | **0.7354** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.8007 | 0.6105 | **0.8814** | **0.9081** | **0.8829** | **0.7928** | **0.9037** | <span style="color:red"><strong>0.9210</strong></span> | 0.8391 | **0.8363** | 0.8201 | **0.8423** |
| baseline | 0.8066 | 0.6697 | 0.8689 | 0.9048 | 0.8765 | 0.7720 | 0.8907 | 0.8952 | 0.8664 | 0.7448 | 0.8325 | 0.8173 |
| scGPT_human | <span style="color:red"><strong>0.8403</strong></span> | <span style="color:red"><strong>0.7591</strong></span> | **0.8775** | **0.9115** | 0.8633 | <span style="color:red"><strong>0.8710</strong></span> | **0.9003** | **0.9208** | **0.8705** | **0.7589** | **0.8475** | 0.8067 |
| v4_bias_rec_best | 0.8007 | **0.6981** | **0.8769** | 0.9038 | 0.8644 | **0.8612** | **0.9050** | 0.8877 | 0.8490 | **0.8254** | **0.8441** | <span style="color:red"><strong>0.8565</strong></span> |
| v4_plain_best | 0.7803 | **0.6944** | **0.8735** | **0.9086** | **0.8800** | **0.7966** | **0.8976** | **0.8962** | 0.8330 | **0.7636** | **0.8346** | **0.8274** |
| v4_type_pe_best | **0.8270** | **0.7240** | <span style="color:red"><strong>0.8827</strong></span> | <span style="color:red"><strong>0.9121</strong></span> | <span style="color:red"><strong>0.8926</strong></span> | **0.7842** | <span style="color:red"><strong>0.9122</strong></span> | 0.8827 | 0.8628 | <span style="color:red"><strong>0.8374</strong></span> | <span style="color:red"><strong>0.8559</strong></span> | **0.8349** |
| scconcept | 0.6642 | **0.7209** | 0.7761 | 0.7654 | 0.7643 | 0.6176 | 0.7623 | 0.7145 | 0.7043 | 0.5745 | 0.7065 | 0.7011 |
| scconcept_encoded | 0.6473 | **0.6960** | 0.7672 | 0.6745 | 0.7460 | 0.6478 | 0.6898 | 0.6649 | 0.6809 | 0.5950 | 0.7030 | 0.6732 |
| cl_scratch_v5 | **0.8099** | 0.6685 | **0.8826** | **0.9069** | **0.8855** | 0.7654 | **0.8924** | **0.9093** | <span style="color:red"><strong>0.8758</strong></span> | **0.7874** | **0.8526** | **0.8363** |
| cl_v6_fair | **0.8181** | **0.6807** | **0.8752** | 0.9041 | 0.8752 | **0.7963** | **0.9055** | **0.9118** | 0.8617 | **0.7956** | **0.8386** | **0.8439** |

##### Aggregate mean across STRING 500-gene datasets

Latent variables: metric=AUROC, negative_protocol=tf_stratified_1to10, network_group=STRING, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.8185** |
| baseline | 0.8006 |
| scGPT_human | **0.8380** |
| v4_bias_rec_best | <span style="color:red"><strong>0.8388</strong></span> |
| v4_plain_best | **0.8145** |
| v4_type_pe_best | **0.8292** |
| scconcept | 0.6823 |
| scconcept_encoded | 0.6586 |
| cl_scratch_v5 | **0.8123** |
| cl_v6_fair | **0.8221** |

##### Aggregate mean across STRING 1000-gene datasets

Latent variables: metric=AUROC, negative_protocol=tf_stratified_1to10, network_group=STRING, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.8546 |
| baseline | 0.8570 |
| scGPT_human | **0.8666** |
| v4_bias_rec_best | 0.8567 |
| v4_plain_best | 0.8498 |
| v4_type_pe_best | <span style="color:red"><strong>0.8722</strong></span> |
| scconcept | 0.7296 |
| scconcept_encoded | 0.7057 |
| cl_scratch_v5 | **0.8665** |
| cl_v6_fair | **0.8624** |

### Negative protocol: full_candidate

Latent variables: metric=AUROC, negative_protocol=full_candidate, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.8420 | 0.7997 | 0.8916 | 0.8154 | 0.7021 | **0.8983** | 0.8177 | **0.8736** | **0.7732** | <span style="color:red"><strong>0.8702</strong></span> | **0.7957** |
| baseline | 0.8548 | <span style="color:red"><strong>0.8241</strong></span> | 0.8973 | 0.8366 | 0.8515 | 0.8926 | 0.8321 | 0.8724 | 0.7633 | 0.8587 | 0.7857 |
| scGPT_human | 0.8420 | 0.8024 | 0.8779 | 0.8366 | 0.7912 | **0.8967** | 0.8032 | 0.8708 | 0.7590 | **0.8598** | 0.7696 |
| v4_bias_rec_best | 0.8547 | 0.8159 | **0.8983** | 0.8123 | 0.6732 | **0.8996** | **0.8329** | 0.8667 | **0.7805** | 0.8583 | 0.7799 |
| v4_plain_best | 0.8532 | 0.8090 | <span style="color:red"><strong>0.8988</strong></span> | 0.8087 | <span style="color:red"><strong>0.8517</strong></span> | **0.8992** | 0.8306 | **0.8737** | 0.7602 | **0.8604** | 0.7842 |
| v4_type_pe_best | <span style="color:red"><strong>0.8608</strong></span> | 0.8161 | **0.8976** | 0.8174 | 0.7654 | **0.8963** | **0.8330** | 0.8722 | 0.7614 | **0.8608** | <span style="color:red"><strong>0.7959</strong></span> |
| scconcept | 0.8265 | 0.8039 | 0.8424 | 0.7669 | 0.6766 | 0.8792 | 0.7806 | 0.8482 | 0.7263 | 0.8427 | 0.7158 |
| scconcept_encoded | 0.8312 | 0.7982 | 0.8410 | 0.8195 | 0.6115 | 0.8797 | 0.8003 | 0.8511 | 0.7275 | 0.8411 | 0.7136 |
| cl_scratch_v5 | 0.8357 | 0.8085 | 0.8958 | 0.8342 | 0.6906 | **0.8976** | **0.8394** | **0.8744** | **0.7682** | **0.8597** | 0.7787 |
| cl_v6_fair | 0.8486 | 0.7884 | **0.8978** | <span style="color:red"><strong>0.8556</strong></span> | 0.6337 | <span style="color:red"><strong>0.9014</strong></span> | <span style="color:red"><strong>0.8424</strong></span> | <span style="color:red"><strong>0.8758</strong></span> | <span style="color:red"><strong>0.7851</strong></span> | **0.8616** | **0.7865** |

##### Aggregate mean across Specific 500-gene datasets

Latent variables: metric=AUROC, negative_protocol=full_candidate, network_group=Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.7777 |
| baseline | <span style="color:red"><strong>0.8113</strong></span> |
| scGPT_human | 0.7851 |
| v4_bias_rec_best | 0.7765 |
| v4_plain_best | 0.8072 |
| v4_type_pe_best | 0.7944 |
| scconcept | 0.7406 |
| scconcept_encoded | 0.7302 |
| cl_scratch_v5 | 0.7771 |
| cl_v6_fair | 0.7672 |

##### Aggregate mean across Specific 1000-gene datasets

Latent variables: metric=AUROC, negative_protocol=full_candidate, network_group=Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.8652 |
| baseline | 0.8687 |
| scGPT_human | 0.8640 |
| v4_bias_rec_best | 0.8650 |
| v4_plain_best | 0.8657 |
| v4_type_pe_best | 0.8675 |
| scconcept | 0.8343 |
| scconcept_encoded | 0.8439 |
| cl_scratch_v5 | 0.8663 |
| cl_v6_fair | <span style="color:red"><strong>0.8735</strong></span> |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.8906** | **0.8460** | <span style="color:red"><strong>0.8513</strong></span> | <span style="color:red"><strong>0.8318</strong></span> | **0.8732** | **0.6444** | <span style="color:red"><strong>0.8718</strong></span> | **0.8408** | 0.8301 | 0.7985 | 0.8247 | **0.8292** |
| baseline | 0.8865 | 0.8450 | 0.8405 | 0.7533 | 0.8687 | 0.6128 | 0.8697 | 0.8306 | 0.8431 | 0.8032 | 0.8384 | 0.7872 |
| scGPT_human | 0.8661 | **0.8584** | 0.8369 | **0.8094** | 0.8545 | <span style="color:red"><strong>0.7449</strong></span> | 0.8611 | **0.8579** | 0.8410 | 0.8030 | 0.8383 | **0.8484** |
| v4_bias_rec_best | 0.8778 | 0.8418 | 0.8214 | **0.7937** | 0.8635 | **0.6719** | 0.8587 | <span style="color:red"><strong>0.8646</strong></span> | **0.8508** | <span style="color:red"><strong>0.8315</strong></span> | 0.8242 | **0.8423** |
| v4_plain_best | <span style="color:red"><strong>0.8984</strong></span> | **0.8665** | **0.8497** | **0.7972** | **0.8748** | **0.6904** | 0.8663 | **0.8423** | **0.8482** | 0.7833 | 0.8269 | <span style="color:red"><strong>0.8491</strong></span> |
| v4_type_pe_best | **0.8964** | <span style="color:red"><strong>0.8680</strong></span> | **0.8466** | **0.7722** | 0.8680 | **0.6781** | 0.8651 | 0.8206 | **0.8598** | 0.7935 | **0.8449** | **0.8336** |
| scconcept | 0.8412 | 0.8381 | 0.7886 | **0.7818** | 0.7650 | 0.5705 | 0.7993 | 0.7146 | 0.7988 | 0.7612 | 0.8093 | 0.7455 |
| scconcept_encoded | 0.8456 | 0.7989 | 0.7940 | 0.7166 | 0.7387 | **0.6547** | 0.8008 | 0.7486 | 0.7631 | 0.7112 | 0.7802 | 0.7335 |
| cl_scratch_v5 | **0.8901** | **0.8568** | 0.8258 | 0.7512 | <span style="color:red"><strong>0.8776</strong></span> | **0.6580** | **0.8698** | **0.8419** | **0.8505** | 0.7774 | **0.8441** | **0.8141** |
| cl_v6_fair | **0.8931** | **0.8531** | 0.8306 | **0.7725** | **0.8715** | **0.6627** | **0.8713** | **0.8505** | <span style="color:red"><strong>0.8620</strong></span> | 0.7811 | <span style="color:red"><strong>0.8546</strong></span> | **0.8229** |

##### Aggregate mean across Non-Specific 500-gene datasets

Latent variables: metric=AUROC, negative_protocol=full_candidate, network_group=Non-Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.7984** |
| baseline | 0.7720 |
| scGPT_human | <span style="color:red"><strong>0.8203</strong></span> |
| v4_bias_rec_best | **0.8076** |
| v4_plain_best | **0.8048** |
| v4_type_pe_best | **0.7943** |
| scconcept | 0.7353 |
| scconcept_encoded | 0.7272 |
| cl_scratch_v5 | **0.7832** |
| cl_v6_fair | **0.7905** |

##### Aggregate mean across Non-Specific 1000-gene datasets

Latent variables: metric=AUROC, negative_protocol=full_candidate, network_group=Non-Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.8570 |
| baseline | 0.8578 |
| scGPT_human | 0.8497 |
| v4_bias_rec_best | 0.8494 |
| v4_plain_best | **0.8607** |
| v4_type_pe_best | **0.8634** |
| scconcept | 0.8004 |
| scconcept_encoded | 0.7870 |
| cl_scratch_v5 | **0.8596** |
| cl_v6_fair | <span style="color:red"><strong>0.8639</strong></span> |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.8427 | 0.7640 | <span style="color:red"><strong>0.9021</strong></span> | 0.9037 | 0.9026 | **0.8602** | 0.8889 | <span style="color:red"><strong>0.9322</strong></span> | 0.8761 | **0.8521** | **0.8633** | **0.8690** |
| baseline | 0.8491 | 0.7796 | 0.8906 | <span style="color:red"><strong>0.9174</strong></span> | 0.9029 | 0.8596 | 0.8894 | 0.9076 | 0.8807 | 0.8289 | 0.8617 | 0.8545 |
| scGPT_human | 0.8379 | <span style="color:red"><strong>0.8775</strong></span> | **0.8972** | 0.9034 | 0.8920 | **0.8740** | **0.8916** | **0.9243** | 0.8778 | 0.7866 | 0.8580 | 0.8367 |
| v4_bias_rec_best | 0.8331 | **0.7964** | 0.8879 | 0.8990 | 0.8963 | **0.8674** | **0.8923** | 0.8989 | 0.8600 | **0.8325** | 0.8611 | **0.8648** |
| v4_plain_best | 0.8144 | **0.7925** | **0.8912** | 0.8978 | 0.9019 | **0.8869** | 0.8877 | 0.8949 | 0.8782 | 0.8209 | **0.8667** | **0.8669** |
| v4_type_pe_best | <span style="color:red"><strong>0.8520</strong></span> | **0.8115** | **0.8994** | 0.9087 | <span style="color:red"><strong>0.9064</strong></span> | **0.8709** | <span style="color:red"><strong>0.9053</strong></span> | 0.8955 | <span style="color:red"><strong>0.8828</strong></span> | <span style="color:red"><strong>0.8571</strong></span> | <span style="color:red"><strong>0.8865</strong></span> | **0.8553** |
| scconcept | 0.7705 | 0.7560 | 0.8494 | 0.7898 | 0.8353 | 0.7048 | 0.8361 | 0.8260 | 0.8154 | 0.6765 | 0.7940 | 0.7690 |
| scconcept_encoded | 0.7440 | 0.7258 | 0.8011 | 0.7920 | 0.8203 | 0.7396 | 0.8026 | 0.7942 | 0.7830 | 0.6602 | 0.7258 | 0.7562 |
| cl_scratch_v5 | 0.8363 | 0.7565 | 0.8884 | 0.8873 | 0.8992 | **0.8907** | 0.8881 | **0.9202** | 0.8742 | **0.8390** | **0.8826** | **0.8670** |
| cl_v6_fair | **0.8491** | 0.7684 | 0.8905 | 0.9004 | 0.8945 | <span style="color:red"><strong>0.8980</strong></span> | **0.8921** | 0.9070 | 0.8707 | 0.8068 | **0.8690** | <span style="color:red"><strong>0.8714</strong></span> |

##### Aggregate mean across STRING 500-gene datasets

Latent variables: metric=AUROC, negative_protocol=full_candidate, network_group=STRING, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.8635** |
| baseline | 0.8579 |
| scGPT_human | <span style="color:red"><strong>0.8671</strong></span> |
| v4_bias_rec_best | **0.8598** |
| v4_plain_best | **0.8600** |
| v4_type_pe_best | **0.8665** |
| scconcept | 0.7537 |
| scconcept_encoded | 0.7447 |
| cl_scratch_v5 | **0.8601** |
| cl_v6_fair | **0.8587** |

##### Aggregate mean across STRING 1000-gene datasets

Latent variables: metric=AUROC, negative_protocol=full_candidate, network_group=STRING, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.8793** |
| baseline | 0.8791 |
| scGPT_human | 0.8758 |
| v4_bias_rec_best | 0.8718 |
| v4_plain_best | 0.8734 |
| v4_type_pe_best | <span style="color:red"><strong>0.8888</strong></span> |
| scconcept | 0.8168 |
| scconcept_encoded | 0.7795 |
| cl_scratch_v5 | 0.8781 |
| cl_v6_fair | 0.8777 |

## AUPRC (Main)

### Negative protocol: tf_stratified_1to10

Latent variables: metric=AUPRC, negative_protocol=tf_stratified_1to10, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.4650 | 0.3945 | 0.7451 | **0.3619** | 0.1333 | 0.8919 | 0.7811 | <span style="color:red"><strong>0.8685</strong></span> | **0.8067** | <span style="color:red"><strong>0.8898</strong></span> | <span style="color:red"><strong>0.8501</strong></span> |
| baseline | <span style="color:red"><strong>0.4835</strong></span> | 0.4243 | 0.7670 | 0.3602 | 0.1704 | 0.8923 | 0.7898 | 0.8572 | 0.7764 | 0.8772 | 0.8176 |
| scGPT_human | 0.4802 | **0.4285** | 0.7351 | 0.3572 | <span style="color:red"><strong>0.2207</strong></span> | 0.8837 | 0.7621 | 0.8556 | **0.7924** | **0.8894** | **0.8225** |
| v4_bias_rec_best | 0.4585 | 0.4214 | 0.7518 | **0.3826** | 0.0860 | 0.8908 | 0.7745 | **0.8638** | **0.7960** | **0.8811** | **0.8260** |
| v4_plain_best | 0.4798 | 0.4018 | 0.7629 | <span style="color:red"><strong>0.3959</strong></span> | **0.1827** | 0.8894 | 0.7579 | **0.8621** | **0.7821** | **0.8782** | **0.8421** |
| v4_type_pe_best | 0.4798 | **0.4297** | 0.7618 | **0.3605** | 0.1540 | 0.8917 | <span style="color:red"><strong>0.7987</strong></span> | **0.8601** | **0.7913** | **0.8867** | **0.8339** |
| scconcept | 0.3888 | 0.3954 | 0.6809 | 0.3012 | **0.2064** | 0.8665 | 0.7010 | 0.8135 | 0.7500 | 0.8733 | 0.7585 |
| scconcept_encoded | 0.4057 | 0.3606 | 0.6534 | 0.2921 | 0.0943 | 0.8606 | 0.7328 | 0.8178 | 0.7561 | 0.8560 | 0.7590 |
| cl_scratch_v5 | 0.4542 | <span style="color:red"><strong>0.4427</strong></span> | 0.7550 | **0.3953** | 0.1421 | 0.8897 | 0.7853 | **0.8648** | **0.8056** | **0.8809** | **0.8183** |
| cl_v6_fair | 0.4322 | 0.3744 | <span style="color:red"><strong>0.7685</strong></span> | **0.3948** | 0.1392 | <span style="color:red"><strong>0.8937</strong></span> | 0.7747 | **0.8656** | <span style="color:red"><strong>0.8129</strong></span> | **0.8823** | **0.8271** |

##### Aggregate mean across Specific 500-gene datasets

Latent variables: metric=AUPRC, negative_protocol=tf_stratified_1to10, network_group=Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.5931 |
| baseline | 0.5957 |
| scGPT_human | <span style="color:red"><strong>0.6052</strong></span> |
| v4_bias_rec_best | 0.5808 |
| v4_plain_best | 0.5933 |
| v4_type_pe_best | **0.6015** |
| scconcept | 0.5622 |
| scconcept_encoded | 0.5406 |
| cl_scratch_v5 | **0.5988** |
| cl_v6_fair | 0.5856 |

##### Aggregate mean across Specific 1000-gene datasets

Latent variables: metric=AUPRC, negative_protocol=tf_stratified_1to10, network_group=Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.7037 |
| baseline | 0.7062 |
| scGPT_human | 0.7002 |
| v4_bias_rec_best | 0.7048 |
| v4_plain_best | <span style="color:red"><strong>0.7114</strong></span> |
| v4_type_pe_best | **0.7068** |
| scconcept | 0.6540 |
| scconcept_encoded | 0.6476 |
| cl_scratch_v5 | **0.7067** |
| cl_v6_fair | 0.7062 |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.2320 | 0.2242 | 0.2621 | **0.2301** | **0.4104** | 0.2820 | **0.3718** | **0.3439** | **0.3494** | 0.2333 | **0.3089** | **0.2885** |
| baseline | 0.2374 | 0.2264 | 0.2795 | 0.2235 | 0.3821 | 0.4860 | 0.3613 | 0.3365 | 0.3182 | 0.2759 | 0.2754 | 0.2731 |
| scGPT_human | 0.2205 | <span style="color:red"><strong>0.2417</strong></span> | <span style="color:red"><strong>0.3495</strong></span> | <span style="color:red"><strong>0.3189</strong></span> | **0.4045** | 0.3009 | 0.3451 | <span style="color:red"><strong>0.4245</strong></span> | <span style="color:red"><strong>0.3821</strong></span> | <span style="color:red"><strong>0.4093</strong></span> | <span style="color:red"><strong>0.3398</strong></span> | <span style="color:red"><strong>0.4063</strong></span> |
| v4_bias_rec_best | 0.2096 | 0.1685 | 0.2234 | **0.2520** | 0.3757 | 0.4168 | 0.3392 | **0.3569** | **0.3773** | 0.2345 | **0.3012** | **0.2849** |
| v4_plain_best | 0.2217 | 0.2072 | **0.2848** | **0.2739** | 0.3634 | 0.3879 | 0.3552 | **0.3510** | **0.3241** | 0.2636 | 0.2686 | **0.3602** |
| v4_type_pe_best | <span style="color:red"><strong>0.2613</strong></span> | 0.1588 | **0.2883** | 0.1879 | **0.3830** | 0.3758 | 0.3478 | **0.3618** | **0.3420** | 0.2751 | **0.3195** | **0.4016** |
| scconcept | 0.1722 | 0.1743 | 0.2014 | 0.1349 | 0.2010 | 0.1560 | 0.1714 | 0.1179 | 0.1970 | 0.2357 | 0.2031 | 0.1576 |
| scconcept_encoded | 0.1504 | 0.1383 | 0.1830 | 0.1524 | 0.1656 | 0.1747 | 0.1742 | 0.1390 | 0.1852 | 0.1567 | 0.2009 | 0.1564 |
| cl_scratch_v5 | **0.2484** | 0.2197 | **0.2848** | **0.2268** | **0.4347** | 0.3722 | <span style="color:red"><strong>0.3903</strong></span> | 0.3223 | **0.3613** | 0.2240 | **0.3041** | **0.3479** |
| cl_v6_fair | **0.2432** | 0.1887 | 0.2745 | 0.1599 | <span style="color:red"><strong>0.4406</strong></span> | <span style="color:red"><strong>0.5096</strong></span> | 0.3485 | 0.3217 | **0.3612** | 0.2410 | **0.3304** | 0.2650 |

##### Aggregate mean across Non-Specific 500-gene datasets

Latent variables: metric=AUPRC, negative_protocol=tf_stratified_1to10, network_group=Non-Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.2670 |
| baseline | 0.3036 |
| scGPT_human | <span style="color:red"><strong>0.3503</strong></span> |
| v4_bias_rec_best | 0.2856 |
| v4_plain_best | **0.3073** |
| v4_type_pe_best | 0.2935 |
| scconcept | 0.1628 |
| scconcept_encoded | 0.1529 |
| cl_scratch_v5 | 0.2855 |
| cl_v6_fair | 0.2810 |

##### Aggregate mean across Non-Specific 1000-gene datasets

Latent variables: metric=AUPRC, negative_protocol=tf_stratified_1to10, network_group=Non-Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.3224** |
| baseline | 0.3090 |
| scGPT_human | <span style="color:red"><strong>0.3402</strong></span> |
| v4_bias_rec_best | 0.3044 |
| v4_plain_best | 0.3030 |
| v4_type_pe_best | **0.3236** |
| scconcept | 0.1910 |
| scconcept_encoded | 0.1765 |
| cl_scratch_v5 | **0.3373** |
| cl_v6_fair | **0.3331** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.3987 | 0.2852 | 0.5399 | **0.6128** | 0.5500 | 0.3464 | **0.6288** | **0.6565** | 0.4859 | **0.4456** | **0.4728** | **0.5042** |
| baseline | 0.4246 | 0.3138 | <span style="color:red"><strong>0.5550</strong></span> | 0.5806 | 0.5681 | 0.3583 | 0.6204 | 0.6304 | 0.5454 | 0.2662 | 0.4644 | 0.5012 |
| scGPT_human | <span style="color:red"><strong>0.4582</strong></span> | <span style="color:red"><strong>0.4131</strong></span> | 0.5272 | <span style="color:red"><strong>0.6196</strong></span> | 0.5268 | <span style="color:red"><strong>0.5559</strong></span> | <span style="color:red"><strong>0.6414</strong></span> | <span style="color:red"><strong>0.7016</strong></span> | <span style="color:red"><strong>0.5736</strong></span> | **0.2765** | <span style="color:red"><strong>0.5303</strong></span> | <span style="color:red"><strong>0.5406</strong></span> |
| v4_bias_rec_best | 0.3750 | 0.2451 | 0.5446 | 0.5664 | 0.5390 | **0.4608** | 0.6081 | **0.6503** | 0.4925 | <span style="color:red"><strong>0.5121</strong></span> | 0.4639 | **0.5402** |
| v4_plain_best | 0.3816 | 0.2748 | 0.5222 | 0.5799 | 0.5659 | **0.4109** | **0.6315** | **0.6477** | 0.4807 | **0.3074** | **0.4702** | **0.5344** |
| v4_type_pe_best | 0.4219 | **0.3834** | 0.5233 | 0.5784 | <span style="color:red"><strong>0.6014</strong></span> | 0.3546 | **0.6237** | **0.6341** | 0.5332 | **0.4569** | **0.4793** | 0.4936 |
| scconcept | 0.2093 | **0.3983** | 0.2853 | 0.2428 | 0.3274 | 0.2151 | 0.2896 | 0.2626 | 0.2125 | 0.1382 | 0.2414 | 0.3028 |
| scconcept_encoded | 0.1569 | 0.2549 | 0.2707 | 0.1792 | 0.2800 | 0.2170 | 0.2152 | 0.1849 | 0.1922 | 0.1365 | 0.2030 | 0.2433 |
| cl_scratch_v5 | 0.4113 | **0.3297** | 0.5369 | 0.5372 | 0.5639 | **0.4101** | 0.6182 | **0.6893** | **0.5594** | **0.3313** | **0.4983** | 0.4692 |
| cl_v6_fair | **0.4282** | **0.3271** | 0.5116 | **0.5829** | 0.5448 | **0.4168** | **0.6264** | 0.6187 | 0.5371 | **0.3794** | **0.4966** | 0.5001 |

##### Aggregate mean across STRING 500-gene datasets

Latent variables: metric=AUPRC, negative_protocol=tf_stratified_1to10, network_group=STRING, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.4751** |
| baseline | 0.4418 |
| scGPT_human | <span style="color:red"><strong>0.5179</strong></span> |
| v4_bias_rec_best | **0.4958** |
| v4_plain_best | **0.4592** |
| v4_type_pe_best | **0.4835** |
| scconcept | 0.2600 |
| scconcept_encoded | 0.2026 |
| cl_scratch_v5 | **0.4611** |
| cl_v6_fair | **0.4708** |

##### Aggregate mean across STRING 1000-gene datasets

Latent variables: metric=AUPRC, negative_protocol=tf_stratified_1to10, network_group=STRING, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.5127 |
| baseline | 0.5297 |
| scGPT_human | <span style="color:red"><strong>0.5429</strong></span> |
| v4_bias_rec_best | 0.5038 |
| v4_plain_best | 0.5087 |
| v4_type_pe_best | **0.5305** |
| scconcept | 0.2609 |
| scconcept_encoded | 0.2197 |
| cl_scratch_v5 | **0.5313** |
| cl_v6_fair | 0.5241 |

### Negative protocol: full_candidate

Latent variables: metric=AUPRC, negative_protocol=full_candidate, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.4392 | 0.3885 | 0.7633 | 0.3678 | 0.1196 | **0.8914** | 0.7493 | **0.8577** | **0.8097** | <span style="color:red"><strong>0.8932</strong></span> | **0.8338** |
| baseline | 0.4586 | 0.4212 | 0.7653 | 0.3847 | <span style="color:red"><strong>0.1930</strong></span> | 0.8812 | 0.7737 | 0.8571 | 0.7946 | 0.8818 | 0.8295 |
| scGPT_human | 0.4440 | 0.4162 | 0.7275 | 0.3744 | 0.1727 | **0.8922** | 0.7445 | 0.8563 | 0.7873 | **0.8825** | 0.8262 |
| v4_bias_rec_best | 0.4570 | 0.4159 | **0.7699** | 0.3441 | 0.1298 | **0.8912** | 0.7719 | 0.8518 | **0.7972** | **0.8823** | **0.8306** |
| v4_plain_best | **0.4739** | 0.4159 | <span style="color:red"><strong>0.7825</strong></span> | 0.3406 | 0.1651 | **0.8900** | **0.7760** | **0.8589** | 0.7870 | **0.8837** | 0.8280 |
| v4_type_pe_best | <span style="color:red"><strong>0.4836</strong></span> | <span style="color:red"><strong>0.4271</strong></span> | **0.7819** | 0.3294 | 0.1315 | **0.8887** | **0.7888** | 0.8551 | **0.7989** | **0.8837** | <span style="color:red"><strong>0.8436</strong></span> |
| scconcept | 0.4082 | 0.4115 | 0.6711 | 0.2498 | 0.1838 | 0.8671 | 0.6769 | 0.8226 | 0.7487 | 0.8634 | 0.7617 |
| scconcept_encoded | 0.4094 | 0.3858 | 0.6720 | 0.2890 | 0.0609 | 0.8681 | 0.7163 | 0.8298 | 0.7596 | 0.8613 | 0.7722 |
| cl_scratch_v5 | 0.4514 | 0.4189 | 0.7645 | 0.3663 | 0.1078 | **0.8887** | <span style="color:red"><strong>0.7903</strong></span> | **0.8637** | 0.7899 | **0.8830** | **0.8318** |
| cl_v6_fair | 0.4509 | 0.3830 | **0.7690** | <span style="color:red"><strong>0.4064</strong></span> | 0.1044 | <span style="color:red"><strong>0.8968</strong></span> | **0.7897** | <span style="color:red"><strong>0.8655</strong></span> | <span style="color:red"><strong>0.8147</strong></span> | **0.8842** | **0.8361** |

##### Aggregate mean across Specific 500-gene datasets

Latent variables: metric=AUPRC, negative_protocol=full_candidate, network_group=Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.5801 |
| baseline | <span style="color:red"><strong>0.6024</strong></span> |
| scGPT_human | 0.5894 |
| v4_bias_rec_best | 0.5891 |
| v4_plain_best | 0.5944 |
| v4_type_pe_best | 0.5980 |
| scconcept | 0.5565 |
| scconcept_encoded | 0.5390 |
| cl_scratch_v5 | 0.5877 |
| cl_v6_fair | 0.5856 |

##### Aggregate mean across Specific 1000-gene datasets

Latent variables: metric=AUPRC, negative_protocol=full_candidate, network_group=Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.7021 |
| baseline | 0.7048 |
| scGPT_human | 0.6961 |
| v4_bias_rec_best | 0.6994 |
| v4_plain_best | **0.7049** |
| v4_type_pe_best | 0.7037 |
| scconcept | 0.6471 |
| scconcept_encoded | 0.6549 |
| cl_scratch_v5 | 0.7030 |
| cl_v6_fair | <span style="color:red"><strong>0.7121</strong></span> |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.1548** | 0.2019 | **0.1446** | **0.1237** | **0.2209** | **0.1332** | **0.2591** | **0.2519** | <span style="color:red"><strong>0.2683</strong></span> | 0.1488 | **0.2069** | **0.1677** |
| baseline | 0.1545 | <span style="color:red"><strong>0.2235</strong></span> | 0.1155 | 0.0906 | 0.1818 | 0.1265 | 0.2530 | 0.2107 | 0.2330 | 0.1621 | 0.1758 | 0.1387 |
| scGPT_human | 0.1514 | 0.2007 | <span style="color:red"><strong>0.2079</strong></span> | <span style="color:red"><strong>0.1301</strong></span> | <span style="color:red"><strong>0.2389</strong></span> | 0.0798 | **0.2567** | <span style="color:red"><strong>0.2685</strong></span> | **0.2600** | <span style="color:red"><strong>0.2106</strong></span> | **0.2007** | <span style="color:red"><strong>0.3169</strong></span> |
| v4_bias_rec_best | 0.1514 | 0.1783 | 0.1020 | **0.1244** | 0.1786 | 0.1227 | 0.2232 | **0.2353** | **0.2507** | 0.1573 | 0.1574 | **0.2603** |
| v4_plain_best | **0.1676** | 0.1891 | **0.1222** | **0.1270** | **0.2157** | 0.0791 | 0.2217 | 0.1853 | **0.2580** | 0.1506 | <span style="color:red"><strong>0.2341</strong></span> | **0.2768** |
| v4_type_pe_best | <span style="color:red"><strong>0.1715</strong></span> | 0.2045 | **0.1448** | **0.1047** | 0.1798 | 0.1172 | 0.2429 | **0.2299** | **0.2551** | **0.1991** | **0.2087** | **0.2655** |
| scconcept | 0.1303 | 0.1346 | 0.0736 | 0.0760 | 0.1067 | 0.0653 | 0.0797 | 0.0703 | 0.1017 | 0.0972 | 0.0989 | 0.0883 |
| scconcept_encoded | 0.1120 | 0.0925 | 0.0645 | 0.0473 | 0.0749 | 0.0233 | 0.0758 | 0.0824 | 0.0711 | 0.0721 | 0.0753 | 0.0888 |
| cl_scratch_v5 | **0.1668** | 0.2183 | **0.1643** | **0.1012** | **0.2320** | **0.1342** | <span style="color:red"><strong>0.2738</strong></span> | **0.2562** | **0.2407** | 0.1296 | **0.1908** | **0.2543** |
| cl_v6_fair | **0.1589** | 0.1989 | **0.1262** | **0.1282** | **0.1946** | <span style="color:red"><strong>0.1916</strong></span> | 0.2241 | **0.2202** | 0.2285 | 0.1508 | **0.1983** | **0.2819** |

##### Aggregate mean across Non-Specific 500-gene datasets

Latent variables: metric=AUPRC, negative_protocol=full_candidate, network_group=Non-Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.1712** |
| baseline | 0.1587 |
| scGPT_human | <span style="color:red"><strong>0.2011</strong></span> |
| v4_bias_rec_best | **0.1797** |
| v4_plain_best | **0.1680** |
| v4_type_pe_best | **0.1868** |
| scconcept | 0.0886 |
| scconcept_encoded | 0.0677 |
| cl_scratch_v5 | **0.1823** |
| cl_v6_fair | **0.1953** |

##### Aggregate mean across Non-Specific 1000-gene datasets

Latent variables: metric=AUPRC, negative_protocol=full_candidate, network_group=Non-Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.2091** |
| baseline | 0.1856 |
| scGPT_human | <span style="color:red"><strong>0.2193</strong></span> |
| v4_bias_rec_best | 0.1772 |
| v4_plain_best | **0.2032** |
| v4_type_pe_best | **0.2005** |
| scconcept | 0.0985 |
| scconcept_encoded | 0.0789 |
| cl_scratch_v5 | **0.2114** |
| cl_v6_fair | **0.1884** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | <span style="color:red"><strong>0.2633</strong></span> | 0.1699 | 0.4407 | 0.5099 | 0.4361 | **0.3563** | <span style="color:red"><strong>0.5105</strong></span> | **0.5577** | **0.3614** | **0.2107** | <span style="color:red"><strong>0.3464</strong></span> | **0.3080** |
| baseline | 0.2484 | 0.1700 | <span style="color:red"><strong>0.4466</strong></span> | 0.5505 | 0.4565 | 0.3554 | 0.4971 | 0.5255 | 0.3591 | 0.1569 | 0.2994 | 0.2705 |
| scGPT_human | 0.2283 | <span style="color:red"><strong>0.3573</strong></span> | 0.4324 | <span style="color:red"><strong>0.5691</strong></span> | 0.4391 | **0.3946** | **0.5010** | <span style="color:red"><strong>0.6067</strong></span> | **0.3843** | **0.1887** | **0.3409** | **0.3400** |
| v4_bias_rec_best | 0.2085 | 0.1344 | 0.4212 | 0.4852 | 0.4315 | **0.4145** | 0.4764 | **0.5641** | 0.3162 | <span style="color:red"><strong>0.2221</strong></span> | 0.2651 | **0.3476** |
| v4_plain_best | 0.2453 | 0.1652 | 0.4215 | 0.4862 | **0.4592** | <span style="color:red"><strong>0.4771</strong></span> | **0.5005** | **0.5474** | **0.3872** | **0.1908** | **0.3289** | **0.3299** |
| v4_type_pe_best | 0.2393 | 0.1532 | 0.4336 | 0.5148 | <span style="color:red"><strong>0.4832</strong></span> | **0.3867** | 0.4932 | **0.5644** | **0.3800** | **0.1678** | **0.3237** | <span style="color:red"><strong>0.4148</strong></span> |
| scconcept | 0.0477 | 0.1494 | 0.2499 | 0.1498 | 0.2192 | 0.0989 | 0.1407 | 0.1256 | 0.0968 | 0.0506 | 0.0995 | 0.1544 |
| scconcept_encoded | 0.0397 | 0.0820 | 0.1287 | 0.1374 | 0.1909 | 0.0749 | 0.1380 | 0.1323 | 0.0586 | 0.0357 | 0.0422 | 0.1117 |
| cl_scratch_v5 | 0.2191 | 0.1639 | 0.4326 | 0.4888 | 0.4558 | **0.4251** | **0.5021** | **0.5903** | <span style="color:red"><strong>0.3954</strong></span> | 0.1408 | **0.3157** | **0.3411** |
| cl_v6_fair | 0.2400 | 0.1545 | 0.4304 | 0.4661 | **0.4627** | **0.4575** | **0.5070** | 0.5243 | 0.3539 | 0.1503 | **0.3428** | **0.3533** |

##### Aggregate mean across STRING 500-gene datasets

Latent variables: metric=AUPRC, negative_protocol=full_candidate, network_group=STRING, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.3521** |
| baseline | 0.3381 |
| scGPT_human | <span style="color:red"><strong>0.4094</strong></span> |
| v4_bias_rec_best | **0.3613** |
| v4_plain_best | **0.3661** |
| v4_type_pe_best | **0.3669** |
| scconcept | 0.1214 |
| scconcept_encoded | 0.0957 |
| cl_scratch_v5 | **0.3584** |
| cl_v6_fair | **0.3510** |

##### Aggregate mean across STRING 1000-gene datasets

Latent variables: metric=AUPRC, negative_protocol=full_candidate, network_group=STRING, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | <span style="color:red"><strong>0.3931</strong></span> |
| baseline | 0.3845 |
| scGPT_human | **0.3877** |
| v4_bias_rec_best | 0.3531 |
| v4_plain_best | **0.3904** |
| v4_type_pe_best | **0.3922** |
| scconcept | 0.1423 |
| scconcept_encoded | 0.0997 |
| cl_scratch_v5 | **0.3868** |
| cl_v6_fair | **0.3895** |

## AUPRC_LIFT (Main)

### Negative protocol: tf_stratified_1to10

Latent variables: metric=AUPRC_LIFT, negative_protocol=tf_stratified_1to10, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 1.6231 | 1.4798 | 2.3781 | **2.1612** | 1.4666 | 1.4510 | 1.6319 | <span style="color:red"><strong>1.5025</strong></span> | **1.4585** | <span style="color:red"><strong>1.4266</strong></span> | <span style="color:red"><strong>1.4437</strong></span> |
| baseline | <span style="color:red"><strong>1.6875</strong></span> | 1.5918 | 2.4479 | 2.1510 | 1.8741 | 1.4517 | 1.6501 | 1.4830 | 1.4038 | 1.4064 | 1.3884 |
| scGPT_human | 1.6759 | **1.6075** | 2.3461 | 2.1330 | <span style="color:red"><strong>2.4280</strong></span> | 1.4376 | 1.5923 | 1.4802 | **1.4326** | **1.4259** | **1.3968** |
| v4_bias_rec_best | 1.6005 | 1.5808 | 2.3994 | **2.2847** | 0.9464 | 1.4492 | 1.6182 | **1.4944** | **1.4391** | **1.4127** | **1.4027** |
| v4_plain_best | 1.6748 | 1.5072 | 2.4350 | <span style="color:red"><strong>2.3639</strong></span> | **2.0096** | 1.4469 | 1.5835 | **1.4914** | **1.4141** | **1.4079** | **1.4301** |
| v4_type_pe_best | 1.6745 | **1.6119** | 2.4316 | **2.1530** | 1.6936 | 1.4507 | <span style="color:red"><strong>1.6687</strong></span> | **1.4879** | **1.4308** | **1.4216** | **1.4162** |
| scconcept | 1.3569 | 1.4832 | 2.1732 | 1.7988 | **2.2700** | 1.4096 | 1.4646 | 1.4074 | 1.3560 | 1.4002 | 1.2880 |
| scconcept_encoded | 1.4161 | 1.3528 | 2.0856 | 1.7441 | 1.0371 | 1.4001 | 1.5311 | 1.4149 | 1.3671 | 1.3725 | 1.2889 |
| cl_scratch_v5 | 1.5852 | <span style="color:red"><strong>1.6610</strong></span> | 2.4098 | **2.3603** | 1.5633 | 1.4475 | 1.6408 | **1.4962** | **1.4565** | **1.4124** | **1.3895** |
| cl_v6_fair | 1.5084 | 1.4045 | <span style="color:red"><strong>2.4527</strong></span> | **2.3576** | 1.5313 | <span style="color:red"><strong>1.4540</strong></span> | 1.6185 | **1.4975** | <span style="color:red"><strong>1.4697</strong></span> | **1.4145** | **1.4045** |

##### Aggregate mean across Specific 500-gene datasets

Latent variables: metric=AUPRC_LIFT, negative_protocol=tf_stratified_1to10, network_group=Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 1.4961 |
| baseline | 1.5817 |
| scGPT_human | <span style="color:red"><strong>1.6915</strong></span> |
| v4_bias_rec_best | 1.3974 |
| v4_plain_best | **1.5889** |
| v4_type_pe_best | 1.5642 |
| scconcept | 1.5723 |
| scconcept_encoded | 1.3154 |
| cl_scratch_v5 | 1.5422 |
| cl_v6_fair | 1.4857 |

##### Aggregate mean across Specific 1000-gene datasets

Latent variables: metric=AUPRC_LIFT, negative_protocol=tf_stratified_1to10, network_group=Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 1.7571 |
| baseline | 1.7713 |
| scGPT_human | 1.7498 |
| v4_bias_rec_best | **1.7735** |
| v4_plain_best | <span style="color:red"><strong>1.8033</strong></span> |
| v4_type_pe_best | 1.7699 |
| scconcept | 1.5910 |
| scconcept_encoded | 1.5722 |
| cl_scratch_v5 | **1.7852** |
| cl_v6_fair | **1.7808** |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 2.0042 | 2.0069 | 2.8828 | **2.5311** | **4.5139** | 3.1021 | **3.8354** | **3.4864** | **3.7316** | 2.5658 | **3.3316** | **3.1731** |
| baseline | 2.0513 | 2.0267 | 3.0748 | 2.4581 | 4.2026 | 5.3455 | 3.7265 | 3.4110 | 3.3983 | 3.0352 | 2.9695 | 3.0039 |
| scGPT_human | 1.9048 | <span style="color:red"><strong>2.1635</strong></span> | <span style="color:red"><strong>3.8448</strong></span> | <span style="color:red"><strong>3.5077</strong></span> | **4.4492** | 3.3104 | 3.5596 | <span style="color:red"><strong>4.3025</strong></span> | <span style="color:red"><strong>4.0799</strong></span> | <span style="color:red"><strong>4.5025</strong></span> | <span style="color:red"><strong>3.6645</strong></span> | <span style="color:red"><strong>4.4697</strong></span> |
| v4_bias_rec_best | 1.8105 | 1.5089 | 2.4578 | **2.7725** | 4.1325 | 4.5844 | 3.4986 | **3.6173** | **4.0287** | 2.5797 | **3.2483** | **3.1344** |
| v4_plain_best | 1.9154 | 1.8547 | **3.1326** | **3.0125** | 3.9970 | 4.2674 | 3.6633 | **3.5574** | **3.4610** | 2.8991 | 2.8969 | **3.9621** |
| v4_type_pe_best | <span style="color:red"><strong>2.2572</strong></span> | 1.4216 | **3.1712** | 2.0674 | **4.2127** | 4.1343 | 3.5879 | **3.6671** | **3.6522** | 3.0259 | **3.4455** | **4.4172** |
| scconcept | 1.4882 | 1.5608 | 2.2150 | 1.4840 | 2.2108 | 1.7165 | 1.7677 | 1.1953 | 2.1035 | 2.5925 | 2.1907 | 1.7336 |
| scconcept_encoded | 1.2991 | 1.2381 | 2.0127 | 1.6768 | 1.8215 | 1.9217 | 1.7965 | 1.4094 | 1.9781 | 1.7233 | 2.1670 | 1.7204 |
| cl_scratch_v5 | **2.1463** | 1.9672 | **3.1325** | **2.4946** | **4.7814** | 4.0940 | <span style="color:red"><strong>4.0256</strong></span> | 3.2674 | **3.8583** | 2.4641 | **3.2799** | **3.8264** |
| cl_v6_fair | **2.1013** | 1.6890 | 3.0194 | 1.7586 | <span style="color:red"><strong>4.8466</strong></span> | <span style="color:red"><strong>5.6059</strong></span> | 3.5943 | 3.2606 | **3.8568** | 2.6508 | **3.5633** | 2.9150 |

##### Aggregate mean across Non-Specific 500-gene datasets

Latent variables: metric=AUPRC_LIFT, negative_protocol=tf_stratified_1to10, network_group=Non-Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 2.8109 |
| baseline | 3.2134 |
| scGPT_human | <span style="color:red"><strong>3.7094</strong></span> |
| v4_bias_rec_best | 3.0329 |
| v4_plain_best | **3.2589** |
| v4_type_pe_best | 3.1222 |
| scconcept | 1.7138 |
| scconcept_encoded | 1.6150 |
| cl_scratch_v5 | 3.0189 |
| cl_v6_fair | 2.9800 |

##### Aggregate mean across Non-Specific 1000-gene datasets

Latent variables: metric=AUPRC_LIFT, negative_protocol=tf_stratified_1to10, network_group=Non-Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **3.3833** |
| baseline | 3.2372 |
| scGPT_human | <span style="color:red"><strong>3.5838</strong></span> |
| v4_bias_rec_best | 3.1961 |
| v4_plain_best | 3.1777 |
| v4_type_pe_best | **3.3878** |
| scconcept | 1.9960 |
| scconcept_encoded | 1.8458 |
| cl_scratch_v5 | **3.5373** |
| cl_v6_fair | **3.4970** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 4.3854 | 3.1370 | 5.9394 | **6.7044** | 6.0503 | 3.6847 | **6.9166** | **7.1154** | 5.3451 | **4.9012** | **5.2011** | **5.5463** |
| baseline | 4.6705 | 3.4515 | <span style="color:red"><strong>6.1055</strong></span> | 6.3516 | 6.2492 | 3.8111 | 6.8247 | 6.8332 | 5.9997 | 2.9282 | 5.1084 | 5.5136 |
| scGPT_human | <span style="color:red"><strong>5.0404</strong></span> | <span style="color:red"><strong>4.5445</strong></span> | 5.7987 | <span style="color:red"><strong>6.7782</strong></span> | 5.7950 | <span style="color:red"><strong>5.9130</strong></span> | <span style="color:red"><strong>7.0553</strong></span> | <span style="color:red"><strong>7.6041</strong></span> | <span style="color:red"><strong>6.3091</strong></span> | **3.0416** | <span style="color:red"><strong>5.8332</strong></span> | <span style="color:red"><strong>5.9468</strong></span> |
| v4_bias_rec_best | 4.1250 | 2.6962 | 5.9905 | 6.1965 | 5.9288 | **4.9016** | 6.6890 | **7.0487** | 5.4173 | <span style="color:red"><strong>5.6332</strong></span> | 5.1024 | **5.9422** |
| v4_plain_best | 4.1976 | 3.0224 | 5.7441 | 6.3440 | 6.2249 | **4.3708** | **6.9469** | **7.0201** | 5.2877 | **3.3819** | **5.1725** | **5.8783** |
| v4_type_pe_best | 4.6408 | **4.2178** | 5.7559 | 6.3281 | <span style="color:red"><strong>6.6157</strong></span> | 3.7716 | **6.8602** | **6.8724** | 5.8650 | **5.0261** | **5.2723** | 5.4293 |
| scconcept | 2.3026 | **4.3818** | 3.1388 | 2.6563 | 3.6019 | 2.2880 | 3.1853 | 2.8457 | 2.3371 | 1.5200 | 2.6557 | 3.3309 |
| scconcept_encoded | 1.7258 | 2.8039 | 2.9773 | 1.9600 | 3.0796 | 2.3077 | 2.3671 | 2.0046 | 2.1141 | 1.5014 | 2.2331 | 2.6758 |
| cl_scratch_v5 | 4.5242 | **3.6271** | 5.9062 | 5.8773 | 6.2025 | **4.3622** | 6.8003 | **7.4710** | **6.1534** | **3.6438** | **5.4814** | 5.1616 |
| cl_v6_fair | **4.7097** | **3.5976** | 5.6274 | **6.3773** | 5.9932 | **4.4337** | **6.8909** | 6.7060 | 5.9080 | **4.1734** | **5.4631** | 5.5016 |

##### Aggregate mean across STRING 500-gene datasets

Latent variables: metric=AUPRC_LIFT, negative_protocol=tf_stratified_1to10, network_group=STRING, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **5.1815** |
| baseline | 4.8149 |
| scGPT_human | <span style="color:red"><strong>5.6380</strong></span> |
| v4_bias_rec_best | **5.4031** |
| v4_plain_best | **5.0029** |
| v4_type_pe_best | **5.2742** |
| scconcept | 2.8371 |
| scconcept_encoded | 2.2089 |
| cl_scratch_v5 | **5.0238** |
| cl_v6_fair | **5.1316** |

##### Aggregate mean across STRING 1000-gene datasets

Latent variables: metric=AUPRC_LIFT, negative_protocol=tf_stratified_1to10, network_group=STRING, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 5.6397 |
| baseline | 5.8263 |
| scGPT_human | <span style="color:red"><strong>5.9719</strong></span> |
| v4_bias_rec_best | 5.5422 |
| v4_plain_best | 5.5956 |
| v4_type_pe_best | **5.8350** |
| scconcept | 2.8702 |
| scconcept_encoded | 2.4162 |
| cl_scratch_v5 | **5.8447** |
| cl_v6_fair | 5.7654 |

### Negative protocol: full_candidate

Latent variables: metric=AUPRC_LIFT, negative_protocol=full_candidate, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 2.7079 | 2.3997 | 3.3116 | 4.8466 | 3.4526 | **1.8046** | 1.8493 | **1.7590** | **1.4639** | <span style="color:red"><strong>1.5810</strong></span> | **1.4068** |
| baseline | 2.8276 | 2.6017 | 3.3203 | 5.0696 | <span style="color:red"><strong>5.5715</strong></span> | 1.7837 | 1.9096 | 1.7578 | 1.4367 | 1.5609 | 1.3997 |
| scGPT_human | 2.7372 | 2.5710 | 3.1560 | 4.9334 | 4.9854 | **1.8060** | 1.8375 | 1.7562 | 1.4235 | **1.5621** | 1.3940 |
| v4_bias_rec_best | 2.8172 | 2.5692 | **3.3401** | 4.5353 | 3.7470 | **1.8040** | 1.9051 | 1.7470 | **1.4413** | **1.5617** | **1.4014** |
| v4_plain_best | **2.9214** | 2.5694 | <span style="color:red"><strong>3.3948</strong></span> | 4.4889 | 4.7659 | **1.8016** | **1.9153** | **1.7615** | 1.4229 | **1.5641** | 1.3971 |
| v4_type_pe_best | <span style="color:red"><strong>2.9813</strong></span> | <span style="color:red"><strong>2.6383</strong></span> | **3.3923** | 4.3404 | 3.7961 | **1.7989** | **1.9468** | 1.7538 | **1.4445** | **1.5642** | <span style="color:red"><strong>1.4234</strong></span> |
| scconcept | 2.5169 | 2.5419 | 2.9115 | 3.2919 | 5.3065 | 1.7554 | 1.6706 | 1.6872 | 1.3536 | 1.5283 | 1.2851 |
| scconcept_encoded | 2.5242 | 2.3836 | 2.9154 | 3.8090 | 1.7571 | 1.7572 | 1.7680 | 1.7018 | 1.3733 | 1.5246 | 1.3028 |
| cl_scratch_v5 | 2.7832 | 2.5877 | 3.3167 | 4.8272 | 3.1130 | **1.7991** | <span style="color:red"><strong>1.9505</strong></span> | **1.7714** | 1.4281 | **1.5630** | **1.4035** |
| cl_v6_fair | 2.7800 | 2.3660 | **3.3363** | <span style="color:red"><strong>5.3563</strong></span> | 3.0150 | <span style="color:red"><strong>1.8153</strong></span> | **1.9491** | <span style="color:red"><strong>1.7751</strong></span> | <span style="color:red"><strong>1.4730</strong></span> | **1.5651** | **1.4108** |

##### Aggregate mean across Specific 500-gene datasets

Latent variables: metric=AUPRC_LIFT, negative_protocol=full_candidate, network_group=Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 2.1145 |
| baseline | <span style="color:red"><strong>2.5838</strong></span> |
| scGPT_human | 2.4423 |
| v4_bias_rec_best | 2.2128 |
| v4_plain_best | 2.4141 |
| v4_type_pe_best | 2.2498 |
| scconcept | 2.4315 |
| scconcept_encoded | 1.7170 |
| cl_scratch_v5 | 2.0966 |
| cl_v6_fair | 2.0428 |

##### Aggregate mean across Specific 1000-gene datasets

Latent variables: metric=AUPRC_LIFT, negative_protocol=full_candidate, network_group=Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 2.6684 |
| baseline | 2.7200 |
| scGPT_human | 2.6585 |
| v4_bias_rec_best | 2.6342 |
| v4_plain_best | 2.6554 |
| v4_type_pe_best | 2.6385 |
| scconcept | 2.2818 |
| scconcept_encoded | 2.3720 |
| cl_scratch_v5 | 2.6768 |
| cl_v6_fair | <span style="color:red"><strong>2.7713</strong></span> |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **9.3147** | 8.9030 | **13.0763** | **7.4170** | **15.4089** | **9.8176** | **16.1215** | **9.2746** | <span style="color:red"><strong>21.6974</strong></span> | 6.6323 | **15.6081** | **6.7548** |
| baseline | 9.3012 | <span style="color:red"><strong>9.8550</strong></span> | 10.4433 | 5.4356 | 12.6841 | 9.3292 | 15.7458 | 7.7592 | 18.8433 | 7.2224 | 13.2607 | 5.5884 |
| scGPT_human | 9.1115 | 8.8506 | <span style="color:red"><strong>18.7911</strong></span> | <span style="color:red"><strong>7.8038</strong></span> | <span style="color:red"><strong>16.6627</strong></span> | 5.8807 | **15.9744** | <span style="color:red"><strong>9.8867</strong></span> | **21.0316** | <span style="color:red"><strong>9.3851</strong></span> | **15.1446** | <span style="color:red"><strong>12.7637</strong></span> |
| v4_bias_rec_best | 9.1110 | 7.8635 | 9.2224 | **7.4618** | 12.4601 | 9.0440 | 13.8877 | **8.6620** | **20.2765** | 7.0108 | 11.8768 | **10.4858** |
| v4_plain_best | **10.0900** | 8.3404 | **11.0457** | **7.6157** | **15.0506** | 5.8328 | 13.7982 | 6.8233 | **20.8712** | 6.7131 | <span style="color:red"><strong>17.6623</strong></span> | **11.1487** |
| v4_type_pe_best | <span style="color:red"><strong>10.3207</strong></span> | 9.0156 | **13.0913** | **6.2757** | 12.5456 | 8.6422 | 15.1114 | **8.4660** | **20.6348** | **8.8739** | **15.7418** | **10.6961** |
| scconcept | 7.8424 | 5.9363 | 6.6508 | 4.5599 | 7.4418 | 4.8148 | 4.9595 | 2.5866 | 8.2279 | 4.3336 | 7.4649 | 3.5562 |
| scconcept_encoded | 6.7415 | 4.0800 | 5.8311 | 2.8376 | 5.2268 | 1.7161 | 4.7187 | 3.0320 | 5.7471 | 3.2120 | 5.6804 | 3.5756 |
| cl_scratch_v5 | **10.0390** | 9.6253 | **14.8518** | **6.0696** | **16.1839** | **9.8926** | <span style="color:red"><strong>17.0393</strong></span> | **9.4331** | **19.4713** | 5.7753 | **14.3934** | **10.2454** |
| cl_v6_fair | **9.5626** | 8.7690 | **11.4073** | **7.6893** | **13.5779** | <span style="color:red"><strong>14.1269</strong></span> | 13.9445 | **8.1058** | 18.4838 | 6.7181 | **14.9580** | **11.3554** |

##### Aggregate mean across Non-Specific 500-gene datasets

Latent variables: metric=AUPRC_LIFT, negative_protocol=full_candidate, network_group=Non-Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **8.1332** |
| baseline | 7.5316 |
| scGPT_human | **9.0951** |
| v4_bias_rec_best | **8.4213** |
| v4_plain_best | **7.7457** |
| v4_type_pe_best | **8.6616** |
| scconcept | 4.2979 |
| scconcept_encoded | 3.0756 |
| cl_scratch_v5 | **8.5069** |
| cl_v6_fair | <span style="color:red"><strong>9.4608</strong></span> |

##### Aggregate mean across Non-Specific 1000-gene datasets

Latent variables: metric=AUPRC_LIFT, negative_protocol=full_candidate, network_group=Non-Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **15.2045** |
| baseline | 13.3797 |
| scGPT_human | <span style="color:red"><strong>16.1193</strong></span> |
| v4_bias_rec_best | 12.8058 |
| v4_plain_best | **14.7530** |
| v4_type_pe_best | **14.5743** |
| scconcept | 7.0979 |
| scconcept_encoded | 5.6576 |
| cl_scratch_v5 | **15.3298** |
| cl_v6_fair | **13.6557** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | <span style="color:red"><strong>27.5724</strong></span> | 14.7483 | 25.0754 | 18.4848 | 19.2620 | **13.7444** | <span style="color:red"><strong>33.5703</strong></span> | **26.0161** | **36.8470** | **17.2883** | <span style="color:red"><strong>35.6446</strong></span> | **22.0118** |
| baseline | 26.0197 | 14.7561 | <span style="color:red"><strong>25.4086</strong></span> | 19.9594 | 20.1643 | 13.7115 | 32.6912 | 24.5131 | 36.6067 | 12.8669 | 30.8046 | 19.3318 |
| scGPT_human | 23.9111 | <span style="color:red"><strong>31.0030</strong></span> | 24.6001 | <span style="color:red"><strong>20.6329</strong></span> | 19.3948 | **15.2234** | **32.9451** | <span style="color:red"><strong>28.3019</strong></span> | **39.1794** | **15.4809** | **35.0796** | **24.3012** |
| v4_bias_rec_best | 21.8359 | 11.6616 | 23.9656 | 17.5895 | 19.0591 | **15.9911** | 31.3245 | **26.3110** | 32.2372 | <span style="color:red"><strong>18.2161</strong></span> | 27.2789 | **24.8432** |
| v4_plain_best | 25.6916 | 14.3332 | 23.9796 | 17.6248 | **20.2817** | <span style="color:red"><strong>18.4030</strong></span> | **32.9133** | **25.5315** | **39.4743** | **15.6527** | **33.8483** | **23.5815** |
| v4_type_pe_best | 25.0587 | 13.2936 | 24.6724 | 18.6629 | <span style="color:red"><strong>21.3439</strong></span> | **14.9156** | 32.4320 | **26.3256** | **38.7361** | **13.7625** | **33.3117** | <span style="color:red"><strong>29.6484</strong></span> |
| scconcept | 4.9998 | 12.9653 | 14.2204 | 5.4316 | 9.6833 | 3.8137 | 9.2512 | 5.8602 | 9.8655 | 4.1476 | 10.2398 | 11.0357 |
| scconcept_encoded | 4.1623 | 7.1172 | 7.3228 | 4.9799 | 8.4336 | 2.8898 | 9.0736 | 6.1720 | 5.9760 | 2.9303 | 4.3421 | 7.9866 |
| cl_scratch_v5 | 22.9494 | 14.2246 | 24.6123 | 17.7213 | 20.1329 | **16.4004** | **33.0155** | **27.5360** | <span style="color:red"><strong>40.3130</strong></span> | 11.5530 | **32.4867** | **24.3785** |
| cl_v6_fair | 25.1326 | 13.4063 | 24.4882 | 16.8968 | **20.4399** | **17.6470** | **33.3417** | 24.4554 | 36.0769 | 12.3258 | **35.2757** | **25.2527** |

##### Aggregate mean across STRING 500-gene datasets

Latent variables: metric=AUPRC_LIFT, negative_protocol=full_candidate, network_group=STRING, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **18.7156** |
| baseline | 17.5231 |
| scGPT_human | <span style="color:red"><strong>22.4905</strong></span> |
| v4_bias_rec_best | **19.1021** |
| v4_plain_best | **19.1878** |
| v4_type_pe_best | **19.4348** |
| scconcept | 7.2090 |
| scconcept_encoded | 5.3460 |
| cl_scratch_v5 | **18.6356** |
| cl_v6_fair | **18.3307** |

##### Aggregate mean across STRING 1000-gene datasets

Latent variables: metric=AUPRC_LIFT, negative_protocol=full_candidate, network_group=STRING, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | <span style="color:red"><strong>29.6619</strong></span> |
| baseline | 28.6159 |
| scGPT_human | **29.1850** |
| v4_bias_rec_best | 25.9502 |
| v4_plain_best | **29.3648** |
| v4_type_pe_best | **29.2591** |
| scconcept | 9.7100 |
| scconcept_encoded | 6.5517 |
| cl_scratch_v5 | **28.9183** |
| cl_v6_fair | **29.1258** |

## PRECISION_AT_K (Main)

### Negative protocol: tf_stratified_1to10

Latent variables: metric=PRECISION_AT_K, negative_protocol=tf_stratified_1to10, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.4745 | 0.3905 | 0.6861 | 0.3714 | 0.1875 | 0.8003 | 0.7128 | <span style="color:red"><strong>0.7877</strong></span> | **0.7277** | **0.8016** | <span style="color:red"><strong>0.7700</strong></span> |
| baseline | 0.4745 | 0.4231 | 0.6992 | 0.3750 | 0.1875 | 0.8016 | <span style="color:red"><strong>0.7149</strong></span> | 0.7774 | 0.7188 | 0.7944 | 0.7491 |
| scGPT_human | <span style="color:red"><strong>0.4842</strong></span> | 0.4172 | 0.6617 | **0.3786** | <span style="color:red"><strong>0.2500</strong></span> | <span style="color:red"><strong>0.8030</strong></span> | 0.6851 | 0.7738 | **0.7277** | <span style="color:red"><strong>0.8038</strong></span> | **0.7509** |
| v4_bias_rec_best | 0.4660 | 0.4083 | 0.6955 | **0.3893** | 0.0625 | 0.7993 | 0.7021 | 0.7753 | <span style="color:red"><strong>0.7533</strong></span> | **0.8014** | **0.7591** |
| v4_plain_best | **0.4782** | 0.4172 | <span style="color:red"><strong>0.7011</strong></span> | **0.3964** | 0.1875 | 0.7979 | 0.6915 | **0.7818** | 0.7154 | **0.7980** | **0.7645** |
| v4_type_pe_best | **0.4757** | **0.4497** | 0.6992 | 0.3643 | 0.0625 | 0.7979 | <span style="color:red"><strong>0.7149</strong></span> | **0.7798** | **0.7333** | **0.7985** | **0.7600** |
| scconcept | 0.4005 | 0.4024 | 0.6523 | 0.3143 | 0.1875 | 0.7817 | 0.6511 | 0.7487 | 0.6808 | **0.7978** | 0.7118 |
| scconcept_encoded | 0.4211 | 0.4024 | 0.6335 | 0.3500 | 0.0625 | 0.7797 | 0.6681 | 0.7460 | 0.6953 | 0.7849 | 0.7027 |
| cl_scratch_v5 | 0.4612 | <span style="color:red"><strong>0.4527</strong></span> | 0.6823 | **0.3821** | <span style="color:red"><strong>0.2500</strong></span> | 0.7976 | 0.6915 | 0.7741 | **0.7321** | **0.7973** | **0.7564** |
| cl_v6_fair | 0.4539 | 0.3876 | 0.6823 | <span style="color:red"><strong>0.4250</strong></span> | 0.1875 | 0.7982 | 0.6957 | **0.7809** | **0.7321** | **0.7997** | **0.7564** |

##### Aggregate mean across Specific 500-gene datasets

Latent variables: metric=PRECISION_AT_K, negative_protocol=tf_stratified_1to10, network_group=Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.5577 |
| baseline | 0.5587 |
| scGPT_human | **0.5662** |
| v4_bias_rec_best | 0.5371 |
| v4_plain_best | 0.5552 |
| v4_type_pe_best | 0.5441 |
| scconcept | 0.5267 |
| scconcept_encoded | 0.5062 |
| cl_scratch_v5 | <span style="color:red"><strong>0.5765</strong></span> |
| cl_v6_fair | 0.5519 |

##### Aggregate mean across Specific 1000-gene datasets

Latent variables: metric=PRECISION_AT_K, negative_protocol=tf_stratified_1to10, network_group=Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.6536 |
| baseline | 0.6537 |
| scGPT_human | 0.6508 |
| v4_bias_rec_best | **0.6545** |
| v4_plain_best | <span style="color:red"><strong>0.6589</strong></span> |
| v4_type_pe_best | 0.6526 |
| scconcept | 0.6159 |
| scconcept_encoded | 0.6192 |
| cl_scratch_v5 | 0.6491 |
| cl_v6_fair | **0.6567** |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.2609 | <span style="color:red"><strong>0.2381</strong></span> | 0.2938 | **0.2586** | **0.4457** | 0.3182 | <span style="color:red"><strong>0.4045</strong></span> | 0.3258 | **0.3540** | **0.3077** | **0.3333** | 0.2500 |
| baseline | 0.2857 | 0.2024 | 0.2990 | 0.2069 | 0.3915 | 0.4545 | 0.3792 | 0.3485 | 0.3212 | 0.2821 | 0.3137 | 0.2717 |
| scGPT_human | 0.2360 | **0.2143** | <span style="color:red"><strong>0.3351</strong></span> | <span style="color:red"><strong>0.3276</strong></span> | **0.4302** | 0.3182 | **0.3876** | <span style="color:red"><strong>0.4242</strong></span> | **0.3723** | <span style="color:red"><strong>0.4103</strong></span> | **0.3529** | **0.3804** |
| v4_bias_rec_best | 0.2391 | 0.1905 | 0.2732 | **0.2931** | **0.4070** | **0.4545** | 0.3371 | 0.3182 | <span style="color:red"><strong>0.4088</strong></span> | 0.2821 | **0.3170** | **0.2826** |
| v4_plain_best | 0.2453 | **0.2024** | **0.3093** | **0.2931** | 0.3566 | 0.3636 | **0.3876** | **0.3636** | **0.3358** | **0.2821** | 0.3039 | **0.3478** |
| v4_type_pe_best | <span style="color:red"><strong>0.3106</strong></span> | 0.1786 | **0.3093** | 0.1897 | **0.4225** | 0.4545 | 0.3596 | **0.3788** | 0.3212 | 0.2564 | **0.3301** | <span style="color:red"><strong>0.4130</strong></span> |
| scconcept | 0.1677 | 0.1786 | 0.1856 | 0.1897 | 0.2519 | 0.1818 | 0.1854 | 0.1136 | 0.2372 | 0.2436 | 0.2288 | 0.1848 |
| scconcept_encoded | 0.1304 | 0.1548 | 0.1804 | 0.1207 | 0.2132 | 0.2727 | 0.2022 | 0.1515 | 0.2080 | 0.2179 | 0.2255 | 0.1522 |
| cl_scratch_v5 | 0.2857 | **0.2262** | 0.2990 | **0.2414** | <span style="color:red"><strong>0.4496</strong></span> | 0.4091 | <span style="color:red"><strong>0.4045</strong></span> | 0.3182 | **0.3796** | 0.2436 | **0.3170** | **0.3913** |
| cl_v6_fair | 0.2516 | <span style="color:red"><strong>0.2381</strong></span> | 0.2784 | 0.1724 | **0.4419** | <span style="color:red"><strong>0.5000</strong></span> | 0.3708 | 0.3182 | **0.3613** | **0.2821** | <span style="color:red"><strong>0.3562</strong></span> | 0.2500 |

##### Aggregate mean across Non-Specific 500-gene datasets

Latent variables: metric=PRECISION_AT_K, negative_protocol=tf_stratified_1to10, network_group=Non-Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.2831 |
| baseline | 0.2943 |
| scGPT_human | <span style="color:red"><strong>0.3458</strong></span> |
| v4_bias_rec_best | **0.3035** |
| v4_plain_best | **0.3088** |
| v4_type_pe_best | **0.3118** |
| scconcept | 0.1820 |
| scconcept_encoded | 0.1783 |
| cl_scratch_v5 | **0.3050** |
| cl_v6_fair | 0.2935 |

##### Aggregate mean across Non-Specific 1000-gene datasets

Latent variables: metric=PRECISION_AT_K, negative_protocol=tf_stratified_1to10, network_group=Non-Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.3487** |
| baseline | 0.3317 |
| scGPT_human | **0.3524** |
| v4_bias_rec_best | 0.3304 |
| v4_plain_best | 0.3231 |
| v4_type_pe_best | **0.3422** |
| scconcept | 0.2094 |
| scconcept_encoded | 0.1933 |
| cl_scratch_v5 | <span style="color:red"><strong>0.3559</strong></span> |
| cl_v6_fair | **0.3433** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.4076 | 0.2812 | 0.5070 | **0.5448** | **0.5789** | **0.4091** | **0.5914** | 0.6048 | 0.4612 | **0.4516** | **0.4662** | **0.4706** |
| baseline | 0.4286 | 0.3281 | <span style="color:red"><strong>0.5302</strong></span> | 0.5373 | 0.5694 | 0.3636 | 0.5806 | 0.6210 | 0.5233 | 0.1935 | 0.4561 | 0.4412 |
| scGPT_human | **0.4580** | **0.3750** | 0.5116 | <span style="color:red"><strong>0.5970</strong></span> | 0.5407 | <span style="color:red"><strong>0.5758</strong></span> | **0.6048** | **0.6371** | <span style="color:red"><strong>0.5271</strong></span> | **0.2742** | <span style="color:red"><strong>0.5034</strong></span> | **0.4706** |
| v4_bias_rec_best | 0.3908 | 0.3125 | <span style="color:red"><strong>0.5302</strong></span> | **0.5821** | 0.5359 | **0.4394** | 0.5699 | <span style="color:red"><strong>0.6532</strong></span> | 0.4612 | <span style="color:red"><strong>0.4839</strong></span> | 0.4426 | <span style="color:red"><strong>0.5441</strong></span> |
| v4_plain_best | 0.3866 | **0.3594** | 0.4977 | **0.5597** | 0.5526 | **0.4091** | **0.6048** | <span style="color:red"><strong>0.6532</strong></span> | 0.4574 | **0.3226** | 0.4291 | **0.4706** |
| v4_type_pe_best | <span style="color:red"><strong>0.4622</strong></span> | **0.3750** | 0.4953 | **0.5597** | <span style="color:red"><strong>0.5909</strong></span> | **0.4242** | <span style="color:red"><strong>0.6156</strong></span> | **0.6290** | 0.4845 | **0.4677** | **0.4865** | **0.4853** |
| scconcept | 0.2395 | <span style="color:red"><strong>0.3906</strong></span> | 0.3233 | 0.3209 | 0.3995 | 0.2576 | 0.3038 | 0.3145 | 0.2558 | 0.1290 | 0.3007 | 0.3235 |
| scconcept_encoded | 0.2101 | 0.2344 | 0.3140 | 0.1642 | 0.3230 | 0.2273 | 0.2634 | 0.2097 | 0.2481 | 0.1129 | 0.2635 | 0.2500 |
| cl_scratch_v5 | 0.3992 | 0.3281 | 0.5116 | 0.5149 | <span style="color:red"><strong>0.5909</strong></span> | **0.4697** | **0.6048** | <span style="color:red"><strong>0.6532</strong></span> | 0.5155 | **0.3226** | 0.4561 | 0.4412 |
| cl_v6_fair | 0.3908 | 0.3281 | 0.5093 | 0.5075 | **0.5885** | **0.4242** | **0.6129** | 0.6129 | 0.4845 | **0.3871** | 0.4527 | **0.4706** |

##### Aggregate mean across STRING 500-gene datasets

Latent variables: metric=PRECISION_AT_K, negative_protocol=tf_stratified_1to10, network_group=STRING, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.4604** |
| baseline | 0.4141 |
| scGPT_human | **0.4883** |
| v4_bias_rec_best | <span style="color:red"><strong>0.5025</strong></span> |
| v4_plain_best | **0.4624** |
| v4_type_pe_best | **0.4902** |
| scconcept | 0.2894 |
| scconcept_encoded | 0.1997 |
| cl_scratch_v5 | **0.4550** |
| cl_v6_fair | **0.4551** |

##### Aggregate mean across STRING 1000-gene datasets

Latent variables: metric=PRECISION_AT_K, negative_protocol=tf_stratified_1to10, network_group=STRING, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.5021 |
| baseline | 0.5147 |
| scGPT_human | <span style="color:red"><strong>0.5243</strong></span> |
| v4_bias_rec_best | 0.4884 |
| v4_plain_best | 0.4880 |
| v4_type_pe_best | **0.5225** |
| scconcept | 0.3038 |
| scconcept_encoded | 0.2703 |
| cl_scratch_v5 | 0.5130 |
| cl_v6_fair | 0.5064 |

### Negative protocol: full_candidate

Latent variables: metric=PRECISION_AT_K, negative_protocol=full_candidate, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.4757** | 0.3905 | 0.7011 | 0.3929 | <span style="color:red"><strong>0.1875</strong></span> | **0.8050** | 0.6723 | 0.7774 | **0.7344** | <span style="color:red"><strong>0.8115</strong></span> | <span style="color:red"><strong>0.7836</strong></span> |
| baseline | 0.4709 | 0.4172 | <span style="color:red"><strong>0.7124</strong></span> | 0.4071 | <span style="color:red"><strong>0.1875</strong></span> | 0.7966 | 0.6830 | 0.7783 | 0.7288 | 0.8028 | 0.7636 |
| scGPT_human | **0.4733** | **0.4467** | 0.6748 | 0.3964 | <span style="color:red"><strong>0.1875</strong></span> | **0.8026** | 0.6681 | 0.7765 | 0.7243 | **0.8043** | 0.7482 |
| v4_bias_rec_best | **0.4769** | **0.4260** | 0.7011 | 0.3429 | 0.0625 | **0.8080** | **0.6872** | 0.7715 | <span style="color:red"><strong>0.7400</strong></span> | 0.7976 | 0.7591 |
| v4_plain_best | **0.4818** | **0.4231** | 0.7030 | 0.3357 | 0.1250 | **0.8074** | **0.7043** | **0.7792** | 0.7221 | 0.7990 | 0.7627 |
| v4_type_pe_best | <span style="color:red"><strong>0.4964</strong></span> | **0.4408** | 0.6880 | 0.3536 | <span style="color:red"><strong>0.1875</strong></span> | **0.8033** | **0.7064** | **0.7786** | 0.7266 | **0.8038** | **0.7736** |
| scconcept | 0.4393 | <span style="color:red"><strong>0.4497</strong></span> | 0.6391 | 0.3071 | <span style="color:red"><strong>0.1875</strong></span> | 0.7868 | 0.6404 | 0.7555 | 0.7143 | 0.7877 | 0.7255 |
| scconcept_encoded | 0.4223 | **0.4231** | 0.6523 | 0.3464 | 0.0000 | 0.7861 | 0.6596 | 0.7543 | 0.6987 | 0.7873 | 0.7227 |
| cl_scratch_v5 | 0.4636 | 0.4142 | 0.6805 | <span style="color:red"><strong>0.4107</strong></span> | <span style="color:red"><strong>0.1875</strong></span> | **0.8013** | **0.6957** | 0.7783 | **0.7288** | 0.8019 | 0.7618 |
| cl_v6_fair | 0.4648 | 0.3935 | 0.6842 | 0.3964 | <span style="color:red"><strong>0.1875</strong></span> | <span style="color:red"><strong>0.8097</strong></span> | <span style="color:red"><strong>0.7191</strong></span> | <span style="color:red"><strong>0.7798</strong></span> | **0.7388** | **0.8040** | 0.7636 |

##### Aggregate mean across Specific 500-gene datasets

Latent variables: metric=PRECISION_AT_K, negative_protocol=full_candidate, network_group=Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.5537 |
| baseline | 0.5560 |
| scGPT_human | 0.5550 |
| v4_bias_rec_best | 0.5350 |
| v4_plain_best | 0.5474 |
| v4_type_pe_best | <span style="color:red"><strong>0.5670</strong></span> |
| scconcept | 0.5435 |
| scconcept_encoded | 0.5008 |
| cl_scratch_v5 | **0.5576** |
| cl_v6_fair | **0.5605** |

##### Aggregate mean across Specific 1000-gene datasets

Latent variables: metric=PRECISION_AT_K, negative_protocol=full_candidate, network_group=Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.6606 |
| baseline | <span style="color:red"><strong>0.6613</strong></span> |
| scGPT_human | 0.6547 |
| v4_bias_rec_best | 0.6497 |
| v4_plain_best | 0.6510 |
| v4_type_pe_best | 0.6539 |
| scconcept | 0.6193 |
| scconcept_encoded | 0.6248 |
| cl_scratch_v5 | 0.6560 |
| cl_v6_fair | 0.6565 |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.2236** | <span style="color:red"><strong>0.2738</strong></span> | **0.1804** | **0.1724** | **0.2868** | **0.1818** | **0.3174** | **0.2803** | **0.2737** | **0.1795** | **0.2549** | 0.1630 |
| baseline | 0.2112 | 0.2619 | 0.1546 | 0.1552 | 0.2481 | 0.1364 | 0.3006 | 0.2576 | 0.2518 | 0.1667 | 0.2320 | 0.1957 |
| scGPT_human | 0.1957 | 0.2143 | <span style="color:red"><strong>0.2320</strong></span> | <span style="color:red"><strong>0.1897</strong></span> | <span style="color:red"><strong>0.3062</strong></span> | 0.0909 | **0.3090** | **0.2955** | <span style="color:red"><strong>0.2956</strong></span> | <span style="color:red"><strong>0.2564</strong></span> | <span style="color:red"><strong>0.2582</strong></span> | **0.2826** |
| v4_bias_rec_best | **0.2174** | 0.2024 | **0.2062** | <span style="color:red"><strong>0.1897</strong></span> | **0.2674** | 0.1364 | 0.2809 | 0.2500 | **0.2664** | **0.2308** | 0.2222 | **0.2935** |
| v4_plain_best | <span style="color:red"><strong>0.2391</strong></span> | 0.2500 | **0.1856** | <span style="color:red"><strong>0.1897</strong></span> | **0.2868** | 0.1364 | 0.2809 | 0.2424 | **0.2664** | **0.1795** | **0.2516** | <span style="color:red"><strong>0.3261</strong></span> |
| v4_type_pe_best | **0.2267** | <span style="color:red"><strong>0.2738</strong></span> | **0.1907** | 0.1207 | **0.2674** | 0.1364 | 0.2978 | **0.2727** | <span style="color:red"><strong>0.2956</strong></span> | **0.2179** | <span style="color:red"><strong>0.2582</strong></span> | **0.3043** |
| scconcept | 0.1863 | 0.1548 | 0.0979 | 0.0690 | 0.1899 | 0.0455 | 0.1292 | 0.0682 | 0.1387 | 0.1410 | 0.1667 | 0.1630 |
| scconcept_encoded | 0.1335 | 0.0714 | 0.0928 | 0.0517 | 0.1279 | 0.0000 | 0.1236 | 0.1212 | 0.1058 | 0.0769 | 0.1242 | 0.1087 |
| cl_scratch_v5 | **0.2329** | 0.2619 | **0.2062** | 0.1207 | **0.2946** | **0.1818** | <span style="color:red"><strong>0.3202</strong></span> | <span style="color:red"><strong>0.3106</strong></span> | <span style="color:red"><strong>0.2956</strong></span> | 0.1667 | 0.2059 | <span style="color:red"><strong>0.3261</strong></span> |
| cl_v6_fair | 0.1988 | 0.2500 | **0.2010** | 0.1379 | 0.2481 | <span style="color:red"><strong>0.2273</strong></span> | 0.2949 | 0.2500 | 0.2445 | **0.1795** | 0.2222 | **0.2935** |

##### Aggregate mean across Non-Specific 500-gene datasets

Latent variables: metric=PRECISION_AT_K, negative_protocol=full_candidate, network_group=Non-Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.2085** |
| baseline | 0.1956 |
| scGPT_human | **0.2216** |
| v4_bias_rec_best | **0.2171** |
| v4_plain_best | **0.2207** |
| v4_type_pe_best | **0.2210** |
| scconcept | 0.1069 |
| scconcept_encoded | 0.0717 |
| cl_scratch_v5 | <span style="color:red"><strong>0.2280</strong></span> |
| cl_v6_fair | **0.2230** |

##### Aggregate mean across Non-Specific 1000-gene datasets

Latent variables: metric=PRECISION_AT_K, negative_protocol=full_candidate, network_group=Non-Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.2561** |
| baseline | 0.2330 |
| scGPT_human | <span style="color:red"><strong>0.2661</strong></span> |
| v4_bias_rec_best | **0.2434** |
| v4_plain_best | **0.2517** |
| v4_type_pe_best | **0.2561** |
| scconcept | 0.1515 |
| scconcept_encoded | 0.1180 |
| cl_scratch_v5 | **0.2592** |
| cl_v6_fair | **0.2349** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | <span style="color:red"><strong>0.3025</strong></span> | 0.2031 | <span style="color:red"><strong>0.4698</strong></span> | 0.5075 | **0.4976** | **0.4242** | **0.5081** | **0.5484** | 0.3643 | <span style="color:red"><strong>0.2903</strong></span> | <span style="color:red"><strong>0.3682</strong></span> | **0.3382** |
| baseline | 0.2815 | 0.2031 | 0.4558 | 0.5522 | 0.4785 | 0.3939 | 0.5054 | 0.5081 | 0.3837 | 0.2258 | 0.3176 | 0.3235 |
| scGPT_human | **0.2857** | <span style="color:red"><strong>0.3438</strong></span> | 0.4535 | <span style="color:red"><strong>0.5597</strong></span> | 0.4617 | **0.4848** | 0.4839 | <span style="color:red"><strong>0.5968</strong></span> | <span style="color:red"><strong>0.4031</strong></span> | **0.2581** | **0.3649** | **0.3382** |
| v4_bias_rec_best | 0.2815 | 0.1875 | **0.4605** | 0.5075 | 0.4641 | **0.4091** | 0.4946 | **0.5565** | 0.3256 | <span style="color:red"><strong>0.2903</strong></span> | **0.3243** | **0.4118** |
| v4_plain_best | 0.2731 | **0.2188** | 0.4372 | 0.4627 | 0.4641 | <span style="color:red"><strong>0.5152</strong></span> | **0.5081** | **0.5161** | **0.3915** | **0.2581** | **0.3277** | **0.3529** |
| v4_type_pe_best | **0.2983** | 0.2031 | 0.4488 | 0.5373 | **0.4904** | **0.4242** | 0.5054 | **0.5645** | **0.3876** | 0.2258 | **0.3412** | <span style="color:red"><strong>0.4265</strong></span> |
| scconcept | 0.0882 | **0.2188** | 0.2977 | 0.1940 | 0.2919 | 0.1364 | 0.2097 | 0.1694 | 0.1318 | 0.0323 | 0.1385 | 0.1765 |
| scconcept_encoded | 0.0714 | 0.1719 | 0.1837 | 0.2015 | 0.2990 | 0.0758 | 0.2016 | 0.1452 | 0.1008 | 0.0806 | 0.0642 | 0.1618 |
| cl_scratch_v5 | 0.2773 | **0.2344** | 0.4535 | 0.4851 | **0.4952** | **0.4848** | <span style="color:red"><strong>0.5188</strong></span> | <span style="color:red"><strong>0.5968</strong></span> | **0.3992** | 0.1935 | **0.3243** | **0.3676** |
| cl_v6_fair | **0.2899** | **0.2656** | 0.4442 | 0.4851 | <span style="color:red"><strong>0.5167</strong></span> | **0.4697** | 0.5000 | **0.5242** | **0.3915** | 0.1774 | **0.3412** | **0.3971** |

##### Aggregate mean across STRING 500-gene datasets

Latent variables: metric=PRECISION_AT_K, negative_protocol=full_candidate, network_group=STRING, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.3853** |
| baseline | 0.3678 |
| scGPT_human | <span style="color:red"><strong>0.4302</strong></span> |
| v4_bias_rec_best | **0.3938** |
| v4_plain_best | **0.3873** |
| v4_type_pe_best | **0.3969** |
| scconcept | 0.1545 |
| scconcept_encoded | 0.1394 |
| cl_scratch_v5 | **0.3937** |
| cl_v6_fair | **0.3865** |

##### Aggregate mean across STRING 1000-gene datasets

Latent variables: metric=PRECISION_AT_K, negative_protocol=full_candidate, network_group=STRING, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | <span style="color:red"><strong>0.4184</strong></span> |
| baseline | 0.4037 |
| scGPT_human | **0.4088** |
| v4_bias_rec_best | 0.3918 |
| v4_plain_best | 0.4003 |
| v4_type_pe_best | **0.4120** |
| scconcept | 0.1930 |
| scconcept_encoded | 0.1535 |
| cl_scratch_v5 | **0.4114** |
| cl_v6_fair | **0.4139** |

## RECALL_AT_K (Main)

### Negative protocol: tf_stratified_1to10

Latent variables: metric=RECALL_AT_K, negative_protocol=tf_stratified_1to10, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.4745 | 0.3905 | 0.6861 | 0.3714 | 0.1875 | 0.8003 | 0.7128 | <span style="color:red"><strong>0.7877</strong></span> | **0.7277** | **0.8016** | <span style="color:red"><strong>0.7700</strong></span> |
| baseline | 0.4745 | 0.4231 | 0.6992 | 0.3750 | 0.1875 | 0.8016 | <span style="color:red"><strong>0.7149</strong></span> | 0.7774 | 0.7188 | 0.7944 | 0.7491 |
| scGPT_human | <span style="color:red"><strong>0.4842</strong></span> | 0.4172 | 0.6617 | **0.3786** | <span style="color:red"><strong>0.2500</strong></span> | <span style="color:red"><strong>0.8030</strong></span> | 0.6851 | 0.7738 | **0.7277** | <span style="color:red"><strong>0.8038</strong></span> | **0.7509** |
| v4_bias_rec_best | 0.4660 | 0.4083 | 0.6955 | **0.3893** | 0.0625 | 0.7993 | 0.7021 | 0.7753 | <span style="color:red"><strong>0.7533</strong></span> | **0.8014** | **0.7591** |
| v4_plain_best | **0.4782** | 0.4172 | <span style="color:red"><strong>0.7011</strong></span> | **0.3964** | 0.1875 | 0.7979 | 0.6915 | **0.7818** | 0.7154 | **0.7980** | **0.7645** |
| v4_type_pe_best | **0.4757** | **0.4497** | 0.6992 | 0.3643 | 0.0625 | 0.7979 | <span style="color:red"><strong>0.7149</strong></span> | **0.7798** | **0.7333** | **0.7985** | **0.7600** |
| scconcept | 0.4005 | 0.4024 | 0.6523 | 0.3143 | 0.1875 | 0.7817 | 0.6511 | 0.7487 | 0.6808 | **0.7978** | 0.7118 |
| scconcept_encoded | 0.4211 | 0.4024 | 0.6335 | 0.3500 | 0.0625 | 0.7797 | 0.6681 | 0.7460 | 0.6953 | 0.7849 | 0.7027 |
| cl_scratch_v5 | 0.4612 | <span style="color:red"><strong>0.4527</strong></span> | 0.6823 | **0.3821** | <span style="color:red"><strong>0.2500</strong></span> | 0.7976 | 0.6915 | 0.7741 | **0.7321** | **0.7973** | **0.7564** |
| cl_v6_fair | 0.4539 | 0.3876 | 0.6823 | <span style="color:red"><strong>0.4250</strong></span> | 0.1875 | 0.7982 | 0.6957 | **0.7809** | **0.7321** | **0.7997** | **0.7564** |

##### Aggregate mean across Specific 500-gene datasets

Latent variables: metric=RECALL_AT_K, negative_protocol=tf_stratified_1to10, network_group=Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.5577 |
| baseline | 0.5587 |
| scGPT_human | **0.5662** |
| v4_bias_rec_best | 0.5371 |
| v4_plain_best | 0.5552 |
| v4_type_pe_best | 0.5441 |
| scconcept | 0.5267 |
| scconcept_encoded | 0.5062 |
| cl_scratch_v5 | <span style="color:red"><strong>0.5765</strong></span> |
| cl_v6_fair | 0.5519 |

##### Aggregate mean across Specific 1000-gene datasets

Latent variables: metric=RECALL_AT_K, negative_protocol=tf_stratified_1to10, network_group=Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.6536 |
| baseline | 0.6537 |
| scGPT_human | 0.6508 |
| v4_bias_rec_best | **0.6545** |
| v4_plain_best | <span style="color:red"><strong>0.6589</strong></span> |
| v4_type_pe_best | 0.6526 |
| scconcept | 0.6159 |
| scconcept_encoded | 0.6192 |
| cl_scratch_v5 | 0.6491 |
| cl_v6_fair | **0.6567** |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.2609 | <span style="color:red"><strong>0.2381</strong></span> | 0.2938 | **0.2586** | **0.4457** | 0.3182 | <span style="color:red"><strong>0.4045</strong></span> | 0.3258 | **0.3540** | **0.3077** | **0.3333** | 0.2500 |
| baseline | 0.2857 | 0.2024 | 0.2990 | 0.2069 | 0.3915 | 0.4545 | 0.3792 | 0.3485 | 0.3212 | 0.2821 | 0.3137 | 0.2717 |
| scGPT_human | 0.2360 | **0.2143** | <span style="color:red"><strong>0.3351</strong></span> | <span style="color:red"><strong>0.3276</strong></span> | **0.4302** | 0.3182 | **0.3876** | <span style="color:red"><strong>0.4242</strong></span> | **0.3723** | <span style="color:red"><strong>0.4103</strong></span> | **0.3529** | **0.3804** |
| v4_bias_rec_best | 0.2391 | 0.1905 | 0.2732 | **0.2931** | **0.4070** | **0.4545** | 0.3371 | 0.3182 | <span style="color:red"><strong>0.4088</strong></span> | 0.2821 | **0.3170** | **0.2826** |
| v4_plain_best | 0.2453 | **0.2024** | **0.3093** | **0.2931** | 0.3566 | 0.3636 | **0.3876** | **0.3636** | **0.3358** | **0.2821** | 0.3039 | **0.3478** |
| v4_type_pe_best | <span style="color:red"><strong>0.3106</strong></span> | 0.1786 | **0.3093** | 0.1897 | **0.4225** | 0.4545 | 0.3596 | **0.3788** | 0.3212 | 0.2564 | **0.3301** | <span style="color:red"><strong>0.4130</strong></span> |
| scconcept | 0.1677 | 0.1786 | 0.1856 | 0.1897 | 0.2519 | 0.1818 | 0.1854 | 0.1136 | 0.2372 | 0.2436 | 0.2288 | 0.1848 |
| scconcept_encoded | 0.1304 | 0.1548 | 0.1804 | 0.1207 | 0.2132 | 0.2727 | 0.2022 | 0.1515 | 0.2080 | 0.2179 | 0.2255 | 0.1522 |
| cl_scratch_v5 | 0.2857 | **0.2262** | 0.2990 | **0.2414** | <span style="color:red"><strong>0.4496</strong></span> | 0.4091 | <span style="color:red"><strong>0.4045</strong></span> | 0.3182 | **0.3796** | 0.2436 | **0.3170** | **0.3913** |
| cl_v6_fair | 0.2516 | <span style="color:red"><strong>0.2381</strong></span> | 0.2784 | 0.1724 | **0.4419** | <span style="color:red"><strong>0.5000</strong></span> | 0.3708 | 0.3182 | **0.3613** | **0.2821** | <span style="color:red"><strong>0.3562</strong></span> | 0.2500 |

##### Aggregate mean across Non-Specific 500-gene datasets

Latent variables: metric=RECALL_AT_K, negative_protocol=tf_stratified_1to10, network_group=Non-Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.2831 |
| baseline | 0.2943 |
| scGPT_human | <span style="color:red"><strong>0.3458</strong></span> |
| v4_bias_rec_best | **0.3035** |
| v4_plain_best | **0.3088** |
| v4_type_pe_best | **0.3118** |
| scconcept | 0.1820 |
| scconcept_encoded | 0.1783 |
| cl_scratch_v5 | **0.3050** |
| cl_v6_fair | 0.2935 |

##### Aggregate mean across Non-Specific 1000-gene datasets

Latent variables: metric=RECALL_AT_K, negative_protocol=tf_stratified_1to10, network_group=Non-Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.3487** |
| baseline | 0.3317 |
| scGPT_human | **0.3524** |
| v4_bias_rec_best | 0.3304 |
| v4_plain_best | 0.3231 |
| v4_type_pe_best | **0.3422** |
| scconcept | 0.2094 |
| scconcept_encoded | 0.1933 |
| cl_scratch_v5 | <span style="color:red"><strong>0.3559</strong></span> |
| cl_v6_fair | **0.3433** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.4076 | 0.2812 | 0.5070 | **0.5448** | **0.5789** | **0.4091** | **0.5914** | 0.6048 | 0.4612 | **0.4516** | **0.4662** | **0.4706** |
| baseline | 0.4286 | 0.3281 | <span style="color:red"><strong>0.5302</strong></span> | 0.5373 | 0.5694 | 0.3636 | 0.5806 | 0.6210 | 0.5233 | 0.1935 | 0.4561 | 0.4412 |
| scGPT_human | **0.4580** | **0.3750** | 0.5116 | <span style="color:red"><strong>0.5970</strong></span> | 0.5407 | <span style="color:red"><strong>0.5758</strong></span> | **0.6048** | **0.6371** | <span style="color:red"><strong>0.5271</strong></span> | **0.2742** | <span style="color:red"><strong>0.5034</strong></span> | **0.4706** |
| v4_bias_rec_best | 0.3908 | 0.3125 | <span style="color:red"><strong>0.5302</strong></span> | **0.5821** | 0.5359 | **0.4394** | 0.5699 | <span style="color:red"><strong>0.6532</strong></span> | 0.4612 | <span style="color:red"><strong>0.4839</strong></span> | 0.4426 | <span style="color:red"><strong>0.5441</strong></span> |
| v4_plain_best | 0.3866 | **0.3594** | 0.4977 | **0.5597** | 0.5526 | **0.4091** | **0.6048** | <span style="color:red"><strong>0.6532</strong></span> | 0.4574 | **0.3226** | 0.4291 | **0.4706** |
| v4_type_pe_best | <span style="color:red"><strong>0.4622</strong></span> | **0.3750** | 0.4953 | **0.5597** | <span style="color:red"><strong>0.5909</strong></span> | **0.4242** | <span style="color:red"><strong>0.6156</strong></span> | **0.6290** | 0.4845 | **0.4677** | **0.4865** | **0.4853** |
| scconcept | 0.2395 | <span style="color:red"><strong>0.3906</strong></span> | 0.3233 | 0.3209 | 0.3995 | 0.2576 | 0.3038 | 0.3145 | 0.2558 | 0.1290 | 0.3007 | 0.3235 |
| scconcept_encoded | 0.2101 | 0.2344 | 0.3140 | 0.1642 | 0.3230 | 0.2273 | 0.2634 | 0.2097 | 0.2481 | 0.1129 | 0.2635 | 0.2500 |
| cl_scratch_v5 | 0.3992 | 0.3281 | 0.5116 | 0.5149 | <span style="color:red"><strong>0.5909</strong></span> | **0.4697** | **0.6048** | <span style="color:red"><strong>0.6532</strong></span> | 0.5155 | **0.3226** | 0.4561 | 0.4412 |
| cl_v6_fair | 0.3908 | 0.3281 | 0.5093 | 0.5075 | **0.5885** | **0.4242** | **0.6129** | 0.6129 | 0.4845 | **0.3871** | 0.4527 | **0.4706** |

##### Aggregate mean across STRING 500-gene datasets

Latent variables: metric=RECALL_AT_K, negative_protocol=tf_stratified_1to10, network_group=STRING, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.4604** |
| baseline | 0.4141 |
| scGPT_human | **0.4883** |
| v4_bias_rec_best | <span style="color:red"><strong>0.5025</strong></span> |
| v4_plain_best | **0.4624** |
| v4_type_pe_best | **0.4902** |
| scconcept | 0.2894 |
| scconcept_encoded | 0.1997 |
| cl_scratch_v5 | **0.4550** |
| cl_v6_fair | **0.4551** |

##### Aggregate mean across STRING 1000-gene datasets

Latent variables: metric=RECALL_AT_K, negative_protocol=tf_stratified_1to10, network_group=STRING, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.5021 |
| baseline | 0.5147 |
| scGPT_human | <span style="color:red"><strong>0.5243</strong></span> |
| v4_bias_rec_best | 0.4884 |
| v4_plain_best | 0.4880 |
| v4_type_pe_best | **0.5225** |
| scconcept | 0.3038 |
| scconcept_encoded | 0.2703 |
| cl_scratch_v5 | 0.5130 |
| cl_v6_fair | 0.5064 |

### Negative protocol: full_candidate

Latent variables: metric=RECALL_AT_K, negative_protocol=full_candidate, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.4757** | 0.3905 | 0.7011 | 0.3929 | <span style="color:red"><strong>0.1875</strong></span> | **0.8050** | 0.6723 | 0.7774 | **0.7344** | <span style="color:red"><strong>0.8115</strong></span> | <span style="color:red"><strong>0.7836</strong></span> |
| baseline | 0.4709 | 0.4172 | <span style="color:red"><strong>0.7124</strong></span> | 0.4071 | <span style="color:red"><strong>0.1875</strong></span> | 0.7966 | 0.6830 | 0.7783 | 0.7288 | 0.8028 | 0.7636 |
| scGPT_human | **0.4733** | **0.4467** | 0.6748 | 0.3964 | <span style="color:red"><strong>0.1875</strong></span> | **0.8026** | 0.6681 | 0.7765 | 0.7243 | **0.8043** | 0.7482 |
| v4_bias_rec_best | **0.4769** | **0.4260** | 0.7011 | 0.3429 | 0.0625 | **0.8080** | **0.6872** | 0.7715 | <span style="color:red"><strong>0.7400</strong></span> | 0.7976 | 0.7591 |
| v4_plain_best | **0.4818** | **0.4231** | 0.7030 | 0.3357 | 0.1250 | **0.8074** | **0.7043** | **0.7792** | 0.7221 | 0.7990 | 0.7627 |
| v4_type_pe_best | <span style="color:red"><strong>0.4964</strong></span> | **0.4408** | 0.6880 | 0.3536 | <span style="color:red"><strong>0.1875</strong></span> | **0.8033** | **0.7064** | **0.7786** | 0.7266 | **0.8038** | **0.7736** |
| scconcept | 0.4393 | <span style="color:red"><strong>0.4497</strong></span> | 0.6391 | 0.3071 | <span style="color:red"><strong>0.1875</strong></span> | 0.7868 | 0.6404 | 0.7555 | 0.7143 | 0.7877 | 0.7255 |
| scconcept_encoded | 0.4223 | **0.4231** | 0.6523 | 0.3464 | 0.0000 | 0.7861 | 0.6596 | 0.7543 | 0.6987 | 0.7873 | 0.7227 |
| cl_scratch_v5 | 0.4636 | 0.4142 | 0.6805 | <span style="color:red"><strong>0.4107</strong></span> | <span style="color:red"><strong>0.1875</strong></span> | **0.8013** | **0.6957** | 0.7783 | **0.7288** | 0.8019 | 0.7618 |
| cl_v6_fair | 0.4648 | 0.3935 | 0.6842 | 0.3964 | <span style="color:red"><strong>0.1875</strong></span> | <span style="color:red"><strong>0.8097</strong></span> | <span style="color:red"><strong>0.7191</strong></span> | <span style="color:red"><strong>0.7798</strong></span> | **0.7388** | **0.8040** | 0.7636 |

##### Aggregate mean across Specific 500-gene datasets

Latent variables: metric=RECALL_AT_K, negative_protocol=full_candidate, network_group=Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.5537 |
| baseline | 0.5560 |
| scGPT_human | 0.5550 |
| v4_bias_rec_best | 0.5350 |
| v4_plain_best | 0.5474 |
| v4_type_pe_best | <span style="color:red"><strong>0.5670</strong></span> |
| scconcept | 0.5435 |
| scconcept_encoded | 0.5008 |
| cl_scratch_v5 | **0.5576** |
| cl_v6_fair | **0.5605** |

##### Aggregate mean across Specific 1000-gene datasets

Latent variables: metric=RECALL_AT_K, negative_protocol=full_candidate, network_group=Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.6606 |
| baseline | <span style="color:red"><strong>0.6613</strong></span> |
| scGPT_human | 0.6547 |
| v4_bias_rec_best | 0.6497 |
| v4_plain_best | 0.6510 |
| v4_type_pe_best | 0.6539 |
| scconcept | 0.6193 |
| scconcept_encoded | 0.6248 |
| cl_scratch_v5 | 0.6560 |
| cl_v6_fair | 0.6565 |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.2236** | <span style="color:red"><strong>0.2738</strong></span> | **0.1804** | **0.1724** | **0.2868** | **0.1818** | **0.3174** | **0.2803** | **0.2737** | **0.1795** | **0.2549** | 0.1630 |
| baseline | 0.2112 | 0.2619 | 0.1546 | 0.1552 | 0.2481 | 0.1364 | 0.3006 | 0.2576 | 0.2518 | 0.1667 | 0.2320 | 0.1957 |
| scGPT_human | 0.1957 | 0.2143 | <span style="color:red"><strong>0.2320</strong></span> | <span style="color:red"><strong>0.1897</strong></span> | <span style="color:red"><strong>0.3062</strong></span> | 0.0909 | **0.3090** | **0.2955** | <span style="color:red"><strong>0.2956</strong></span> | <span style="color:red"><strong>0.2564</strong></span> | <span style="color:red"><strong>0.2582</strong></span> | **0.2826** |
| v4_bias_rec_best | **0.2174** | 0.2024 | **0.2062** | <span style="color:red"><strong>0.1897</strong></span> | **0.2674** | 0.1364 | 0.2809 | 0.2500 | **0.2664** | **0.2308** | 0.2222 | **0.2935** |
| v4_plain_best | <span style="color:red"><strong>0.2391</strong></span> | 0.2500 | **0.1856** | <span style="color:red"><strong>0.1897</strong></span> | **0.2868** | 0.1364 | 0.2809 | 0.2424 | **0.2664** | **0.1795** | **0.2516** | <span style="color:red"><strong>0.3261</strong></span> |
| v4_type_pe_best | **0.2267** | <span style="color:red"><strong>0.2738</strong></span> | **0.1907** | 0.1207 | **0.2674** | 0.1364 | 0.2978 | **0.2727** | <span style="color:red"><strong>0.2956</strong></span> | **0.2179** | <span style="color:red"><strong>0.2582</strong></span> | **0.3043** |
| scconcept | 0.1863 | 0.1548 | 0.0979 | 0.0690 | 0.1899 | 0.0455 | 0.1292 | 0.0682 | 0.1387 | 0.1410 | 0.1667 | 0.1630 |
| scconcept_encoded | 0.1335 | 0.0714 | 0.0928 | 0.0517 | 0.1279 | 0.0000 | 0.1236 | 0.1212 | 0.1058 | 0.0769 | 0.1242 | 0.1087 |
| cl_scratch_v5 | **0.2329** | 0.2619 | **0.2062** | 0.1207 | **0.2946** | **0.1818** | <span style="color:red"><strong>0.3202</strong></span> | <span style="color:red"><strong>0.3106</strong></span> | <span style="color:red"><strong>0.2956</strong></span> | 0.1667 | 0.2059 | <span style="color:red"><strong>0.3261</strong></span> |
| cl_v6_fair | 0.1988 | 0.2500 | **0.2010** | 0.1379 | 0.2481 | <span style="color:red"><strong>0.2273</strong></span> | 0.2949 | 0.2500 | 0.2445 | **0.1795** | 0.2222 | **0.2935** |

##### Aggregate mean across Non-Specific 500-gene datasets

Latent variables: metric=RECALL_AT_K, negative_protocol=full_candidate, network_group=Non-Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.2085** |
| baseline | 0.1956 |
| scGPT_human | **0.2216** |
| v4_bias_rec_best | **0.2171** |
| v4_plain_best | **0.2207** |
| v4_type_pe_best | **0.2210** |
| scconcept | 0.1069 |
| scconcept_encoded | 0.0717 |
| cl_scratch_v5 | <span style="color:red"><strong>0.2280</strong></span> |
| cl_v6_fair | **0.2230** |

##### Aggregate mean across Non-Specific 1000-gene datasets

Latent variables: metric=RECALL_AT_K, negative_protocol=full_candidate, network_group=Non-Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.2561** |
| baseline | 0.2330 |
| scGPT_human | <span style="color:red"><strong>0.2661</strong></span> |
| v4_bias_rec_best | **0.2434** |
| v4_plain_best | **0.2517** |
| v4_type_pe_best | **0.2561** |
| scconcept | 0.1515 |
| scconcept_encoded | 0.1180 |
| cl_scratch_v5 | **0.2592** |
| cl_v6_fair | **0.2349** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | <span style="color:red"><strong>0.3025</strong></span> | 0.2031 | <span style="color:red"><strong>0.4698</strong></span> | 0.5075 | **0.4976** | **0.4242** | **0.5081** | **0.5484** | 0.3643 | <span style="color:red"><strong>0.2903</strong></span> | <span style="color:red"><strong>0.3682</strong></span> | **0.3382** |
| baseline | 0.2815 | 0.2031 | 0.4558 | 0.5522 | 0.4785 | 0.3939 | 0.5054 | 0.5081 | 0.3837 | 0.2258 | 0.3176 | 0.3235 |
| scGPT_human | **0.2857** | <span style="color:red"><strong>0.3438</strong></span> | 0.4535 | <span style="color:red"><strong>0.5597</strong></span> | 0.4617 | **0.4848** | 0.4839 | <span style="color:red"><strong>0.5968</strong></span> | <span style="color:red"><strong>0.4031</strong></span> | **0.2581** | **0.3649** | **0.3382** |
| v4_bias_rec_best | 0.2815 | 0.1875 | **0.4605** | 0.5075 | 0.4641 | **0.4091** | 0.4946 | **0.5565** | 0.3256 | <span style="color:red"><strong>0.2903</strong></span> | **0.3243** | **0.4118** |
| v4_plain_best | 0.2731 | **0.2188** | 0.4372 | 0.4627 | 0.4641 | <span style="color:red"><strong>0.5152</strong></span> | **0.5081** | **0.5161** | **0.3915** | **0.2581** | **0.3277** | **0.3529** |
| v4_type_pe_best | **0.2983** | 0.2031 | 0.4488 | 0.5373 | **0.4904** | **0.4242** | 0.5054 | **0.5645** | **0.3876** | 0.2258 | **0.3412** | <span style="color:red"><strong>0.4265</strong></span> |
| scconcept | 0.0882 | **0.2188** | 0.2977 | 0.1940 | 0.2919 | 0.1364 | 0.2097 | 0.1694 | 0.1318 | 0.0323 | 0.1385 | 0.1765 |
| scconcept_encoded | 0.0714 | 0.1719 | 0.1837 | 0.2015 | 0.2990 | 0.0758 | 0.2016 | 0.1452 | 0.1008 | 0.0806 | 0.0642 | 0.1618 |
| cl_scratch_v5 | 0.2773 | **0.2344** | 0.4535 | 0.4851 | **0.4952** | **0.4848** | <span style="color:red"><strong>0.5188</strong></span> | <span style="color:red"><strong>0.5968</strong></span> | **0.3992** | 0.1935 | **0.3243** | **0.3676** |
| cl_v6_fair | **0.2899** | **0.2656** | 0.4442 | 0.4851 | <span style="color:red"><strong>0.5167</strong></span> | **0.4697** | 0.5000 | **0.5242** | **0.3915** | 0.1774 | **0.3412** | **0.3971** |

##### Aggregate mean across STRING 500-gene datasets

Latent variables: metric=RECALL_AT_K, negative_protocol=full_candidate, network_group=STRING, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.3853** |
| baseline | 0.3678 |
| scGPT_human | <span style="color:red"><strong>0.4302</strong></span> |
| v4_bias_rec_best | **0.3938** |
| v4_plain_best | **0.3873** |
| v4_type_pe_best | **0.3969** |
| scconcept | 0.1545 |
| scconcept_encoded | 0.1394 |
| cl_scratch_v5 | **0.3937** |
| cl_v6_fair | **0.3865** |

##### Aggregate mean across STRING 1000-gene datasets

Latent variables: metric=RECALL_AT_K, negative_protocol=full_candidate, network_group=STRING, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | <span style="color:red"><strong>0.4184</strong></span> |
| baseline | 0.4037 |
| scGPT_human | **0.4088** |
| v4_bias_rec_best | 0.3918 |
| v4_plain_best | 0.4003 |
| v4_type_pe_best | **0.4120** |
| scconcept | 0.1930 |
| scconcept_encoded | 0.1535 |
| cl_scratch_v5 | **0.4114** |
| cl_v6_fair | **0.4139** |

## F1 (Main)

### Negative protocol: tf_stratified_1to10

Latent variables: metric=F1, negative_protocol=tf_stratified_1to10, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.4112 | 0.3411 | 0.6818 | **0.3448** | **0.0667** | 0.8064 | 0.7007 | <span style="color:red"><strong>0.7902</strong></span> | **0.7283** | <span style="color:red"><strong>0.8092</strong></span> | **0.7751** |
| baseline | 0.4139 | 0.3452 | 0.7008 | 0.3303 | 0.0000 | 0.8091 | 0.7154 | 0.7880 | 0.7260 | 0.8046 | 0.7557 |
| scGPT_human | 0.3972 | **0.4212** | 0.6740 | **0.3332** | **0.1000** | 0.8040 | 0.6921 | 0.7777 | **0.7321** | **0.8085** | **0.7562** |
| v4_bias_rec_best | 0.4109 | **0.3544** | 0.6939 | **0.3491** | 0.0000 | 0.8066 | 0.7009 | 0.7849 | <span style="color:red"><strong>0.7682</strong></span> | **0.8051** | **0.7605** |
| v4_plain_best | <span style="color:red"><strong>0.4225</strong></span> | **0.3870** | <span style="color:red"><strong>0.7106</strong></span> | 0.3263 | 0.0000 | <span style="color:red"><strong>0.8096</strong></span> | 0.6887 | 0.7860 | 0.7201 | **0.8079** | <span style="color:red"><strong>0.7841</strong></span> |
| v4_type_pe_best | 0.4112 | <span style="color:red"><strong>0.4346</strong></span> | 0.6945 | 0.3255 | **0.1000** | 0.8048 | <span style="color:red"><strong>0.7171</strong></span> | 0.7819 | **0.7446** | **0.8057** | **0.7732** |
| scconcept | 0.3638 | **0.3604** | 0.6522 | 0.2080 | <span style="color:red"><strong>0.1111</strong></span> | 0.7911 | 0.6617 | 0.7599 | 0.6802 | 0.8035 | 0.7283 |
| scconcept_encoded | 0.3678 | **0.3917** | 0.6434 | 0.2431 | 0.0000 | 0.7885 | 0.6680 | 0.7545 | 0.7191 | 0.8017 | 0.7354 |
| cl_scratch_v5 | 0.3903 | **0.3911** | 0.6822 | **0.3501** | **0.0909** | 0.8057 | 0.6980 | 0.7837 | **0.7315** | **0.8083** | 0.7521 |
| cl_v6_fair | 0.3821 | 0.3043 | 0.6901 | <span style="color:red"><strong>0.3636</strong></span> | **0.0833** | 0.7997 | 0.7118 | 0.7829 | **0.7520** | **0.8063** | 0.7557 |

##### Aggregate mean across Specific 500-gene datasets

Latent variables: metric=F1, negative_protocol=tf_stratified_1to10, network_group=Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.5224** |
| baseline | 0.5085 |
| scGPT_human | **0.5403** |
| v4_bias_rec_best | **0.5168** |
| v4_plain_best | **0.5160** |
| v4_type_pe_best | <span style="color:red"><strong>0.5539</strong></span> |
| scconcept | 0.5084 |
| scconcept_encoded | 0.5028 |
| cl_scratch_v5 | **0.5327** |
| cl_v6_fair | **0.5214** |

##### Aggregate mean across Specific 1000-gene datasets

Latent variables: metric=F1, negative_protocol=tf_stratified_1to10, network_group=Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.6406 |
| baseline | 0.6411 |
| scGPT_human | 0.6324 |
| v4_bias_rec_best | **0.6417** |
| v4_plain_best | <span style="color:red"><strong>0.6438</strong></span> |
| v4_type_pe_best | 0.6373 |
| scconcept | 0.5964 |
| scconcept_encoded | 0.5998 |
| cl_scratch_v5 | 0.6367 |
| cl_v6_fair | 0.6374 |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.1231 | 0.1237 | 0.1584 | **0.2024** | <span style="color:red"><strong>0.4034</strong></span> | 0.2500 | <span style="color:red"><strong>0.4072</strong></span> | **0.3490** | **0.3212** | 0.1765 | **0.2898** | 0.2521 |
| baseline | 0.1438 | 0.1294 | 0.2669 | 0.1387 | 0.3374 | 0.4000 | 0.3584 | 0.3416 | 0.2710 | 0.2113 | 0.2000 | 0.2628 |
| scGPT_human | <span style="color:red"><strong>0.2101</strong></span> | <span style="color:red"><strong>0.2163</strong></span> | <span style="color:red"><strong>0.3010</strong></span> | <span style="color:red"><strong>0.2735</strong></span> | **0.3799** | 0.0714 | 0.3365 | <span style="color:red"><strong>0.4125</strong></span> | **0.3374** | <span style="color:red"><strong>0.3463</strong></span> | <span style="color:red"><strong>0.3377</strong></span> | **0.3287** |
| v4_bias_rec_best | 0.0980 | 0.0633 | 0.1789 | **0.2154** | 0.2510 | 0.1538 | 0.3087 | 0.3108 | <span style="color:red"><strong>0.3538</strong></span> | 0.1512 | **0.2616** | 0.2482 |
| v4_plain_best | **0.2090** | 0.0617 | 0.2523 | **0.1874** | **0.3588** | 0.2667 | 0.3415 | 0.3370 | **0.2996** | 0.1999 | **0.2321** | **0.2897** |
| v4_type_pe_best | **0.1922** | 0.0964 | 0.1786 | **0.1481** | **0.3658** | <span style="color:red"><strong>0.4734</strong></span> | 0.3157 | 0.2957 | **0.3127** | 0.1897 | **0.3005** | <span style="color:red"><strong>0.3719</strong></span> |
| scconcept | 0.1363 | 0.0972 | 0.1713 | 0.1020 | 0.2059 | 0.0000 | 0.1095 | 0.0682 | 0.1971 | 0.1548 | 0.1647 | 0.1279 |
| scconcept_encoded | 0.0721 | 0.0894 | 0.1301 | 0.0727 | 0.1982 | 0.0588 | 0.1584 | 0.0909 | 0.1572 | 0.1095 | **0.2027** | 0.1172 |
| cl_scratch_v5 | 0.1362 | **0.1529** | 0.2308 | 0.1240 | **0.4027** | 0.1875 | **0.3624** | 0.3187 | **0.3462** | 0.1713 | **0.2587** | **0.3260** |
| cl_v6_fair | 0.1405 | **0.1562** | 0.2175 | 0.1132 | **0.3984** | **0.4575** | 0.3371 | 0.3361 | **0.3494** | 0.1888 | **0.2779** | **0.2646** |

##### Aggregate mean across Non-Specific 500-gene datasets

Latent variables: metric=F1, negative_protocol=tf_stratified_1to10, network_group=Non-Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.2256 |
| baseline | 0.2473 |
| scGPT_human | <span style="color:red"><strong>0.2748</strong></span> |
| v4_bias_rec_best | 0.1904 |
| v4_plain_best | 0.2237 |
| v4_type_pe_best | **0.2625** |
| scconcept | 0.0917 |
| scconcept_encoded | 0.0898 |
| cl_scratch_v5 | 0.2134 |
| cl_v6_fair | **0.2527** |

##### Aggregate mean across Non-Specific 1000-gene datasets

Latent variables: metric=F1, negative_protocol=tf_stratified_1to10, network_group=Non-Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.2839** |
| baseline | 0.2629 |
| scGPT_human | <span style="color:red"><strong>0.3171</strong></span> |
| v4_bias_rec_best | 0.2420 |
| v4_plain_best | **0.2822** |
| v4_type_pe_best | **0.2776** |
| scconcept | 0.1641 |
| scconcept_encoded | 0.1531 |
| cl_scratch_v5 | **0.2895** |
| cl_v6_fair | **0.2868** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.3958 | 0.2344 | 0.5099 | 0.5311 | 0.5449 | **0.1964** | **0.5757** | 0.5704 | 0.4559 | **0.4036** | 0.4245 | 0.3983 |
| baseline | 0.4143 | 0.2794 | <span style="color:red"><strong>0.5273</strong></span> | 0.5546 | 0.5598 | 0.1857 | 0.5693 | 0.6133 | 0.5038 | 0.1549 | 0.4297 | 0.4153 |
| scGPT_human | <span style="color:red"><strong>0.4283</strong></span> | 0.2453 | 0.5104 | <span style="color:red"><strong>0.5907</strong></span> | 0.5254 | <span style="color:red"><strong>0.5667</strong></span> | **0.6074** | 0.6013 | **0.5073** | 0.1250 | <span style="color:red"><strong>0.4960</strong></span> | <span style="color:red"><strong>0.5000</strong></span> |
| v4_bias_rec_best | 0.3862 | 0.1974 | 0.5197 | **0.5676** | 0.5268 | **0.4089** | **0.5729** | 0.6006 | 0.4538 | <span style="color:red"><strong>0.4618</strong></span> | 0.3383 | **0.4411** |
| v4_plain_best | 0.3945 | 0.2794 | 0.4669 | **0.5609** | 0.5594 | **0.2714** | **0.6069** | <span style="color:red"><strong>0.6426</strong></span> | 0.4512 | **0.1864** | 0.4227 | 0.3994 |
| v4_type_pe_best | **0.4231** | 0.2464 | 0.4799 | **0.5752** | **0.5683** | **0.2464** | **0.6055** | **0.6354** | 0.4665 | **0.3294** | **0.4569** | 0.3187 |
| scconcept | 0.1246 | <span style="color:red"><strong>0.3855</strong></span> | 0.2441 | 0.1661 | 0.3542 | 0.1400 | 0.2707 | 0.1917 | 0.1373 | 0.0577 | 0.2418 | 0.2105 |
| scconcept_encoded | 0.1107 | 0.1818 | 0.2548 | 0.1090 | 0.2326 | 0.1129 | 0.1758 | 0.1591 | 0.1811 | 0.0189 | 0.2338 | 0.1930 |
| cl_scratch_v5 | 0.3748 | 0.2542 | 0.4931 | 0.4861 | **0.5634** | **0.2615** | **0.5984** | **0.6144** | <span style="color:red"><strong>0.5116</strong></span> | **0.1613** | **0.4457** | 0.3855 |
| cl_v6_fair | 0.4006 | 0.2281 | 0.4782 | 0.5116 | <span style="color:red"><strong>0.5776</strong></span> | **0.2394** | <span style="color:red"><strong>0.6144</strong></span> | 0.5999 | 0.4713 | **0.3129** | **0.4391** | 0.3965 |

##### Aggregate mean across STRING 500-gene datasets

Latent variables: metric=F1, negative_protocol=tf_stratified_1to10, network_group=STRING, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.3890** |
| baseline | 0.3672 |
| scGPT_human | **0.4382** |
| v4_bias_rec_best | <span style="color:red"><strong>0.4462</strong></span> |
| v4_plain_best | **0.3900** |
| v4_type_pe_best | **0.3919** |
| scconcept | 0.1919 |
| scconcept_encoded | 0.1291 |
| cl_scratch_v5 | 0.3605 |
| cl_v6_fair | **0.3814** |

##### Aggregate mean across STRING 1000-gene datasets

Latent variables: metric=F1, negative_protocol=tf_stratified_1to10, network_group=STRING, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.4845 |
| baseline | 0.5007 |
| scGPT_human | <span style="color:red"><strong>0.5125</strong></span> |
| v4_bias_rec_best | 0.4663 |
| v4_plain_best | 0.4836 |
| v4_type_pe_best | 0.5000 |
| scconcept | 0.2288 |
| scconcept_encoded | 0.1981 |
| cl_scratch_v5 | 0.4978 |
| cl_v6_fair | 0.4969 |

### Negative protocol: full_candidate

Latent variables: metric=F1, negative_protocol=full_candidate, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.4005** | **0.3528** | **0.7037** | **0.3294** | 0.0000 | **0.8092** | 0.6816 | 0.7819 | **0.7403** | **0.8113** | <span style="color:red"><strong>0.7929</strong></span> |
| baseline | 0.3603 | 0.3236 | 0.6966 | 0.3276 | 0.0833 | 0.8008 | 0.6925 | <span style="color:red"><strong>0.7890</strong></span> | 0.7357 | 0.8072 | 0.7794 |
| scGPT_human | 0.3049 | <span style="color:red"><strong>0.4341</strong></span> | 0.6639 | <span style="color:red"><strong>0.3891</strong></span> | **0.1000** | **0.8068** | 0.6779 | 0.7771 | 0.7277 | **0.8104** | 0.7598 |
| v4_bias_rec_best | <span style="color:red"><strong>0.4451</strong></span> | **0.3712** | 0.6853 | 0.3008 | 0.0833 | **0.8107** | **0.6988** | 0.7780 | <span style="color:red"><strong>0.7584</strong></span> | **0.8077** | 0.7781 |
| v4_plain_best | **0.4368** | **0.3629** | <span style="color:red"><strong>0.7117</strong></span> | 0.3171 | 0.0833 | **0.8074** | **0.7046** | 0.7840 | 0.7352 | **0.8096** | 0.7708 |
| v4_type_pe_best | **0.4219** | **0.3801** | 0.6883 | 0.3212 | 0.0000 | <span style="color:red"><strong>0.8112</strong></span> | 0.6834 | 0.7858 | **0.7416** | <span style="color:red"><strong>0.8132</strong></span> | 0.7761 |
| scconcept | 0.2696 | **0.3932** | 0.6570 | 0.2354 | <span style="color:red"><strong>0.1111</strong></span> | 0.7908 | 0.6406 | 0.7633 | 0.7167 | 0.8023 | 0.7407 |
| scconcept_encoded | 0.3526 | **0.3801** | 0.6665 | 0.2657 | 0.0000 | 0.7916 | 0.6582 | 0.7639 | 0.7192 | 0.7983 | 0.7374 |
| cl_scratch_v5 | **0.3951** | **0.3870** | 0.6766 | **0.3768** | **0.0909** | **0.8087** | 0.6910 | 0.7832 | 0.7292 | **0.8096** | 0.7697 |
| cl_v6_fair | **0.4252** | **0.3302** | 0.6914 | **0.3517** | 0.0000 | **0.8101** | <span style="color:red"><strong>0.7229</strong></span> | 0.7785 | **0.7361** | **0.8109** | 0.7726 |

##### Aggregate mean across Specific 500-gene datasets

Latent variables: metric=F1, negative_protocol=full_candidate, network_group=Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.5135 |
| baseline | 0.5229 |
| scGPT_human | <span style="color:red"><strong>0.5399</strong></span> |
| v4_bias_rec_best | **0.5380** |
| v4_plain_best | **0.5314** |
| v4_type_pe_best | 0.5162 |
| scconcept | 0.5205 |
| scconcept_encoded | 0.4990 |
| cl_scratch_v5 | **0.5336** |
| cl_v6_fair | 0.5124 |

##### Aggregate mean across Specific 1000-gene datasets

Latent variables: metric=F1, negative_protocol=full_candidate, network_group=Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.6393** |
| baseline | 0.6302 |
| scGPT_human | 0.6254 |
| v4_bias_rec_best | **0.6379** |
| v4_plain_best | **0.6444** |
| v4_type_pe_best | **0.6403** |
| scconcept | 0.5864 |
| scconcept_encoded | 0.6064 |
| cl_scratch_v5 | **0.6417** |
| cl_v6_fair | <span style="color:red"><strong>0.6446</strong></span> |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.0565 | **0.1519** | **0.1393** | **0.0870** | **0.1253** | 0.0714 | <span style="color:red"><strong>0.3040</strong></span> | **0.2220** | <span style="color:red"><strong>0.3109</strong></span> | 0.1067 | **0.2068** | **0.1379** |
| baseline | 0.0659 | 0.1184 | 0.0813 | 0.0444 | 0.1040 | 0.0833 | 0.2801 | 0.2114 | 0.2403 | 0.1235 | 0.1972 | 0.1220 |
| scGPT_human | **0.0660** | <span style="color:red"><strong>0.1620</strong></span> | <span style="color:red"><strong>0.2141</strong></span> | 0.0256 | **0.2269** | 0.0000 | 0.2788 | <span style="color:red"><strong>0.2737</strong></span> | **0.3018** | <span style="color:red"><strong>0.2033</strong></span> | 0.1923 | <span style="color:red"><strong>0.2599</strong></span> |
| v4_bias_rec_best | 0.0448 | 0.0995 | 0.0651 | <span style="color:red"><strong>0.0952</strong></span> | **0.1266** | **0.1250** | 0.2409 | 0.1305 | **0.2559** | 0.1200 | 0.1108 | **0.2465** |
| v4_plain_best | **0.1009** | 0.1131 | **0.0966** | **0.0923** | **0.2286** | 0.0769 | 0.2123 | 0.2009 | **0.2691** | **0.1266** | <span style="color:red"><strong>0.2477</strong></span> | **0.2409** |
| v4_type_pe_best | <span style="color:red"><strong>0.1039</strong></span> | 0.0909 | **0.0982** | **0.0667** | 0.1027 | 0.0714 | 0.2213 | **0.2635** | 0.2231 | **0.1238** | **0.2183** | **0.2061** |
| scconcept | **0.0688** | 0.0563 | 0.0526 | 0.0227 | **0.1215** | 0.0714 | 0.0528 | 0.0442 | 0.1051 | 0.0746 | 0.0632 | 0.0824 |
| scconcept_encoded | 0.0619 | 0.0429 | 0.0336 | 0.0385 | 0.0667 | 0.0000 | 0.0263 | 0.0759 | 0.0437 | 0.0429 | 0.0423 | 0.0843 |
| cl_scratch_v5 | 0.0628 | **0.1481** | **0.1806** | **0.0513** | <span style="color:red"><strong>0.2456</strong></span> | 0.0833 | 0.2653 | **0.2492** | **0.2716** | 0.1184 | 0.1942 | **0.2228** |
| cl_v6_fair | 0.0633 | 0.1136 | 0.0720 | **0.0889** | **0.1200** | <span style="color:red"><strong>0.1429</strong></span> | 0.1932 | 0.1724 | **0.2594** | **0.1333** | 0.1818 | **0.1843** |

##### Aggregate mean across Non-Specific 500-gene datasets

Latent variables: metric=F1, negative_protocol=full_candidate, network_group=Non-Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.1295** |
| baseline | 0.1172 |
| scGPT_human | <span style="color:red"><strong>0.1541</strong></span> |
| v4_bias_rec_best | **0.1361** |
| v4_plain_best | **0.1418** |
| v4_type_pe_best | **0.1370** |
| scconcept | 0.0586 |
| scconcept_encoded | 0.0474 |
| cl_scratch_v5 | **0.1455** |
| cl_v6_fair | **0.1392** |

##### Aggregate mean across Non-Specific 1000-gene datasets

Latent variables: metric=F1, negative_protocol=full_candidate, network_group=Non-Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.1905** |
| baseline | 0.1615 |
| scGPT_human | <span style="color:red"><strong>0.2133</strong></span> |
| v4_bias_rec_best | 0.1407 |
| v4_plain_best | **0.1925** |
| v4_type_pe_best | 0.1612 |
| scconcept | 0.0774 |
| scconcept_encoded | 0.0457 |
| cl_scratch_v5 | **0.2033** |
| cl_v6_fair | 0.1483 |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | <span style="color:red"><strong>0.3551</strong></span> | **0.1837** | **0.4408** | 0.4948 | 0.4039 | 0.3480 | 0.5028 | **0.5592** | **0.3964** | 0.1676 | **0.3673** | 0.2254 |
| baseline | 0.2906 | 0.1538 | 0.4189 | 0.5383 | 0.4066 | 0.3519 | 0.5031 | 0.4766 | 0.3580 | <span style="color:red"><strong>0.2110</strong></span> | 0.3244 | 0.3500 |
| scGPT_human | 0.2786 | <span style="color:red"><strong>0.2000</strong></span> | **0.4377** | <span style="color:red"><strong>0.5559</strong></span> | <span style="color:red"><strong>0.4438</strong></span> | **0.4532** | **0.5211** | **0.5723** | **0.4182** | 0.1102 | <span style="color:red"><strong>0.3916</strong></span> | 0.3271 |
| v4_bias_rec_best | 0.2549 | 0.1273 | <span style="color:red"><strong>0.4495</strong></span> | 0.4634 | 0.3945 | **0.3761** | 0.4789 | **0.5479** | 0.3277 | 0.1682 | 0.2041 | 0.3036 |
| v4_plain_best | 0.2811 | **0.1754** | **0.4268** | 0.4381 | **0.4219** | <span style="color:red"><strong>0.5201</strong></span> | 0.4961 | **0.5132** | **0.4022** | 0.1646 | **0.3439** | 0.3455 |
| v4_type_pe_best | 0.2597 | **0.1569** | **0.4396** | 0.5177 | **0.4409** | **0.3797** | 0.4909 | **0.5392** | **0.4092** | 0.0638 | **0.3444** | <span style="color:red"><strong>0.4453</strong></span> |
| scconcept | 0.0448 | **0.1667** | 0.2163 | 0.0630 | 0.2042 | 0.0941 | 0.1503 | 0.0873 | 0.0733 | 0.0256 | 0.0857 | 0.1346 |
| scconcept_encoded | 0.0261 | 0.0870 | 0.0899 | 0.1080 | 0.1405 | 0.0429 | 0.0890 | 0.1093 | 0.0172 | 0.0233 | 0.0215 | 0.1311 |
| cl_scratch_v5 | 0.2249 | 0.1452 | **0.4423** | 0.4379 | **0.4199** | **0.4102** | <span style="color:red"><strong>0.5380</strong></span> | <span style="color:red"><strong>0.5834</strong></span> | <span style="color:red"><strong>0.4313</strong></span> | 0.1087 | **0.3348** | 0.3414 |
| cl_v6_fair | 0.2587 | **0.1667** | **0.4354** | 0.4247 | **0.4233** | **0.4361** | **0.5057** | **0.5467** | **0.4002** | 0.0727 | **0.3635** | **0.3589** |

##### Aggregate mean across STRING 500-gene datasets

Latent variables: metric=F1, negative_protocol=full_candidate, network_group=STRING, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.3298 |
| baseline | 0.3469 |
| scGPT_human | <span style="color:red"><strong>0.3698</strong></span> |
| v4_bias_rec_best | 0.3311 |
| v4_plain_best | **0.3595** |
| v4_type_pe_best | **0.3504** |
| scconcept | 0.0952 |
| scconcept_encoded | 0.0836 |
| cl_scratch_v5 | 0.3378 |
| cl_v6_fair | 0.3343 |

##### Aggregate mean across STRING 1000-gene datasets

Latent variables: metric=F1, negative_protocol=full_candidate, network_group=STRING, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.4111** |
| baseline | 0.3836 |
| scGPT_human | <span style="color:red"><strong>0.4152</strong></span> |
| v4_bias_rec_best | 0.3516 |
| v4_plain_best | **0.3953** |
| v4_type_pe_best | **0.3974** |
| scconcept | 0.1291 |
| scconcept_encoded | 0.0641 |
| cl_scratch_v5 | **0.3985** |
| cl_v6_fair | **0.3978** |

## SPECIFICITY (Supplementary)

### Negative protocol: tf_stratified_1to10

Latent variables: metric=SPECIFICITY, negative_protocol=tf_stratified_1to10, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.8509** | 0.8505 | 0.8774 | 0.9059 | 0.9625 | 0.6394 | 0.7559 | **0.6873** | **0.6533** | **0.6168** | **0.6315** |
| baseline | 0.8470 | 0.8527 | 0.8868 | 0.9246 | 0.9875 | 0.6416 | <span style="color:red"><strong>0.7637</strong></span> | 0.6310 | 0.6326 | 0.6025 | 0.5820 |
| scGPT_human | <span style="color:red"><strong>0.8743</strong></span> | 0.8000 | 0.8722 | 0.9138 | **0.9938** | <span style="color:red"><strong>0.6507</strong></span> | 0.6934 | **0.6561** | **0.6395** | **0.6263** | **0.6094** |
| v4_bias_rec_best | 0.8431 | 0.8430 | 0.8851 | **0.9260** | 0.9688 | 0.6200 | 0.7383 | **0.6476** | **0.6519** | <span style="color:red"><strong>0.6485</strong></span> | **0.6263** |
| v4_plain_best | **0.8733** | 0.8161 | <span style="color:red"><strong>0.8902</strong></span> | <span style="color:red"><strong>0.9325</strong></span> | 0.9812 | 0.6216 | 0.7246 | **0.6756** | **0.6367** | **0.6136** | **0.6224** |
| v4_type_pe_best | **0.8665** | 0.8333 | 0.8756 | **0.9289** | **0.9938** | 0.6313 | 0.7363 | **0.6723** | 0.5843 | **0.6311** | <span style="color:red"><strong>0.6328</strong></span> |
| scconcept | 0.8095 | 0.8247 | 0.8302 | 0.9052 | <span style="color:red"><strong>1.0000</strong></span> | 0.6146 | 0.6387 | 0.6006 | 0.5953 | **0.6092** | 0.5247 |
| scconcept_encoded | 0.8212 | 0.7763 | 0.8559 | 0.9167 | 0.9750 | 0.6055 | 0.6602 | 0.6148 | 0.5677 | 0.5627 | 0.5169 |
| cl_scratch_v5 | **0.8577** | <span style="color:red"><strong>0.8559</strong></span> | 0.8868 | 0.9246 | 0.9875 | 0.6222 | 0.7168 | **0.6399** | <span style="color:red"><strong>0.6727</strong></span> | 0.6009 | **0.6302** |
| cl_v6_fair | **0.8567** | 0.8473 | **0.8885** | 0.9195 | 0.9812 | 0.6039 | 0.7012 | <span style="color:red"><strong>0.6934</strong></span> | 0.6064 | **0.6334** | **0.5990** |

##### Aggregate mean across Specific 500-gene datasets

Latent variables: metric=SPECIFICITY, negative_protocol=tf_stratified_1to10, network_group=Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.7707** |
| baseline | 0.7637 |
| scGPT_human | 0.7472 |
| v4_bias_rec_best | **0.7657** |
| v4_plain_best | 0.7562 |
| v4_type_pe_best | 0.7561 |
| scconcept | 0.7167 |
| scconcept_encoded | 0.6992 |
| cl_scratch_v5 | <span style="color:red"><strong>0.7726</strong></span> |
| cl_v6_fair | 0.7470 |

##### Aggregate mean across Specific 1000-gene datasets

Latent variables: metric=SPECIFICITY, negative_protocol=tf_stratified_1to10, network_group=Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.7629** |
| baseline | 0.7556 |
| scGPT_human | **0.7656** |
| v4_bias_rec_best | **0.7617** |
| v4_plain_best | <span style="color:red"><strong>0.7678</strong></span> |
| v4_type_pe_best | **0.7676** |
| scconcept | 0.7282 |
| scconcept_encoded | 0.7295 |
| cl_scratch_v5 | 0.7553 |
| cl_v6_fair | **0.7659** |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.9610 | 0.9356 | <span style="color:red"><strong>0.9624</strong></span> | **0.9534** | 0.9636 | 0.9909 | 0.9557 | **0.9461** | **0.9691** | 0.9603 | 0.9726 | **0.9750** |
| baseline | 0.9610 | 0.9521 | 0.9515 | 0.9448 | 0.9651 | 0.9909 | 0.9647 | 0.9295 | 0.9653 | 0.9641 | 0.9726 | 0.9620 |
| scGPT_human | 0.9203 | **0.9611** | 0.9479 | **0.9690** | 0.9601 | 0.9909 | 0.9581 | <span style="color:red"><strong>0.9693</strong></span> | 0.9555 | **0.9705** | 0.9446 | <span style="color:red"><strong>0.9859</strong></span> |
| v4_bias_rec_best | **0.9622** | 0.9521 | **0.9521** | 0.9414 | <span style="color:red"><strong>0.9717</strong></span> | <span style="color:red"><strong>1.0000</strong></span> | 0.9593 | **0.9337** | <span style="color:red"><strong>0.9713</strong></span> | 0.9564 | 0.9716 | 0.9522 |
| v4_plain_best | 0.9459 | 0.9476 | **0.9572** | **0.9534** | **0.9651** | <span style="color:red"><strong>1.0000</strong></span> | **0.9665** | **0.9320** | **0.9661** | 0.9564 | 0.9703 | **0.9674** |
| v4_type_pe_best | <span style="color:red"><strong>0.9720</strong></span> | 0.9506 | **0.9526** | **0.9707** | 0.9616 | 0.9682 | **0.9662** | **0.9395** | 0.9540 | 0.9590 | 0.9723 | **0.9641** |
| scconcept | 0.9301 | <span style="color:red"><strong>0.9656</strong></span> | 0.9490 | <span style="color:red"><strong>0.9741</strong></span> | 0.9349 | **0.9955** | 0.9469 | **0.9502** | 0.9427 | <span style="color:red"><strong>0.9744</strong></span> | 0.9395 | **0.9685** |
| scconcept_encoded | 0.9500 | 0.9326 | 0.9510 | **0.9621** | 0.9484 | 0.9727 | 0.9499 | **0.9428** | 0.9472 | 0.9615 | 0.9466 | **0.9674** |
| cl_scratch_v5 | **0.9663** | **0.9551** | **0.9536** | **0.9707** | **0.9663** | 0.9909 | <span style="color:red"><strong>0.9707</strong></span> | **0.9328** | 0.9600 | 0.9603 | <span style="color:red"><strong>0.9733</strong></span> | **0.9685** |
| cl_v6_fair | **0.9638** | 0.9416 | 0.9495 | **0.9690** | **0.9674** | 0.9773 | **0.9656** | **0.9362** | 0.9615 | 0.9397 | 0.9646 | **0.9630** |

##### Aggregate mean across Non-Specific 500-gene datasets

Latent variables: metric=SPECIFICITY, negative_protocol=tf_stratified_1to10, network_group=Non-Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.9602** |
| baseline | 0.9572 |
| scGPT_human | <span style="color:red"><strong>0.9744</strong></span> |
| v4_bias_rec_best | 0.9560 |
| v4_plain_best | **0.9595** |
| v4_type_pe_best | **0.9587** |
| scconcept | **0.9714** |
| scconcept_encoded | 0.9565 |
| cl_scratch_v5 | **0.9630** |
| cl_v6_fair | 0.9545 |

##### Aggregate mean across Non-Specific 1000-gene datasets

Latent variables: metric=SPECIFICITY, negative_protocol=tf_stratified_1to10, network_group=Non-Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.9640** |
| baseline | 0.9634 |
| scGPT_human | 0.9477 |
| v4_bias_rec_best | **0.9647** |
| v4_plain_best | 0.9619 |
| v4_type_pe_best | 0.9631 |
| scconcept | 0.9405 |
| scconcept_encoded | 0.9489 |
| cl_scratch_v5 | <span style="color:red"><strong>0.9650</strong></span> |
| cl_v6_fair | 0.9621 |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.9534 | 0.9734 | 0.9642 | 0.9625 | 0.9684 | **0.9811** | 0.9667 | **0.9705** | 0.9605 | **0.9645** | **0.9662** | 0.9706 |
| baseline | 0.9563 | 0.9734 | <span style="color:red"><strong>0.9709</strong></span> | 0.9625 | <span style="color:red"><strong>0.9718</strong></span> | 0.9623 | <span style="color:red"><strong>0.9699</strong></span> | 0.9689 | 0.9636 | 0.9532 | 0.9649 | 0.9794 |
| scGPT_human | <span style="color:red"><strong>0.9626</strong></span> | <span style="color:red"><strong>0.9875</strong></span> | 0.9602 | <span style="color:red"><strong>0.9662</strong></span> | 0.9608 | 0.9591 | 0.9616 | <span style="color:red"><strong>0.9762</strong></span> | <span style="color:red"><strong>0.9647</strong></span> | <span style="color:red"><strong>0.9823</strong></span> | 0.9571 | **0.9853** |
| v4_bias_rec_best | 0.9462 | 0.9547 | 0.9665 | **0.9640** | 0.9675 | 0.9465 | 0.9656 | **0.9713** | **0.9643** | **0.9581** | <span style="color:red"><strong>0.9689</strong></span> | <span style="color:red"><strong>0.9882</strong></span> |
| v4_plain_best | 0.9555 | 0.9734 | 0.9647 | **0.9647** | 0.9708 | **0.9717** | 0.9675 | **0.9713** | 0.9593 | **0.9726** | 0.9564 | **0.9868** |
| v4_type_pe_best | 0.9525 | 0.9688 | 0.9679 | 0.9617 | 0.9711 | **0.9701** | 0.9653 | 0.9672 | 0.9578 | **0.9677** | **0.9659** | <span style="color:red"><strong>0.9882</strong></span> |
| scconcept | 0.9454 | **0.9781** | 0.9553 | 0.9542 | 0.9514 | <span style="color:red"><strong>0.9843</strong></span> | 0.9497 | **0.9713** | 0.9516 | **0.9710** | 0.9436 | **0.9838** |
| scconcept_encoded | 0.9471 | **0.9797** | 0.9607 | 0.9550 | 0.9665 | **0.9654** | 0.9645 | 0.9590 | 0.9496 | **0.9661** | 0.9500 | **0.9824** |
| cl_scratch_v5 | 0.9466 | **0.9812** | 0.9651 | 0.9602 | 0.9691 | **0.9764** | 0.9669 | 0.9639 | 0.9589 | **0.9661** | 0.9618 | 0.9750 |
| cl_v6_fair | 0.9542 | **0.9812** | 0.9660 | 0.9489 | 0.9682 | **0.9670** | 0.9685 | 0.9639 | 0.9547 | **0.9661** | 0.9635 | **0.9809** |

##### Aggregate mean across STRING 500-gene datasets

Latent variables: metric=SPECIFICITY, negative_protocol=tf_stratified_1to10, network_group=STRING, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.9704** |
| baseline | 0.9666 |
| scGPT_human | <span style="color:red"><strong>0.9761</strong></span> |
| v4_bias_rec_best | 0.9638 |
| v4_plain_best | **0.9734** |
| v4_type_pe_best | **0.9706** |
| scconcept | **0.9738** |
| scconcept_encoded | **0.9679** |
| cl_scratch_v5 | **0.9705** |
| cl_v6_fair | **0.9680** |

##### Aggregate mean across STRING 1000-gene datasets

Latent variables: metric=SPECIFICITY, negative_protocol=tf_stratified_1to10, network_group=STRING, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.9632 |
| baseline | <span style="color:red"><strong>0.9662</strong></span> |
| scGPT_human | 0.9612 |
| v4_bias_rec_best | 0.9632 |
| v4_plain_best | 0.9624 |
| v4_type_pe_best | 0.9634 |
| scconcept | 0.9495 |
| scconcept_encoded | 0.9564 |
| cl_scratch_v5 | 0.9614 |
| cl_v6_fair | 0.9625 |

### Negative protocol: full_candidate

Latent variables: metric=SPECIFICITY, negative_protocol=full_candidate, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.9269 | 0.9171 | 0.9319 | 0.9716 | **0.9978** | 0.7757 | 0.7638 | **0.7701** | <span style="color:red"><strong>0.6892</strong></span> | <span style="color:red"><strong>0.7449</strong></span> | **0.6045** |
| baseline | 0.9408 | 0.9257 | 0.9330 | 0.9733 | 0.9933 | 0.7806 | 0.7739 | 0.7487 | 0.6561 | 0.6973 | 0.5886 |
| scGPT_human | <span style="color:red"><strong>0.9450</strong></span> | 0.9051 | 0.9313 | 0.9622 | **0.9978** | **0.7935** | 0.7652 | **0.7856** | 0.6506 | **0.7026** | <span style="color:red"><strong>0.6230</strong></span> |
| v4_bias_rec_best | 0.9138 | 0.9229 | 0.9302 | <span style="color:red"><strong>0.9792</strong></span> | 0.9933 | **0.7928** | 0.7725 | **0.7637** | 0.6188 | **0.7097** | **0.6019** |
| v4_plain_best | 0.9220 | <span style="color:red"><strong>0.9320</strong></span> | **0.9426** | 0.9698 | 0.9933 | <span style="color:red"><strong>0.8011</strong></span> | **0.8014** | **0.7786** | 0.6312 | 0.6932 | 0.5873 |
| v4_type_pe_best | 0.9342 | **0.9280** | **0.9347** | **0.9762** | 0.9933 | 0.7668 | <span style="color:red"><strong>0.8261</strong></span> | **0.7699** | 0.6229 | 0.6826 | 0.5820 |
| scconcept | **0.9413** | 0.9183 | 0.9054 | 0.9592 | <span style="color:red"><strong>1.0000</strong></span> | 0.7754 | 0.7565 | 0.7468 | 0.6354 | 0.6546 | 0.5476 |
| scconcept_encoded | 0.9239 | 0.9154 | 0.9178 | 0.9680 | 0.9888 | 0.7681 | **0.7913** | 0.7414 | 0.5732 | 0.6805 | 0.5066 |
| cl_scratch_v5 | 0.9321 | 0.9217 | <span style="color:red"><strong>0.9499</strong></span> | 0.9721 | **0.9955** | 0.7711 | **0.7986** | **0.7755** | 0.6492 | **0.7044** | 0.5780 |
| cl_v6_fair | 0.9218 | 0.9206 | 0.9257 | **0.9751** | **0.9933** | **0.7875** | **0.7928** | <span style="color:red"><strong>0.8020</strong></span> | **0.6602** | **0.7013** | **0.5992** |

##### Aggregate mean across Specific 500-gene datasets

Latent variables: metric=SPECIFICITY, negative_protocol=full_candidate, network_group=Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | <span style="color:red"><strong>0.7945</strong></span> |
| baseline | 0.7875 |
| scGPT_human | **0.7883** |
| v4_bias_rec_best | 0.7818 |
| v4_plain_best | **0.7890** |
| v4_type_pe_best | **0.7905** |
| scconcept | 0.7716 |
| scconcept_encoded | 0.7551 |
| cl_scratch_v5 | **0.7886** |
| cl_v6_fair | **0.7932** |

##### Aggregate mean across Specific 1000-gene datasets

Latent variables: metric=SPECIFICITY, negative_protocol=full_candidate, network_group=Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | <span style="color:red"><strong>0.8535</strong></span> |
| baseline | 0.8456 |
| scGPT_human | **0.8534** |
| v4_bias_rec_best | **0.8482** |
| v4_plain_best | **0.8512** |
| v4_type_pe_best | 0.8441 |
| scconcept | 0.8304 |
| scconcept_encoded | 0.8333 |
| cl_scratch_v5 | **0.8509** |
| cl_v6_fair | **0.8522** |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.9969** | 0.9931 | 0.9980 | 0.9959 | 0.9988 | 0.9988 | 0.9964 | **0.9898** | **0.9988** | **0.9912** | **0.9986** | **0.9928** |
| baseline | 0.9967 | 0.9931 | <span style="color:red"><strong>0.9990</strong></span> | 0.9959 | 0.9989 | <span style="color:red"><strong>1.0000</strong></span> | 0.9971 | 0.9892 | 0.9987 | 0.9906 | 0.9978 | 0.9903 |
| scGPT_human | 0.9935 | <span style="color:red"><strong>0.9945</strong></span> | 0.9935 | **0.9971** | 0.9946 | 0.9988 | 0.9953 | **0.9907** | 0.9954 | **0.9921** | 0.9960 | <span style="color:red"><strong>0.9947</strong></span> |
| v4_bias_rec_best | <span style="color:red"><strong>0.9980</strong></span> | 0.9923 | 0.9983 | **0.9971** | 0.9985 | 0.9981 | 0.9961 | 0.9873 | **0.9988** | **0.9921** | <span style="color:red"><strong>0.9990</strong></span> | **0.9906** |
| v4_plain_best | **0.9973** | **0.9939** | 0.9974 | 0.9944 | 0.9979 | 0.9994 | 0.9965 | 0.9858 | **0.9989** | **0.9912** | **0.9989** | **0.9939** |
| v4_type_pe_best | **0.9975** | 0.9923 | 0.9982 | **0.9962** | <span style="color:red"><strong>0.9990</strong></span> | 0.9988 | **0.9975** | 0.9879 | <span style="color:red"><strong>0.9992</strong></span> | 0.9900 | **0.9980** | **0.9914** |
| scconcept | 0.9950 | 0.9931 | 0.9942 | 0.9956 | 0.9966 | 0.9988 | 0.9967 | 0.9858 | 0.9957 | <span style="color:red"><strong>0.9932</strong></span> | 0.9963 | **0.9911** |
| scconcept_encoded | 0.9959 | 0.9914 | 0.9973 | 0.9939 | 0.9978 | 0.9988 | <span style="color:red"><strong>0.9979</strong></span> | 0.9856 | 0.9983 | **0.9918** | **0.9987** | **0.9917** |
| cl_scratch_v5 | **0.9974** | 0.9925 | 0.9979 | <span style="color:red"><strong>0.9977</strong></span> | 0.9971 | <span style="color:red"><strong>1.0000</strong></span> | 0.9968 | 0.9873 | 0.9977 | **0.9918** | **0.9979** | **0.9911** |
| cl_v6_fair | **0.9975** | 0.9901 | 0.9989 | **0.9965** | 0.9980 | 0.9994 | **0.9974** | <span style="color:red"><strong>0.9911</strong></span> | 0.9977 | **0.9923** | **0.9984** | 0.9884 |

##### Aggregate mean across Non-Specific 500-gene datasets

Latent variables: metric=SPECIFICITY, negative_protocol=full_candidate, network_group=Non-Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.9936** |
| baseline | 0.9932 |
| scGPT_human | <span style="color:red"><strong>0.9946</strong></span> |
| v4_bias_rec_best | 0.9929 |
| v4_plain_best | 0.9931 |
| v4_type_pe_best | 0.9928 |
| scconcept | 0.9929 |
| scconcept_encoded | 0.9922 |
| cl_scratch_v5 | **0.9934** |
| cl_v6_fair | 0.9930 |

##### Aggregate mean across Non-Specific 1000-gene datasets

Latent variables: metric=SPECIFICITY, negative_protocol=full_candidate, network_group=Non-Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.9979 |
| baseline | 0.9980 |
| scGPT_human | 0.9947 |
| v4_bias_rec_best | **0.9981** |
| v4_plain_best | 0.9978 |
| v4_type_pe_best | <span style="color:red"><strong>0.9982</strong></span> |
| scconcept | 0.9957 |
| scconcept_encoded | 0.9976 |
| cl_scratch_v5 | 0.9975 |
| cl_v6_fair | 0.9980 |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.9984 | <span style="color:red"><strong>0.9985</strong></span> | 0.9971 | **0.9917** | 0.9965 | **0.9944** | **0.9979** | 0.9949 | 0.9981 | **0.9972** | **0.9992** | **0.9979** |
| baseline | 0.9987 | 0.9978 | 0.9979 | 0.9903 | 0.9972 | 0.9935 | 0.9977 | 0.9949 | 0.9990 | 0.9962 | 0.9990 | 0.9967 |
| scGPT_human | 0.9962 | <span style="color:red"><strong>0.9985</strong></span> | 0.9953 | <span style="color:red"><strong>0.9930</strong></span> | 0.9941 | <span style="color:red"><strong>0.9964</strong></span> | 0.9953 | <span style="color:red"><strong>0.9968</strong></span> | 0.9963 | <span style="color:red"><strong>0.9992</strong></span> | 0.9977 | <span style="color:red"><strong>0.9990</strong></span> |
| v4_bias_rec_best | 0.9983 | 0.9971 | 0.9959 | **0.9905** | 0.9967 | 0.9903 | 0.9976 | **0.9959** | <span style="color:red"><strong>0.9991</strong></span> | **0.9970** | <span style="color:red"><strong>0.9993</strong></span> | **0.9973** |
| v4_plain_best | <span style="color:red"><strong>0.9990</strong></span> | 0.9973 | 0.9970 | 0.9877 | 0.9968 | 0.9927 | **0.9979** | **0.9959** | 0.9989 | **0.9984** | **0.9993** | **0.9971** |
| v4_type_pe_best | **0.9988** | **0.9980** | 0.9974 | **0.9909** | 0.9965 | 0.9915 | **0.9980** | **0.9956** | **0.9990** | **0.9974** | 0.9990 | **0.9983** |
| scconcept | 0.9970 | 0.9976 | 0.9971 | 0.9886 | 0.9957 | 0.9847 | 0.9968 | 0.9926 | 0.9973 | **0.9986** | 0.9981 | **0.9977** |
| scconcept_encoded | **0.9988** | **0.9982** | <span style="color:red"><strong>0.9984</strong></span> | 0.9892 | 0.9965 | 0.9863 | **0.9982** | 0.9926 | 0.9984 | **0.9974** | 0.9988 | **0.9969** |
| cl_scratch_v5 | **0.9989** | 0.9962 | 0.9971 | **0.9915** | 0.9970 | **0.9944** | 0.9974 | **0.9958** | **0.9990** | **0.9966** | 0.9989 | **0.9971** |
| cl_v6_fair | 0.9985 | 0.9967 | 0.9975 | 0.9894 | <span style="color:red"><strong>0.9972</strong></span> | 0.9931 | <span style="color:red"><strong>0.9983</strong></span> | 0.9947 | 0.9984 | 0.9960 | 0.9989 | **0.9981** |

##### Aggregate mean across STRING 500-gene datasets

Latent variables: metric=SPECIFICITY, negative_protocol=full_candidate, network_group=STRING, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.9958** |
| baseline | 0.9949 |
| scGPT_human | <span style="color:red"><strong>0.9972</strong></span> |
| v4_bias_rec_best | 0.9947 |
| v4_plain_best | 0.9949 |
| v4_type_pe_best | **0.9953** |
| scconcept | 0.9933 |
| scconcept_encoded | 0.9934 |
| cl_scratch_v5 | **0.9953** |
| cl_v6_fair | 0.9947 |

##### Aggregate mean across STRING 1000-gene datasets

Latent variables: metric=SPECIFICITY, negative_protocol=full_candidate, network_group=STRING, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.9979 |
| baseline | <span style="color:red"><strong>0.9982</strong></span> |
| scGPT_human | 0.9958 |
| v4_bias_rec_best | 0.9978 |
| v4_plain_best | 0.9981 |
| v4_type_pe_best | 0.9981 |
| scconcept | 0.9970 |
| scconcept_encoded | 0.9982 |
| cl_scratch_v5 | 0.9981 |
| cl_v6_fair | 0.9981 |

## AUPRC_GAIN (Supplementary)

### Negative protocol: tf_stratified_1to10

Latent variables: metric=AUPRC_GAIN, negative_protocol=tf_stratified_1to10, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.1785 | 0.1279 | 0.4318 | **0.1945** | 0.0424 | 0.2772 | 0.3025 | <span style="color:red"><strong>0.2905</strong></span> | **0.2536** | <span style="color:red"><strong>0.2661</strong></span> | <span style="color:red"><strong>0.2613</strong></span> |
| baseline | <span style="color:red"><strong>0.1970</strong></span> | 0.1578 | 0.4536 | 0.1928 | 0.0795 | 0.2777 | 0.3112 | 0.2792 | 0.2233 | 0.2535 | 0.2287 |
| scGPT_human | 0.1937 | **0.1619** | 0.4218 | 0.1897 | <span style="color:red"><strong>0.1298</strong></span> | 0.2690 | 0.2835 | 0.2776 | **0.2393** | **0.2656** | **0.2337** |
| v4_bias_rec_best | 0.1720 | 0.1548 | 0.4384 | **0.2151** | -0.0049 | 0.2761 | 0.2959 | **0.2858** | **0.2429** | **0.2574** | **0.2371** |
| v4_plain_best | 0.1933 | 0.1352 | 0.4496 | <span style="color:red"><strong>0.2284</strong></span> | **0.0918** | 0.2747 | 0.2793 | **0.2841** | **0.2290** | **0.2544** | **0.2533** |
| v4_type_pe_best | 0.1933 | **0.1631** | 0.4485 | **0.1931** | 0.0631 | 0.2770 | <span style="color:red"><strong>0.3201</strong></span> | **0.2820** | **0.2382** | **0.2630** | **0.2451** |
| scconcept | 0.1023 | 0.1288 | 0.3676 | 0.1338 | **0.1155** | 0.2518 | 0.2224 | 0.2355 | 0.1969 | 0.2496 | 0.1696 |
| scconcept_encoded | 0.1192 | 0.0940 | 0.3401 | 0.1246 | 0.0034 | 0.2459 | 0.2542 | 0.2398 | 0.2030 | 0.2323 | 0.1701 |
| cl_scratch_v5 | 0.1677 | <span style="color:red"><strong>0.1762</strong></span> | 0.4417 | **0.2278** | 0.0512 | 0.2750 | 0.3067 | **0.2868** | **0.2525** | **0.2572** | **0.2294** |
| cl_v6_fair | 0.1457 | 0.1078 | <span style="color:red"><strong>0.4552</strong></span> | **0.2273** | 0.0483 | <span style="color:red"><strong>0.2790</strong></span> | 0.2960 | **0.2876** | <span style="color:red"><strong>0.2598</strong></span> | **0.2585** | **0.2382** |

##### Aggregate mean across Specific 500-gene datasets

Latent variables: metric=AUPRC_GAIN, negative_protocol=tf_stratified_1to10, network_group=Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.1975 |
| baseline | 0.2001 |
| scGPT_human | <span style="color:red"><strong>0.2096</strong></span> |
| v4_bias_rec_best | 0.1852 |
| v4_plain_best | 0.1977 |
| v4_type_pe_best | **0.2059** |
| scconcept | 0.1666 |
| scconcept_encoded | 0.1450 |
| cl_scratch_v5 | **0.2032** |
| cl_v6_fair | 0.1900 |

##### Aggregate mean across Specific 1000-gene datasets

Latent variables: metric=AUPRC_GAIN, negative_protocol=tf_stratified_1to10, network_group=Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.2731 |
| baseline | 0.2756 |
| scGPT_human | 0.2696 |
| v4_bias_rec_best | 0.2741 |
| v4_plain_best | <span style="color:red"><strong>0.2807</strong></span> |
| v4_type_pe_best | **0.2761** |
| scconcept | 0.2234 |
| scconcept_encoded | 0.2170 |
| cl_scratch_v5 | **0.2760** |
| cl_v6_fair | 0.2756 |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.1162 | 0.1125 | 0.1712 | **0.1392** | **0.3194** | 0.1911 | **0.2749** | **0.2453** | **0.2558** | 0.1423 | **0.2162** | **0.1976** |
| baseline | 0.1217 | 0.1147 | 0.1886 | 0.1326 | 0.2911 | 0.3950 | 0.2643 | 0.2379 | 0.2246 | 0.1850 | 0.1826 | 0.1822 |
| scGPT_human | 0.1047 | <span style="color:red"><strong>0.1300</strong></span> | <span style="color:red"><strong>0.2586</strong></span> | <span style="color:red"><strong>0.2280</strong></span> | **0.3136** | 0.2100 | 0.2481 | <span style="color:red"><strong>0.3258</strong></span> | <span style="color:red"><strong>0.2884</strong></span> | <span style="color:red"><strong>0.3184</strong></span> | <span style="color:red"><strong>0.2471</strong></span> | <span style="color:red"><strong>0.3154</strong></span> |
| v4_bias_rec_best | 0.0938 | 0.0568 | 0.1325 | **0.1611** | 0.2848 | 0.3259 | 0.2422 | **0.2582** | **0.2836** | 0.1436 | **0.2085** | **0.1940** |
| v4_plain_best | 0.1060 | 0.0955 | **0.1939** | **0.1830** | 0.2725 | 0.2970 | 0.2582 | **0.2523** | **0.2305** | 0.1726 | 0.1759 | **0.2693** |
| v4_type_pe_best | <span style="color:red"><strong>0.1455</strong></span> | 0.0471 | **0.1974** | 0.0970 | **0.2921** | 0.2849 | 0.2509 | **0.2631** | **0.2484** | 0.1842 | **0.2268** | **0.3107** |
| scconcept | 0.0565 | 0.0626 | 0.1105 | 0.0440 | 0.1101 | 0.0651 | 0.0744 | 0.0193 | 0.1033 | 0.1448 | 0.1104 | 0.0667 |
| scconcept_encoded | 0.0346 | 0.0266 | 0.0921 | 0.0615 | 0.0747 | 0.0838 | 0.0772 | 0.0404 | 0.0916 | 0.0658 | 0.1082 | 0.0655 |
| cl_scratch_v5 | **0.1327** | 0.1080 | **0.1939** | **0.1359** | **0.3438** | 0.2813 | <span style="color:red"><strong>0.2933</strong></span> | 0.2237 | **0.2677** | 0.1331 | **0.2114** | **0.2569** |
| cl_v6_fair | **0.1275** | 0.0770 | 0.1836 | 0.0690 | <span style="color:red"><strong>0.3497</strong></span> | <span style="color:red"><strong>0.4187</strong></span> | 0.2515 | 0.2230 | **0.2675** | 0.1501 | **0.2377** | 0.1741 |

##### Aggregate mean across Non-Specific 500-gene datasets

Latent variables: metric=AUPRC_GAIN, negative_protocol=tf_stratified_1to10, network_group=Non-Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.1713 |
| baseline | 0.2079 |
| scGPT_human | <span style="color:red"><strong>0.2546</strong></span> |
| v4_bias_rec_best | 0.1899 |
| v4_plain_best | **0.2116** |
| v4_type_pe_best | 0.1978 |
| scconcept | 0.0671 |
| scconcept_encoded | 0.0573 |
| cl_scratch_v5 | 0.1898 |
| cl_v6_fair | 0.1853 |

##### Aggregate mean across Non-Specific 1000-gene datasets

Latent variables: metric=AUPRC_GAIN, negative_protocol=tf_stratified_1to10, network_group=Non-Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.2256** |
| baseline | 0.2122 |
| scGPT_human | <span style="color:red"><strong>0.2434</strong></span> |
| v4_bias_rec_best | 0.2076 |
| v4_plain_best | 0.2061 |
| v4_type_pe_best | **0.2268** |
| scconcept | 0.0942 |
| scconcept_encoded | 0.0797 |
| cl_scratch_v5 | **0.2404** |
| cl_v6_fair | **0.2362** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.3078 | 0.1943 | 0.4490 | **0.5214** | 0.4591 | 0.2524 | **0.5379** | **0.5642** | 0.3950 | **0.3547** | **0.3819** | **0.4133** |
| baseline | 0.3337 | 0.2229 | <span style="color:red"><strong>0.4641</strong></span> | 0.4892 | 0.4772 | 0.2643 | 0.5295 | 0.5382 | 0.4545 | 0.1753 | 0.3735 | 0.4103 |
| scGPT_human | <span style="color:red"><strong>0.3673</strong></span> | <span style="color:red"><strong>0.3222</strong></span> | 0.4362 | <span style="color:red"><strong>0.5282</strong></span> | 0.4359 | <span style="color:red"><strong>0.4619</strong></span> | <span style="color:red"><strong>0.5505</strong></span> | <span style="color:red"><strong>0.6093</strong></span> | <span style="color:red"><strong>0.4826</strong></span> | **0.1856** | <span style="color:red"><strong>0.4394</strong></span> | <span style="color:red"><strong>0.4497</strong></span> |
| v4_bias_rec_best | 0.2841 | 0.1542 | 0.4537 | 0.4750 | 0.4481 | **0.3668** | 0.5172 | **0.5581** | 0.4016 | <span style="color:red"><strong>0.4212</strong></span> | 0.3729 | **0.4493** |
| v4_plain_best | 0.2907 | 0.1839 | 0.4313 | 0.4885 | 0.4750 | **0.3169** | **0.5406** | **0.5554** | 0.3898 | **0.2165** | **0.3793** | **0.4435** |
| v4_type_pe_best | 0.3310 | **0.2925** | 0.4324 | 0.4870 | <span style="color:red"><strong>0.5105</strong></span> | 0.2606 | **0.5327** | **0.5418** | 0.4423 | **0.3660** | **0.3884** | 0.4027 |
| scconcept | 0.1184 | **0.3074** | 0.1944 | 0.1514 | 0.2365 | 0.1211 | 0.1987 | 0.1703 | 0.1216 | 0.0473 | 0.1505 | 0.2119 |
| scconcept_encoded | 0.0660 | 0.1640 | 0.1798 | 0.0877 | 0.1891 | 0.1229 | 0.1243 | 0.0927 | 0.1013 | 0.0456 | 0.1121 | 0.1523 |
| cl_scratch_v5 | 0.3204 | **0.2388** | 0.4460 | 0.4458 | 0.4730 | **0.3161** | 0.5273 | **0.5970** | **0.4685** | **0.2403** | **0.4074** | 0.3783 |
| cl_v6_fair | **0.3372** | **0.2361** | 0.4207 | **0.4915** | 0.4539 | **0.3228** | **0.5355** | 0.5264 | 0.4462 | **0.2885** | **0.4057** | 0.4092 |

##### Aggregate mean across STRING 500-gene datasets

Latent variables: metric=AUPRC_GAIN, negative_protocol=tf_stratified_1to10, network_group=STRING, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.3834** |
| baseline | 0.3500 |
| scGPT_human | <span style="color:red"><strong>0.4262</strong></span> |
| v4_bias_rec_best | **0.4041** |
| v4_plain_best | **0.3674** |
| v4_type_pe_best | **0.3918** |
| scconcept | 0.1682 |
| scconcept_encoded | 0.1109 |
| cl_scratch_v5 | **0.3694** |
| cl_v6_fair | **0.3791** |

##### Aggregate mean across STRING 1000-gene datasets

Latent variables: metric=AUPRC_GAIN, negative_protocol=tf_stratified_1to10, network_group=STRING, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.4218 |
| baseline | 0.4388 |
| scGPT_human | <span style="color:red"><strong>0.4520</strong></span> |
| v4_bias_rec_best | 0.4129 |
| v4_plain_best | 0.4178 |
| v4_type_pe_best | **0.4395** |
| scconcept | 0.1700 |
| scconcept_encoded | 0.1287 |
| cl_scratch_v5 | **0.4404** |
| cl_v6_fair | 0.4332 |

### Negative protocol: full_candidate

Latent variables: metric=AUPRC_GAIN, negative_protocol=full_candidate, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.2770 | 0.2266 | 0.5328 | 0.2919 | 0.0849 | **0.3974** | 0.3441 | **0.3701** | **0.2566** | <span style="color:red"><strong>0.3283</strong></span> | **0.2411** |
| baseline | 0.2964 | 0.2593 | 0.5348 | 0.3088 | <span style="color:red"><strong>0.1583</strong></span> | 0.3872 | 0.3685 | 0.3695 | 0.2415 | 0.3169 | 0.2369 |
| scGPT_human | 0.2818 | 0.2543 | 0.4970 | 0.2985 | 0.1380 | **0.3982** | 0.3393 | 0.3687 | 0.2343 | **0.3176** | 0.2335 |
| v4_bias_rec_best | 0.2948 | 0.2540 | **0.5394** | 0.2683 | 0.0951 | **0.3972** | 0.3667 | 0.3642 | **0.2441** | **0.3174** | **0.2379** |
| v4_plain_best | **0.3117** | 0.2541 | <span style="color:red"><strong>0.5520</strong></span> | 0.2647 | 0.1304 | **0.3960** | **0.3709** | **0.3713** | 0.2339 | **0.3187** | 0.2353 |
| v4_type_pe_best | <span style="color:red"><strong>0.3214</strong></span> | <span style="color:red"><strong>0.2652</strong></span> | **0.5514** | 0.2535 | 0.0968 | **0.3947** | **0.3836** | 0.3675 | **0.2458** | **0.3188** | <span style="color:red"><strong>0.2509</strong></span> |
| scconcept | 0.2460 | 0.2496 | 0.4406 | 0.1739 | 0.1491 | 0.3731 | 0.2717 | 0.3351 | 0.1956 | 0.2985 | 0.1690 |
| scconcept_encoded | 0.2472 | 0.2240 | 0.4415 | 0.2131 | 0.0262 | 0.3741 | 0.3112 | 0.3422 | 0.2065 | 0.2964 | 0.1795 |
| cl_scratch_v5 | 0.2892 | 0.2570 | 0.5340 | 0.2904 | 0.0732 | **0.3947** | <span style="color:red"><strong>0.3851</strong></span> | **0.3761** | 0.2368 | **0.3181** | **0.2391** |
| cl_v6_fair | 0.2887 | 0.2211 | **0.5385** | <span style="color:red"><strong>0.3306</strong></span> | 0.0698 | <span style="color:red"><strong>0.4028</strong></span> | **0.3846** | <span style="color:red"><strong>0.3779</strong></span> | <span style="color:red"><strong>0.2616</strong></span> | **0.3193** | **0.2435** |

##### Aggregate mean across Specific 500-gene datasets

Latent variables: metric=AUPRC_GAIN, negative_protocol=full_candidate, network_group=Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.2307 |
| baseline | <span style="color:red"><strong>0.2529</strong></span> |
| scGPT_human | 0.2399 |
| v4_bias_rec_best | 0.2396 |
| v4_plain_best | 0.2449 |
| v4_type_pe_best | 0.2485 |
| scconcept | 0.2070 |
| scconcept_encoded | 0.1895 |
| cl_scratch_v5 | 0.2382 |
| cl_v6_fair | 0.2361 |

##### Aggregate mean across Specific 1000-gene datasets

Latent variables: metric=AUPRC_GAIN, negative_protocol=full_candidate, network_group=Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.3663 |
| baseline | 0.3689 |
| scGPT_human | 0.3603 |
| v4_bias_rec_best | 0.3635 |
| v4_plain_best | **0.3691** |
| v4_type_pe_best | 0.3679 |
| scconcept | 0.3112 |
| scconcept_encoded | 0.3191 |
| cl_scratch_v5 | 0.3671 |
| cl_v6_fair | <span style="color:red"><strong>0.3763</strong></span> |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.1381** | 0.1792 | **0.1336** | **0.1070** | **0.2066** | **0.1196** | **0.2430** | **0.2247** | <span style="color:red"><strong>0.2559</strong></span> | 0.1264 | **0.1936** | **0.1429** |
| baseline | 0.1379 | <span style="color:red"><strong>0.2008</strong></span> | 0.1045 | 0.0740 | 0.1675 | 0.1130 | 0.2370 | 0.1836 | 0.2206 | 0.1396 | 0.1625 | 0.1139 |
| scGPT_human | 0.1348 | 0.1780 | <span style="color:red"><strong>0.1968</strong></span> | <span style="color:red"><strong>0.1135</strong></span> | <span style="color:red"><strong>0.2245</strong></span> | 0.0662 | **0.2407** | <span style="color:red"><strong>0.2414</strong></span> | **0.2477** | <span style="color:red"><strong>0.1882</strong></span> | **0.1875** | <span style="color:red"><strong>0.2920</strong></span> |
| v4_bias_rec_best | 0.1348 | 0.1557 | 0.0910 | **0.1078** | 0.1643 | 0.1091 | 0.2071 | **0.2081** | **0.2383** | 0.1349 | 0.1442 | **0.2355** |
| v4_plain_best | **0.1510** | 0.1665 | **0.1111** | **0.1103** | **0.2014** | 0.0656 | 0.2057 | 0.1582 | **0.2457** | 0.1282 | <span style="color:red"><strong>0.2209</strong></span> | **0.2519** |
| v4_type_pe_best | <span style="color:red"><strong>0.1549</strong></span> | 0.1818 | **0.1338** | **0.0880** | 0.1655 | 0.1037 | 0.2268 | **0.2028** | **0.2428** | **0.1767** | **0.1954** | **0.2407** |
| scconcept | 0.1137 | 0.1119 | 0.0625 | 0.0594 | 0.0923 | 0.0517 | 0.0636 | 0.0431 | 0.0894 | 0.0748 | 0.0857 | 0.0635 |
| scconcept_encoded | 0.0954 | 0.0698 | 0.0534 | 0.0306 | 0.0606 | 0.0097 | 0.0598 | 0.0552 | 0.0587 | 0.0496 | 0.0620 | 0.0639 |
| cl_scratch_v5 | **0.1502** | 0.1956 | **0.1532** | **0.0845** | **0.2177** | **0.1206** | <span style="color:red"><strong>0.2578</strong></span> | **0.2290** | **0.2284** | 0.1072 | **0.1775** | **0.2295** |
| cl_v6_fair | **0.1423** | 0.1762 | **0.1151** | **0.1116** | **0.1803** | <span style="color:red"><strong>0.1780</strong></span> | 0.2080 | **0.1930** | 0.2162 | 0.1283 | **0.1850** | **0.2571** |

##### Aggregate mean across Non-Specific 500-gene datasets

Latent variables: metric=AUPRC_GAIN, negative_protocol=full_candidate, network_group=Non-Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.1500** |
| baseline | 0.1375 |
| scGPT_human | <span style="color:red"><strong>0.1799</strong></span> |
| v4_bias_rec_best | **0.1585** |
| v4_plain_best | **0.1468** |
| v4_type_pe_best | **0.1656** |
| scconcept | 0.0674 |
| scconcept_encoded | 0.0465 |
| cl_scratch_v5 | **0.1611** |
| cl_v6_fair | **0.1740** |

##### Aggregate mean across Non-Specific 1000-gene datasets

Latent variables: metric=AUPRC_GAIN, negative_protocol=full_candidate, network_group=Non-Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.1951** |
| baseline | 0.1717 |
| scGPT_human | <span style="color:red"><strong>0.2053</strong></span> |
| v4_bias_rec_best | 0.1633 |
| v4_plain_best | **0.1893** |
| v4_type_pe_best | **0.1865** |
| scconcept | 0.0845 |
| scconcept_encoded | 0.0650 |
| cl_scratch_v5 | **0.1975** |
| cl_v6_fair | **0.1745** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | <span style="color:red"><strong>0.2537</strong></span> | 0.1584 | 0.4231 | 0.4823 | 0.4134 | **0.3304** | <span style="color:red"><strong>0.4953</strong></span> | **0.5363** | **0.3516** | **0.1986** | <span style="color:red"><strong>0.3367</strong></span> | **0.2940** |
| baseline | 0.2389 | 0.1585 | <span style="color:red"><strong>0.4290</strong></span> | 0.5230 | 0.4339 | 0.3295 | 0.4819 | 0.5041 | 0.3493 | 0.1447 | 0.2897 | 0.2565 |
| scGPT_human | 0.2188 | <span style="color:red"><strong>0.3457</strong></span> | 0.4148 | <span style="color:red"><strong>0.5415</strong></span> | 0.4164 | **0.3687** | **0.4858** | <span style="color:red"><strong>0.5853</strong></span> | **0.3745** | **0.1765** | **0.3312** | **0.3260** |
| v4_bias_rec_best | 0.1989 | 0.1229 | 0.4036 | 0.4576 | 0.4088 | **0.3886** | 0.4612 | **0.5426** | 0.3064 | <span style="color:red"><strong>0.2099</strong></span> | 0.2554 | **0.3336** |
| v4_plain_best | 0.2358 | 0.1536 | 0.4039 | 0.4586 | **0.4365** | <span style="color:red"><strong>0.4511</strong></span> | **0.4853** | **0.5259** | **0.3774** | **0.1786** | **0.3192** | **0.3160** |
| v4_type_pe_best | 0.2297 | 0.1417 | 0.4161 | 0.4872 | <span style="color:red"><strong>0.4606</strong></span> | **0.3607** | 0.4780 | **0.5429** | **0.3702** | **0.1556** | **0.3140** | <span style="color:red"><strong>0.4008</strong></span> |
| scconcept | 0.0382 | 0.1379 | 0.2324 | 0.1222 | 0.1966 | 0.0729 | 0.1255 | 0.1042 | 0.0870 | 0.0384 | 0.0898 | 0.1404 |
| scconcept_encoded | 0.0302 | 0.0705 | 0.1111 | 0.1098 | 0.1683 | 0.0490 | 0.1228 | 0.1109 | 0.0488 | 0.0235 | 0.0325 | 0.0978 |
| cl_scratch_v5 | 0.2096 | 0.1524 | 0.4150 | 0.4612 | 0.4331 | **0.3992** | **0.4869** | **0.5689** | <span style="color:red"><strong>0.3856</strong></span> | 0.1286 | **0.3060** | **0.3271** |
| cl_v6_fair | 0.2304 | 0.1430 | 0.4128 | 0.4385 | **0.4401** | **0.4315** | **0.4918** | 0.5028 | 0.3441 | 0.1381 | **0.3331** | **0.3393** |

##### Aggregate mean across STRING 500-gene datasets

Latent variables: metric=AUPRC_GAIN, negative_protocol=full_candidate, network_group=STRING, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.3333** |
| baseline | 0.3194 |
| scGPT_human | <span style="color:red"><strong>0.3906</strong></span> |
| v4_bias_rec_best | **0.3425** |
| v4_plain_best | **0.3473** |
| v4_type_pe_best | **0.3482** |
| scconcept | 0.1027 |
| scconcept_encoded | 0.0769 |
| cl_scratch_v5 | **0.3396** |
| cl_v6_fair | **0.3322** |

##### Aggregate mean across STRING 1000-gene datasets

Latent variables: metric=AUPRC_GAIN, negative_protocol=full_candidate, network_group=STRING, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | <span style="color:red"><strong>0.3790</strong></span> |
| baseline | 0.3704 |
| scGPT_human | **0.3736** |
| v4_bias_rec_best | 0.3391 |
| v4_plain_best | **0.3763** |
| v4_type_pe_best | **0.3781** |
| scconcept | 0.1282 |
| scconcept_encoded | 0.0856 |
| cl_scratch_v5 | **0.3727** |
| cl_v6_fair | **0.3754** |

## DELTA_AUPRC_VS_BASELINE (Supplementary)

### Negative protocol: tf_stratified_1to10

Latent variables: metric=DELTA_AUPRC_VS_BASELINE, negative_protocol=tf_stratified_1to10, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | -0.0184 | -0.0299 | -0.0219 | **0.0017** | -0.0370 | -0.0004 | -0.0087 | <span style="color:red"><strong>0.0112</strong></span> | **0.0303** | <span style="color:red"><strong>0.0126</strong></span> | <span style="color:red"><strong>0.0325</strong></span> |
| baseline | <span style="color:red"><strong>0.0000</strong></span> | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| scGPT_human | -0.0033 | **0.0042** | -0.0319 | -0.0030 | <span style="color:red"><strong>0.0504</strong></span> | -0.0087 | -0.0277 | -0.0016 | **0.0160** | **0.0121** | **0.0049** |
| v4_bias_rec_best | -0.0249 | -0.0029 | -0.0152 | **0.0224** | -0.0843 | -0.0016 | -0.0153 | **0.0065** | **0.0195** | **0.0039** | **0.0084** |
| v4_plain_best | -0.0037 | -0.0226 | -0.0041 | <span style="color:red"><strong>0.0356</strong></span> | **0.0123** | -0.0030 | -0.0319 | **0.0048** | **0.0057** | **0.0009** | **0.0245** |
| v4_type_pe_best | -0.0037 | **0.0053** | -0.0051 | **0.0003** | -0.0164 | -0.0006 | <span style="color:red"><strong>0.0089</strong></span> | **0.0028** | **0.0149** | **0.0095** | **0.0163** |
| scconcept | -0.0947 | -0.0290 | -0.0861 | -0.0590 | **0.0360** | -0.0259 | -0.0888 | -0.0437 | -0.0264 | -0.0039 | -0.0591 |
| scconcept_encoded | -0.0778 | -0.0637 | -0.1135 | -0.0681 | -0.0761 | -0.0317 | -0.0570 | -0.0394 | -0.0203 | -0.0212 | -0.0586 |
| cl_scratch_v5 | -0.0293 | <span style="color:red"><strong>0.0184</strong></span> | -0.0119 | **0.0351** | -0.0283 | -0.0026 | -0.0044 | **0.0076** | **0.0291** | **0.0037** | **0.0007** |
| cl_v6_fair | -0.0513 | -0.0499 | <span style="color:red"><strong>0.0015</strong></span> | **0.0346** | -0.0312 | <span style="color:red"><strong>0.0014</strong></span> | -0.0151 | **0.0084** | <span style="color:red"><strong>0.0365</strong></span> | **0.0050** | **0.0095** |

##### Aggregate mean across Specific 500-gene datasets

Latent variables: metric=DELTA_AUPRC_VS_BASELINE, negative_protocol=tf_stratified_1to10, network_group=Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | -0.0026 |
| baseline | 0.0000 |
| scGPT_human | <span style="color:red"><strong>0.0096</strong></span> |
| v4_bias_rec_best | -0.0149 |
| v4_plain_best | -0.0024 |
| v4_type_pe_best | **0.0058** |
| scconcept | -0.0335 |
| scconcept_encoded | -0.0551 |
| cl_scratch_v5 | **0.0031** |
| cl_v6_fair | -0.0101 |

##### Aggregate mean across Specific 1000-gene datasets

Latent variables: metric=DELTA_AUPRC_VS_BASELINE, negative_protocol=tf_stratified_1to10, network_group=Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | -0.0025 |
| baseline | 0.0000 |
| scGPT_human | -0.0061 |
| v4_bias_rec_best | -0.0015 |
| v4_plain_best | <span style="color:red"><strong>0.0051</strong></span> |
| v4_type_pe_best | **0.0005** |
| scconcept | -0.0522 |
| scconcept_encoded | -0.0586 |
| cl_scratch_v5 | **0.0004** |
| cl_v6_fair | -0.0001 |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | -0.0055 | -0.0022 | -0.0175 | **0.0066** | **0.0283** | -0.2040 | **0.0106** | **0.0074** | **0.0312** | -0.0427 | **0.0336** | **0.0154** |
| baseline | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| scGPT_human | -0.0170 | <span style="color:red"><strong>0.0153</strong></span> | <span style="color:red"><strong>0.0700</strong></span> | <span style="color:red"><strong>0.0954</strong></span> | **0.0224** | -0.1850 | -0.0162 | <span style="color:red"><strong>0.0880</strong></span> | <span style="color:red"><strong>0.0638</strong></span> | <span style="color:red"><strong>0.1334</strong></span> | <span style="color:red"><strong>0.0644</strong></span> | <span style="color:red"><strong>0.1333</strong></span> |
| v4_bias_rec_best | -0.0279 | -0.0578 | -0.0561 | **0.0286** | -0.0064 | -0.0692 | -0.0221 | **0.0204** | **0.0590** | -0.0414 | **0.0259** | **0.0119** |
| v4_plain_best | -0.0157 | -0.0192 | **0.0053** | **0.0504** | -0.0187 | -0.0980 | -0.0061 | **0.0145** | **0.0059** | -0.0124 | -0.0067 | **0.0871** |
| v4_type_pe_best | <span style="color:red"><strong>0.0238</strong></span> | -0.0676 | **0.0088** | -0.0355 | **0.0009** | -0.1101 | -0.0134 | **0.0253** | **0.0238** | -0.0008 | **0.0441** | **0.1285** |
| scconcept | -0.0652 | -0.0520 | -0.0782 | -0.0885 | -0.1811 | -0.3299 | -0.1899 | -0.2186 | -0.1212 | -0.0402 | -0.0722 | -0.1155 |
| scconcept_encoded | -0.0871 | -0.0881 | -0.0966 | -0.0710 | -0.2165 | -0.3113 | -0.1871 | -0.1975 | -0.1330 | -0.1193 | -0.0744 | -0.1167 |
| cl_scratch_v5 | **0.0110** | -0.0067 | **0.0052** | **0.0033** | **0.0526** | -0.1138 | <span style="color:red"><strong>0.0290</strong></span> | -0.0142 | **0.0431** | -0.0519 | **0.0288** | **0.0748** |
| cl_v6_fair | **0.0058** | -0.0377 | -0.0050 | -0.0636 | <span style="color:red"><strong>0.0586</strong></span> | <span style="color:red"><strong>0.0237</strong></span> | -0.0128 | -0.0148 | **0.0429** | -0.0350 | **0.0551** | -0.0081 |

##### Aggregate mean across Non-Specific 500-gene datasets

Latent variables: metric=DELTA_AUPRC_VS_BASELINE, negative_protocol=tf_stratified_1to10, network_group=Non-Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | -0.0366 |
| baseline | 0.0000 |
| scGPT_human | <span style="color:red"><strong>0.0467</strong></span> |
| v4_bias_rec_best | -0.0179 |
| v4_plain_best | **0.0037** |
| v4_type_pe_best | -0.0101 |
| scconcept | -0.1408 |
| scconcept_encoded | -0.1506 |
| cl_scratch_v5 | -0.0181 |
| cl_v6_fair | -0.0226 |

##### Aggregate mean across Non-Specific 1000-gene datasets

Latent variables: metric=DELTA_AUPRC_VS_BASELINE, negative_protocol=tf_stratified_1to10, network_group=Non-Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.0135** |
| baseline | 0.0000 |
| scGPT_human | <span style="color:red"><strong>0.0313</strong></span> |
| v4_bias_rec_best | -0.0046 |
| v4_plain_best | -0.0060 |
| v4_type_pe_best | **0.0147** |
| scconcept | -0.1180 |
| scconcept_encoded | -0.1324 |
| cl_scratch_v5 | **0.0283** |
| cl_v6_fair | **0.0241** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | -0.0259 | -0.0286 | -0.0151 | **0.0323** | -0.0181 | -0.0119 | **0.0084** | **0.0260** | -0.0595 | **0.1794** | **0.0084** | **0.0030** |
| baseline | 0.0000 | 0.0000 | <span style="color:red"><strong>0.0000</strong></span> | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| scGPT_human | <span style="color:red"><strong>0.0336</strong></span> | <span style="color:red"><strong>0.0994</strong></span> | -0.0279 | <span style="color:red"><strong>0.0390</strong></span> | -0.0413 | <span style="color:red"><strong>0.1976</strong></span> | <span style="color:red"><strong>0.0210</strong></span> | <span style="color:red"><strong>0.0711</strong></span> | <span style="color:red"><strong>0.0281</strong></span> | **0.0103** | <span style="color:red"><strong>0.0659</strong></span> | <span style="color:red"><strong>0.0394</strong></span> |
| v4_bias_rec_best | -0.0496 | -0.0687 | -0.0105 | -0.0142 | -0.0291 | **0.1025** | -0.0123 | **0.0199** | -0.0529 | <span style="color:red"><strong>0.2459</strong></span> | -0.0005 | **0.0390** |
| v4_plain_best | -0.0430 | -0.0390 | -0.0329 | -0.0007 | -0.0022 | **0.0526** | **0.0111** | **0.0172** | -0.0647 | **0.0412** | **0.0058** | **0.0332** |
| v4_type_pe_best | -0.0027 | **0.0697** | -0.0318 | -0.0021 | <span style="color:red"><strong>0.0333</strong></span> | -0.0037 | **0.0032** | **0.0036** | -0.0122 | **0.1907** | **0.0149** | -0.0077 |
| scconcept | -0.2153 | **0.0846** | -0.2697 | -0.3378 | -0.2407 | -0.1432 | -0.3309 | -0.3679 | -0.3330 | -0.1280 | -0.2230 | -0.1984 |
| scconcept_encoded | -0.2677 | -0.0589 | -0.2844 | -0.4014 | -0.2881 | -0.1413 | -0.4052 | -0.4455 | -0.3532 | -0.1297 | -0.2614 | -0.2580 |
| cl_scratch_v5 | -0.0133 | **0.0160** | -0.0181 | -0.0434 | -0.0042 | **0.0518** | -0.0022 | **0.0589** | **0.0140** | **0.0651** | **0.0339** | -0.0320 |
| cl_v6_fair | **0.0036** | **0.0133** | -0.0435 | **0.0023** | -0.0233 | **0.0585** | **0.0060** | -0.0117 | -0.0083 | **0.1132** | **0.0322** | -0.0011 |

##### Aggregate mean across STRING 500-gene datasets

Latent variables: metric=DELTA_AUPRC_VS_BASELINE, negative_protocol=tf_stratified_1to10, network_group=STRING, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.0334** |
| baseline | 0.0000 |
| scGPT_human | <span style="color:red"><strong>0.0761</strong></span> |
| v4_bias_rec_best | **0.0541** |
| v4_plain_best | **0.0174** |
| v4_type_pe_best | **0.0417** |
| scconcept | -0.1818 |
| scconcept_encoded | -0.2391 |
| cl_scratch_v5 | **0.0194** |
| cl_v6_fair | **0.0291** |

##### Aggregate mean across STRING 1000-gene datasets

Latent variables: metric=DELTA_AUPRC_VS_BASELINE, negative_protocol=tf_stratified_1to10, network_group=STRING, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | -0.0170 |
| baseline | 0.0000 |
| scGPT_human | <span style="color:red"><strong>0.0132</strong></span> |
| v4_bias_rec_best | -0.0258 |
| v4_plain_best | -0.0210 |
| v4_type_pe_best | **0.0008** |
| scconcept | -0.2687 |
| scconcept_encoded | -0.3100 |
| cl_scratch_v5 | **0.0017** |
| cl_v6_fair | -0.0055 |

### Negative protocol: full_candidate

Latent variables: metric=DELTA_AUPRC_VS_BASELINE, negative_protocol=full_candidate, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | -0.0194 | -0.0327 | -0.0020 | -0.0169 | -0.0734 | **0.0103** | -0.0244 | **0.0006** | **0.0150** | <span style="color:red"><strong>0.0114</strong></span> | **0.0042** |
| baseline | 0.0000 | 0.0000 | 0.0000 | 0.0000 | <span style="color:red"><strong>0.0000</strong></span> | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| scGPT_human | -0.0147 | -0.0050 | -0.0379 | -0.0103 | -0.0203 | **0.0110** | -0.0292 | -0.0008 | -0.0073 | **0.0007** | -0.0033 |
| v4_bias_rec_best | -0.0017 | -0.0053 | **0.0046** | -0.0405 | -0.0632 | **0.0100** | -0.0018 | -0.0053 | **0.0025** | **0.0005** | **0.0010** |
| v4_plain_best | **0.0152** | -0.0052 | <span style="color:red"><strong>0.0172</strong></span> | -0.0441 | -0.0279 | **0.0088** | **0.0023** | **0.0018** | -0.0076 | **0.0018** | -0.0015 |
| v4_type_pe_best | <span style="color:red"><strong>0.0249</strong></span> | <span style="color:red"><strong>0.0059</strong></span> | **0.0166** | -0.0553 | -0.0615 | **0.0075** | **0.0151** | -0.0020 | **0.0043** | **0.0019** | <span style="color:red"><strong>0.0141</strong></span> |
| scconcept | -0.0504 | -0.0097 | -0.0942 | -0.1349 | -0.0092 | -0.0140 | -0.0968 | -0.0344 | -0.0459 | -0.0184 | -0.0679 |
| scconcept_encoded | -0.0492 | -0.0353 | -0.0933 | -0.0957 | -0.1321 | -0.0131 | -0.0574 | -0.0273 | -0.0350 | -0.0205 | -0.0574 |
| cl_scratch_v5 | -0.0072 | -0.0023 | -0.0008 | -0.0184 | -0.0851 | **0.0076** | <span style="color:red"><strong>0.0166</strong></span> | **0.0066** | -0.0048 | **0.0012** | **0.0023** |
| cl_v6_fair | -0.0077 | -0.0381 | **0.0037** | <span style="color:red"><strong>0.0218</strong></span> | -0.0885 | <span style="color:red"><strong>0.0156</strong></span> | **0.0160** | <span style="color:red"><strong>0.0084</strong></span> | <span style="color:red"><strong>0.0201</strong></span> | **0.0024** | **0.0066** |

##### Aggregate mean across Specific 500-gene datasets

Latent variables: metric=DELTA_AUPRC_VS_BASELINE, negative_protocol=full_candidate, network_group=Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | -0.0222 |
| baseline | <span style="color:red"><strong>0.0000</strong></span> |
| scGPT_human | -0.0130 |
| v4_bias_rec_best | -0.0133 |
| v4_plain_best | -0.0080 |
| v4_type_pe_best | -0.0044 |
| scconcept | -0.0459 |
| scconcept_encoded | -0.0634 |
| cl_scratch_v5 | -0.0147 |
| cl_v6_fair | -0.0168 |

##### Aggregate mean across Specific 1000-gene datasets

Latent variables: metric=DELTA_AUPRC_VS_BASELINE, negative_protocol=full_candidate, network_group=Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | -0.0027 |
| baseline | 0.0000 |
| scGPT_human | -0.0087 |
| v4_bias_rec_best | -0.0054 |
| v4_plain_best | **0.0001** |
| v4_type_pe_best | -0.0011 |
| scconcept | -0.0577 |
| scconcept_encoded | -0.0498 |
| cl_scratch_v5 | -0.0018 |
| cl_v6_fair | <span style="color:red"><strong>0.0074</strong></span> |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.0002** | -0.0216 | **0.0291** | **0.0330** | **0.0391** | **0.0066** | **0.0060** | **0.0412** | <span style="color:red"><strong>0.0353</strong></span> | -0.0132 | **0.0311** | **0.0290** |
| baseline | 0.0000 | <span style="color:red"><strong>0.0000</strong></span> | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| scGPT_human | -0.0032 | -0.0228 | <span style="color:red"><strong>0.0923</strong></span> | <span style="color:red"><strong>0.0395</strong></span> | <span style="color:red"><strong>0.0570</strong></span> | -0.0468 | **0.0037** | <span style="color:red"><strong>0.0578</strong></span> | **0.0271** | <span style="color:red"><strong>0.0485</strong></span> | **0.0250** | <span style="color:red"><strong>0.1781</strong></span> |
| v4_bias_rec_best | -0.0032 | -0.0452 | -0.0135 | **0.0338** | -0.0032 | -0.0039 | -0.0299 | **0.0245** | **0.0177** | -0.0047 | -0.0183 | **0.1216** |
| v4_plain_best | **0.0131** | -0.0343 | **0.0067** | **0.0364** | **0.0339** | -0.0474 | -0.0313 | -0.0254 | **0.0251** | -0.0114 | <span style="color:red"><strong>0.0583</strong></span> | **0.1380** |
| v4_type_pe_best | <span style="color:red"><strong>0.0169</strong></span> | -0.0190 | **0.0293** | **0.0140** | -0.0020 | -0.0093 | -0.0102 | **0.0192** | **0.0222** | **0.0371** | **0.0329** | **0.1268** |
| scconcept | -0.0242 | -0.0889 | -0.0420 | -0.0146 | -0.0751 | -0.0612 | -0.1733 | -0.1405 | -0.1312 | -0.0648 | -0.0768 | -0.0505 |
| scconcept_encoded | -0.0425 | -0.1310 | -0.0510 | -0.0433 | -0.1069 | -0.1033 | -0.1772 | -0.1284 | -0.1619 | -0.0900 | -0.1005 | -0.0500 |
| cl_scratch_v5 | **0.0123** | -0.0052 | **0.0488** | **0.0106** | **0.0502** | **0.0076** | <span style="color:red"><strong>0.0208</strong></span> | **0.0455** | **0.0078** | -0.0325 | **0.0150** | **0.1156** |
| cl_v6_fair | **0.0043** | -0.0246 | **0.0107** | **0.0376** | **0.0128** | <span style="color:red"><strong>0.0651</strong></span> | -0.0289 | **0.0094** | -0.0044 | -0.0113 | **0.0225** | **0.1432** |

##### Aggregate mean across Non-Specific 500-gene datasets

Latent variables: metric=DELTA_AUPRC_VS_BASELINE, negative_protocol=full_candidate, network_group=Non-Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.0125** |
| baseline | 0.0000 |
| scGPT_human | <span style="color:red"><strong>0.0424</strong></span> |
| v4_bias_rec_best | **0.0210** |
| v4_plain_best | **0.0093** |
| v4_type_pe_best | **0.0281** |
| scconcept | -0.0701 |
| scconcept_encoded | -0.0910 |
| cl_scratch_v5 | **0.0236** |
| cl_v6_fair | **0.0365** |

##### Aggregate mean across Non-Specific 1000-gene datasets

Latent variables: metric=DELTA_AUPRC_VS_BASELINE, negative_protocol=full_candidate, network_group=Non-Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.0235** |
| baseline | 0.0000 |
| scGPT_human | <span style="color:red"><strong>0.0337</strong></span> |
| v4_bias_rec_best | -0.0084 |
| v4_plain_best | **0.0176** |
| v4_type_pe_best | **0.0148** |
| scconcept | -0.0871 |
| scconcept_encoded | -0.1067 |
| cl_scratch_v5 | **0.0258** |
| cl_v6_fair | **0.0028** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | <span style="color:red"><strong>0.0148</strong></span> | -0.0001 | -0.0059 | -0.0407 | -0.0204 | **0.0009** | <span style="color:red"><strong>0.0134</strong></span> | **0.0322** | **0.0024** | **0.0539** | <span style="color:red"><strong>0.0470</strong></span> | **0.0375** |
| baseline | 0.0000 | 0.0000 | <span style="color:red"><strong>0.0000</strong></span> | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| scGPT_human | -0.0201 | <span style="color:red"><strong>0.1872</strong></span> | -0.0142 | <span style="color:red"><strong>0.0186</strong></span> | -0.0174 | **0.0392** | **0.0039** | <span style="color:red"><strong>0.0812</strong></span> | **0.0252** | **0.0319** | **0.0415** | **0.0695** |
| v4_bias_rec_best | -0.0399 | -0.0357 | -0.0254 | -0.0654 | -0.0250 | **0.0591** | -0.0208 | **0.0385** | -0.0429 | <span style="color:red"><strong>0.0652</strong></span> | -0.0343 | **0.0771** |
| v4_plain_best | -0.0031 | -0.0049 | -0.0251 | -0.0644 | **0.0027** | <span style="color:red"><strong>0.1216</strong></span> | **0.0034** | **0.0218** | **0.0281** | **0.0340** | **0.0296** | **0.0595** |
| v4_type_pe_best | -0.0092 | -0.0169 | -0.0129 | -0.0358 | <span style="color:red"><strong>0.0267</strong></span> | **0.0312** | -0.0039 | **0.0389** | **0.0209** | **0.0109** | **0.0244** | <span style="color:red"><strong>0.1443</strong></span> |
| scconcept | -0.2007 | -0.0206 | -0.1966 | -0.4007 | -0.2373 | -0.2566 | -0.3565 | -0.3999 | -0.2623 | -0.1063 | -0.1999 | -0.1161 |
| scconcept_encoded | -0.2087 | -0.0880 | -0.3179 | -0.4132 | -0.2656 | -0.2805 | -0.3592 | -0.3932 | -0.3005 | -0.1211 | -0.2572 | -0.1587 |
| cl_scratch_v5 | -0.0293 | -0.0061 | -0.0140 | -0.0617 | -0.0007 | **0.0697** | **0.0049** | **0.0648** | <span style="color:red"><strong>0.0364</strong></span> | -0.0160 | **0.0163** | **0.0706** |
| cl_v6_fair | -0.0085 | -0.0156 | -0.0162 | -0.0845 | **0.0062** | **0.1020** | **0.0099** | -0.0012 | -0.0052 | -0.0066 | **0.0435** | **0.0828** |

##### Aggregate mean across STRING 500-gene datasets

Latent variables: metric=DELTA_AUPRC_VS_BASELINE, negative_protocol=full_candidate, network_group=STRING, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.0140** |
| baseline | 0.0000 |
| scGPT_human | <span style="color:red"><strong>0.0713</strong></span> |
| v4_bias_rec_best | **0.0232** |
| v4_plain_best | **0.0279** |
| v4_type_pe_best | **0.0288** |
| scconcept | -0.2167 |
| scconcept_encoded | -0.2425 |
| cl_scratch_v5 | **0.0202** |
| cl_v6_fair | **0.0128** |

##### Aggregate mean across STRING 1000-gene datasets

Latent variables: metric=DELTA_AUPRC_VS_BASELINE, negative_protocol=full_candidate, network_group=STRING, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | <span style="color:red"><strong>0.0086</strong></span> |
| baseline | 0.0000 |
| scGPT_human | **0.0031** |
| v4_bias_rec_best | -0.0314 |
| v4_plain_best | **0.0059** |
| v4_type_pe_best | **0.0076** |
| scconcept | -0.2422 |
| scconcept_encoded | -0.2848 |
| cl_scratch_v5 | **0.0023** |
| cl_v6_fair | **0.0050** |

## LIFT_RATIO_VS_BASELINE (Supplementary)

### Negative protocol: tf_stratified_1to10

Latent variables: metric=LIFT_RATIO_VS_BASELINE, negative_protocol=tf_stratified_1to10, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.9617 | 0.9329 | 0.9723 | **1.0088** | 0.7844 | 0.9995 | 0.9886 | <span style="color:red"><strong>1.0131</strong></span> | **1.0389** | <span style="color:red"><strong>1.0144</strong></span> | <span style="color:red"><strong>1.0398</strong></span> |
| baseline | <span style="color:red"><strong>1.0000</strong></span> | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| scGPT_human | 0.9933 | **1.0151** | 0.9560 | **1.0035** | <span style="color:red"><strong>1.2952</strong></span> | 0.9903 | 0.9640 | 0.9981 | **1.0203** | **1.0138** | **1.0059** |
| v4_bias_rec_best | 0.9501 | 0.9967 | 0.9794 | **1.0590** | 0.5063 | 0.9983 | 0.9798 | **1.0076** | **1.0251** | **1.0045** | **1.0101** |
| v4_plain_best | 0.9938 | 0.9505 | 0.9945 | **1.0992** | **1.0666** | 0.9967 | 0.9589 | **1.0056** | **1.0072** | **1.0011** | **1.0300** |
| v4_type_pe_best | 0.9924 | **1.0160** | 0.9933 | **1.0057** | 0.9136 | 0.9993 | <span style="color:red"><strong>1.0107</strong></span> | **1.0033** | **1.0193** | **1.0108** | **1.0199** |
| scconcept | 0.8062 | 0.9381 | 0.8859 | 0.8368 | **1.2228** | 0.9710 | 0.8861 | 0.9490 | 0.9658 | 0.9955 | 0.9275 |
| scconcept_encoded | 0.8427 | 0.8549 | 0.8500 | 0.8297 | 0.5507 | 0.9645 | 0.9270 | 0.9540 | 0.9739 | 0.9759 | 0.9284 |
| cl_scratch_v5 | 0.9407 | <span style="color:red"><strong>1.0443</strong></span> | 0.9835 | <span style="color:red"><strong>1.1054</strong></span> | 0.8389 | 0.9971 | 0.9939 | **1.0089** | **1.0376** | **1.0042** | **1.0006** |
| cl_v6_fair | 0.8941 | 0.8855 | <span style="color:red"><strong>1.0016</strong></span> | **1.0980** | 0.8208 | <span style="color:red"><strong>1.0015</strong></span> | 0.9801 | **1.0098** | <span style="color:red"><strong>1.0470</strong></span> | **1.0057** | **1.0115** |

##### Aggregate mean across Specific 500-gene datasets

Latent variables: metric=LIFT_RATIO_VS_BASELINE, negative_protocol=tf_stratified_1to10, network_group=Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.9569 |
| baseline | 1.0000 |
| scGPT_human | <span style="color:red"><strong>1.0601</strong></span> |
| v4_bias_rec_best | 0.9036 |
| v4_plain_best | **1.0026** |
| v4_type_pe_best | 0.9959 |
| scconcept | 0.9880 |
| scconcept_encoded | 0.8470 |
| cl_scratch_v5 | 0.9830 |
| cl_v6_fair | 0.9490 |

##### Aggregate mean across Specific 1000-gene datasets

Latent variables: metric=LIFT_RATIO_VS_BASELINE, negative_protocol=tf_stratified_1to10, network_group=Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.9950 |
| baseline | 1.0000 |
| scGPT_human | 0.9925 |
| v4_bias_rec_best | 0.9998 |
| v4_plain_best | <span style="color:red"><strong>1.0151</strong></span> |
| v4_type_pe_best | **1.0008** |
| scconcept | 0.9074 |
| scconcept_encoded | 0.9028 |
| cl_scratch_v5 | **1.0066** |
| cl_v6_fair | **1.0018** |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.9789 | 0.9874 | 0.9424 | **1.0624** | **1.0787** | 0.5506 | **1.0268** | **1.0167** | **1.0948** | 0.8351 | **1.1211** | **1.0577** |
| baseline | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| scGPT_human | 0.9151 | <span style="color:red"><strong>1.0587</strong></span> | <span style="color:red"><strong>1.2452</strong></span> | <span style="color:red"><strong>1.4701</strong></span> | **1.0646** | 0.6215 | 0.9486 | <span style="color:red"><strong>1.2636</strong></span> | <span style="color:red"><strong>1.1964</strong></span> | <span style="color:red"><strong>1.4934</strong></span> | <span style="color:red"><strong>1.2325</strong></span> | <span style="color:red"><strong>1.4834</strong></span> |
| v4_bias_rec_best | 0.8784 | 0.7553 | 0.8035 | **1.1532** | **1.0145** | 0.8249 | 0.9348 | **1.0506** | **1.1836** | 0.8452 | **1.0932** | **1.0432** |
| v4_plain_best | 0.9404 | 0.9456 | **1.0010** | **1.2219** | 0.9797 | 0.7737 | 0.9824 | **1.0290** | **1.0165** | 0.9525 | 0.9754 | **1.3168** |
| v4_type_pe_best | <span style="color:red"><strong>1.1082</strong></span> | 0.7043 | **1.0315** | 0.9964 | **1.0169** | 0.7729 | 0.9629 | **1.0674** | **1.0692** | 0.9960 | **1.1599** | **1.4712** |
| scconcept | 0.7311 | 0.7631 | 0.7284 | 0.6649 | 0.5777 | 0.3152 | 0.4772 | 0.3564 | 0.6197 | 0.8573 | 0.7373 | 0.5738 |
| scconcept_encoded | 0.6410 | 0.6257 | 0.6551 | 0.7771 | 0.4670 | 0.3651 | 0.4783 | 0.4129 | 0.5781 | 0.5702 | 0.7293 | 0.5687 |
| cl_scratch_v5 | **1.0469** | 0.9525 | **1.0154** | **1.0211** | **1.1745** | 0.7457 | <span style="color:red"><strong>1.0787</strong></span> | 0.9570 | **1.1317** | 0.8112 | **1.1034** | **1.2756** |
| cl_v6_fair | **1.0290** | 0.8129 | 0.9809 | 0.8223 | <span style="color:red"><strong>1.1930</strong></span> | <span style="color:red"><strong>1.0571</strong></span> | 0.9589 | 0.9501 | **1.1315** | 0.8701 | **1.1989** | 0.9716 |

##### Aggregate mean across Non-Specific 500-gene datasets

Latent variables: metric=LIFT_RATIO_VS_BASELINE, negative_protocol=tf_stratified_1to10, network_group=Non-Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.9183 |
| baseline | 1.0000 |
| scGPT_human | <span style="color:red"><strong>1.2318</strong></span> |
| v4_bias_rec_best | 0.9454 |
| v4_plain_best | **1.0399** |
| v4_type_pe_best | **1.0014** |
| scconcept | 0.5884 |
| scconcept_encoded | 0.5533 |
| cl_scratch_v5 | 0.9605 |
| cl_v6_fair | 0.9140 |

##### Aggregate mean across Non-Specific 1000-gene datasets

Latent variables: metric=LIFT_RATIO_VS_BASELINE, negative_protocol=tf_stratified_1to10, network_group=Non-Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **1.0404** |
| baseline | 1.0000 |
| scGPT_human | <span style="color:red"><strong>1.1004</strong></span> |
| v4_bias_rec_best | 0.9847 |
| v4_plain_best | 0.9826 |
| v4_type_pe_best | **1.0581** |
| scconcept | 0.6452 |
| scconcept_encoded | 0.5915 |
| cl_scratch_v5 | **1.0917** |
| cl_v6_fair | **1.0820** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.9280 | 0.8486 | 0.9716 | **1.0545** | 0.9734 | 0.9701 | **1.0206** | **1.0490** | 0.8885 | **1.6856** | **1.0261** | **1.0162** |
| baseline | 1.0000 | 1.0000 | <span style="color:red"><strong>1.0000</strong></span> | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| scGPT_human | <span style="color:red"><strong>1.0829</strong></span> | **1.8370** | 0.9428 | <span style="color:red"><strong>1.0717</strong></span> | 0.9215 | <span style="color:red"><strong>1.5713</strong></span> | <span style="color:red"><strong>1.0384</strong></span> | <span style="color:red"><strong>1.1349</strong></span> | <span style="color:red"><strong>1.0671</strong></span> | **1.0330** | <span style="color:red"><strong>1.1558</strong></span> | <span style="color:red"><strong>1.0886</strong></span> |
| v4_bias_rec_best | 0.8756 | **1.1574** | 0.9779 | 0.9652 | 0.9571 | **1.3053** | 0.9812 | **1.0405** | 0.8932 | <span style="color:red"><strong>1.9327</strong></span> | **1.0122** | **1.0852** |
| v4_plain_best | 0.8921 | 0.9413 | 0.9345 | 0.9929 | 0.9983 | **1.1269** | **1.0293** | **1.0316** | 0.8853 | **1.1567** | **1.0110** | **1.0612** |
| v4_type_pe_best | 0.9840 | **1.4837** | 0.9401 | 0.9892 | <span style="color:red"><strong>1.0575</strong></span> | 0.9829 | **1.0109** | **1.0075** | 0.9804 | **1.7333** | **1.0253** | **1.0018** |
| scconcept | 0.5164 | <span style="color:red"><strong>2.1770</strong></span> | 0.5187 | 0.4221 | 0.5807 | 0.5927 | 0.4690 | 0.4429 | 0.3917 | 0.5139 | 0.5245 | 0.5694 |
| scconcept_encoded | 0.3851 | **1.0773** | 0.4879 | 0.3135 | 0.5008 | 0.6041 | 0.3720 | 0.3059 | 0.3553 | 0.5105 | 0.4435 | 0.4721 |
| cl_scratch_v5 | 0.9715 | **1.2239** | 0.9617 | 0.9225 | 0.9918 | **1.1380** | 0.9963 | **1.1099** | **1.0240** | **1.2541** | **1.0678** | 0.9528 |
| cl_v6_fair | **1.0240** | **1.1562** | 0.9158 | **1.0033** | 0.9536 | **1.1680** | **1.0106** | 0.9821 | 0.9817 | **1.4391** | **1.0766** | **1.0032** |

##### Aggregate mean across STRING 500-gene datasets

Latent variables: metric=LIFT_RATIO_VS_BASELINE, negative_protocol=tf_stratified_1to10, network_group=STRING, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **1.1040** |
| baseline | 1.0000 |
| scGPT_human | <span style="color:red"><strong>1.2894</strong></span> |
| v4_bias_rec_best | **1.2477** |
| v4_plain_best | **1.0518** |
| v4_type_pe_best | **1.1997** |
| scconcept | 0.7863 |
| scconcept_encoded | 0.5472 |
| cl_scratch_v5 | **1.1002** |
| cl_v6_fair | **1.1253** |

##### Aggregate mean across STRING 1000-gene datasets

Latent variables: metric=LIFT_RATIO_VS_BASELINE, negative_protocol=tf_stratified_1to10, network_group=STRING, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.9680 |
| baseline | 1.0000 |
| scGPT_human | <span style="color:red"><strong>1.0348</strong></span> |
| v4_bias_rec_best | 0.9495 |
| v4_plain_best | 0.9584 |
| v4_type_pe_best | 0.9997 |
| scconcept | 0.5002 |
| scconcept_encoded | 0.4241 |
| cl_scratch_v5 | **1.0022** |
| cl_v6_fair | 0.9937 |

### Negative protocol: full_candidate

Latent variables: metric=LIFT_RATIO_VS_BASELINE, negative_protocol=full_candidate, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.9581 | 0.9266 | 0.9972 | 0.9660 | 0.6251 | **1.0117** | 0.9675 | **1.0007** | **1.0191** | <span style="color:red"><strong>1.0129</strong></span> | **1.0051** |
| baseline | 1.0000 | 1.0000 | 1.0000 | 1.0000 | <span style="color:red"><strong>1.0000</strong></span> | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| scGPT_human | 0.9689 | 0.9955 | 0.9491 | 0.9668 | 0.8996 | **1.0125** | 0.9605 | 0.9990 | 0.9905 | **1.0008** | 0.9958 |
| v4_bias_rec_best | 0.9967 | 0.9892 | **1.0052** | 0.8955 | 0.6440 | **1.0114** | 0.9975 | 0.9939 | **1.0032** | **1.0005** | **1.0012** |
| v4_plain_best | **1.0340** | 0.9920 | <span style="color:red"><strong>1.0235</strong></span> | 0.8868 | 0.8347 | **1.0101** | **1.0022** | **1.0021** | 0.9906 | **1.0021** | 0.9981 |
| v4_type_pe_best | <span style="color:red"><strong>1.0557</strong></span> | <span style="color:red"><strong>1.0197</strong></span> | **1.0220** | 0.8641 | 0.6707 | **1.0086** | **1.0195** | 0.9977 | **1.0055** | **1.0022** | <span style="color:red"><strong>1.0169</strong></span> |
| scconcept | 0.8911 | 0.9831 | 0.8761 | 0.6509 | 0.9008 | 0.9842 | 0.8718 | 0.9598 | 0.9424 | 0.9791 | 0.9181 |
| scconcept_encoded | 0.8924 | 0.9210 | 0.8774 | 0.7582 | 0.3295 | 0.9851 | 0.9261 | 0.9681 | 0.9562 | 0.9767 | 0.9307 |
| cl_scratch_v5 | 0.9848 | 0.9979 | 0.9991 | 0.9605 | 0.5377 | **1.0086** | <span style="color:red"><strong>1.0212</strong></span> | **1.0077** | 0.9941 | **1.0014** | **1.0027** |
| cl_v6_fair | 0.9841 | 0.9128 | **1.0047** | <span style="color:red"><strong>1.0555</strong></span> | 0.5060 | <span style="color:red"><strong>1.0178</strong></span> | **1.0206** | <span style="color:red"><strong>1.0098</strong></span> | <span style="color:red"><strong>1.0255</strong></span> | **1.0027** | **1.0079** |

##### Aggregate mean across Specific 500-gene datasets

Latent variables: metric=LIFT_RATIO_VS_BASELINE, negative_protocol=full_candidate, network_group=Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.9087 |
| baseline | <span style="color:red"><strong>1.0000</strong></span> |
| scGPT_human | 0.9684 |
| v4_bias_rec_best | 0.9270 |
| v4_plain_best | 0.9635 |
| v4_type_pe_best | 0.9464 |
| scconcept | 0.9233 |
| scconcept_encoded | 0.8127 |
| cl_scratch_v5 | 0.9107 |
| cl_v6_fair | 0.8946 |

##### Aggregate mean across Specific 1000-gene datasets

Latent variables: metric=LIFT_RATIO_VS_BASELINE, negative_protocol=full_candidate, network_group=Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | 0.9911 |
| baseline | 1.0000 |
| scGPT_human | 0.9829 |
| v4_bias_rec_best | 0.9839 |
| v4_plain_best | 0.9931 |
| v4_type_pe_best | 0.9917 |
| scconcept | 0.8902 |
| scconcept_encoded | 0.9097 |
| cl_scratch_v5 | 0.9937 |
| cl_v6_fair | <span style="color:red"><strong>1.0124</strong></span> |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.9996 | 0.9109 | **1.2727** | **1.4675** | **1.2246** | 0.7950 | **1.0159** | **1.1984** | <span style="color:red"><strong>1.1518</strong></span> | 0.9656 | **1.1665** | **1.2496** |
| baseline | 1.0000 | <span style="color:red"><strong>1.0000</strong></span> | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| scGPT_human | 0.9740 | 0.9027 | <span style="color:red"><strong>1.8491</strong></span> | **1.4874** | <span style="color:red"><strong>1.3040</strong></span> | 0.6914 | 0.9978 | <span style="color:red"><strong>1.3666</strong></span> | **1.0891** | **1.3598** | **1.1406** | <span style="color:red"><strong>2.3042</strong></span> |
| v4_bias_rec_best | 0.9786 | 0.7897 | 0.8853 | <span style="color:red"><strong>1.5037</strong></span> | 0.9839 | 0.8106 | 0.8743 | **1.1275** | **1.0897** | **1.0633** | 0.9142 | **1.8873** |
| v4_plain_best | **1.0850** | 0.8450 | **1.0745** | **1.4349** | **1.1828** | 0.5216 | 0.8680 | 0.8824 | **1.1053** | 0.9207 | <span style="color:red"><strong>1.3307</strong></span> | **2.0090** |
| v4_type_pe_best | <span style="color:red"><strong>1.1122</strong></span> | 0.9131 | **1.2666** | **1.2993** | 0.9931 | 0.7523 | 0.9540 | **1.1768** | **1.1115** | <span style="color:red"><strong>1.3630</strong></span> | **1.1832** | **1.9180** |
| scconcept | 0.8389 | 0.6033 | 0.6309 | 0.9499 | 0.5938 | 0.4558 | 0.3196 | 0.3613 | 0.4404 | 0.6012 | 0.5714 | 0.6360 |
| scconcept_encoded | 0.7238 | 0.4124 | 0.5623 | 0.5543 | 0.4176 | 0.2628 | 0.3017 | 0.4246 | 0.3141 | 0.5189 | 0.4501 | 0.6353 |
| cl_scratch_v5 | **1.0797** | 0.9757 | **1.4335** | **1.1674** | **1.2678** | **1.0137** | <span style="color:red"><strong>1.0761</strong></span> | **1.2272** | **1.0432** | 0.7632 | **1.0730** | **1.8332** |
| cl_v6_fair | **1.0287** | 0.8927 | **1.0839** | **1.4738** | **1.0701** | <span style="color:red"><strong>1.7607</strong></span> | 0.8839 | **1.0859** | 0.9798 | 0.8825 | **1.1173** | **2.0514** |

##### Aggregate mean across Non-Specific 500-gene datasets

Latent variables: metric=LIFT_RATIO_VS_BASELINE, negative_protocol=full_candidate, network_group=Non-Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **1.0978** |
| baseline | 1.0000 |
| scGPT_human | **1.3520** |
| v4_bias_rec_best | **1.1970** |
| v4_plain_best | **1.1023** |
| v4_type_pe_best | **1.2371** |
| scconcept | 0.6013 |
| scconcept_encoded | 0.4680 |
| cl_scratch_v5 | **1.1634** |
| cl_v6_fair | <span style="color:red"><strong>1.3578</strong></span> |

##### Aggregate mean across Non-Specific 1000-gene datasets

Latent variables: metric=LIFT_RATIO_VS_BASELINE, negative_protocol=full_candidate, network_group=Non-Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **1.1385** |
| baseline | 1.0000 |
| scGPT_human | <span style="color:red"><strong>1.2258</strong></span> |
| v4_bias_rec_best | 0.9543 |
| v4_plain_best | **1.1077** |
| v4_type_pe_best | **1.1034** |
| scconcept | 0.5658 |
| scconcept_encoded | 0.4616 |
| cl_scratch_v5 | **1.1622** |
| cl_v6_fair | **1.0273** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | <span style="color:red"><strong>1.0618</strong></span> | 0.8101 | 0.9849 | 0.9217 | 0.9626 | **1.1444** | <span style="color:red"><strong>1.0273</strong></span> | **1.0640** | **1.0090** | **1.3268** | <span style="color:red"><strong>1.1565</strong></span> | **1.1378** |
| baseline | 1.0000 | 1.0000 | <span style="color:red"><strong>1.0000</strong></span> | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| scGPT_human | 0.9067 | <span style="color:red"><strong>2.7305</strong></span> | 0.9668 | <span style="color:red"><strong>1.0349</strong></span> | 0.9566 | **1.2779** | **1.0017** | <span style="color:red"><strong>1.1743</strong></span> | **1.0629** | **1.3008** | **1.1421** | **1.2822** |
| v4_bias_rec_best | 0.8381 | 0.6885 | 0.9445 | 0.8911 | 0.9448 | **1.3065** | 0.9595 | **1.0856** | 0.8792 | <span style="color:red"><strong>1.3878</strong></span> | 0.8879 | **1.2874** |
| v4_plain_best | 0.9946 | 0.9679 | 0.9388 | 0.8779 | **1.0041** | <span style="color:red"><strong>1.4792</strong></span> | **1.0106** | **1.0625** | **1.0755** | **1.2994** | **1.0965** | **1.2219** |
| v4_type_pe_best | 0.9640 | 0.7518 | 0.9698 | 0.9285 | <span style="color:red"><strong>1.0640</strong></span> | **1.1424** | 0.9984 | **1.0809** | **1.0603** | **1.0917** | **1.0818** | <span style="color:red"><strong>1.5529</strong></span> |
| scconcept | 0.1979 | 0.7985 | 0.5535 | 0.2723 | 0.4871 | 0.2853 | 0.2887 | 0.2431 | 0.2641 | 0.3826 | 0.3324 | 0.6209 |
| scconcept_encoded | 0.1655 | 0.5211 | 0.2982 | 0.2461 | 0.4350 | 0.2695 | 0.2872 | 0.2646 | 0.1641 | 0.2577 | 0.1436 | 0.4231 |
| cl_scratch_v5 | 0.8882 | 0.9011 | 0.9671 | 0.8869 | 0.9974 | **1.3457** | **1.0147** | **1.1359** | <span style="color:red"><strong>1.1004</strong></span> | 0.9123 | **1.0504** | **1.2786** |
| cl_v6_fair | 0.9641 | 0.9394 | 0.9596 | 0.8403 | **1.0093** | **1.4720** | **1.0252** | **1.0104** | 0.9899 | 0.9053 | **1.1440** | **1.3017** |

##### Aggregate mean across STRING 500-gene datasets

Latent variables: metric=LIFT_RATIO_VS_BASELINE, negative_protocol=full_candidate, network_group=STRING, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **1.0675** |
| baseline | 1.0000 |
| scGPT_human | <span style="color:red"><strong>1.4668</strong></span> |
| v4_bias_rec_best | **1.1078** |
| v4_plain_best | **1.1515** |
| v4_type_pe_best | **1.0914** |
| scconcept | 0.4338 |
| scconcept_encoded | 0.3304 |
| cl_scratch_v5 | **1.0768** |
| cl_v6_fair | **1.0782** |

##### Aggregate mean across STRING 1000-gene datasets

Latent variables: metric=LIFT_RATIO_VS_BASELINE, negative_protocol=full_candidate, network_group=STRING, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | <span style="color:red"><strong>1.0337</strong></span> |
| baseline | 1.0000 |
| scGPT_human | **1.0061** |
| v4_bias_rec_best | 0.9090 |
| v4_plain_best | **1.0200** |
| v4_type_pe_best | **1.0230** |
| scconcept | 0.3539 |
| scconcept_encoded | 0.2489 |
| cl_scratch_v5 | **1.0030** |
| cl_v6_fair | **1.0154** |

## DELTA_PRECISION_AT_K_VS_BASELINE (Supplementary)

### Negative protocol: tf_stratified_1to10

Latent variables: metric=DELTA_PRECISION_AT_K_VS_BASELINE, negative_protocol=tf_stratified_1to10, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.0000 | -0.0325 | -0.0132 | -0.0036 | 0.0000 | -0.0013 | -0.0021 | <span style="color:red"><strong>0.0104</strong></span> | **0.0089** | **0.0072** | <span style="color:red"><strong>0.0209</strong></span> |
| baseline | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | <span style="color:red"><strong>0.0000</strong></span> | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| scGPT_human | <span style="color:red"><strong>0.0097</strong></span> | -0.0059 | -0.0376 | **0.0036** | <span style="color:red"><strong>0.0625</strong></span> | <span style="color:red"><strong>0.0013</strong></span> | -0.0298 | -0.0036 | **0.0089** | <span style="color:red"><strong>0.0093</strong></span> | **0.0018** |
| v4_bias_rec_best | -0.0085 | -0.0148 | -0.0038 | **0.0143** | -0.1250 | -0.0024 | -0.0128 | -0.0021 | <span style="color:red"><strong>0.0346</strong></span> | **0.0069** | **0.0100** |
| v4_plain_best | **0.0036** | -0.0059 | <span style="color:red"><strong>0.0019</strong></span> | **0.0214** | 0.0000 | -0.0037 | -0.0234 | **0.0044** | -0.0033 | **0.0036** | **0.0155** |
| v4_type_pe_best | **0.0012** | **0.0266** | 0.0000 | -0.0107 | -0.1250 | -0.0037 | <span style="color:red"><strong>-0.0000</strong></span> | **0.0024** | **0.0145** | **0.0041** | **0.0109** |
| scconcept | -0.0740 | -0.0207 | -0.0470 | -0.0607 | 0.0000 | -0.0199 | -0.0638 | -0.0287 | -0.0379 | **0.0034** | -0.0373 |
| scconcept_encoded | -0.0534 | -0.0207 | -0.0658 | -0.0250 | -0.1250 | -0.0219 | -0.0468 | -0.0314 | -0.0234 | -0.0096 | -0.0464 |
| cl_scratch_v5 | -0.0133 | <span style="color:red"><strong>0.0296</strong></span> | -0.0169 | **0.0071** | <span style="color:red"><strong>0.0625</strong></span> | -0.0040 | -0.0234 | -0.0033 | **0.0134** | **0.0029** | **0.0073** |
| cl_v6_fair | -0.0206 | -0.0355 | -0.0169 | <span style="color:red"><strong>0.0500</strong></span> | 0.0000 | -0.0034 | -0.0191 | **0.0036** | **0.0134** | **0.0053** | **0.0073** |

##### Aggregate mean across Specific 500-gene datasets

Latent variables: metric=DELTA_PRECISION_AT_K_VS_BASELINE, negative_protocol=tf_stratified_1to10, network_group=Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | -0.0010 |
| baseline | 0.0000 |
| scGPT_human | **0.0075** |
| v4_bias_rec_best | -0.0216 |
| v4_plain_best | -0.0034 |
| v4_type_pe_best | -0.0146 |
| scconcept | -0.0320 |
| scconcept_encoded | -0.0525 |
| cl_scratch_v5 | <span style="color:red"><strong>0.0179</strong></span> |
| cl_v6_fair | -0.0068 |

##### Aggregate mean across Specific 1000-gene datasets

Latent variables: metric=DELTA_PRECISION_AT_K_VS_BASELINE, negative_protocol=tf_stratified_1to10, network_group=Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | -0.0001 |
| baseline | 0.0000 |
| scGPT_human | -0.0029 |
| v4_bias_rec_best | **0.0008** |
| v4_plain_best | <span style="color:red"><strong>0.0052</strong></span> |
| v4_type_pe_best | -0.0011 |
| scconcept | -0.0378 |
| scconcept_encoded | -0.0345 |
| cl_scratch_v5 | -0.0046 |
| cl_v6_fair | **0.0030** |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | -0.0248 | <span style="color:red"><strong>0.0357</strong></span> | -0.0052 | **0.0517** | **0.0543** | -0.1364 | <span style="color:red"><strong>0.0253</strong></span> | -0.0227 | **0.0328** | **0.0256** | **0.0196** | -0.0217 |
| baseline | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| scGPT_human | -0.0497 | **0.0119** | <span style="color:red"><strong>0.0361</strong></span> | <span style="color:red"><strong>0.1207</strong></span> | **0.0388** | -0.1364 | **0.0084** | <span style="color:red"><strong>0.0758</strong></span> | **0.0511** | <span style="color:red"><strong>0.1282</strong></span> | **0.0392** | **0.1087** |
| v4_bias_rec_best | -0.0466 | -0.0119 | -0.0258 | **0.0862** | **0.0155** | **0.0000** | -0.0421 | -0.0303 | <span style="color:red"><strong>0.0876</strong></span> | 0.0000 | **0.0033** | **0.0109** |
| v4_plain_best | -0.0404 | **0.0000** | **0.0103** | **0.0862** | -0.0349 | -0.0909 | **0.0084** | **0.0152** | **0.0146** | **0.0000** | -0.0098 | **0.0761** |
| v4_type_pe_best | <span style="color:red"><strong>0.0248</strong></span> | -0.0238 | **0.0103** | -0.0172 | **0.0310** | -0.0000 | -0.0197 | **0.0303** | 0.0000 | -0.0256 | **0.0163** | <span style="color:red"><strong>0.1413</strong></span> |
| scconcept | -0.1180 | -0.0238 | -0.1134 | -0.0172 | -0.1395 | -0.2727 | -0.1938 | -0.2348 | -0.0839 | -0.0385 | -0.0850 | -0.0870 |
| scconcept_encoded | -0.1553 | -0.0476 | -0.1186 | -0.0862 | -0.1783 | -0.1818 | -0.1770 | -0.1970 | -0.1131 | -0.0641 | -0.0882 | -0.1196 |
| cl_scratch_v5 | 0.0000 | **0.0238** | -0.0000 | **0.0345** | <span style="color:red"><strong>0.0581</strong></span> | -0.0455 | <span style="color:red"><strong>0.0253</strong></span> | -0.0303 | **0.0584** | -0.0385 | **0.0033** | **0.1196** |
| cl_v6_fair | -0.0342 | <span style="color:red"><strong>0.0357</strong></span> | -0.0206 | -0.0345 | **0.0504** | <span style="color:red"><strong>0.0455</strong></span> | -0.0084 | -0.0303 | **0.0401** | **0.0000** | <span style="color:red"><strong>0.0425</strong></span> | -0.0217 |

##### Aggregate mean across Non-Specific 500-gene datasets

Latent variables: metric=DELTA_PRECISION_AT_K_VS_BASELINE, negative_protocol=tf_stratified_1to10, network_group=Non-Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | -0.0113 |
| baseline | 0.0000 |
| scGPT_human | <span style="color:red"><strong>0.0515</strong></span> |
| v4_bias_rec_best | **0.0091** |
| v4_plain_best | **0.0144** |
| v4_type_pe_best | **0.0175** |
| scconcept | -0.1123 |
| scconcept_encoded | -0.1160 |
| cl_scratch_v5 | **0.0106** |
| cl_v6_fair | -0.0009 |

##### Aggregate mean across Non-Specific 1000-gene datasets

Latent variables: metric=DELTA_PRECISION_AT_K_VS_BASELINE, negative_protocol=tf_stratified_1to10, network_group=Non-Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.0170** |
| baseline | 0.0000 |
| scGPT_human | **0.0206** |
| v4_bias_rec_best | -0.0014 |
| v4_plain_best | -0.0086 |
| v4_type_pe_best | **0.0105** |
| scconcept | -0.1223 |
| scconcept_encoded | -0.1384 |
| cl_scratch_v5 | <span style="color:red"><strong>0.0242</strong></span> |
| cl_v6_fair | **0.0116** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | -0.0210 | -0.0469 | -0.0233 | **0.0075** | **0.0096** | **0.0455** | **0.0108** | -0.0161 | -0.0620 | **0.2581** | **0.0101** | **0.0294** |
| baseline | 0.0000 | 0.0000 | <span style="color:red"><strong>0.0000</strong></span> | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| scGPT_human | **0.0294** | **0.0469** | -0.0186 | <span style="color:red"><strong>0.0597</strong></span> | -0.0287 | <span style="color:red"><strong>0.2121</strong></span> | **0.0242** | **0.0161** | <span style="color:red"><strong>0.0039</strong></span> | **0.0806** | <span style="color:red"><strong>0.0473</strong></span> | **0.0294** |
| v4_bias_rec_best | -0.0378 | -0.0156 | <span style="color:red"><strong>0.0000</strong></span> | **0.0448** | -0.0335 | **0.0758** | -0.0108 | <span style="color:red"><strong>0.0323</strong></span> | -0.0620 | <span style="color:red"><strong>0.2903</strong></span> | -0.0135 | <span style="color:red"><strong>0.1029</strong></span> |
| v4_plain_best | -0.0420 | **0.0312** | -0.0326 | **0.0224** | -0.0167 | **0.0455** | **0.0242** | <span style="color:red"><strong>0.0323</strong></span> | -0.0659 | **0.1290** | -0.0270 | **0.0294** |
| v4_type_pe_best | <span style="color:red"><strong>0.0336</strong></span> | **0.0469** | -0.0349 | **0.0224** | <span style="color:red"><strong>0.0215</strong></span> | **0.0606** | <span style="color:red"><strong>0.0349</strong></span> | **0.0081** | -0.0388 | **0.2742** | **0.0304** | **0.0441** |
| scconcept | -0.1891 | <span style="color:red"><strong>0.0625</strong></span> | -0.2070 | -0.2164 | -0.1699 | -0.1061 | -0.2769 | -0.3065 | -0.2674 | -0.0645 | -0.1554 | -0.1176 |
| scconcept_encoded | -0.2185 | -0.0938 | -0.2163 | -0.3731 | -0.2464 | -0.1364 | -0.3172 | -0.4113 | -0.2752 | -0.0806 | -0.1926 | -0.1912 |
| cl_scratch_v5 | -0.0294 | 0.0000 | -0.0186 | -0.0224 | <span style="color:red"><strong>0.0215</strong></span> | **0.1061** | **0.0242** | <span style="color:red"><strong>0.0323</strong></span> | -0.0078 | **0.1290** | -0.0000 | **0.0000** |
| cl_v6_fair | -0.0378 | 0.0000 | -0.0209 | -0.0299 | **0.0191** | **0.0606** | **0.0323** | -0.0081 | -0.0388 | **0.1935** | -0.0034 | **0.0294** |

##### Aggregate mean across STRING 500-gene datasets

Latent variables: metric=DELTA_PRECISION_AT_K_VS_BASELINE, negative_protocol=tf_stratified_1to10, network_group=STRING, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.0462** |
| baseline | 0.0000 |
| scGPT_human | **0.0741** |
| v4_bias_rec_best | <span style="color:red"><strong>0.0884</strong></span> |
| v4_plain_best | **0.0483** |
| v4_type_pe_best | **0.0760** |
| scconcept | -0.1248 |
| scconcept_encoded | -0.2144 |
| cl_scratch_v5 | **0.0408** |
| cl_v6_fair | **0.0409** |

##### Aggregate mean across STRING 1000-gene datasets

Latent variables: metric=DELTA_PRECISION_AT_K_VS_BASELINE, negative_protocol=tf_stratified_1to10, network_group=STRING, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | -0.0126 |
| baseline | 0.0000 |
| scGPT_human | <span style="color:red"><strong>0.0096</strong></span> |
| v4_bias_rec_best | -0.0263 |
| v4_plain_best | -0.0267 |
| v4_type_pe_best | **0.0078** |
| scconcept | -0.2109 |
| scconcept_encoded | -0.2444 |
| cl_scratch_v5 | -0.0017 |
| cl_v6_fair | -0.0082 |

### Negative protocol: full_candidate

Latent variables: metric=DELTA_PRECISION_AT_K_VS_BASELINE, negative_protocol=full_candidate, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.0049** | -0.0266 | -0.0113 | -0.0143 | <span style="color:red"><strong>0.0000</strong></span> | **0.0084** | -0.0106 | -0.0009 | **0.0056** | <span style="color:red"><strong>0.0086</strong></span> | <span style="color:red"><strong>0.0200</strong></span> |
| baseline | 0.0000 | 0.0000 | <span style="color:red"><strong>0.0000</strong></span> | 0.0000 | <span style="color:red"><strong>0.0000</strong></span> | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| scGPT_human | **0.0024** | **0.0296** | -0.0376 | -0.0107 | <span style="color:red"><strong>0.0000</strong></span> | **0.0061** | -0.0149 | -0.0018 | -0.0045 | **0.0014** | -0.0155 |
| v4_bias_rec_best | **0.0061** | **0.0089** | -0.0113 | -0.0643 | -0.1250 | **0.0115** | **0.0043** | -0.0068 | <span style="color:red"><strong>0.0112</strong></span> | -0.0053 | -0.0045 |
| v4_plain_best | **0.0109** | **0.0059** | -0.0094 | -0.0714 | -0.0625 | **0.0108** | **0.0213** | **0.0009** | -0.0067 | -0.0038 | -0.0009 |
| v4_type_pe_best | <span style="color:red"><strong>0.0255</strong></span> | **0.0237** | -0.0244 | -0.0536 | <span style="color:red"><strong>0.0000</strong></span> | **0.0067** | **0.0234** | **0.0003** | -0.0022 | **0.0010** | **0.0100** |
| scconcept | -0.0316 | <span style="color:red"><strong>0.0325</strong></span> | -0.0733 | -0.1000 | <span style="color:red"><strong>0.0000</strong></span> | -0.0098 | -0.0426 | -0.0228 | -0.0145 | -0.0151 | -0.0382 |
| scconcept_encoded | -0.0485 | **0.0059** | -0.0602 | -0.0607 | -0.1875 | -0.0105 | -0.0234 | -0.0240 | -0.0301 | -0.0156 | -0.0409 |
| cl_scratch_v5 | -0.0073 | -0.0030 | -0.0320 | <span style="color:red"><strong>0.0036</strong></span> | <span style="color:red"><strong>0.0000</strong></span> | **0.0047** | **0.0128** | -0.0000 | **0.0000** | -0.0010 | -0.0018 |
| cl_v6_fair | -0.0061 | -0.0237 | -0.0282 | -0.0107 | <span style="color:red"><strong>0.0000</strong></span> | <span style="color:red"><strong>0.0132</strong></span> | <span style="color:red"><strong>0.0362</strong></span> | <span style="color:red"><strong>0.0015</strong></span> | **0.0100** | **0.0012** | 0.0000 |

##### Aggregate mean across Specific 500-gene datasets

Latent variables: metric=DELTA_PRECISION_AT_K_VS_BASELINE, negative_protocol=full_candidate, network_group=Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | -0.0023 |
| baseline | 0.0000 |
| scGPT_human | -0.0010 |
| v4_bias_rec_best | -0.0211 |
| v4_plain_best | -0.0086 |
| v4_type_pe_best | <span style="color:red"><strong>0.0110</strong></span> |
| scconcept | -0.0125 |
| scconcept_encoded | -0.0552 |
| cl_scratch_v5 | **0.0016** |
| cl_v6_fair | **0.0045** |

##### Aggregate mean across Specific 1000-gene datasets

Latent variables: metric=DELTA_PRECISION_AT_K_VS_BASELINE, negative_protocol=full_candidate, network_group=Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | -0.0008 |
| baseline | <span style="color:red"><strong>0.0000</strong></span> |
| scGPT_human | -0.0067 |
| v4_bias_rec_best | -0.0117 |
| v4_plain_best | -0.0103 |
| v4_type_pe_best | -0.0074 |
| scconcept | -0.0421 |
| scconcept_encoded | -0.0366 |
| cl_scratch_v5 | -0.0053 |
| cl_v6_fair | -0.0049 |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.0124** | <span style="color:red"><strong>0.0119</strong></span> | **0.0258** | **0.0172** | **0.0388** | **0.0455** | **0.0169** | **0.0227** | **0.0219** | **0.0128** | **0.0229** | -0.0326 |
| baseline | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| scGPT_human | -0.0155 | -0.0476 | <span style="color:red"><strong>0.0773</strong></span> | <span style="color:red"><strong>0.0345</strong></span> | <span style="color:red"><strong>0.0581</strong></span> | -0.0455 | **0.0084** | **0.0379** | <span style="color:red"><strong>0.0438</strong></span> | <span style="color:red"><strong>0.0897</strong></span> | <span style="color:red"><strong>0.0261</strong></span> | **0.0870** |
| v4_bias_rec_best | **0.0062** | -0.0595 | **0.0515** | <span style="color:red"><strong>0.0345</strong></span> | **0.0194** | **0.0000** | -0.0197 | -0.0076 | **0.0146** | **0.0641** | -0.0098 | **0.0978** |
| v4_plain_best | <span style="color:red"><strong>0.0280</strong></span> | -0.0119 | **0.0309** | <span style="color:red"><strong>0.0345</strong></span> | **0.0388** | **0.0000** | -0.0197 | -0.0152 | **0.0146** | **0.0128** | **0.0196** | <span style="color:red"><strong>0.1304</strong></span> |
| v4_type_pe_best | **0.0155** | <span style="color:red"><strong>0.0119</strong></span> | **0.0361** | -0.0345 | **0.0194** | **0.0000** | -0.0028 | **0.0152** | <span style="color:red"><strong>0.0438</strong></span> | **0.0513** | <span style="color:red"><strong>0.0261</strong></span> | **0.1087** |
| scconcept | -0.0248 | -0.1071 | -0.0567 | -0.0862 | -0.0581 | -0.0909 | -0.1713 | -0.1894 | -0.1131 | -0.0256 | -0.0654 | -0.0326 |
| scconcept_encoded | -0.0776 | -0.1905 | -0.0619 | -0.1034 | -0.1202 | -0.1364 | -0.1770 | -0.1364 | -0.1460 | -0.0897 | -0.1078 | -0.0870 |
| cl_scratch_v5 | **0.0217** | 0.0000 | **0.0515** | -0.0345 | **0.0465** | **0.0455** | <span style="color:red"><strong>0.0197</strong></span> | <span style="color:red"><strong>0.0530</strong></span> | <span style="color:red"><strong>0.0438</strong></span> | 0.0000 | -0.0261 | <span style="color:red"><strong>0.1304</strong></span> |
| cl_v6_fair | -0.0124 | -0.0119 | **0.0464** | -0.0172 | **0.0000** | <span style="color:red"><strong>0.0909</strong></span> | -0.0056 | -0.0076 | -0.0073 | **0.0128** | -0.0098 | **0.0978** |

##### Aggregate mean across Non-Specific 500-gene datasets

Latent variables: metric=DELTA_PRECISION_AT_K_VS_BASELINE, negative_protocol=full_candidate, network_group=Non-Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.0129** |
| baseline | 0.0000 |
| scGPT_human | **0.0260** |
| v4_bias_rec_best | **0.0216** |
| v4_plain_best | **0.0251** |
| v4_type_pe_best | **0.0254** |
| scconcept | -0.0887 |
| scconcept_encoded | -0.1239 |
| cl_scratch_v5 | <span style="color:red"><strong>0.0324</strong></span> |
| cl_v6_fair | **0.0275** |

##### Aggregate mean across Non-Specific 1000-gene datasets

Latent variables: metric=DELTA_PRECISION_AT_K_VS_BASELINE, negative_protocol=full_candidate, network_group=Non-Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.0231** |
| baseline | 0.0000 |
| scGPT_human | <span style="color:red"><strong>0.0330</strong></span> |
| v4_bias_rec_best | **0.0104** |
| v4_plain_best | **0.0187** |
| v4_type_pe_best | **0.0230** |
| scconcept | -0.0816 |
| scconcept_encoded | -0.1151 |
| cl_scratch_v5 | **0.0262** |
| cl_v6_fair | **0.0019** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | <span style="color:red"><strong>0.0210</strong></span> | 0.0000 | <span style="color:red"><strong>0.0140</strong></span> | -0.0448 | **0.0191** | **0.0303** | **0.0027** | **0.0403** | -0.0194 | <span style="color:red"><strong>0.0645</strong></span> | <span style="color:red"><strong>0.0507</strong></span> | **0.0147** |
| baseline | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| scGPT_human | **0.0042** | <span style="color:red"><strong>0.1406</strong></span> | -0.0023 | <span style="color:red"><strong>0.0075</strong></span> | -0.0167 | **0.0909** | -0.0215 | <span style="color:red"><strong>0.0887</strong></span> | <span style="color:red"><strong>0.0194</strong></span> | **0.0323** | **0.0473** | **0.0147** |
| v4_bias_rec_best | -0.0000 | -0.0156 | **0.0047** | -0.0448 | -0.0144 | **0.0152** | -0.0108 | **0.0484** | -0.0581 | <span style="color:red"><strong>0.0645</strong></span> | **0.0068** | **0.0882** |
| v4_plain_best | -0.0084 | **0.0156** | -0.0186 | -0.0896 | -0.0144 | <span style="color:red"><strong>0.1212</strong></span> | **0.0027** | **0.0081** | **0.0078** | **0.0323** | **0.0101** | **0.0294** |
| v4_type_pe_best | **0.0168** | 0.0000 | -0.0070 | -0.0149 | **0.0120** | **0.0303** | 0.0000 | **0.0565** | **0.0039** | **0.0000** | **0.0236** | <span style="color:red"><strong>0.1029</strong></span> |
| scconcept | -0.1933 | **0.0156** | -0.1581 | -0.3582 | -0.1866 | -0.2576 | -0.2957 | -0.3387 | -0.2519 | -0.1935 | -0.1791 | -0.1471 |
| scconcept_encoded | -0.2101 | -0.0312 | -0.2721 | -0.3507 | -0.1794 | -0.3182 | -0.3038 | -0.3629 | -0.2829 | -0.1452 | -0.2534 | -0.1618 |
| cl_scratch_v5 | -0.0042 | **0.0312** | -0.0023 | -0.0672 | **0.0167** | **0.0909** | <span style="color:red"><strong>0.0134</strong></span> | <span style="color:red"><strong>0.0887</strong></span> | **0.0155** | -0.0323 | **0.0068** | **0.0441** |
| cl_v6_fair | **0.0084** | **0.0625** | -0.0116 | -0.0672 | <span style="color:red"><strong>0.0383</strong></span> | **0.0758** | -0.0054 | **0.0161** | **0.0078** | -0.0484 | **0.0236** | **0.0735** |

##### Aggregate mean across STRING 500-gene datasets

Latent variables: metric=DELTA_PRECISION_AT_K_VS_BASELINE, negative_protocol=full_candidate, network_group=STRING, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.0175** |
| baseline | 0.0000 |
| scGPT_human | <span style="color:red"><strong>0.0624</strong></span> |
| v4_bias_rec_best | **0.0260** |
| v4_plain_best | **0.0195** |
| v4_type_pe_best | **0.0291** |
| scconcept | -0.2132 |
| scconcept_encoded | -0.2283 |
| cl_scratch_v5 | **0.0259** |
| cl_v6_fair | **0.0187** |

##### Aggregate mean across STRING 1000-gene datasets

Latent variables: metric=DELTA_PRECISION_AT_K_VS_BASELINE, negative_protocol=full_candidate, network_group=STRING, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | <span style="color:red"><strong>0.0147</strong></span> |
| baseline | 0.0000 |
| scGPT_human | **0.0051** |
| v4_bias_rec_best | -0.0120 |
| v4_plain_best | -0.0035 |
| v4_type_pe_best | **0.0082** |
| scconcept | -0.2108 |
| scconcept_encoded | -0.2503 |
| cl_scratch_v5 | **0.0077** |
| cl_v6_fair | **0.0102** |

## DELTA_RECALL_AT_K_VS_BASELINE (Supplementary)

### Negative protocol: tf_stratified_1to10

Latent variables: metric=DELTA_RECALL_AT_K_VS_BASELINE, negative_protocol=tf_stratified_1to10, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.0000 | -0.0325 | -0.0132 | -0.0036 | 0.0000 | -0.0013 | -0.0021 | <span style="color:red"><strong>0.0104</strong></span> | **0.0089** | **0.0072** | <span style="color:red"><strong>0.0209</strong></span> |
| baseline | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | <span style="color:red"><strong>0.0000</strong></span> | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| scGPT_human | <span style="color:red"><strong>0.0097</strong></span> | -0.0059 | -0.0376 | **0.0036** | <span style="color:red"><strong>0.0625</strong></span> | <span style="color:red"><strong>0.0013</strong></span> | -0.0298 | -0.0036 | **0.0089** | <span style="color:red"><strong>0.0093</strong></span> | **0.0018** |
| v4_bias_rec_best | -0.0085 | -0.0148 | -0.0038 | **0.0143** | -0.1250 | -0.0024 | -0.0128 | -0.0021 | <span style="color:red"><strong>0.0346</strong></span> | **0.0069** | **0.0100** |
| v4_plain_best | **0.0036** | -0.0059 | <span style="color:red"><strong>0.0019</strong></span> | **0.0214** | 0.0000 | -0.0037 | -0.0234 | **0.0044** | -0.0033 | **0.0036** | **0.0155** |
| v4_type_pe_best | **0.0012** | **0.0266** | 0.0000 | -0.0107 | -0.1250 | -0.0037 | <span style="color:red"><strong>-0.0000</strong></span> | **0.0024** | **0.0145** | **0.0041** | **0.0109** |
| scconcept | -0.0740 | -0.0207 | -0.0470 | -0.0607 | 0.0000 | -0.0199 | -0.0638 | -0.0287 | -0.0379 | **0.0034** | -0.0373 |
| scconcept_encoded | -0.0534 | -0.0207 | -0.0658 | -0.0250 | -0.1250 | -0.0219 | -0.0468 | -0.0314 | -0.0234 | -0.0096 | -0.0464 |
| cl_scratch_v5 | -0.0133 | <span style="color:red"><strong>0.0296</strong></span> | -0.0169 | **0.0071** | <span style="color:red"><strong>0.0625</strong></span> | -0.0040 | -0.0234 | -0.0033 | **0.0134** | **0.0029** | **0.0073** |
| cl_v6_fair | -0.0206 | -0.0355 | -0.0169 | <span style="color:red"><strong>0.0500</strong></span> | 0.0000 | -0.0034 | -0.0191 | **0.0036** | **0.0134** | **0.0053** | **0.0073** |

##### Aggregate mean across Specific 500-gene datasets

Latent variables: metric=DELTA_RECALL_AT_K_VS_BASELINE, negative_protocol=tf_stratified_1to10, network_group=Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | -0.0010 |
| baseline | 0.0000 |
| scGPT_human | **0.0075** |
| v4_bias_rec_best | -0.0216 |
| v4_plain_best | -0.0034 |
| v4_type_pe_best | -0.0146 |
| scconcept | -0.0320 |
| scconcept_encoded | -0.0525 |
| cl_scratch_v5 | <span style="color:red"><strong>0.0179</strong></span> |
| cl_v6_fair | -0.0068 |

##### Aggregate mean across Specific 1000-gene datasets

Latent variables: metric=DELTA_RECALL_AT_K_VS_BASELINE, negative_protocol=tf_stratified_1to10, network_group=Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | -0.0001 |
| baseline | 0.0000 |
| scGPT_human | -0.0029 |
| v4_bias_rec_best | **0.0008** |
| v4_plain_best | <span style="color:red"><strong>0.0052</strong></span> |
| v4_type_pe_best | -0.0011 |
| scconcept | -0.0378 |
| scconcept_encoded | -0.0345 |
| cl_scratch_v5 | -0.0046 |
| cl_v6_fair | **0.0030** |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | -0.0248 | <span style="color:red"><strong>0.0357</strong></span> | -0.0052 | **0.0517** | **0.0543** | -0.1364 | <span style="color:red"><strong>0.0253</strong></span> | -0.0227 | **0.0328** | **0.0256** | **0.0196** | -0.0217 |
| baseline | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| scGPT_human | -0.0497 | **0.0119** | <span style="color:red"><strong>0.0361</strong></span> | <span style="color:red"><strong>0.1207</strong></span> | **0.0388** | -0.1364 | **0.0084** | <span style="color:red"><strong>0.0758</strong></span> | **0.0511** | <span style="color:red"><strong>0.1282</strong></span> | **0.0392** | **0.1087** |
| v4_bias_rec_best | -0.0466 | -0.0119 | -0.0258 | **0.0862** | **0.0155** | **0.0000** | -0.0421 | -0.0303 | <span style="color:red"><strong>0.0876</strong></span> | 0.0000 | **0.0033** | **0.0109** |
| v4_plain_best | -0.0404 | **0.0000** | **0.0103** | **0.0862** | -0.0349 | -0.0909 | **0.0084** | **0.0152** | **0.0146** | **0.0000** | -0.0098 | **0.0761** |
| v4_type_pe_best | <span style="color:red"><strong>0.0248</strong></span> | -0.0238 | **0.0103** | -0.0172 | **0.0310** | -0.0000 | -0.0197 | **0.0303** | 0.0000 | -0.0256 | **0.0163** | <span style="color:red"><strong>0.1413</strong></span> |
| scconcept | -0.1180 | -0.0238 | -0.1134 | -0.0172 | -0.1395 | -0.2727 | -0.1938 | -0.2348 | -0.0839 | -0.0385 | -0.0850 | -0.0870 |
| scconcept_encoded | -0.1553 | -0.0476 | -0.1186 | -0.0862 | -0.1783 | -0.1818 | -0.1770 | -0.1970 | -0.1131 | -0.0641 | -0.0882 | -0.1196 |
| cl_scratch_v5 | 0.0000 | **0.0238** | -0.0000 | **0.0345** | <span style="color:red"><strong>0.0581</strong></span> | -0.0455 | <span style="color:red"><strong>0.0253</strong></span> | -0.0303 | **0.0584** | -0.0385 | **0.0033** | **0.1196** |
| cl_v6_fair | -0.0342 | <span style="color:red"><strong>0.0357</strong></span> | -0.0206 | -0.0345 | **0.0504** | <span style="color:red"><strong>0.0455</strong></span> | -0.0084 | -0.0303 | **0.0401** | **0.0000** | <span style="color:red"><strong>0.0425</strong></span> | -0.0217 |

##### Aggregate mean across Non-Specific 500-gene datasets

Latent variables: metric=DELTA_RECALL_AT_K_VS_BASELINE, negative_protocol=tf_stratified_1to10, network_group=Non-Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | -0.0113 |
| baseline | 0.0000 |
| scGPT_human | <span style="color:red"><strong>0.0515</strong></span> |
| v4_bias_rec_best | **0.0091** |
| v4_plain_best | **0.0144** |
| v4_type_pe_best | **0.0175** |
| scconcept | -0.1123 |
| scconcept_encoded | -0.1160 |
| cl_scratch_v5 | **0.0106** |
| cl_v6_fair | -0.0009 |

##### Aggregate mean across Non-Specific 1000-gene datasets

Latent variables: metric=DELTA_RECALL_AT_K_VS_BASELINE, negative_protocol=tf_stratified_1to10, network_group=Non-Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.0170** |
| baseline | 0.0000 |
| scGPT_human | **0.0206** |
| v4_bias_rec_best | -0.0014 |
| v4_plain_best | -0.0086 |
| v4_type_pe_best | **0.0105** |
| scconcept | -0.1223 |
| scconcept_encoded | -0.1384 |
| cl_scratch_v5 | <span style="color:red"><strong>0.0242</strong></span> |
| cl_v6_fair | **0.0116** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | -0.0210 | -0.0469 | -0.0233 | **0.0075** | **0.0096** | **0.0455** | **0.0108** | -0.0161 | -0.0620 | **0.2581** | **0.0101** | **0.0294** |
| baseline | 0.0000 | 0.0000 | <span style="color:red"><strong>0.0000</strong></span> | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| scGPT_human | **0.0294** | **0.0469** | -0.0186 | <span style="color:red"><strong>0.0597</strong></span> | -0.0287 | <span style="color:red"><strong>0.2121</strong></span> | **0.0242** | **0.0161** | <span style="color:red"><strong>0.0039</strong></span> | **0.0806** | <span style="color:red"><strong>0.0473</strong></span> | **0.0294** |
| v4_bias_rec_best | -0.0378 | -0.0156 | <span style="color:red"><strong>0.0000</strong></span> | **0.0448** | -0.0335 | **0.0758** | -0.0108 | <span style="color:red"><strong>0.0323</strong></span> | -0.0620 | <span style="color:red"><strong>0.2903</strong></span> | -0.0135 | <span style="color:red"><strong>0.1029</strong></span> |
| v4_plain_best | -0.0420 | **0.0312** | -0.0326 | **0.0224** | -0.0167 | **0.0455** | **0.0242** | <span style="color:red"><strong>0.0323</strong></span> | -0.0659 | **0.1290** | -0.0270 | **0.0294** |
| v4_type_pe_best | <span style="color:red"><strong>0.0336</strong></span> | **0.0469** | -0.0349 | **0.0224** | <span style="color:red"><strong>0.0215</strong></span> | **0.0606** | <span style="color:red"><strong>0.0349</strong></span> | **0.0081** | -0.0388 | **0.2742** | **0.0304** | **0.0441** |
| scconcept | -0.1891 | <span style="color:red"><strong>0.0625</strong></span> | -0.2070 | -0.2164 | -0.1699 | -0.1061 | -0.2769 | -0.3065 | -0.2674 | -0.0645 | -0.1554 | -0.1176 |
| scconcept_encoded | -0.2185 | -0.0938 | -0.2163 | -0.3731 | -0.2464 | -0.1364 | -0.3172 | -0.4113 | -0.2752 | -0.0806 | -0.1926 | -0.1912 |
| cl_scratch_v5 | -0.0294 | 0.0000 | -0.0186 | -0.0224 | <span style="color:red"><strong>0.0215</strong></span> | **0.1061** | **0.0242** | <span style="color:red"><strong>0.0323</strong></span> | -0.0078 | **0.1290** | -0.0000 | **0.0000** |
| cl_v6_fair | -0.0378 | 0.0000 | -0.0209 | -0.0299 | **0.0191** | **0.0606** | **0.0323** | -0.0081 | -0.0388 | **0.1935** | -0.0034 | **0.0294** |

##### Aggregate mean across STRING 500-gene datasets

Latent variables: metric=DELTA_RECALL_AT_K_VS_BASELINE, negative_protocol=tf_stratified_1to10, network_group=STRING, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.0462** |
| baseline | 0.0000 |
| scGPT_human | **0.0741** |
| v4_bias_rec_best | <span style="color:red"><strong>0.0884</strong></span> |
| v4_plain_best | **0.0483** |
| v4_type_pe_best | **0.0760** |
| scconcept | -0.1248 |
| scconcept_encoded | -0.2144 |
| cl_scratch_v5 | **0.0408** |
| cl_v6_fair | **0.0409** |

##### Aggregate mean across STRING 1000-gene datasets

Latent variables: metric=DELTA_RECALL_AT_K_VS_BASELINE, negative_protocol=tf_stratified_1to10, network_group=STRING, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | -0.0126 |
| baseline | 0.0000 |
| scGPT_human | <span style="color:red"><strong>0.0096</strong></span> |
| v4_bias_rec_best | -0.0263 |
| v4_plain_best | -0.0267 |
| v4_type_pe_best | **0.0078** |
| scconcept | -0.2109 |
| scconcept_encoded | -0.2444 |
| cl_scratch_v5 | -0.0017 |
| cl_v6_fair | -0.0082 |

### Negative protocol: full_candidate

Latent variables: metric=DELTA_RECALL_AT_K_VS_BASELINE, negative_protocol=full_candidate, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.0049** | -0.0266 | -0.0113 | -0.0143 | <span style="color:red"><strong>0.0000</strong></span> | **0.0084** | -0.0106 | -0.0009 | **0.0056** | <span style="color:red"><strong>0.0086</strong></span> | <span style="color:red"><strong>0.0200</strong></span> |
| baseline | 0.0000 | 0.0000 | <span style="color:red"><strong>0.0000</strong></span> | 0.0000 | <span style="color:red"><strong>0.0000</strong></span> | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| scGPT_human | **0.0024** | **0.0296** | -0.0376 | -0.0107 | <span style="color:red"><strong>0.0000</strong></span> | **0.0061** | -0.0149 | -0.0018 | -0.0045 | **0.0014** | -0.0155 |
| v4_bias_rec_best | **0.0061** | **0.0089** | -0.0113 | -0.0643 | -0.1250 | **0.0115** | **0.0043** | -0.0068 | <span style="color:red"><strong>0.0112</strong></span> | -0.0053 | -0.0045 |
| v4_plain_best | **0.0109** | **0.0059** | -0.0094 | -0.0714 | -0.0625 | **0.0108** | **0.0213** | **0.0009** | -0.0067 | -0.0038 | -0.0009 |
| v4_type_pe_best | <span style="color:red"><strong>0.0255</strong></span> | **0.0237** | -0.0244 | -0.0536 | <span style="color:red"><strong>0.0000</strong></span> | **0.0067** | **0.0234** | **0.0003** | -0.0022 | **0.0010** | **0.0100** |
| scconcept | -0.0316 | <span style="color:red"><strong>0.0325</strong></span> | -0.0733 | -0.1000 | <span style="color:red"><strong>0.0000</strong></span> | -0.0098 | -0.0426 | -0.0228 | -0.0145 | -0.0151 | -0.0382 |
| scconcept_encoded | -0.0485 | **0.0059** | -0.0602 | -0.0607 | -0.1875 | -0.0105 | -0.0234 | -0.0240 | -0.0301 | -0.0156 | -0.0409 |
| cl_scratch_v5 | -0.0073 | -0.0030 | -0.0320 | <span style="color:red"><strong>0.0036</strong></span> | <span style="color:red"><strong>0.0000</strong></span> | **0.0047** | **0.0128** | -0.0000 | **0.0000** | -0.0010 | -0.0018 |
| cl_v6_fair | -0.0061 | -0.0237 | -0.0282 | -0.0107 | <span style="color:red"><strong>0.0000</strong></span> | <span style="color:red"><strong>0.0132</strong></span> | <span style="color:red"><strong>0.0362</strong></span> | <span style="color:red"><strong>0.0015</strong></span> | **0.0100** | **0.0012** | 0.0000 |

##### Aggregate mean across Specific 500-gene datasets

Latent variables: metric=DELTA_RECALL_AT_K_VS_BASELINE, negative_protocol=full_candidate, network_group=Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | -0.0023 |
| baseline | 0.0000 |
| scGPT_human | -0.0010 |
| v4_bias_rec_best | -0.0211 |
| v4_plain_best | -0.0086 |
| v4_type_pe_best | <span style="color:red"><strong>0.0110</strong></span> |
| scconcept | -0.0125 |
| scconcept_encoded | -0.0552 |
| cl_scratch_v5 | **0.0016** |
| cl_v6_fair | **0.0045** |

##### Aggregate mean across Specific 1000-gene datasets

Latent variables: metric=DELTA_RECALL_AT_K_VS_BASELINE, negative_protocol=full_candidate, network_group=Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | -0.0008 |
| baseline | <span style="color:red"><strong>0.0000</strong></span> |
| scGPT_human | -0.0067 |
| v4_bias_rec_best | -0.0117 |
| v4_plain_best | -0.0103 |
| v4_type_pe_best | -0.0074 |
| scconcept | -0.0421 |
| scconcept_encoded | -0.0366 |
| cl_scratch_v5 | -0.0053 |
| cl_v6_fair | -0.0049 |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.0124** | <span style="color:red"><strong>0.0119</strong></span> | **0.0258** | **0.0172** | **0.0388** | **0.0455** | **0.0169** | **0.0227** | **0.0219** | **0.0128** | **0.0229** | -0.0326 |
| baseline | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| scGPT_human | -0.0155 | -0.0476 | <span style="color:red"><strong>0.0773</strong></span> | <span style="color:red"><strong>0.0345</strong></span> | <span style="color:red"><strong>0.0581</strong></span> | -0.0455 | **0.0084** | **0.0379** | <span style="color:red"><strong>0.0438</strong></span> | <span style="color:red"><strong>0.0897</strong></span> | <span style="color:red"><strong>0.0261</strong></span> | **0.0870** |
| v4_bias_rec_best | **0.0062** | -0.0595 | **0.0515** | <span style="color:red"><strong>0.0345</strong></span> | **0.0194** | **0.0000** | -0.0197 | -0.0076 | **0.0146** | **0.0641** | -0.0098 | **0.0978** |
| v4_plain_best | <span style="color:red"><strong>0.0280</strong></span> | -0.0119 | **0.0309** | <span style="color:red"><strong>0.0345</strong></span> | **0.0388** | **0.0000** | -0.0197 | -0.0152 | **0.0146** | **0.0128** | **0.0196** | <span style="color:red"><strong>0.1304</strong></span> |
| v4_type_pe_best | **0.0155** | <span style="color:red"><strong>0.0119</strong></span> | **0.0361** | -0.0345 | **0.0194** | **0.0000** | -0.0028 | **0.0152** | <span style="color:red"><strong>0.0438</strong></span> | **0.0513** | <span style="color:red"><strong>0.0261</strong></span> | **0.1087** |
| scconcept | -0.0248 | -0.1071 | -0.0567 | -0.0862 | -0.0581 | -0.0909 | -0.1713 | -0.1894 | -0.1131 | -0.0256 | -0.0654 | -0.0326 |
| scconcept_encoded | -0.0776 | -0.1905 | -0.0619 | -0.1034 | -0.1202 | -0.1364 | -0.1770 | -0.1364 | -0.1460 | -0.0897 | -0.1078 | -0.0870 |
| cl_scratch_v5 | **0.0217** | 0.0000 | **0.0515** | -0.0345 | **0.0465** | **0.0455** | <span style="color:red"><strong>0.0197</strong></span> | <span style="color:red"><strong>0.0530</strong></span> | <span style="color:red"><strong>0.0438</strong></span> | 0.0000 | -0.0261 | <span style="color:red"><strong>0.1304</strong></span> |
| cl_v6_fair | -0.0124 | -0.0119 | **0.0464** | -0.0172 | **0.0000** | <span style="color:red"><strong>0.0909</strong></span> | -0.0056 | -0.0076 | -0.0073 | **0.0128** | -0.0098 | **0.0978** |

##### Aggregate mean across Non-Specific 500-gene datasets

Latent variables: metric=DELTA_RECALL_AT_K_VS_BASELINE, negative_protocol=full_candidate, network_group=Non-Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.0129** |
| baseline | 0.0000 |
| scGPT_human | **0.0260** |
| v4_bias_rec_best | **0.0216** |
| v4_plain_best | **0.0251** |
| v4_type_pe_best | **0.0254** |
| scconcept | -0.0887 |
| scconcept_encoded | -0.1239 |
| cl_scratch_v5 | <span style="color:red"><strong>0.0324</strong></span> |
| cl_v6_fair | **0.0275** |

##### Aggregate mean across Non-Specific 1000-gene datasets

Latent variables: metric=DELTA_RECALL_AT_K_VS_BASELINE, negative_protocol=full_candidate, network_group=Non-Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.0231** |
| baseline | 0.0000 |
| scGPT_human | <span style="color:red"><strong>0.0330</strong></span> |
| v4_bias_rec_best | **0.0104** |
| v4_plain_best | **0.0187** |
| v4_type_pe_best | **0.0230** |
| scconcept | -0.0816 |
| scconcept_encoded | -0.1151 |
| cl_scratch_v5 | **0.0262** |
| cl_v6_fair | **0.0019** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | <span style="color:red"><strong>0.0210</strong></span> | 0.0000 | <span style="color:red"><strong>0.0140</strong></span> | -0.0448 | **0.0191** | **0.0303** | **0.0027** | **0.0403** | -0.0194 | <span style="color:red"><strong>0.0645</strong></span> | <span style="color:red"><strong>0.0507</strong></span> | **0.0147** |
| baseline | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| scGPT_human | **0.0042** | <span style="color:red"><strong>0.1406</strong></span> | -0.0023 | <span style="color:red"><strong>0.0075</strong></span> | -0.0167 | **0.0909** | -0.0215 | <span style="color:red"><strong>0.0887</strong></span> | <span style="color:red"><strong>0.0194</strong></span> | **0.0323** | **0.0473** | **0.0147** |
| v4_bias_rec_best | -0.0000 | -0.0156 | **0.0047** | -0.0448 | -0.0144 | **0.0152** | -0.0108 | **0.0484** | -0.0581 | <span style="color:red"><strong>0.0645</strong></span> | **0.0068** | **0.0882** |
| v4_plain_best | -0.0084 | **0.0156** | -0.0186 | -0.0896 | -0.0144 | <span style="color:red"><strong>0.1212</strong></span> | **0.0027** | **0.0081** | **0.0078** | **0.0323** | **0.0101** | **0.0294** |
| v4_type_pe_best | **0.0168** | 0.0000 | -0.0070 | -0.0149 | **0.0120** | **0.0303** | 0.0000 | **0.0565** | **0.0039** | **0.0000** | **0.0236** | <span style="color:red"><strong>0.1029</strong></span> |
| scconcept | -0.1933 | **0.0156** | -0.1581 | -0.3582 | -0.1866 | -0.2576 | -0.2957 | -0.3387 | -0.2519 | -0.1935 | -0.1791 | -0.1471 |
| scconcept_encoded | -0.2101 | -0.0312 | -0.2721 | -0.3507 | -0.1794 | -0.3182 | -0.3038 | -0.3629 | -0.2829 | -0.1452 | -0.2534 | -0.1618 |
| cl_scratch_v5 | -0.0042 | **0.0312** | -0.0023 | -0.0672 | **0.0167** | **0.0909** | <span style="color:red"><strong>0.0134</strong></span> | <span style="color:red"><strong>0.0887</strong></span> | **0.0155** | -0.0323 | **0.0068** | **0.0441** |
| cl_v6_fair | **0.0084** | **0.0625** | -0.0116 | -0.0672 | <span style="color:red"><strong>0.0383</strong></span> | **0.0758** | -0.0054 | **0.0161** | **0.0078** | -0.0484 | **0.0236** | **0.0735** |

##### Aggregate mean across STRING 500-gene datasets

Latent variables: metric=DELTA_RECALL_AT_K_VS_BASELINE, negative_protocol=full_candidate, network_group=STRING, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.0175** |
| baseline | 0.0000 |
| scGPT_human | <span style="color:red"><strong>0.0624</strong></span> |
| v4_bias_rec_best | **0.0260** |
| v4_plain_best | **0.0195** |
| v4_type_pe_best | **0.0291** |
| scconcept | -0.2132 |
| scconcept_encoded | -0.2283 |
| cl_scratch_v5 | **0.0259** |
| cl_v6_fair | **0.0187** |

##### Aggregate mean across STRING 1000-gene datasets

Latent variables: metric=DELTA_RECALL_AT_K_VS_BASELINE, negative_protocol=full_candidate, network_group=STRING, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | <span style="color:red"><strong>0.0147</strong></span> |
| baseline | 0.0000 |
| scGPT_human | **0.0051** |
| v4_bias_rec_best | -0.0120 |
| v4_plain_best | -0.0035 |
| v4_type_pe_best | **0.0082** |
| scconcept | -0.2108 |
| scconcept_encoded | -0.2503 |
| cl_scratch_v5 | **0.0077** |
| cl_v6_fair | **0.0102** |

