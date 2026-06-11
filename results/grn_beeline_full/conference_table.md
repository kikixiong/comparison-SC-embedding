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
| baseline | <span style="color:red"><strong>0.7217</strong></span> | 0.6884 | 0.8645 | 0.7041 | <span style="color:red"><strong>0.6492</strong></span> | 0.8327 | 0.7802 | 0.8135 | 0.7479 | 0.8154 | 0.7720 |
| scGPT_human | 0.7086 | 0.6812 | 0.8379 | 0.6972 | 0.5750 | 0.8254 | 0.7571 | 0.8116 | **0.7670** | <span style="color:red"><strong>0.8275</strong></span> | 0.7698 |
| v4_bias_rec_best | 0.7042 | 0.6717 | 0.8591 | 0.6940 | 0.3836 | **0.8333** | 0.7745 | **0.8163** | <span style="color:red"><strong>0.7883</strong></span> | **0.8217** | **0.7779** |
| v4_plain_best | 0.7120 | 0.6567 | 0.8580 | **0.7180** | 0.6016 | 0.8305 | 0.7528 | **0.8176** | **0.7522** | **0.8193** | **0.7916** |
| v4_type_pe_best | 0.7116 | <span style="color:red"><strong>0.7099</strong></span> | 0.8596 | 0.6987 | 0.5125 | 0.8325 | <span style="color:red"><strong>0.7957</strong></span> | **0.8163** | **0.7601** | **0.8248** | **0.7855** |
| scconcept | 0.6249 | 0.6441 | 0.7970 | 0.6512 | 0.4531 | 0.8021 | 0.7257 | 0.7707 | 0.7090 | 0.8121 | 0.7066 |
| scconcept_encoded | 0.6572 | 0.6381 | 0.7945 | 0.6816 | 0.4297 | 0.7990 | 0.7435 | 0.7700 | 0.7272 | 0.7935 | 0.7046 |
| cl_scratch_v5 | 0.6992 | **0.6986** | 0.8587 | <span style="color:red"><strong>0.7196</strong></span> | 0.5398 | 0.8291 | **0.7890** | **0.8167** | **0.7752** | **0.8192** | **0.7727** |
| cl_v6_fair | 0.6857 | 0.6422 | 0.8591 | **0.7175** | 0.5547 | 0.8322 | 0.7744 | **0.8198** | **0.7791** | **0.8198** | **0.7767** |
| cl_v6_tau01 | 0.6874 | 0.6675 | 0.8637 | 0.6998 | 0.5281 | 0.8303 | **0.7819** | **0.8222** | **0.7757** | **0.8208** | **0.7826** |
| cl_v6_tau02 | 0.6891 | 0.6551 | 0.8600 | **0.7127** | 0.5055 | **0.8342** | **0.7832** | **0.8215** | **0.7824** | **0.8224** | **0.7837** |
| cl_v6_tau03 | 0.6881 | 0.6517 | 0.8622 | **0.7081** | 0.5172 | 0.8282 | **0.7933** | **0.8159** | **0.7827** | **0.8212** | **0.7844** |
| cl_v7_fair | 0.6909 | 0.6700 | <span style="color:red"><strong>0.8652</strong></span> | **0.7094** | 0.4914 | 0.8312 | **0.7889** | **0.8184** | **0.7750** | **0.8190** | **0.7791** |

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
| cl_v6_tau01 | 0.7072 |
| cl_v6_tau02 | 0.7020 |
| cl_v6_tau03 | 0.7058 |
| cl_v7_fair | 0.7009 |

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
| cl_v6_tau01 | 0.7874 |
| cl_v6_tau02 | 0.7900 |
| cl_v6_tau03 | 0.7873 |
| cl_v7_fair | 0.7890 |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.6678 | 0.6145 | **0.6785** | **0.7065** | **0.7966** | 0.6132 | 0.7799 | 0.7200 | **0.7364** | 0.6205 | **0.7315** | 0.6830 |
| baseline | 0.6683 | 0.6235 | 0.6782 | 0.6607 | 0.7864 | 0.7388 | <span style="color:red"><strong>0.7976</strong></span> | 0.7327 | 0.7245 | 0.6547 | 0.7229 | 0.6925 |
| scGPT_human | 0.6394 | **0.6331** | <span style="color:red"><strong>0.7047</strong></span> | **0.7178** | 0.7677 | 0.6963 | 0.7678 | <span style="color:red"><strong>0.7780</strong></span> | **0.7425** | <span style="color:red"><strong>0.7107</strong></span> | **0.7426** | **0.7174** |
| v4_bias_rec_best | 0.6350 | 0.5756 | 0.6679 | **0.6845** | 0.7839 | 0.7190 | 0.7726 | **0.7568** | **0.7541** | **0.6702** | **0.7297** | **0.6998** |
| v4_plain_best | 0.6640 | <span style="color:red"><strong>0.6442</strong></span> | **0.6991** | **0.6951** | <span style="color:red"><strong>0.8062</strong></span> | 0.7326 | 0.7749 | **0.7599** | 0.6902 | 0.6280 | 0.7005 | **0.7219** |
| v4_type_pe_best | <span style="color:red"><strong>0.6829</strong></span> | 0.5817 | 0.6591 | 0.5546 | **0.7981** | 0.7190 | 0.7825 | 0.7305 | **0.7491** | 0.6281 | **0.7483** | <span style="color:red"><strong>0.7597</strong></span> |
| scconcept | 0.5374 | 0.5681 | 0.5923 | 0.5559 | 0.6508 | 0.5157 | 0.6326 | 0.5130 | 0.6633 | **0.6696** | 0.6536 | 0.5894 |
| scconcept_encoded | 0.5441 | 0.5226 | 0.6119 | 0.5181 | 0.6020 | 0.6260 | 0.6527 | 0.5934 | 0.6461 | 0.5951 | 0.6946 | 0.5888 |
| cl_scratch_v5 | 0.6626 | 0.5998 | **0.6847** | **0.6853** | **0.7973** | 0.6744 | 0.7851 | 0.7154 | **0.7558** | 0.6334 | **0.7442** | **0.7309** |
| cl_v6_fair | 0.6609 | 0.5781 | 0.6679 | 0.5647 | **0.8042** | <span style="color:red"><strong>0.7475</strong></span> | 0.7810 | **0.7458** | <span style="color:red"><strong>0.7587</strong></span> | 0.6300 | **0.7397** | **0.6989** |
| cl_v6_tau01 | **0.6725** | 0.5942 | 0.6757 | **0.7112** | **0.7956** | 0.6897 | 0.7937 | **0.7563** | **0.7573** | 0.6448 | <span style="color:red"><strong>0.7506</strong></span> | **0.7018** |
| cl_v6_tau02 | 0.6617 | 0.5574 | 0.6747 | <span style="color:red"><strong>0.7255</strong></span> | 0.7845 | 0.6876 | 0.7888 | **0.7457** | **0.7518** | 0.6526 | **0.7500** | **0.6963** |
| cl_v6_tau03 | 0.6638 | 0.5690 | 0.6671 | **0.7173** | **0.8019** | 0.7025 | 0.7822 | 0.7280 | **0.7402** | 0.6349 | **0.7475** | 0.6922 |
| cl_v7_fair | 0.6473 | 0.5703 | 0.6611 | **0.7054** | **0.8045** | 0.6777 | 0.7911 | **0.7611** | **0.7554** | 0.6545 | **0.7456** | **0.7059** |

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
| cl_v6_tau01 | 0.6830 |
| cl_v6_tau02 | 0.6775 |
| cl_v6_tau03 | 0.6740 |
| cl_v7_fair | 0.6791 |

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
| cl_scratch_v5 | **0.7383** |
| cl_v6_fair | **0.7354** |
| cl_v6_tau01 | <span style="color:red"><strong>0.7409</strong></span> |
| cl_v6_tau02 | **0.7352** |
| cl_v6_tau03 | **0.7338** |
| cl_v7_fair | **0.7342** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.8007 | 0.6105 | **0.8814** | **0.9081** | **0.8829** | **0.7928** | **0.9037** | <span style="color:red"><strong>0.9210</strong></span> | 0.8391 | **0.8363** | 0.8201 | **0.8423** |
| baseline | 0.8066 | 0.6697 | 0.8689 | 0.9048 | 0.8765 | 0.7720 | 0.8907 | 0.8952 | 0.8664 | 0.7448 | 0.8325 | 0.8173 |
| scGPT_human | <span style="color:red"><strong>0.8403</strong></span> | <span style="color:red"><strong>0.7591</strong></span> | **0.8775** | **0.9115** | 0.8633 | <span style="color:red"><strong>0.8710</strong></span> | **0.9003** | **0.9208** | **0.8705** | **0.7589** | **0.8475** | 0.8067 |
| v4_bias_rec_best | 0.8007 | **0.6981** | **0.8769** | 0.9038 | 0.8644 | **0.8612** | **0.9050** | 0.8877 | 0.8490 | **0.8254** | **0.8441** | <span style="color:red"><strong>0.8565</strong></span> |
| v4_plain_best | 0.7803 | **0.6944** | **0.8735** | **0.9086** | **0.8800** | **0.7966** | **0.8976** | **0.8962** | 0.8330 | **0.7636** | **0.8346** | **0.8274** |
| v4_type_pe_best | **0.8270** | **0.7240** | <span style="color:red"><strong>0.8827</strong></span> | **0.9121** | <span style="color:red"><strong>0.8926</strong></span> | **0.7842** | **0.9122** | 0.8827 | 0.8628 | <span style="color:red"><strong>0.8374</strong></span> | <span style="color:red"><strong>0.8559</strong></span> | **0.8349** |
| scconcept | 0.6642 | **0.7209** | 0.7761 | 0.7654 | 0.7643 | 0.6176 | 0.7623 | 0.7145 | 0.7043 | 0.5745 | 0.7065 | 0.7011 |
| scconcept_encoded | 0.6473 | **0.6960** | 0.7672 | 0.6745 | 0.7460 | 0.6478 | 0.6898 | 0.6649 | 0.6809 | 0.5950 | 0.7030 | 0.6732 |
| cl_scratch_v5 | **0.8099** | 0.6685 | **0.8826** | **0.9069** | **0.8855** | 0.7654 | **0.8924** | **0.9093** | <span style="color:red"><strong>0.8758</strong></span> | **0.7874** | **0.8526** | **0.8363** |
| cl_v6_fair | **0.8181** | **0.6807** | **0.8752** | 0.9041 | 0.8752 | **0.7963** | **0.9055** | **0.9118** | 0.8617 | **0.7956** | **0.8386** | **0.8439** |
| cl_v6_tau01 | 0.7964 | **0.6723** | **0.8783** | **0.9135** | **0.8817** | **0.7753** | <span style="color:red"><strong>0.9146</strong></span> | **0.9072** | **0.8674** | **0.7831** | **0.8371** | **0.8352** |
| cl_v6_tau02 | 0.8061 | 0.6695 | **0.8791** | <span style="color:red"><strong>0.9172</strong></span> | 0.8738 | 0.7689 | **0.9086** | **0.9074** | 0.8555 | **0.7978** | **0.8416** | **0.8375** |
| cl_v6_tau03 | 0.8040 | **0.6769** | **0.8791** | **0.9135** | 0.8759 | **0.7793** | **0.9048** | **0.9052** | 0.8609 | **0.8024** | **0.8472** | **0.8374** |
| cl_v7_fair | **0.8216** | **0.6730** | **0.8772** | **0.9097** | **0.8832** | **0.8026** | **0.9073** | **0.9067** | 0.8650 | **0.7808** | **0.8452** | **0.8426** |

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
| cl_v6_tau01 | **0.8144** |
| cl_v6_tau02 | **0.8164** |
| cl_v6_tau03 | **0.8191** |
| cl_v7_fair | **0.8192** |

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
| cl_v6_tau01 | **0.8626** |
| cl_v6_tau02 | **0.8608** |
| cl_v6_tau03 | **0.8620** |
| cl_v7_fair | **0.8666** |

### Negative protocol: full_candidate

Latent variables: metric=AUROC, negative_protocol=full_candidate, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.8420 | 0.7997 | 0.8916 | 0.8154 | 0.7021 | **0.8983** | 0.8177 | **0.8736** | **0.7732** | <span style="color:red"><strong>0.8702</strong></span> | **0.7957** |
| baseline | 0.8548 | <span style="color:red"><strong>0.8241</strong></span> | 0.8973 | 0.8366 | 0.8515 | 0.8926 | 0.8321 | 0.8724 | 0.7633 | 0.8587 | 0.7857 |
| scGPT_human | 0.8420 | 0.8024 | 0.8779 | 0.8366 | 0.7912 | **0.8967** | 0.8032 | 0.8708 | 0.7590 | **0.8598** | 0.7696 |
| v4_bias_rec_best | 0.8547 | 0.8159 | **0.8983** | 0.8123 | 0.6732 | **0.8996** | **0.8329** | 0.8667 | **0.7805** | 0.8583 | 0.7799 |
| v4_plain_best | 0.8532 | 0.8090 | **0.8988** | 0.8087 | <span style="color:red"><strong>0.8517</strong></span> | **0.8992** | 0.8306 | **0.8737** | 0.7602 | **0.8604** | 0.7842 |
| v4_type_pe_best | <span style="color:red"><strong>0.8608</strong></span> | 0.8161 | **0.8976** | 0.8174 | 0.7654 | **0.8963** | **0.8330** | 0.8722 | 0.7614 | **0.8608** | <span style="color:red"><strong>0.7959</strong></span> |
| scconcept | 0.8265 | 0.8039 | 0.8424 | 0.7669 | 0.6766 | 0.8792 | 0.7806 | 0.8482 | 0.7263 | 0.8427 | 0.7158 |
| scconcept_encoded | 0.8312 | 0.7982 | 0.8410 | 0.8195 | 0.6115 | 0.8797 | 0.8003 | 0.8511 | 0.7275 | 0.8411 | 0.7136 |
| cl_scratch_v5 | 0.8357 | 0.8085 | 0.8958 | 0.8342 | 0.6906 | **0.8976** | **0.8394** | **0.8744** | **0.7682** | **0.8597** | 0.7787 |
| cl_v6_fair | 0.8486 | 0.7884 | **0.8978** | <span style="color:red"><strong>0.8556</strong></span> | 0.6337 | **0.9014** | <span style="color:red"><strong>0.8424</strong></span> | **0.8758** | **0.7851** | **0.8616** | **0.7865** |
| cl_v6_tau01 | 0.8501 | 0.7954 | **0.8981** | **0.8466** | 0.6317 | <span style="color:red"><strong>0.9020</strong></span> | **0.8414** | **0.8761** | **0.7857** | **0.8625** | 0.7773 |
| cl_v6_tau02 | 0.8512 | 0.7893 | 0.8926 | **0.8443** | 0.6541 | **0.8987** | 0.8321 | **0.8774** | **0.7834** | **0.8630** | 0.7834 |
| cl_v6_tau03 | 0.8510 | 0.7851 | **0.8977** | **0.8378** | 0.6141 | **0.8999** | 0.8306 | **0.8768** | <span style="color:red"><strong>0.7893</strong></span> | **0.8646** | **0.7865** |
| cl_v7_fair | 0.8511 | 0.7994 | <span style="color:red"><strong>0.8996</strong></span> | 0.8356 | 0.6712 | **0.8970** | **0.8414** | <span style="color:red"><strong>0.8784</strong></span> | **0.7797** | **0.8640** | 0.7833 |

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
| cl_v6_tau01 | 0.7663 |
| cl_v6_tau02 | 0.7685 |
| cl_v6_tau03 | 0.7611 |
| cl_v7_fair | 0.7750 |

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
| cl_v6_tau01 | **0.8726** |
| cl_v6_tau02 | **0.8712** |
| cl_v6_tau03 | **0.8713** |
| cl_v7_fair | **0.8710** |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.8906** | **0.8460** | <span style="color:red"><strong>0.8513</strong></span> | <span style="color:red"><strong>0.8318</strong></span> | **0.8732** | **0.6444** | **0.8718** | **0.8408** | 0.8301 | 0.7985 | 0.8247 | **0.8292** |
| baseline | 0.8865 | 0.8450 | 0.8405 | 0.7533 | 0.8687 | 0.6128 | 0.8697 | 0.8306 | 0.8431 | 0.8032 | 0.8384 | 0.7872 |
| scGPT_human | 0.8661 | **0.8584** | 0.8369 | **0.8094** | 0.8545 | <span style="color:red"><strong>0.7449</strong></span> | 0.8611 | **0.8579** | 0.8410 | 0.8030 | 0.8383 | **0.8484** |
| v4_bias_rec_best | 0.8778 | 0.8418 | 0.8214 | **0.7937** | 0.8635 | **0.6719** | 0.8587 | <span style="color:red"><strong>0.8646</strong></span> | **0.8508** | <span style="color:red"><strong>0.8315</strong></span> | 0.8242 | **0.8423** |
| v4_plain_best | **0.8984** | **0.8665** | **0.8497** | **0.7972** | **0.8748** | **0.6904** | 0.8663 | **0.8423** | **0.8482** | 0.7833 | 0.8269 | <span style="color:red"><strong>0.8491</strong></span> |
| v4_type_pe_best | **0.8964** | <span style="color:red"><strong>0.8680</strong></span> | **0.8466** | **0.7722** | 0.8680 | **0.6781** | 0.8651 | 0.8206 | **0.8598** | 0.7935 | **0.8449** | **0.8336** |
| scconcept | 0.8412 | 0.8381 | 0.7886 | **0.7818** | 0.7650 | 0.5705 | 0.7993 | 0.7146 | 0.7988 | 0.7612 | 0.8093 | 0.7455 |
| scconcept_encoded | 0.8456 | 0.7989 | 0.7940 | 0.7166 | 0.7387 | **0.6547** | 0.8008 | 0.7486 | 0.7631 | 0.7112 | 0.7802 | 0.7335 |
| cl_scratch_v5 | **0.8901** | **0.8568** | 0.8258 | 0.7512 | <span style="color:red"><strong>0.8776</strong></span> | **0.6580** | **0.8698** | **0.8419** | **0.8505** | 0.7774 | **0.8441** | **0.8141** |
| cl_v6_fair | **0.8931** | **0.8531** | 0.8306 | **0.7725** | **0.8715** | **0.6627** | **0.8713** | **0.8505** | <span style="color:red"><strong>0.8620</strong></span> | 0.7811 | **0.8546** | **0.8229** |
| cl_v6_tau01 | <span style="color:red"><strong>0.8986</strong></span> | **0.8538** | 0.8200 | **0.7999** | 0.8660 | **0.6514** | 0.8686 | **0.8597** | **0.8601** | 0.7768 | **0.8456** | **0.8235** |
| cl_v6_tau02 | **0.8958** | **0.8454** | **0.8432** | **0.8059** | 0.8669 | **0.6562** | <span style="color:red"><strong>0.8741</strong></span> | **0.8507** | **0.8514** | 0.7835 | **0.8509** | **0.8302** |
| cl_v6_tau03 | **0.8945** | 0.8437 | 0.8209 | **0.8083** | **0.8727** | **0.6638** | 0.8687 | **0.8539** | **0.8544** | 0.7807 | <span style="color:red"><strong>0.8551</strong></span> | **0.8291** |
| cl_v7_fair | **0.8935** | **0.8557** | 0.8167 | **0.7683** | **0.8765** | **0.6417** | **0.8706** | **0.8578** | **0.8541** | 0.7774 | **0.8524** | **0.8233** |

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
| cl_v6_tau01 | **0.7942** |
| cl_v6_tau02 | **0.7953** |
| cl_v6_tau03 | **0.7966** |
| cl_v7_fair | **0.7874** |

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
| cl_v6_tau01 | **0.8598** |
| cl_v6_tau02 | **0.8637** |
| cl_v6_tau03 | **0.8611** |
| cl_v7_fair | **0.8606** |

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
| cl_v6_fair | **0.8491** | 0.7684 | 0.8905 | 0.9004 | 0.8945 | <span style="color:red"><strong>0.8980</strong></span> | **0.8921** | 0.9070 | 0.8707 | 0.8068 | **0.8690** | **0.8714** |
| cl_v6_tau01 | 0.8106 | 0.7613 | **0.8960** | 0.9087 | 0.9024 | **0.8856** | **0.8972** | **0.9183** | 0.8752 | 0.8144 | **0.8745** | **0.8569** |
| cl_v6_tau02 | 0.8194 | 0.7698 | **0.8918** | 0.8978 | 0.8993 | **0.8813** | **0.8992** | **0.9178** | 0.8701 | 0.8159 | **0.8713** | **0.8593** |
| cl_v6_tau03 | 0.8363 | 0.7699 | 0.8864 | 0.9034 | **0.9032** | **0.8908** | **0.9025** | **0.9127** | 0.8702 | 0.8147 | **0.8774** | **0.8605** |
| cl_v7_fair | 0.8483 | 0.7633 | **0.8961** | 0.9054 | 0.8948 | **0.8937** | **0.8902** | 0.9016 | 0.8674 | 0.8139 | **0.8777** | <span style="color:red"><strong>0.8787</strong></span> |

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
| cl_v6_tau01 | 0.8575 |
| cl_v6_tau02 | 0.8570 |
| cl_v6_tau03 | **0.8587** |
| cl_v7_fair | **0.8594** |

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
| cl_v6_tau01 | 0.8760 |
| cl_v6_tau02 | 0.8752 |
| cl_v6_tau03 | **0.8793** |
| cl_v7_fair | **0.8791** |

## AUPRC (Main)

### Negative protocol: tf_stratified_1to10

Latent variables: metric=AUPRC, negative_protocol=tf_stratified_1to10, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.4650 | 0.3945 | 0.7451 | **0.3619** | 0.1333 | 0.8919 | 0.7811 | **0.8685** | **0.8067** | <span style="color:red"><strong>0.8898</strong></span> | <span style="color:red"><strong>0.8501</strong></span> |
| baseline | <span style="color:red"><strong>0.4835</strong></span> | 0.4243 | 0.7670 | 0.3602 | 0.1704 | 0.8923 | 0.7898 | 0.8572 | 0.7764 | 0.8772 | 0.8176 |
| scGPT_human | 0.4802 | **0.4285** | 0.7351 | 0.3572 | <span style="color:red"><strong>0.2207</strong></span> | 0.8837 | 0.7621 | 0.8556 | **0.7924** | **0.8894** | **0.8225** |
| v4_bias_rec_best | 0.4585 | 0.4214 | 0.7518 | **0.3826** | 0.0860 | 0.8908 | 0.7745 | **0.8638** | **0.7960** | **0.8811** | **0.8260** |
| v4_plain_best | 0.4798 | 0.4018 | 0.7629 | **0.3959** | **0.1827** | 0.8894 | 0.7579 | **0.8621** | **0.7821** | **0.8782** | **0.8421** |
| v4_type_pe_best | 0.4798 | **0.4297** | 0.7618 | **0.3605** | 0.1540 | 0.8917 | <span style="color:red"><strong>0.7987</strong></span> | **0.8601** | **0.7913** | **0.8867** | **0.8339** |
| scconcept | 0.3888 | 0.3954 | 0.6809 | 0.3012 | **0.2064** | 0.8665 | 0.7010 | 0.8135 | 0.7500 | 0.8733 | 0.7585 |
| scconcept_encoded | 0.4057 | 0.3606 | 0.6534 | 0.2921 | 0.0943 | 0.8606 | 0.7328 | 0.8178 | 0.7561 | 0.8560 | 0.7590 |
| cl_scratch_v5 | 0.4542 | <span style="color:red"><strong>0.4427</strong></span> | 0.7550 | **0.3953** | 0.1421 | 0.8897 | 0.7853 | **0.8648** | **0.8056** | **0.8809** | **0.8183** |
| cl_v6_fair | 0.4322 | 0.3744 | **0.7685** | **0.3948** | 0.1392 | <span style="color:red"><strong>0.8937</strong></span> | 0.7747 | **0.8656** | <span style="color:red"><strong>0.8129</strong></span> | **0.8823** | **0.8271** |
| cl_v6_tau01 | 0.4456 | 0.3983 | **0.7732** | **0.3954** | 0.1678 | 0.8922 | 0.7815 | <span style="color:red"><strong>0.8703</strong></span> | **0.8053** | **0.8825** | **0.8309** |
| cl_v6_tau02 | 0.4458 | 0.3908 | 0.7598 | <span style="color:red"><strong>0.3984</strong></span> | 0.1380 | **0.8936** | 0.7796 | **0.8697** | **0.8083** | **0.8842** | **0.8336** |
| cl_v6_tau03 | 0.4329 | 0.3819 | **0.7687** | **0.3870** | 0.1296 | 0.8897 | **0.7922** | **0.8660** | **0.8080** | **0.8831** | **0.8365** |
| cl_v7_fair | 0.4390 | 0.4043 | <span style="color:red"><strong>0.7788</strong></span> | **0.3808** | 0.1277 | **0.8927** | **0.7908** | **0.8659** | **0.8066** | **0.8811** | **0.8311** |

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
| cl_v6_tau01 | **0.5968** |
| cl_v6_tau02 | 0.5901 |
| cl_v6_tau03 | 0.5896 |
| cl_v7_fair | 0.5921 |

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
| cl_v6_tau01 | **0.7099** |
| cl_v6_tau02 | **0.7086** |
| cl_v6_tau03 | 0.7046 |
| cl_v7_fair | **0.7064** |

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
| cl_v6_tau01 | **0.2379** | 0.1749 | **0.2857** | **0.2841** | **0.4118** | 0.3968 | **0.3667** | **0.3481** | **0.3663** | 0.2331 | **0.3309** | **0.2852** |
| cl_v6_tau02 | **0.2413** | 0.1654 | **0.2825** | **0.2747** | 0.3634 | 0.3839 | 0.3567 | **0.3421** | **0.3632** | 0.2413 | **0.3215** | 0.2550 |
| cl_v6_tau03 | 0.2274 | 0.1653 | 0.2769 | **0.2660** | **0.4114** | 0.3779 | 0.3474 | 0.3293 | **0.3499** | 0.2252 | **0.3193** | 0.2719 |
| cl_v7_fair | 0.2169 | 0.1730 | 0.2693 | **0.2737** | **0.4179** | 0.3668 | **0.3703** | **0.3474** | **0.3566** | 0.2741 | **0.3169** | 0.2676 |

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
| cl_v6_tau01 | 0.2870 |
| cl_v6_tau02 | 0.2771 |
| cl_v6_tau03 | 0.2726 |
| cl_v7_fair | 0.2838 |

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
| cl_v6_tau01 | **0.3332** |
| cl_v6_tau02 | **0.3214** |
| cl_v6_tau03 | **0.3221** |
| cl_v7_fair | **0.3246** |

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
| cl_v6_tau01 | 0.3934 | **0.3623** | 0.5159 | **0.6023** | 0.5571 | **0.3904** | **0.6221** | 0.6181 | 0.5389 | **0.3336** | **0.5000** | **0.5091** |
| cl_v6_tau02 | 0.4056 | **0.3334** | 0.5293 | **0.5988** | 0.5375 | **0.3854** | 0.6112 | **0.6543** | 0.5092 | **0.3683** | **0.5127** | **0.5089** |
| cl_v6_tau03 | 0.4081 | **0.3390** | 0.5263 | 0.5787 | 0.5362 | **0.3949** | 0.6147 | 0.6240 | 0.5237 | **0.3737** | **0.4998** | **0.5112** |
| cl_v7_fair | **0.4407** | **0.3297** | 0.5224 | 0.5748 | **0.5732** | **0.4346** | 0.6134 | **0.6362** | 0.5277 | **0.3436** | **0.4917** | **0.5074** |

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
| cl_v6_tau01 | **0.4693** |
| cl_v6_tau02 | **0.4748** |
| cl_v6_tau03 | **0.4703** |
| cl_v7_fair | **0.4711** |

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
| cl_v6_tau01 | 0.5212 |
| cl_v6_tau02 | 0.5176 |
| cl_v6_tau03 | 0.5181 |
| cl_v7_fair | 0.5282 |

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
| cl_scratch_v5 | 0.4514 | 0.4189 | 0.7645 | 0.3663 | 0.1078 | **0.8887** | **0.7903** | **0.8637** | 0.7899 | **0.8830** | **0.8318** |
| cl_v6_fair | 0.4509 | 0.3830 | **0.7690** | <span style="color:red"><strong>0.4064</strong></span> | 0.1044 | **0.8968** | **0.7897** | **0.8655** | <span style="color:red"><strong>0.8147</strong></span> | **0.8842** | **0.8361** |
| cl_v6_tau01 | 0.4536 | 0.3956 | **0.7763** | **0.3996** | 0.1299 | <span style="color:red"><strong>0.8969</strong></span> | <span style="color:red"><strong>0.7927</strong></span> | **0.8655** | **0.8133** | **0.8891** | 0.8261 |
| cl_v6_tau02 | **0.4602** | 0.3959 | 0.7578 | 0.3844 | 0.1293 | **0.8911** | **0.7784** | <span style="color:red"><strong>0.8690</strong></span> | **0.8090** | **0.8866** | **0.8316** |
| cl_v6_tau03 | 0.4494 | 0.3842 | **0.7774** | 0.3647 | 0.0932 | **0.8939** | **0.7787** | **0.8684** | **0.8144** | **0.8913** | **0.8384** |
| cl_v7_fair | 0.4529 | 0.3881 | **0.7780** | 0.3769 | 0.0842 | **0.8892** | **0.7898** | **0.8681** | **0.8102** | **0.8893** | **0.8332** |

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
| cl_v6_tau01 | 0.5915 |
| cl_v6_tau02 | 0.5888 |
| cl_v6_tau03 | 0.5818 |
| cl_v7_fair | 0.5811 |

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
| cl_v6_fair | **0.7121** |
| cl_v6_tau01 | <span style="color:red"><strong>0.7135</strong></span> |
| cl_v6_tau02 | **0.7082** |
| cl_v6_tau03 | **0.7075** |
| cl_v7_fair | **0.7091** |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.1548** | 0.2019 | **0.1446** | **0.1237** | **0.2209** | **0.1332** | **0.2591** | **0.2519** | <span style="color:red"><strong>0.2683</strong></span> | 0.1488 | **0.2069** | **0.1677** |
| baseline | 0.1545 | <span style="color:red"><strong>0.2235</strong></span> | 0.1155 | 0.0906 | 0.1818 | 0.1265 | 0.2530 | 0.2107 | 0.2330 | 0.1621 | 0.1758 | 0.1387 |
| scGPT_human | 0.1514 | 0.2007 | <span style="color:red"><strong>0.2079</strong></span> | <span style="color:red"><strong>0.1301</strong></span> | <span style="color:red"><strong>0.2389</strong></span> | 0.0798 | **0.2567** | **0.2685** | **0.2600** | <span style="color:red"><strong>0.2106</strong></span> | **0.2007** | <span style="color:red"><strong>0.3169</strong></span> |
| v4_bias_rec_best | 0.1514 | 0.1783 | 0.1020 | **0.1244** | 0.1786 | 0.1227 | 0.2232 | **0.2353** | **0.2507** | 0.1573 | 0.1574 | **0.2603** |
| v4_plain_best | **0.1676** | 0.1891 | **0.1222** | **0.1270** | **0.2157** | 0.0791 | 0.2217 | 0.1853 | **0.2580** | 0.1506 | <span style="color:red"><strong>0.2341</strong></span> | **0.2768** |
| v4_type_pe_best | <span style="color:red"><strong>0.1715</strong></span> | 0.2045 | **0.1448** | **0.1047** | 0.1798 | 0.1172 | 0.2429 | **0.2299** | **0.2551** | **0.1991** | **0.2087** | **0.2655** |
| scconcept | 0.1303 | 0.1346 | 0.0736 | 0.0760 | 0.1067 | 0.0653 | 0.0797 | 0.0703 | 0.1017 | 0.0972 | 0.0989 | 0.0883 |
| scconcept_encoded | 0.1120 | 0.0925 | 0.0645 | 0.0473 | 0.0749 | 0.0233 | 0.0758 | 0.0824 | 0.0711 | 0.0721 | 0.0753 | 0.0888 |
| cl_scratch_v5 | **0.1668** | 0.2183 | **0.1643** | **0.1012** | **0.2320** | **0.1342** | <span style="color:red"><strong>0.2738</strong></span> | **0.2562** | **0.2407** | 0.1296 | **0.1908** | **0.2543** |
| cl_v6_fair | **0.1589** | 0.1989 | **0.1262** | **0.1282** | **0.1946** | <span style="color:red"><strong>0.1916</strong></span> | 0.2241 | **0.2202** | 0.2285 | 0.1508 | **0.1983** | **0.2819** |
| cl_v6_tau01 | **0.1570** | 0.1990 | **0.1561** | **0.1234** | **0.1894** | **0.1731** | 0.2496 | **0.2347** | **0.2430** | 0.1424 | **0.2027** | **0.2493** |
| cl_v6_tau02 | **0.1560** | 0.2061 | **0.1369** | **0.1008** | **0.2220** | **0.1633** | **0.2531** | <span style="color:red"><strong>0.2687</strong></span> | **0.2468** | **0.1654** | **0.1970** | **0.2913** |
| cl_v6_tau03 | **0.1588** | 0.1810 | **0.1564** | **0.1182** | **0.2307** | **0.1571** | 0.2522 | **0.2589** | **0.2374** | 0.1528 | **0.1878** | **0.2856** |
| cl_v7_fair | **0.1564** | 0.1960 | **0.1425** | **0.1196** | **0.2065** | 0.1155 | 0.2441 | **0.2451** | 0.2252 | **0.1770** | 0.1725 | **0.2394** |

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
| cl_v6_tau01 | **0.1870** |
| cl_v6_tau02 | **0.1993** |
| cl_v6_tau03 | **0.1923** |
| cl_v7_fair | **0.1821** |

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
| cl_v6_tau01 | **0.1996** |
| cl_v6_tau02 | **0.2020** |
| cl_v6_tau03 | **0.2039** |
| cl_v7_fair | **0.1912** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | <span style="color:red"><strong>0.2633</strong></span> | 0.1699 | 0.4407 | 0.5099 | 0.4361 | **0.3563** | **0.5105** | **0.5577** | **0.3614** | **0.2107** | <span style="color:red"><strong>0.3464</strong></span> | **0.3080** |
| baseline | 0.2484 | 0.1700 | <span style="color:red"><strong>0.4466</strong></span> | 0.5505 | 0.4565 | 0.3554 | 0.4971 | 0.5255 | 0.3591 | 0.1569 | 0.2994 | 0.2705 |
| scGPT_human | 0.2283 | <span style="color:red"><strong>0.3573</strong></span> | 0.4324 | <span style="color:red"><strong>0.5691</strong></span> | 0.4391 | **0.3946** | **0.5010** | <span style="color:red"><strong>0.6067</strong></span> | **0.3843** | **0.1887** | **0.3409** | **0.3400** |
| v4_bias_rec_best | 0.2085 | 0.1344 | 0.4212 | 0.4852 | 0.4315 | **0.4145** | 0.4764 | **0.5641** | 0.3162 | <span style="color:red"><strong>0.2221</strong></span> | 0.2651 | **0.3476** |
| v4_plain_best | 0.2453 | 0.1652 | 0.4215 | 0.4862 | **0.4592** | <span style="color:red"><strong>0.4771</strong></span> | **0.5005** | **0.5474** | **0.3872** | **0.1908** | **0.3289** | **0.3299** |
| v4_type_pe_best | 0.2393 | 0.1532 | 0.4336 | 0.5148 | <span style="color:red"><strong>0.4832</strong></span> | **0.3867** | 0.4932 | **0.5644** | **0.3800** | **0.1678** | **0.3237** | <span style="color:red"><strong>0.4148</strong></span> |
| scconcept | 0.0477 | 0.1494 | 0.2499 | 0.1498 | 0.2192 | 0.0989 | 0.1407 | 0.1256 | 0.0968 | 0.0506 | 0.0995 | 0.1544 |
| scconcept_encoded | 0.0397 | 0.0820 | 0.1287 | 0.1374 | 0.1909 | 0.0749 | 0.1380 | 0.1323 | 0.0586 | 0.0357 | 0.0422 | 0.1117 |
| cl_scratch_v5 | 0.2191 | 0.1639 | 0.4326 | 0.4888 | 0.4558 | **0.4251** | **0.5021** | **0.5903** | <span style="color:red"><strong>0.3954</strong></span> | 0.1408 | **0.3157** | **0.3411** |
| cl_v6_fair | 0.2400 | 0.1545 | 0.4304 | 0.4661 | **0.4627** | **0.4575** | **0.5070** | 0.5243 | 0.3539 | 0.1503 | **0.3428** | **0.3533** |
| cl_v6_tau01 | 0.2285 | **0.1743** | 0.4253 | 0.4902 | **0.4683** | **0.4552** | <span style="color:red"><strong>0.5226</strong></span> | **0.5761** | **0.3759** | 0.1524 | **0.3359** | **0.3349** |
| cl_v6_tau02 | 0.2419 | 0.1638 | 0.4315 | 0.4796 | **0.4693** | **0.4103** | **0.5153** | **0.5802** | **0.3909** | **0.1650** | **0.3249** | **0.3676** |
| cl_v6_tau03 | 0.2452 | **0.1720** | 0.4330 | 0.4708 | **0.4620** | **0.4380** | 0.4872 | **0.5714** | **0.3755** | 0.1547 | **0.3280** | **0.3869** |
| cl_v7_fair | 0.2385 | 0.1341 | 0.4309 | 0.4973 | **0.4589** | **0.4505** | **0.5072** | 0.5132 | **0.3890** | 0.1526 | **0.3059** | **0.3868** |

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
| cl_v6_tau01 | **0.3639** |
| cl_v6_tau02 | **0.3611** |
| cl_v6_tau03 | **0.3656** |
| cl_v7_fair | **0.3558** |

##### Aggregate mean across STRING 1000-gene datasets

Latent variables: metric=AUPRC, negative_protocol=full_candidate, network_group=STRING, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.3931** |
| baseline | 0.3845 |
| scGPT_human | **0.3877** |
| v4_bias_rec_best | 0.3531 |
| v4_plain_best | **0.3904** |
| v4_type_pe_best | **0.3922** |
| scconcept | 0.1423 |
| scconcept_encoded | 0.0997 |
| cl_scratch_v5 | **0.3868** |
| cl_v6_fair | **0.3895** |
| cl_v6_tau01 | **0.3928** |
| cl_v6_tau02 | <span style="color:red"><strong>0.3956</strong></span> |
| cl_v6_tau03 | **0.3885** |
| cl_v7_fair | **0.3884** |

## AUPRC_LIFT (Main)

AUPRC_LIFT normalizes AUPRC by the random-ranking baseline, which equals the test positive ratio. It indicates how many times better the model ranks true edges compared with random expectation.

### Negative protocol: tf_stratified_1to10

Latent variables: metric=AUPRC_LIFT, negative_protocol=tf_stratified_1to10, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 1.6231 | 1.4798 | 2.3781 | **2.1612** | 1.4666 | 1.4510 | 1.6319 | **1.5025** | **1.4585** | <span style="color:red"><strong>1.4266</strong></span> | <span style="color:red"><strong>1.4437</strong></span> |
| baseline | <span style="color:red"><strong>1.6875</strong></span> | 1.5918 | 2.4479 | 2.1510 | 1.8741 | 1.4517 | 1.6501 | 1.4830 | 1.4038 | 1.4064 | 1.3884 |
| scGPT_human | 1.6759 | **1.6075** | 2.3461 | 2.1330 | <span style="color:red"><strong>2.4280</strong></span> | 1.4376 | 1.5923 | 1.4802 | **1.4326** | **1.4259** | **1.3968** |
| v4_bias_rec_best | 1.6005 | 1.5808 | 2.3994 | **2.2847** | 0.9464 | 1.4492 | 1.6182 | **1.4944** | **1.4391** | **1.4127** | **1.4027** |
| v4_plain_best | 1.6748 | 1.5072 | 2.4350 | **2.3639** | **2.0096** | 1.4469 | 1.5835 | **1.4914** | **1.4141** | **1.4079** | **1.4301** |
| v4_type_pe_best | 1.6745 | **1.6119** | 2.4316 | **2.1530** | 1.6936 | 1.4507 | <span style="color:red"><strong>1.6687</strong></span> | **1.4879** | **1.4308** | **1.4216** | **1.4162** |
| scconcept | 1.3569 | 1.4832 | 2.1732 | 1.7988 | **2.2700** | 1.4096 | 1.4646 | 1.4074 | 1.3560 | 1.4002 | 1.2880 |
| scconcept_encoded | 1.4161 | 1.3528 | 2.0856 | 1.7441 | 1.0371 | 1.4001 | 1.5311 | 1.4149 | 1.3671 | 1.3725 | 1.2889 |
| cl_scratch_v5 | 1.5852 | <span style="color:red"><strong>1.6610</strong></span> | 2.4098 | **2.3603** | 1.5633 | 1.4475 | 1.6408 | **1.4962** | **1.4565** | **1.4124** | **1.3895** |
| cl_v6_fair | 1.5084 | 1.4045 | **2.4527** | **2.3576** | 1.5313 | <span style="color:red"><strong>1.4540</strong></span> | 1.6185 | **1.4975** | <span style="color:red"><strong>1.4697</strong></span> | **1.4145** | **1.4045** |
| cl_v6_tau01 | 1.5554 | 1.4942 | **2.4679** | **2.3613** | 1.8457 | 1.4515 | 1.6328 | <span style="color:red"><strong>1.5056</strong></span> | **1.4561** | **1.4149** | **1.4109** |
| cl_v6_tau02 | 1.5561 | 1.4659 | 2.4251 | <span style="color:red"><strong>2.3791</strong></span> | 1.5184 | **1.4538** | 1.6289 | **1.5046** | **1.4615** | **1.4175** | **1.4157** |
| cl_v6_tau03 | 1.5111 | 1.4327 | **2.4534** | **2.3108** | 1.4254 | 1.4474 | **1.6552** | **1.4981** | **1.4609** | **1.4158** | **1.4205** |
| cl_v7_fair | 1.5324 | 1.5166 | <span style="color:red"><strong>2.4856</strong></span> | **2.2739** | 1.4047 | **1.4523** | **1.6523** | **1.4980** | **1.4583** | **1.4126** | **1.4114** |

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
| cl_v6_tau01 | 1.5679 |
| cl_v6_tau02 | 1.4981 |
| cl_v6_tau03 | 1.4789 |
| cl_v7_fair | 1.4887 |

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
| cl_v6_tau01 | **1.7928** |
| cl_v6_tau02 | **1.7894** |
| cl_v6_tau03 | **1.7728** |
| cl_v7_fair | **1.7758** |

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
| cl_v6_tau01 | **2.0554** | 1.5657 | **3.1429** | **3.1253** | **4.5302** | 4.3652 | **3.7819** | **3.5286** | **3.9116** | 2.5639 | **3.5683** | **3.1377** |
| cl_v6_tau02 | **2.0850** | 1.4804 | **3.1071** | **3.0221** | 3.9977 | 4.2234 | 3.6788 | **3.4679** | **3.8790** | 2.6543 | **3.4667** | 2.8055 |
| cl_v6_tau03 | 1.9650 | 1.4801 | 3.0463 | **2.9261** | **4.5258** | 4.1566 | 3.5834 | 3.3378 | **3.7363** | 2.4776 | **3.4432** | 2.9910 |
| cl_v7_fair | 1.8738 | 1.5488 | 2.9624 | **3.0107** | **4.5966** | 4.0346 | **3.8191** | **3.5209** | **3.8080** | 3.0155 | **3.4180** | 2.9437 |

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
| cl_v6_tau01 | 3.0477 |
| cl_v6_tau02 | 2.9423 |
| cl_v6_tau03 | 2.8949 |
| cl_v7_fair | 3.0124 |

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
| cl_v6_tau01 | **3.4984** |
| cl_v6_tau02 | **3.3691** |
| cl_v6_tau03 | **3.3833** |
| cl_v7_fair | **3.4130** |

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
| cl_v6_tau01 | 4.3273 | **3.9854** | 5.6746 | **6.5889** | 6.1286 | **4.1526** | **6.8434** | 6.6997 | 5.9279 | **3.6691** | **5.4996** | **5.5996** |
| cl_v6_tau02 | 4.4616 | **3.6669** | 5.8219 | **6.5514** | 5.9122 | **4.0989** | 6.7232 | **7.0914** | 5.6009 | **4.0518** | **5.6398** | **5.5977** |
| cl_v6_tau03 | 4.4894 | **3.7294** | 5.7890 | 6.3314 | 5.8984 | **4.2005** | 6.7618 | 6.7629 | 5.7611 | **4.1104** | **5.4973** | **5.6237** |
| cl_v7_fair | **4.8476** | **3.6269** | 5.7468 | 6.2885 | **6.3051** | **4.6229** | 6.7477 | **6.8953** | 5.8042 | **3.7800** | **5.4083** | **5.5814** |

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
| cl_v6_tau01 | **5.1159** |
| cl_v6_tau02 | **5.1764** |
| cl_v6_tau03 | **5.1264** |
| cl_v7_fair | **5.1325** |

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
| cl_v6_tau01 | 5.7336 |
| cl_v6_tau02 | 5.6933 |
| cl_v6_tau03 | 5.6995 |
| cl_v7_fair | 5.8099 |

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
| cl_scratch_v5 | 2.7832 | 2.5877 | 3.3167 | 4.8272 | 3.1130 | **1.7991** | **1.9505** | **1.7714** | 1.4281 | **1.5630** | **1.4035** |
| cl_v6_fair | 2.7800 | 2.3660 | **3.3363** | <span style="color:red"><strong>5.3563</strong></span> | 3.0150 | **1.8153** | **1.9491** | **1.7751** | <span style="color:red"><strong>1.4730</strong></span> | **1.5651** | **1.4108** |
| cl_v6_tau01 | 2.7965 | 2.4438 | **3.3677** | **5.2663** | 3.7520 | <span style="color:red"><strong>1.8156</strong></span> | <span style="color:red"><strong>1.9565</strong></span> | **1.7750** | **1.4706** | **1.5737** | 1.3938 |
| cl_v6_tau02 | **2.8374** | 2.4455 | 3.2876 | 5.0663 | 3.7345 | **1.8038** | **1.9210** | <span style="color:red"><strong>1.7823</strong></span> | **1.4627** | **1.5693** | **1.4031** |
| cl_v6_tau03 | 2.7705 | 2.3737 | **3.3725** | 4.8057 | 2.6914 | **1.8094** | **1.9219** | **1.7810** | **1.4724** | **1.5776** | **1.4146** |
| cl_v7_fair | 2.7922 | 2.3977 | **3.3752** | 4.9672 | 2.4312 | **1.7999** | **1.9492** | **1.7804** | **1.4649** | **1.5741** | **1.4059** |

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
| cl_v6_tau01 | 2.2033 |
| cl_v6_tau02 | 2.1934 |
| cl_v6_tau03 | 1.9748 |
| cl_v7_fair | 1.9298 |

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
| cl_v6_tau01 | **2.7658** |
| cl_v6_tau02 | **2.7244** |
| cl_v6_tau03 | 2.6861 |
| cl_v7_fair | 2.7148 |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **9.3147** | 8.9030 | **13.0763** | **7.4170** | **15.4089** | **9.8176** | **16.1215** | **9.2746** | <span style="color:red"><strong>21.6974</strong></span> | 6.6323 | **15.6081** | **6.7548** |
| baseline | 9.3012 | <span style="color:red"><strong>9.8550</strong></span> | 10.4433 | 5.4356 | 12.6841 | 9.3292 | 15.7458 | 7.7592 | 18.8433 | 7.2224 | 13.2607 | 5.5884 |
| scGPT_human | 9.1115 | 8.8506 | <span style="color:red"><strong>18.7911</strong></span> | <span style="color:red"><strong>7.8038</strong></span> | <span style="color:red"><strong>16.6627</strong></span> | 5.8807 | **15.9744** | **9.8867** | **21.0316** | <span style="color:red"><strong>9.3851</strong></span> | **15.1446** | <span style="color:red"><strong>12.7637</strong></span> |
| v4_bias_rec_best | 9.1110 | 7.8635 | 9.2224 | **7.4618** | 12.4601 | 9.0440 | 13.8877 | **8.6620** | **20.2765** | 7.0108 | 11.8768 | **10.4858** |
| v4_plain_best | **10.0900** | 8.3404 | **11.0457** | **7.6157** | **15.0506** | 5.8328 | 13.7982 | 6.8233 | **20.8712** | 6.7131 | <span style="color:red"><strong>17.6623</strong></span> | **11.1487** |
| v4_type_pe_best | <span style="color:red"><strong>10.3207</strong></span> | 9.0156 | **13.0913** | **6.2757** | 12.5456 | 8.6422 | 15.1114 | **8.4660** | **20.6348** | **8.8739** | **15.7418** | **10.6961** |
| scconcept | 7.8424 | 5.9363 | 6.6508 | 4.5599 | 7.4418 | 4.8148 | 4.9595 | 2.5866 | 8.2279 | 4.3336 | 7.4649 | 3.5562 |
| scconcept_encoded | 6.7415 | 4.0800 | 5.8311 | 2.8376 | 5.2268 | 1.7161 | 4.7187 | 3.0320 | 5.7471 | 3.2120 | 5.6804 | 3.5756 |
| cl_scratch_v5 | **10.0390** | 9.6253 | **14.8518** | **6.0696** | **16.1839** | **9.8926** | <span style="color:red"><strong>17.0393</strong></span> | **9.4331** | **19.4713** | 5.7753 | **14.3934** | **10.2454** |
| cl_v6_fair | **9.5626** | 8.7690 | **11.4073** | **7.6893** | **13.5779** | <span style="color:red"><strong>14.1269</strong></span> | 13.9445 | **8.1058** | 18.4838 | 6.7181 | **14.9580** | **11.3554** |
| cl_v6_tau01 | **9.4500** | 8.7749 | **14.1096** | **7.3989** | **13.2113** | **12.7627** | 15.5331 | **8.6420** | **19.6528** | 6.3456 | **15.2940** | **10.0444** |
| cl_v6_tau02 | **9.3887** | 9.0863 | **12.3727** | **6.0443** | **15.4892** | **12.0415** | **15.7505** | <span style="color:red"><strong>9.8945</strong></span> | **19.9623** | **7.3704** | **14.8624** | **11.7330** |
| cl_v6_tau03 | **9.5592** | 7.9821 | **14.1393** | **7.0894** | **16.0929** | **11.5797** | 15.6948 | **9.5328** | **19.2024** | 6.8110 | **14.1669** | **11.5052** |
| cl_v7_fair | **9.4109** | 8.6408 | **12.8824** | **7.1720** | **14.4076** | 8.5173 | 15.1881 | **9.0258** | 18.2111 | **7.8899** | 13.0163 | **9.6420** |

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
| cl_v6_tau01 | **8.9948** |
| cl_v6_tau02 | **9.3617** |
| cl_v6_tau03 | **9.0834** |
| cl_v7_fair | **8.4813** |

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
| cl_v6_tau01 | **14.5418** |
| cl_v6_tau02 | **14.6376** |
| cl_v6_tau03 | **14.8092** |
| cl_v7_fair | **13.8527** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | <span style="color:red"><strong>27.5724</strong></span> | 14.7483 | 25.0754 | 18.4848 | 19.2620 | **13.7444** | **33.5703** | **26.0161** | **36.8470** | **17.2883** | <span style="color:red"><strong>35.6446</strong></span> | **22.0118** |
| baseline | 26.0197 | 14.7561 | <span style="color:red"><strong>25.4086</strong></span> | 19.9594 | 20.1643 | 13.7115 | 32.6912 | 24.5131 | 36.6067 | 12.8669 | 30.8046 | 19.3318 |
| scGPT_human | 23.9111 | <span style="color:red"><strong>31.0030</strong></span> | 24.6001 | <span style="color:red"><strong>20.6329</strong></span> | 19.3948 | **15.2234** | **32.9451** | <span style="color:red"><strong>28.3019</strong></span> | **39.1794** | **15.4809** | **35.0796** | **24.3012** |
| v4_bias_rec_best | 21.8359 | 11.6616 | 23.9656 | 17.5895 | 19.0591 | **15.9911** | 31.3245 | **26.3110** | 32.2372 | <span style="color:red"><strong>18.2161</strong></span> | 27.2789 | **24.8432** |
| v4_plain_best | 25.6916 | 14.3332 | 23.9796 | 17.6248 | **20.2817** | <span style="color:red"><strong>18.4030</strong></span> | **32.9133** | **25.5315** | **39.4743** | **15.6527** | **33.8483** | **23.5815** |
| v4_type_pe_best | 25.0587 | 13.2936 | 24.6724 | 18.6629 | <span style="color:red"><strong>21.3439</strong></span> | **14.9156** | 32.4320 | **26.3256** | **38.7361** | **13.7625** | **33.3117** | <span style="color:red"><strong>29.6484</strong></span> |
| scconcept | 4.9998 | 12.9653 | 14.2204 | 5.4316 | 9.6833 | 3.8137 | 9.2512 | 5.8602 | 9.8655 | 4.1476 | 10.2398 | 11.0357 |
| scconcept_encoded | 4.1623 | 7.1172 | 7.3228 | 4.9799 | 8.4336 | 2.8898 | 9.0736 | 6.1720 | 5.9760 | 2.9303 | 4.3421 | 7.9866 |
| cl_scratch_v5 | 22.9494 | 14.2246 | 24.6123 | 17.7213 | 20.1329 | **16.4004** | **33.0155** | **27.5360** | <span style="color:red"><strong>40.3130</strong></span> | 11.5530 | **32.4867** | **24.3785** |
| cl_v6_fair | 25.1326 | 13.4063 | 24.4882 | 16.8968 | **20.4399** | **17.6470** | **33.3417** | 24.4554 | 36.0769 | 12.3258 | **35.2757** | **25.2527** |
| cl_v6_tau01 | 23.9340 | **15.1228** | 24.1981 | 17.7709 | **20.6854** | **17.5611** | <span style="color:red"><strong>34.3678</strong></span> | **26.8740** | **38.3235** | 12.5044 | **34.5631** | **23.9349** |
| cl_v6_tau02 | 25.3360 | 14.2169 | 24.5502 | 17.3862 | **20.7282** | **15.8279** | **33.8881** | **27.0623** | **39.8516** | **13.5316** | **33.4314** | **26.2691** |
| cl_v6_tau03 | 25.6763 | **14.9236** | 24.6393 | 17.0671 | **20.4059** | **16.8959** | 32.0352 | **26.6543** | **38.2765** | 12.6919 | **33.7554** | **27.6547** |
| cl_v7_fair | 24.9734 | 11.6412 | 24.5173 | 18.0305 | **20.2716** | **17.3798** | **33.3520** | 23.9360 | **39.6614** | 12.5187 | **31.4717** | **27.6454** |

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
| cl_v6_tau01 | **18.9613** |
| cl_v6_tau02 | **19.0490** |
| cl_v6_tau03 | **19.3146** |
| cl_v7_fair | **18.5253** |

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
| cl_v6_tau01 | **29.3453** |
| cl_v6_tau02 | **29.6309** |
| cl_v6_tau03 | **29.1314** |
| cl_v7_fair | **29.0412** |

## PRECISION_AT_K (Supplementary)

### Negative protocol: tf_stratified_1to10

Latent variables: metric=PRECISION_AT_K, negative_protocol=tf_stratified_1to10, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.4745 | 0.3905 | 0.6861 | 0.3714 | 0.1875 | 0.8003 | 0.7128 | <span style="color:red"><strong>0.7877</strong></span> | **0.7277** | **0.8016** | <span style="color:red"><strong>0.7700</strong></span> |
| baseline | 0.4745 | 0.4231 | 0.6992 | 0.3750 | 0.1875 | 0.8016 | 0.7149 | 0.7774 | 0.7188 | 0.7944 | 0.7491 |
| scGPT_human | <span style="color:red"><strong>0.4842</strong></span> | 0.4172 | 0.6617 | **0.3786** | <span style="color:red"><strong>0.2500</strong></span> | <span style="color:red"><strong>0.8030</strong></span> | 0.6851 | 0.7738 | **0.7277** | <span style="color:red"><strong>0.8038</strong></span> | **0.7509** |
| v4_bias_rec_best | 0.4660 | 0.4083 | 0.6955 | **0.3893** | 0.0625 | 0.7993 | 0.7021 | 0.7753 | <span style="color:red"><strong>0.7533</strong></span> | **0.8014** | **0.7591** |
| v4_plain_best | **0.4782** | 0.4172 | **0.7011** | **0.3964** | 0.1875 | 0.7979 | 0.6915 | **0.7818** | 0.7154 | **0.7980** | **0.7645** |
| v4_type_pe_best | **0.4757** | **0.4497** | 0.6992 | 0.3643 | 0.0625 | 0.7979 | 0.7149 | **0.7798** | **0.7333** | **0.7985** | **0.7600** |
| scconcept | 0.4005 | 0.4024 | 0.6523 | 0.3143 | 0.1875 | 0.7817 | 0.6511 | 0.7487 | 0.6808 | **0.7978** | 0.7118 |
| scconcept_encoded | 0.4211 | 0.4024 | 0.6335 | 0.3500 | 0.0625 | 0.7797 | 0.6681 | 0.7460 | 0.6953 | 0.7849 | 0.7027 |
| cl_scratch_v5 | 0.4612 | <span style="color:red"><strong>0.4527</strong></span> | 0.6823 | **0.3821** | <span style="color:red"><strong>0.2500</strong></span> | 0.7976 | 0.6915 | 0.7741 | **0.7321** | **0.7973** | **0.7564** |
| cl_v6_fair | 0.4539 | 0.3876 | 0.6823 | <span style="color:red"><strong>0.4250</strong></span> | 0.1875 | 0.7982 | 0.6957 | **0.7809** | **0.7321** | **0.7997** | **0.7564** |
| cl_v6_tau01 | 0.4502 | 0.4024 | <span style="color:red"><strong>0.7049</strong></span> | **0.3857** | 0.1875 | 0.7959 | 0.7106 | **0.7795** | **0.7333** | **0.7990** | **0.7609** |
| cl_v6_tau02 | 0.4539 | 0.3846 | 0.6898 | 0.3679 | 0.1250 | 0.8006 | 0.7064 | **0.7789** | **0.7444** | **0.7985** | **0.7555** |
| cl_v6_tau03 | 0.4575 | 0.4112 | 0.6880 | **0.3929** | 0.1875 | 0.7939 | <span style="color:red"><strong>0.7191</strong></span> | 0.7712 | **0.7400** | **0.8002** | **0.7573** |
| cl_v7_fair | 0.4551 | 0.4142 | **0.7011** | **0.3786** | 0.0625 | 0.7996 | 0.7106 | 0.7771 | **0.7266** | **0.7983** | **0.7627** |

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
| cl_v6_tau01 | **0.5589** |
| cl_v6_tau02 | 0.5432 |
| cl_v6_tau03 | **0.5630** |
| cl_v7_fair | 0.5353 |

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
| cl_v6_tau01 | 0.6525 |
| cl_v6_tau02 | 0.6483 |
| cl_v6_tau03 | 0.6506 |
| cl_v7_fair | 0.6516 |

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
| cl_v6_fair | 0.2516 | <span style="color:red"><strong>0.2381</strong></span> | 0.2784 | 0.1724 | **0.4419** | <span style="color:red"><strong>0.5000</strong></span> | 0.3708 | 0.3182 | **0.3613** | **0.2821** | **0.3562** | 0.2500 |
| cl_v6_tau01 | 0.2484 | **0.2262** | **0.3041** | <span style="color:red"><strong>0.3276</strong></span> | **0.4380** | 0.4091 | **0.3904** | **0.3939** | **0.3650** | 0.2564 | **0.3366** | **0.3043** |
| cl_v6_tau02 | 0.2671 | **0.2262** | 0.2835 | <span style="color:red"><strong>0.3276</strong></span> | 0.3837 | **0.4545** | **0.3792** | **0.3636** | **0.3796** | 0.2692 | <span style="color:red"><strong>0.3595</strong></span> | 0.2500 |
| cl_v6_tau03 | 0.2484 | **0.2143** | 0.2835 | **0.2931** | **0.4186** | 0.4091 | 0.3764 | 0.3409 | **0.3504** | 0.2564 | **0.3366** | 0.2283 |
| cl_v7_fair | 0.2360 | 0.1905 | 0.2732 | **0.3103** | **0.4457** | 0.3636 | **0.3933** | **0.3561** | **0.3869** | **0.2949** | **0.3464** | 0.2500 |

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
| cl_v6_tau01 | **0.3196** |
| cl_v6_tau02 | **0.3152** |
| cl_v6_tau03 | 0.2903 |
| cl_v7_fair | 0.2942 |

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
| cl_v6_tau01 | **0.3471** |
| cl_v6_tau02 | **0.3421** |
| cl_v6_tau03 | **0.3357** |
| cl_v7_fair | **0.3469** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.4076 | 0.2812 | 0.5070 | **0.5448** | **0.5789** | **0.4091** | **0.5914** | 0.6048 | 0.4612 | **0.4516** | **0.4662** | **0.4706** |
| baseline | 0.4286 | 0.3281 | <span style="color:red"><strong>0.5302</strong></span> | 0.5373 | 0.5694 | 0.3636 | 0.5806 | 0.6210 | 0.5233 | 0.1935 | 0.4561 | 0.4412 |
| scGPT_human | **0.4580** | **0.3750** | 0.5116 | <span style="color:red"><strong>0.5970</strong></span> | 0.5407 | <span style="color:red"><strong>0.5758</strong></span> | **0.6048** | **0.6371** | <span style="color:red"><strong>0.5271</strong></span> | **0.2742** | <span style="color:red"><strong>0.5034</strong></span> | **0.4706** |
| v4_bias_rec_best | 0.3908 | 0.3125 | <span style="color:red"><strong>0.5302</strong></span> | **0.5821** | 0.5359 | **0.4394** | 0.5699 | <span style="color:red"><strong>0.6532</strong></span> | 0.4612 | <span style="color:red"><strong>0.4839</strong></span> | 0.4426 | <span style="color:red"><strong>0.5441</strong></span> |
| v4_plain_best | 0.3866 | **0.3594** | 0.4977 | **0.5597** | 0.5526 | **0.4091** | **0.6048** | <span style="color:red"><strong>0.6532</strong></span> | 0.4574 | **0.3226** | 0.4291 | **0.4706** |
| v4_type_pe_best | <span style="color:red"><strong>0.4622</strong></span> | **0.3750** | 0.4953 | **0.5597** | **0.5909** | **0.4242** | <span style="color:red"><strong>0.6156</strong></span> | **0.6290** | 0.4845 | **0.4677** | **0.4865** | **0.4853** |
| scconcept | 0.2395 | <span style="color:red"><strong>0.3906</strong></span> | 0.3233 | 0.3209 | 0.3995 | 0.2576 | 0.3038 | 0.3145 | 0.2558 | 0.1290 | 0.3007 | 0.3235 |
| scconcept_encoded | 0.2101 | 0.2344 | 0.3140 | 0.1642 | 0.3230 | 0.2273 | 0.2634 | 0.2097 | 0.2481 | 0.1129 | 0.2635 | 0.2500 |
| cl_scratch_v5 | 0.3992 | 0.3281 | 0.5116 | 0.5149 | **0.5909** | **0.4697** | **0.6048** | <span style="color:red"><strong>0.6532</strong></span> | 0.5155 | **0.3226** | 0.4561 | 0.4412 |
| cl_v6_fair | 0.3908 | 0.3281 | 0.5093 | 0.5075 | **0.5885** | **0.4242** | **0.6129** | 0.6129 | 0.4845 | **0.3871** | 0.4527 | **0.4706** |
| cl_v6_tau01 | 0.3908 | 0.2969 | 0.5140 | 0.5299 | **0.5933** | **0.3788** | **0.5833** | 0.5726 | 0.5039 | **0.2742** | **0.4662** | **0.4706** |
| cl_v6_tau02 | 0.3992 | 0.3125 | 0.5093 | 0.5373 | <span style="color:red"><strong>0.5981</strong></span> | **0.4091** | **0.5887** | **0.6371** | 0.4806 | **0.3710** | **0.4628** | **0.4853** |
| cl_v6_tau03 | 0.3866 | 0.3125 | 0.5070 | 0.5149 | **0.5933** | **0.3939** | **0.5833** | 0.6210 | 0.5039 | **0.4032** | **0.4628** | **0.5000** |
| cl_v7_fair | 0.4160 | 0.2812 | 0.5070 | 0.5373 | **0.5909** | **0.4242** | 0.5753 | **0.6290** | 0.4884 | **0.3548** | **0.4865** | **0.4706** |

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
| cl_v6_tau01 | **0.4205** |
| cl_v6_tau02 | **0.4587** |
| cl_v6_tau03 | **0.4576** |
| cl_v7_fair | **0.4495** |

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
| cl_v6_tau01 | 0.5086 |
| cl_v6_tau02 | 0.5065 |
| cl_v6_tau03 | 0.5061 |
| cl_v7_fair | 0.5107 |

### Negative protocol: full_candidate

Latent variables: metric=PRECISION_AT_K, negative_protocol=full_candidate, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.4757** | 0.3905 | 0.7011 | 0.3929 | <span style="color:red"><strong>0.1875</strong></span> | **0.8050** | 0.6723 | 0.7774 | **0.7344** | <span style="color:red"><strong>0.8115</strong></span> | <span style="color:red"><strong>0.7836</strong></span> |
| baseline | 0.4709 | 0.4172 | <span style="color:red"><strong>0.7124</strong></span> | 0.4071 | <span style="color:red"><strong>0.1875</strong></span> | 0.7966 | 0.6830 | 0.7783 | 0.7288 | 0.8028 | 0.7636 |
| scGPT_human | **0.4733** | **0.4467** | 0.6748 | 0.3964 | <span style="color:red"><strong>0.1875</strong></span> | **0.8026** | 0.6681 | 0.7765 | 0.7243 | **0.8043** | 0.7482 |
| v4_bias_rec_best | **0.4769** | **0.4260** | 0.7011 | 0.3429 | 0.0625 | **0.8080** | **0.6872** | 0.7715 | **0.7400** | 0.7976 | 0.7591 |
| v4_plain_best | **0.4818** | **0.4231** | 0.7030 | 0.3357 | 0.1250 | **0.8074** | **0.7043** | **0.7792** | 0.7221 | 0.7990 | 0.7627 |
| v4_type_pe_best | <span style="color:red"><strong>0.4964</strong></span> | **0.4408** | 0.6880 | 0.3536 | <span style="color:red"><strong>0.1875</strong></span> | **0.8033** | **0.7064** | **0.7786** | 0.7266 | **0.8038** | **0.7736** |
| scconcept | 0.4393 | <span style="color:red"><strong>0.4497</strong></span> | 0.6391 | 0.3071 | <span style="color:red"><strong>0.1875</strong></span> | 0.7868 | 0.6404 | 0.7555 | 0.7143 | 0.7877 | 0.7255 |
| scconcept_encoded | 0.4223 | **0.4231** | 0.6523 | 0.3464 | 0.0000 | 0.7861 | 0.6596 | 0.7543 | 0.6987 | 0.7873 | 0.7227 |
| cl_scratch_v5 | 0.4636 | 0.4142 | 0.6805 | **0.4107** | <span style="color:red"><strong>0.1875</strong></span> | **0.8013** | **0.6957** | 0.7783 | **0.7288** | 0.8019 | 0.7618 |
| cl_v6_fair | 0.4648 | 0.3935 | 0.6842 | 0.3964 | <span style="color:red"><strong>0.1875</strong></span> | <span style="color:red"><strong>0.8097</strong></span> | <span style="color:red"><strong>0.7191</strong></span> | **0.7798** | **0.7388** | **0.8040** | 0.7636 |
| cl_v6_tau01 | 0.4636 | 0.3935 | 0.6955 | 0.4000 | 0.1250 | **0.8074** | **0.7000** | 0.7783 | <span style="color:red"><strong>0.7433</strong></span> | 0.8028 | 0.7555 |
| cl_v6_tau02 | **0.4757** | 0.3905 | 0.6767 | <span style="color:red"><strong>0.4143</strong></span> | 0.1250 | **0.8053** | **0.6872** | **0.7824** | **0.7388** | **0.8052** | 0.7609 |
| cl_v6_tau03 | 0.4672 | 0.3905 | 0.6955 | 0.3821 | 0.1250 | **0.8090** | **0.6872** | 0.7780 | **0.7388** | 0.8023 | 0.7636 |
| cl_v7_fair | 0.4648 | 0.4112 | 0.6955 | 0.3750 | 0.1250 | **0.8053** | **0.7149** | <span style="color:red"><strong>0.7883</strong></span> | **0.7310** | **0.8033** | 0.7582 |

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
| cl_v6_tau01 | 0.5434 |
| cl_v6_tau02 | 0.5405 |
| cl_v6_tau03 | 0.5410 |
| cl_v7_fair | 0.5481 |

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
| cl_v6_tau01 | 0.6579 |
| cl_v6_tau02 | 0.6599 |
| cl_v6_tau03 | 0.6557 |
| cl_v7_fair | 0.6554 |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.2236** | <span style="color:red"><strong>0.2738</strong></span> | **0.1804** | **0.1724** | **0.2868** | **0.1818** | **0.3174** | **0.2803** | **0.2737** | **0.1795** | **0.2549** | 0.1630 |
| baseline | 0.2112 | 0.2619 | 0.1546 | 0.1552 | 0.2481 | 0.1364 | 0.3006 | 0.2576 | 0.2518 | 0.1667 | 0.2320 | 0.1957 |
| scGPT_human | 0.1957 | 0.2143 | <span style="color:red"><strong>0.2320</strong></span> | <span style="color:red"><strong>0.1897</strong></span> | **0.3062** | 0.0909 | **0.3090** | **0.2955** | **0.2956** | <span style="color:red"><strong>0.2564</strong></span> | <span style="color:red"><strong>0.2582</strong></span> | **0.2826** |
| v4_bias_rec_best | **0.2174** | 0.2024 | **0.2062** | <span style="color:red"><strong>0.1897</strong></span> | **0.2674** | 0.1364 | 0.2809 | 0.2500 | **0.2664** | **0.2308** | 0.2222 | **0.2935** |
| v4_plain_best | <span style="color:red"><strong>0.2391</strong></span> | 0.2500 | **0.1856** | <span style="color:red"><strong>0.1897</strong></span> | **0.2868** | 0.1364 | 0.2809 | 0.2424 | **0.2664** | **0.1795** | **0.2516** | <span style="color:red"><strong>0.3261</strong></span> |
| v4_type_pe_best | **0.2267** | <span style="color:red"><strong>0.2738</strong></span> | **0.1907** | 0.1207 | **0.2674** | 0.1364 | 0.2978 | **0.2727** | **0.2956** | **0.2179** | <span style="color:red"><strong>0.2582</strong></span> | **0.3043** |
| scconcept | 0.1863 | 0.1548 | 0.0979 | 0.0690 | 0.1899 | 0.0455 | 0.1292 | 0.0682 | 0.1387 | 0.1410 | 0.1667 | 0.1630 |
| scconcept_encoded | 0.1335 | 0.0714 | 0.0928 | 0.0517 | 0.1279 | 0.0000 | 0.1236 | 0.1212 | 0.1058 | 0.0769 | 0.1242 | 0.1087 |
| cl_scratch_v5 | **0.2329** | 0.2619 | **0.2062** | 0.1207 | **0.2946** | **0.1818** | <span style="color:red"><strong>0.3202</strong></span> | <span style="color:red"><strong>0.3106</strong></span> | **0.2956** | 0.1667 | 0.2059 | <span style="color:red"><strong>0.3261</strong></span> |
| cl_v6_fair | 0.1988 | 0.2500 | **0.2010** | 0.1379 | 0.2481 | <span style="color:red"><strong>0.2273</strong></span> | 0.2949 | 0.2500 | 0.2445 | **0.1795** | 0.2222 | **0.2935** |
| cl_v6_tau01 | 0.1957 | 0.2024 | **0.1959** | 0.1379 | 0.2481 | <span style="color:red"><strong>0.2273</strong></span> | 0.2978 | **0.2727** | **0.2920** | 0.1667 | 0.2255 | **0.3152** |
| cl_v6_tau02 | **0.2205** | 0.2262 | **0.2062** | 0.1552 | **0.3062** | <span style="color:red"><strong>0.2273</strong></span> | **0.3174** | **0.2879** | <span style="color:red"><strong>0.3029</strong></span> | 0.1667 | **0.2418** | **0.3043** |
| cl_v6_tau03 | 0.2112 | 0.2024 | **0.2216** | 0.1552 | <span style="color:red"><strong>0.3101</strong></span> | 0.1364 | **0.3090** | **0.2727** | 0.2518 | **0.1923** | **0.2386** | <span style="color:red"><strong>0.3261</strong></span> |
| cl_v7_fair | 0.1925 | 0.2262 | **0.1804** | 0.1552 | **0.2791** | 0.1364 | **0.3118** | **0.3030** | 0.2445 | **0.1923** | 0.2190 | **0.2826** |

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
| cl_v6_tau01 | **0.2204** |
| cl_v6_tau02 | **0.2279** |
| cl_v6_tau03 | **0.2142** |
| cl_v7_fair | **0.2159** |

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
| cl_v6_tau01 | **0.2425** |
| cl_v6_tau02 | **0.2658** |
| cl_v6_tau03 | **0.2570** |
| cl_v7_fair | **0.2379** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.3025** | 0.2031 | <span style="color:red"><strong>0.4698</strong></span> | 0.5075 | **0.4976** | **0.4242** | **0.5081** | **0.5484** | 0.3643 | <span style="color:red"><strong>0.2903</strong></span> | <span style="color:red"><strong>0.3682</strong></span> | **0.3382** |
| baseline | 0.2815 | 0.2031 | 0.4558 | 0.5522 | 0.4785 | 0.3939 | 0.5054 | 0.5081 | 0.3837 | 0.2258 | 0.3176 | 0.3235 |
| scGPT_human | **0.2857** | <span style="color:red"><strong>0.3438</strong></span> | 0.4535 | <span style="color:red"><strong>0.5597</strong></span> | 0.4617 | **0.4848** | 0.4839 | <span style="color:red"><strong>0.5968</strong></span> | <span style="color:red"><strong>0.4031</strong></span> | **0.2581** | **0.3649** | **0.3382** |
| v4_bias_rec_best | 0.2815 | 0.1875 | **0.4605** | 0.5075 | 0.4641 | **0.4091** | 0.4946 | **0.5565** | 0.3256 | <span style="color:red"><strong>0.2903</strong></span> | **0.3243** | **0.4118** |
| v4_plain_best | 0.2731 | **0.2188** | 0.4372 | 0.4627 | 0.4641 | <span style="color:red"><strong>0.5152</strong></span> | **0.5081** | **0.5161** | **0.3915** | **0.2581** | **0.3277** | **0.3529** |
| v4_type_pe_best | **0.2983** | 0.2031 | 0.4488 | 0.5373 | **0.4904** | **0.4242** | 0.5054 | **0.5645** | **0.3876** | 0.2258 | **0.3412** | <span style="color:red"><strong>0.4265</strong></span> |
| scconcept | 0.0882 | **0.2188** | 0.2977 | 0.1940 | 0.2919 | 0.1364 | 0.2097 | 0.1694 | 0.1318 | 0.0323 | 0.1385 | 0.1765 |
| scconcept_encoded | 0.0714 | 0.1719 | 0.1837 | 0.2015 | 0.2990 | 0.0758 | 0.2016 | 0.1452 | 0.1008 | 0.0806 | 0.0642 | 0.1618 |
| cl_scratch_v5 | 0.2773 | **0.2344** | 0.4535 | 0.4851 | **0.4952** | **0.4848** | **0.5188** | <span style="color:red"><strong>0.5968</strong></span> | **0.3992** | 0.1935 | **0.3243** | **0.3676** |
| cl_v6_fair | **0.2899** | **0.2656** | 0.4442 | 0.4851 | **0.5167** | **0.4697** | 0.5000 | **0.5242** | **0.3915** | 0.1774 | **0.3412** | **0.3971** |
| cl_v6_tau01 | **0.2899** | **0.2969** | 0.4395 | 0.5075 | **0.5072** | <span style="color:red"><strong>0.5152</strong></span> | <span style="color:red"><strong>0.5269</strong></span> | **0.5565** | 0.3837 | 0.1774 | **0.3480** | **0.4118** |
| cl_v6_tau02 | <span style="color:red"><strong>0.3067</strong></span> | **0.2656** | 0.4395 | 0.4627 | **0.5000** | **0.4545** | **0.5188** | **0.5806** | **0.3992** | **0.2419** | **0.3581** | **0.4118** |
| cl_v6_tau03 | **0.2899** | **0.2500** | **0.4581** | 0.4851 | **0.5024** | **0.4697** | 0.4946 | **0.5484** | **0.3876** | 0.2097 | **0.3311** | <span style="color:red"><strong>0.4265</strong></span> |
| cl_v7_fair | **0.2941** | 0.2031 | 0.4442 | 0.4925 | <span style="color:red"><strong>0.5263</strong></span> | **0.4697** | 0.5054 | **0.5242** | 0.3837 | 0.2258 | 0.3176 | **0.4118** |

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
| cl_v6_tau01 | **0.4109** |
| cl_v6_tau02 | **0.4029** |
| cl_v6_tau03 | **0.3982** |
| cl_v7_fair | **0.3879** |

##### Aggregate mean across STRING 1000-gene datasets

Latent variables: metric=PRECISION_AT_K, negative_protocol=full_candidate, network_group=STRING, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.4184** |
| baseline | 0.4037 |
| scGPT_human | **0.4088** |
| v4_bias_rec_best | 0.3918 |
| v4_plain_best | 0.4003 |
| v4_type_pe_best | **0.4120** |
| scconcept | 0.1930 |
| scconcept_encoded | 0.1535 |
| cl_scratch_v5 | **0.4114** |
| cl_v6_fair | **0.4139** |
| cl_v6_tau01 | **0.4159** |
| cl_v6_tau02 | <span style="color:red"><strong>0.4204</strong></span> |
| cl_v6_tau03 | **0.4106** |
| cl_v7_fair | **0.4119** |

## RECALL_AT_K (Supplementary)

### Negative protocol: tf_stratified_1to10

Latent variables: metric=RECALL_AT_K, negative_protocol=tf_stratified_1to10, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.4745 | 0.3905 | 0.6861 | 0.3714 | 0.1875 | 0.8003 | 0.7128 | <span style="color:red"><strong>0.7877</strong></span> | **0.7277** | **0.8016** | <span style="color:red"><strong>0.7700</strong></span> |
| baseline | 0.4745 | 0.4231 | 0.6992 | 0.3750 | 0.1875 | 0.8016 | 0.7149 | 0.7774 | 0.7188 | 0.7944 | 0.7491 |
| scGPT_human | <span style="color:red"><strong>0.4842</strong></span> | 0.4172 | 0.6617 | **0.3786** | <span style="color:red"><strong>0.2500</strong></span> | <span style="color:red"><strong>0.8030</strong></span> | 0.6851 | 0.7738 | **0.7277** | <span style="color:red"><strong>0.8038</strong></span> | **0.7509** |
| v4_bias_rec_best | 0.4660 | 0.4083 | 0.6955 | **0.3893** | 0.0625 | 0.7993 | 0.7021 | 0.7753 | <span style="color:red"><strong>0.7533</strong></span> | **0.8014** | **0.7591** |
| v4_plain_best | **0.4782** | 0.4172 | **0.7011** | **0.3964** | 0.1875 | 0.7979 | 0.6915 | **0.7818** | 0.7154 | **0.7980** | **0.7645** |
| v4_type_pe_best | **0.4757** | **0.4497** | 0.6992 | 0.3643 | 0.0625 | 0.7979 | 0.7149 | **0.7798** | **0.7333** | **0.7985** | **0.7600** |
| scconcept | 0.4005 | 0.4024 | 0.6523 | 0.3143 | 0.1875 | 0.7817 | 0.6511 | 0.7487 | 0.6808 | **0.7978** | 0.7118 |
| scconcept_encoded | 0.4211 | 0.4024 | 0.6335 | 0.3500 | 0.0625 | 0.7797 | 0.6681 | 0.7460 | 0.6953 | 0.7849 | 0.7027 |
| cl_scratch_v5 | 0.4612 | <span style="color:red"><strong>0.4527</strong></span> | 0.6823 | **0.3821** | <span style="color:red"><strong>0.2500</strong></span> | 0.7976 | 0.6915 | 0.7741 | **0.7321** | **0.7973** | **0.7564** |
| cl_v6_fair | 0.4539 | 0.3876 | 0.6823 | <span style="color:red"><strong>0.4250</strong></span> | 0.1875 | 0.7982 | 0.6957 | **0.7809** | **0.7321** | **0.7997** | **0.7564** |
| cl_v6_tau01 | 0.4502 | 0.4024 | <span style="color:red"><strong>0.7049</strong></span> | **0.3857** | 0.1875 | 0.7959 | 0.7106 | **0.7795** | **0.7333** | **0.7990** | **0.7609** |
| cl_v6_tau02 | 0.4539 | 0.3846 | 0.6898 | 0.3679 | 0.1250 | 0.8006 | 0.7064 | **0.7789** | **0.7444** | **0.7985** | **0.7555** |
| cl_v6_tau03 | 0.4575 | 0.4112 | 0.6880 | **0.3929** | 0.1875 | 0.7939 | <span style="color:red"><strong>0.7191</strong></span> | 0.7712 | **0.7400** | **0.8002** | **0.7573** |
| cl_v7_fair | 0.4551 | 0.4142 | **0.7011** | **0.3786** | 0.0625 | 0.7996 | 0.7106 | 0.7771 | **0.7266** | **0.7983** | **0.7627** |

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
| cl_v6_tau01 | **0.5589** |
| cl_v6_tau02 | 0.5432 |
| cl_v6_tau03 | **0.5630** |
| cl_v7_fair | 0.5353 |

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
| cl_v6_tau01 | 0.6525 |
| cl_v6_tau02 | 0.6483 |
| cl_v6_tau03 | 0.6506 |
| cl_v7_fair | 0.6516 |

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
| cl_v6_fair | 0.2516 | <span style="color:red"><strong>0.2381</strong></span> | 0.2784 | 0.1724 | **0.4419** | <span style="color:red"><strong>0.5000</strong></span> | 0.3708 | 0.3182 | **0.3613** | **0.2821** | **0.3562** | 0.2500 |
| cl_v6_tau01 | 0.2484 | **0.2262** | **0.3041** | <span style="color:red"><strong>0.3276</strong></span> | **0.4380** | 0.4091 | **0.3904** | **0.3939** | **0.3650** | 0.2564 | **0.3366** | **0.3043** |
| cl_v6_tau02 | 0.2671 | **0.2262** | 0.2835 | <span style="color:red"><strong>0.3276</strong></span> | 0.3837 | **0.4545** | **0.3792** | **0.3636** | **0.3796** | 0.2692 | <span style="color:red"><strong>0.3595</strong></span> | 0.2500 |
| cl_v6_tau03 | 0.2484 | **0.2143** | 0.2835 | **0.2931** | **0.4186** | 0.4091 | 0.3764 | 0.3409 | **0.3504** | 0.2564 | **0.3366** | 0.2283 |
| cl_v7_fair | 0.2360 | 0.1905 | 0.2732 | **0.3103** | **0.4457** | 0.3636 | **0.3933** | **0.3561** | **0.3869** | **0.2949** | **0.3464** | 0.2500 |

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
| cl_v6_tau01 | **0.3196** |
| cl_v6_tau02 | **0.3152** |
| cl_v6_tau03 | 0.2903 |
| cl_v7_fair | 0.2942 |

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
| cl_v6_tau01 | **0.3471** |
| cl_v6_tau02 | **0.3421** |
| cl_v6_tau03 | **0.3357** |
| cl_v7_fair | **0.3469** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.4076 | 0.2812 | 0.5070 | **0.5448** | **0.5789** | **0.4091** | **0.5914** | 0.6048 | 0.4612 | **0.4516** | **0.4662** | **0.4706** |
| baseline | 0.4286 | 0.3281 | <span style="color:red"><strong>0.5302</strong></span> | 0.5373 | 0.5694 | 0.3636 | 0.5806 | 0.6210 | 0.5233 | 0.1935 | 0.4561 | 0.4412 |
| scGPT_human | **0.4580** | **0.3750** | 0.5116 | <span style="color:red"><strong>0.5970</strong></span> | 0.5407 | <span style="color:red"><strong>0.5758</strong></span> | **0.6048** | **0.6371** | <span style="color:red"><strong>0.5271</strong></span> | **0.2742** | <span style="color:red"><strong>0.5034</strong></span> | **0.4706** |
| v4_bias_rec_best | 0.3908 | 0.3125 | <span style="color:red"><strong>0.5302</strong></span> | **0.5821** | 0.5359 | **0.4394** | 0.5699 | <span style="color:red"><strong>0.6532</strong></span> | 0.4612 | <span style="color:red"><strong>0.4839</strong></span> | 0.4426 | <span style="color:red"><strong>0.5441</strong></span> |
| v4_plain_best | 0.3866 | **0.3594** | 0.4977 | **0.5597** | 0.5526 | **0.4091** | **0.6048** | <span style="color:red"><strong>0.6532</strong></span> | 0.4574 | **0.3226** | 0.4291 | **0.4706** |
| v4_type_pe_best | <span style="color:red"><strong>0.4622</strong></span> | **0.3750** | 0.4953 | **0.5597** | **0.5909** | **0.4242** | <span style="color:red"><strong>0.6156</strong></span> | **0.6290** | 0.4845 | **0.4677** | **0.4865** | **0.4853** |
| scconcept | 0.2395 | <span style="color:red"><strong>0.3906</strong></span> | 0.3233 | 0.3209 | 0.3995 | 0.2576 | 0.3038 | 0.3145 | 0.2558 | 0.1290 | 0.3007 | 0.3235 |
| scconcept_encoded | 0.2101 | 0.2344 | 0.3140 | 0.1642 | 0.3230 | 0.2273 | 0.2634 | 0.2097 | 0.2481 | 0.1129 | 0.2635 | 0.2500 |
| cl_scratch_v5 | 0.3992 | 0.3281 | 0.5116 | 0.5149 | **0.5909** | **0.4697** | **0.6048** | <span style="color:red"><strong>0.6532</strong></span> | 0.5155 | **0.3226** | 0.4561 | 0.4412 |
| cl_v6_fair | 0.3908 | 0.3281 | 0.5093 | 0.5075 | **0.5885** | **0.4242** | **0.6129** | 0.6129 | 0.4845 | **0.3871** | 0.4527 | **0.4706** |
| cl_v6_tau01 | 0.3908 | 0.2969 | 0.5140 | 0.5299 | **0.5933** | **0.3788** | **0.5833** | 0.5726 | 0.5039 | **0.2742** | **0.4662** | **0.4706** |
| cl_v6_tau02 | 0.3992 | 0.3125 | 0.5093 | 0.5373 | <span style="color:red"><strong>0.5981</strong></span> | **0.4091** | **0.5887** | **0.6371** | 0.4806 | **0.3710** | **0.4628** | **0.4853** |
| cl_v6_tau03 | 0.3866 | 0.3125 | 0.5070 | 0.5149 | **0.5933** | **0.3939** | **0.5833** | 0.6210 | 0.5039 | **0.4032** | **0.4628** | **0.5000** |
| cl_v7_fair | 0.4160 | 0.2812 | 0.5070 | 0.5373 | **0.5909** | **0.4242** | 0.5753 | **0.6290** | 0.4884 | **0.3548** | **0.4865** | **0.4706** |

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
| cl_v6_tau01 | **0.4205** |
| cl_v6_tau02 | **0.4587** |
| cl_v6_tau03 | **0.4576** |
| cl_v7_fair | **0.4495** |

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
| cl_v6_tau01 | 0.5086 |
| cl_v6_tau02 | 0.5065 |
| cl_v6_tau03 | 0.5061 |
| cl_v7_fair | 0.5107 |

### Negative protocol: full_candidate

Latent variables: metric=RECALL_AT_K, negative_protocol=full_candidate, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.4757** | 0.3905 | 0.7011 | 0.3929 | <span style="color:red"><strong>0.1875</strong></span> | **0.8050** | 0.6723 | 0.7774 | **0.7344** | <span style="color:red"><strong>0.8115</strong></span> | <span style="color:red"><strong>0.7836</strong></span> |
| baseline | 0.4709 | 0.4172 | <span style="color:red"><strong>0.7124</strong></span> | 0.4071 | <span style="color:red"><strong>0.1875</strong></span> | 0.7966 | 0.6830 | 0.7783 | 0.7288 | 0.8028 | 0.7636 |
| scGPT_human | **0.4733** | **0.4467** | 0.6748 | 0.3964 | <span style="color:red"><strong>0.1875</strong></span> | **0.8026** | 0.6681 | 0.7765 | 0.7243 | **0.8043** | 0.7482 |
| v4_bias_rec_best | **0.4769** | **0.4260** | 0.7011 | 0.3429 | 0.0625 | **0.8080** | **0.6872** | 0.7715 | **0.7400** | 0.7976 | 0.7591 |
| v4_plain_best | **0.4818** | **0.4231** | 0.7030 | 0.3357 | 0.1250 | **0.8074** | **0.7043** | **0.7792** | 0.7221 | 0.7990 | 0.7627 |
| v4_type_pe_best | <span style="color:red"><strong>0.4964</strong></span> | **0.4408** | 0.6880 | 0.3536 | <span style="color:red"><strong>0.1875</strong></span> | **0.8033** | **0.7064** | **0.7786** | 0.7266 | **0.8038** | **0.7736** |
| scconcept | 0.4393 | <span style="color:red"><strong>0.4497</strong></span> | 0.6391 | 0.3071 | <span style="color:red"><strong>0.1875</strong></span> | 0.7868 | 0.6404 | 0.7555 | 0.7143 | 0.7877 | 0.7255 |
| scconcept_encoded | 0.4223 | **0.4231** | 0.6523 | 0.3464 | 0.0000 | 0.7861 | 0.6596 | 0.7543 | 0.6987 | 0.7873 | 0.7227 |
| cl_scratch_v5 | 0.4636 | 0.4142 | 0.6805 | **0.4107** | <span style="color:red"><strong>0.1875</strong></span> | **0.8013** | **0.6957** | 0.7783 | **0.7288** | 0.8019 | 0.7618 |
| cl_v6_fair | 0.4648 | 0.3935 | 0.6842 | 0.3964 | <span style="color:red"><strong>0.1875</strong></span> | <span style="color:red"><strong>0.8097</strong></span> | <span style="color:red"><strong>0.7191</strong></span> | **0.7798** | **0.7388** | **0.8040** | 0.7636 |
| cl_v6_tau01 | 0.4636 | 0.3935 | 0.6955 | 0.4000 | 0.1250 | **0.8074** | **0.7000** | 0.7783 | <span style="color:red"><strong>0.7433</strong></span> | 0.8028 | 0.7555 |
| cl_v6_tau02 | **0.4757** | 0.3905 | 0.6767 | <span style="color:red"><strong>0.4143</strong></span> | 0.1250 | **0.8053** | **0.6872** | **0.7824** | **0.7388** | **0.8052** | 0.7609 |
| cl_v6_tau03 | 0.4672 | 0.3905 | 0.6955 | 0.3821 | 0.1250 | **0.8090** | **0.6872** | 0.7780 | **0.7388** | 0.8023 | 0.7636 |
| cl_v7_fair | 0.4648 | 0.4112 | 0.6955 | 0.3750 | 0.1250 | **0.8053** | **0.7149** | <span style="color:red"><strong>0.7883</strong></span> | **0.7310** | **0.8033** | 0.7582 |

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
| cl_v6_tau01 | 0.5434 |
| cl_v6_tau02 | 0.5405 |
| cl_v6_tau03 | 0.5410 |
| cl_v7_fair | 0.5481 |

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
| cl_v6_tau01 | 0.6579 |
| cl_v6_tau02 | 0.6599 |
| cl_v6_tau03 | 0.6557 |
| cl_v7_fair | 0.6554 |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.2236** | <span style="color:red"><strong>0.2738</strong></span> | **0.1804** | **0.1724** | **0.2868** | **0.1818** | **0.3174** | **0.2803** | **0.2737** | **0.1795** | **0.2549** | 0.1630 |
| baseline | 0.2112 | 0.2619 | 0.1546 | 0.1552 | 0.2481 | 0.1364 | 0.3006 | 0.2576 | 0.2518 | 0.1667 | 0.2320 | 0.1957 |
| scGPT_human | 0.1957 | 0.2143 | <span style="color:red"><strong>0.2320</strong></span> | <span style="color:red"><strong>0.1897</strong></span> | **0.3062** | 0.0909 | **0.3090** | **0.2955** | **0.2956** | <span style="color:red"><strong>0.2564</strong></span> | <span style="color:red"><strong>0.2582</strong></span> | **0.2826** |
| v4_bias_rec_best | **0.2174** | 0.2024 | **0.2062** | <span style="color:red"><strong>0.1897</strong></span> | **0.2674** | 0.1364 | 0.2809 | 0.2500 | **0.2664** | **0.2308** | 0.2222 | **0.2935** |
| v4_plain_best | <span style="color:red"><strong>0.2391</strong></span> | 0.2500 | **0.1856** | <span style="color:red"><strong>0.1897</strong></span> | **0.2868** | 0.1364 | 0.2809 | 0.2424 | **0.2664** | **0.1795** | **0.2516** | <span style="color:red"><strong>0.3261</strong></span> |
| v4_type_pe_best | **0.2267** | <span style="color:red"><strong>0.2738</strong></span> | **0.1907** | 0.1207 | **0.2674** | 0.1364 | 0.2978 | **0.2727** | **0.2956** | **0.2179** | <span style="color:red"><strong>0.2582</strong></span> | **0.3043** |
| scconcept | 0.1863 | 0.1548 | 0.0979 | 0.0690 | 0.1899 | 0.0455 | 0.1292 | 0.0682 | 0.1387 | 0.1410 | 0.1667 | 0.1630 |
| scconcept_encoded | 0.1335 | 0.0714 | 0.0928 | 0.0517 | 0.1279 | 0.0000 | 0.1236 | 0.1212 | 0.1058 | 0.0769 | 0.1242 | 0.1087 |
| cl_scratch_v5 | **0.2329** | 0.2619 | **0.2062** | 0.1207 | **0.2946** | **0.1818** | <span style="color:red"><strong>0.3202</strong></span> | <span style="color:red"><strong>0.3106</strong></span> | **0.2956** | 0.1667 | 0.2059 | <span style="color:red"><strong>0.3261</strong></span> |
| cl_v6_fair | 0.1988 | 0.2500 | **0.2010** | 0.1379 | 0.2481 | <span style="color:red"><strong>0.2273</strong></span> | 0.2949 | 0.2500 | 0.2445 | **0.1795** | 0.2222 | **0.2935** |
| cl_v6_tau01 | 0.1957 | 0.2024 | **0.1959** | 0.1379 | 0.2481 | <span style="color:red"><strong>0.2273</strong></span> | 0.2978 | **0.2727** | **0.2920** | 0.1667 | 0.2255 | **0.3152** |
| cl_v6_tau02 | **0.2205** | 0.2262 | **0.2062** | 0.1552 | **0.3062** | <span style="color:red"><strong>0.2273</strong></span> | **0.3174** | **0.2879** | <span style="color:red"><strong>0.3029</strong></span> | 0.1667 | **0.2418** | **0.3043** |
| cl_v6_tau03 | 0.2112 | 0.2024 | **0.2216** | 0.1552 | <span style="color:red"><strong>0.3101</strong></span> | 0.1364 | **0.3090** | **0.2727** | 0.2518 | **0.1923** | **0.2386** | <span style="color:red"><strong>0.3261</strong></span> |
| cl_v7_fair | 0.1925 | 0.2262 | **0.1804** | 0.1552 | **0.2791** | 0.1364 | **0.3118** | **0.3030** | 0.2445 | **0.1923** | 0.2190 | **0.2826** |

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
| cl_v6_tau01 | **0.2204** |
| cl_v6_tau02 | **0.2279** |
| cl_v6_tau03 | **0.2142** |
| cl_v7_fair | **0.2159** |

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
| cl_v6_tau01 | **0.2425** |
| cl_v6_tau02 | **0.2658** |
| cl_v6_tau03 | **0.2570** |
| cl_v7_fair | **0.2379** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.3025** | 0.2031 | <span style="color:red"><strong>0.4698</strong></span> | 0.5075 | **0.4976** | **0.4242** | **0.5081** | **0.5484** | 0.3643 | <span style="color:red"><strong>0.2903</strong></span> | <span style="color:red"><strong>0.3682</strong></span> | **0.3382** |
| baseline | 0.2815 | 0.2031 | 0.4558 | 0.5522 | 0.4785 | 0.3939 | 0.5054 | 0.5081 | 0.3837 | 0.2258 | 0.3176 | 0.3235 |
| scGPT_human | **0.2857** | <span style="color:red"><strong>0.3438</strong></span> | 0.4535 | <span style="color:red"><strong>0.5597</strong></span> | 0.4617 | **0.4848** | 0.4839 | <span style="color:red"><strong>0.5968</strong></span> | <span style="color:red"><strong>0.4031</strong></span> | **0.2581** | **0.3649** | **0.3382** |
| v4_bias_rec_best | 0.2815 | 0.1875 | **0.4605** | 0.5075 | 0.4641 | **0.4091** | 0.4946 | **0.5565** | 0.3256 | <span style="color:red"><strong>0.2903</strong></span> | **0.3243** | **0.4118** |
| v4_plain_best | 0.2731 | **0.2188** | 0.4372 | 0.4627 | 0.4641 | <span style="color:red"><strong>0.5152</strong></span> | **0.5081** | **0.5161** | **0.3915** | **0.2581** | **0.3277** | **0.3529** |
| v4_type_pe_best | **0.2983** | 0.2031 | 0.4488 | 0.5373 | **0.4904** | **0.4242** | 0.5054 | **0.5645** | **0.3876** | 0.2258 | **0.3412** | <span style="color:red"><strong>0.4265</strong></span> |
| scconcept | 0.0882 | **0.2188** | 0.2977 | 0.1940 | 0.2919 | 0.1364 | 0.2097 | 0.1694 | 0.1318 | 0.0323 | 0.1385 | 0.1765 |
| scconcept_encoded | 0.0714 | 0.1719 | 0.1837 | 0.2015 | 0.2990 | 0.0758 | 0.2016 | 0.1452 | 0.1008 | 0.0806 | 0.0642 | 0.1618 |
| cl_scratch_v5 | 0.2773 | **0.2344** | 0.4535 | 0.4851 | **0.4952** | **0.4848** | **0.5188** | <span style="color:red"><strong>0.5968</strong></span> | **0.3992** | 0.1935 | **0.3243** | **0.3676** |
| cl_v6_fair | **0.2899** | **0.2656** | 0.4442 | 0.4851 | **0.5167** | **0.4697** | 0.5000 | **0.5242** | **0.3915** | 0.1774 | **0.3412** | **0.3971** |
| cl_v6_tau01 | **0.2899** | **0.2969** | 0.4395 | 0.5075 | **0.5072** | <span style="color:red"><strong>0.5152</strong></span> | <span style="color:red"><strong>0.5269</strong></span> | **0.5565** | 0.3837 | 0.1774 | **0.3480** | **0.4118** |
| cl_v6_tau02 | <span style="color:red"><strong>0.3067</strong></span> | **0.2656** | 0.4395 | 0.4627 | **0.5000** | **0.4545** | **0.5188** | **0.5806** | **0.3992** | **0.2419** | **0.3581** | **0.4118** |
| cl_v6_tau03 | **0.2899** | **0.2500** | **0.4581** | 0.4851 | **0.5024** | **0.4697** | 0.4946 | **0.5484** | **0.3876** | 0.2097 | **0.3311** | <span style="color:red"><strong>0.4265</strong></span> |
| cl_v7_fair | **0.2941** | 0.2031 | 0.4442 | 0.4925 | <span style="color:red"><strong>0.5263</strong></span> | **0.4697** | 0.5054 | **0.5242** | 0.3837 | 0.2258 | 0.3176 | **0.4118** |

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
| cl_v6_tau01 | **0.4109** |
| cl_v6_tau02 | **0.4029** |
| cl_v6_tau03 | **0.3982** |
| cl_v7_fair | **0.3879** |

##### Aggregate mean across STRING 1000-gene datasets

Latent variables: metric=RECALL_AT_K, negative_protocol=full_candidate, network_group=STRING, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.4184** |
| baseline | 0.4037 |
| scGPT_human | **0.4088** |
| v4_bias_rec_best | 0.3918 |
| v4_plain_best | 0.4003 |
| v4_type_pe_best | **0.4120** |
| scconcept | 0.1930 |
| scconcept_encoded | 0.1535 |
| cl_scratch_v5 | **0.4114** |
| cl_v6_fair | **0.4139** |
| cl_v6_tau01 | **0.4159** |
| cl_v6_tau02 | <span style="color:red"><strong>0.4204</strong></span> |
| cl_v6_tau03 | **0.4106** |
| cl_v7_fair | **0.4119** |

## F1 (Supplementary)

### Negative protocol: tf_stratified_1to10

Latent variables: metric=F1, negative_protocol=tf_stratified_1to10, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.4112 | 0.3411 | 0.6818 | **0.3448** | **0.0667** | 0.8064 | 0.7007 | <span style="color:red"><strong>0.7902</strong></span> | **0.7283** | **0.8092** | **0.7751** |
| baseline | 0.4139 | 0.3452 | 0.7008 | 0.3303 | 0.0000 | 0.8091 | 0.7154 | 0.7880 | 0.7260 | 0.8046 | 0.7557 |
| scGPT_human | 0.3972 | **0.4212** | 0.6740 | **0.3332** | **0.1000** | 0.8040 | 0.6921 | 0.7777 | **0.7321** | **0.8085** | **0.7562** |
| v4_bias_rec_best | 0.4109 | **0.3544** | 0.6939 | **0.3491** | 0.0000 | 0.8066 | 0.7009 | 0.7849 | <span style="color:red"><strong>0.7682</strong></span> | **0.8051** | **0.7605** |
| v4_plain_best | <span style="color:red"><strong>0.4225</strong></span> | **0.3870** | <span style="color:red"><strong>0.7106</strong></span> | 0.3263 | 0.0000 | <span style="color:red"><strong>0.8096</strong></span> | 0.6887 | 0.7860 | 0.7201 | **0.8079** | <span style="color:red"><strong>0.7841</strong></span> |
| v4_type_pe_best | 0.4112 | <span style="color:red"><strong>0.4346</strong></span> | 0.6945 | 0.3255 | **0.1000** | 0.8048 | <span style="color:red"><strong>0.7171</strong></span> | 0.7819 | **0.7446** | **0.8057** | **0.7732** |
| scconcept | 0.3638 | **0.3604** | 0.6522 | 0.2080 | <span style="color:red"><strong>0.1111</strong></span> | 0.7911 | 0.6617 | 0.7599 | 0.6802 | 0.8035 | 0.7283 |
| scconcept_encoded | 0.3678 | **0.3917** | 0.6434 | 0.2431 | 0.0000 | 0.7885 | 0.6680 | 0.7545 | 0.7191 | 0.8017 | 0.7354 |
| cl_scratch_v5 | 0.3903 | **0.3911** | 0.6822 | **0.3501** | **0.0909** | 0.8057 | 0.6980 | 0.7837 | **0.7315** | **0.8083** | 0.7521 |
| cl_v6_fair | 0.3821 | 0.3043 | 0.6901 | **0.3636** | **0.0833** | 0.7997 | 0.7118 | 0.7829 | **0.7520** | **0.8063** | 0.7557 |
| cl_v6_tau01 | 0.3958 | **0.3461** | **0.7045** | **0.3551** | **0.1000** | 0.7967 | 0.7079 | 0.7776 | **0.7334** | <span style="color:red"><strong>0.8111</strong></span> | **0.7674** |
| cl_v6_tau02 | 0.4004 | 0.3258 | 0.6834 | **0.3666** | 0.0000 | 0.8054 | 0.7133 | 0.7788 | **0.7516** | 0.8017 | **0.7618** |
| cl_v6_tau03 | 0.3957 | 0.3283 | 0.6918 | <span style="color:red"><strong>0.3701</strong></span> | 0.0000 | 0.8005 | **0.7156** | 0.7736 | **0.7493** | 0.8042 | **0.7700** |
| cl_v7_fair | 0.3940 | **0.3574** | **0.7034** | **0.3401** | 0.0000 | 0.8066 | 0.7133 | 0.7772 | **0.7506** | **0.8075** | **0.7565** |

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
| cl_v6_tau01 | **0.5310** |
| cl_v6_tau02 | **0.5105** |
| cl_v6_tau03 | **0.5127** |
| cl_v7_fair | **0.5156** |

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
| cl_v6_tau01 | 0.6401 |
| cl_v6_tau02 | 0.6394 |
| cl_v6_tau03 | 0.6393 |
| cl_v7_fair | 0.6381 |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.1231 | 0.1237 | 0.1584 | **0.2024** | **0.4034** | 0.2500 | <span style="color:red"><strong>0.4072</strong></span> | **0.3490** | **0.3212** | 0.1765 | **0.2898** | 0.2521 |
| baseline | 0.1438 | 0.1294 | 0.2669 | 0.1387 | 0.3374 | 0.4000 | 0.3584 | 0.3416 | 0.2710 | 0.2113 | 0.2000 | 0.2628 |
| scGPT_human | <span style="color:red"><strong>0.2101</strong></span> | <span style="color:red"><strong>0.2163</strong></span> | <span style="color:red"><strong>0.3010</strong></span> | **0.2735** | **0.3799** | 0.0714 | 0.3365 | <span style="color:red"><strong>0.4125</strong></span> | **0.3374** | <span style="color:red"><strong>0.3463</strong></span> | <span style="color:red"><strong>0.3377</strong></span> | **0.3287** |
| v4_bias_rec_best | 0.0980 | 0.0633 | 0.1789 | **0.2154** | 0.2510 | 0.1538 | 0.3087 | 0.3108 | **0.3538** | 0.1512 | **0.2616** | 0.2482 |
| v4_plain_best | **0.2090** | 0.0617 | 0.2523 | **0.1874** | **0.3588** | 0.2667 | 0.3415 | 0.3370 | **0.2996** | 0.1999 | **0.2321** | **0.2897** |
| v4_type_pe_best | **0.1922** | 0.0964 | 0.1786 | **0.1481** | **0.3658** | <span style="color:red"><strong>0.4734</strong></span> | 0.3157 | 0.2957 | **0.3127** | 0.1897 | **0.3005** | <span style="color:red"><strong>0.3719</strong></span> |
| scconcept | 0.1363 | 0.0972 | 0.1713 | 0.1020 | 0.2059 | 0.0000 | 0.1095 | 0.0682 | 0.1971 | 0.1548 | 0.1647 | 0.1279 |
| scconcept_encoded | 0.0721 | 0.0894 | 0.1301 | 0.0727 | 0.1982 | 0.0588 | 0.1584 | 0.0909 | 0.1572 | 0.1095 | **0.2027** | 0.1172 |
| cl_scratch_v5 | 0.1362 | **0.1529** | 0.2308 | 0.1240 | **0.4027** | 0.1875 | **0.3624** | 0.3187 | **0.3462** | 0.1713 | **0.2587** | **0.3260** |
| cl_v6_fair | 0.1405 | **0.1562** | 0.2175 | 0.1132 | **0.3984** | **0.4575** | 0.3371 | 0.3361 | **0.3494** | 0.1888 | **0.2779** | **0.2646** |
| cl_v6_tau01 | 0.1432 | **0.1327** | 0.2371 | <span style="color:red"><strong>0.3051</strong></span> | **0.3931** | 0.2778 | 0.3572 | 0.3162 | **0.3535** | 0.1781 | **0.3256** | **0.2965** |
| cl_v6_tau02 | 0.1368 | **0.1340** | 0.2336 | **0.2530** | **0.3788** | 0.2778 | 0.3529 | **0.3726** | **0.3516** | 0.1892 | **0.3040** | **0.2646** |
| cl_v6_tau03 | 0.1202 | 0.1111 | 0.2168 | **0.2762** | **0.3857** | 0.2778 | 0.3444 | **0.3452** | **0.3224** | 0.1513 | **0.2799** | 0.2417 |
| cl_v7_fair | **0.1579** | **0.1348** | 0.2163 | **0.2731** | <span style="color:red"><strong>0.4171</strong></span> | 0.2778 | **0.3603** | 0.2988 | <span style="color:red"><strong>0.3590</strong></span> | 0.1917 | **0.2623** | 0.2593 |

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
| cl_v6_tau01 | **0.2510** |
| cl_v6_tau02 | **0.2485** |
| cl_v6_tau03 | 0.2339 |
| cl_v7_fair | 0.2392 |

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
| cl_v6_tau01 | **0.3016** |
| cl_v6_tau02 | **0.2930** |
| cl_v6_tau03 | **0.2782** |
| cl_v7_fair | **0.2955** |

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
| cl_v6_fair | 0.4006 | 0.2281 | 0.4782 | 0.5116 | **0.5776** | **0.2394** | <span style="color:red"><strong>0.6144</strong></span> | 0.5999 | 0.4713 | **0.3129** | **0.4391** | 0.3965 |
| cl_v6_tau01 | 0.3794 | 0.2222 | 0.5068 | 0.4814 | **0.5793** | **0.1875** | 0.5686 | 0.5269 | 0.4664 | **0.2030** | **0.4761** | 0.3879 |
| cl_v6_tau02 | 0.3983 | 0.2154 | 0.5184 | 0.5322 | **0.5754** | **0.2206** | **0.5970** | **0.6233** | 0.4648 | **0.3452** | **0.4438** | 0.4022 |
| cl_v6_tau03 | 0.3640 | 0.2308 | 0.4957 | 0.5001 | **0.5709** | **0.2254** | **0.5825** | 0.5480 | 0.4679 | **0.3485** | **0.4369** | 0.3879 |
| cl_v7_fair | 0.3764 | 0.2373 | 0.5112 | 0.4805 | <span style="color:red"><strong>0.5862</strong></span> | **0.2338** | 0.5542 | **0.6135** | 0.4820 | **0.2549** | 0.4280 | 0.4147 |

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
| cl_v6_tau01 | 0.3348 |
| cl_v6_tau02 | **0.3898** |
| cl_v6_tau03 | **0.3734** |
| cl_v7_fair | **0.3724** |

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
| cl_v6_tau01 | 0.4961 |
| cl_v6_tau02 | 0.4996 |
| cl_v6_tau03 | 0.4863 |
| cl_v7_fair | 0.4897 |

### Negative protocol: full_candidate

Latent variables: metric=F1, negative_protocol=full_candidate, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.4005** | **0.3528** | **0.7037** | **0.3294** | 0.0000 | **0.8092** | 0.6816 | 0.7819 | **0.7403** | **0.8113** | <span style="color:red"><strong>0.7929</strong></span> |
| baseline | 0.3603 | 0.3236 | 0.6966 | 0.3276 | 0.0833 | 0.8008 | 0.6925 | 0.7890 | 0.7357 | 0.8072 | 0.7794 |
| scGPT_human | 0.3049 | <span style="color:red"><strong>0.4341</strong></span> | 0.6639 | **0.3891** | **0.1000** | **0.8068** | 0.6779 | 0.7771 | 0.7277 | **0.8104** | 0.7598 |
| v4_bias_rec_best | <span style="color:red"><strong>0.4451</strong></span> | **0.3712** | 0.6853 | 0.3008 | 0.0833 | **0.8107** | **0.6988** | 0.7780 | <span style="color:red"><strong>0.7584</strong></span> | **0.8077** | 0.7781 |
| v4_plain_best | **0.4368** | **0.3629** | <span style="color:red"><strong>0.7117</strong></span> | 0.3171 | 0.0833 | **0.8074** | **0.7046** | 0.7840 | 0.7352 | **0.8096** | 0.7708 |
| v4_type_pe_best | **0.4219** | **0.3801** | 0.6883 | 0.3212 | 0.0000 | **0.8112** | 0.6834 | 0.7858 | **0.7416** | <span style="color:red"><strong>0.8132</strong></span> | 0.7761 |
| scconcept | 0.2696 | **0.3932** | 0.6570 | 0.2354 | <span style="color:red"><strong>0.1111</strong></span> | 0.7908 | 0.6406 | 0.7633 | 0.7167 | 0.8023 | 0.7407 |
| scconcept_encoded | 0.3526 | **0.3801** | 0.6665 | 0.2657 | 0.0000 | 0.7916 | 0.6582 | 0.7639 | 0.7192 | 0.7983 | 0.7374 |
| cl_scratch_v5 | **0.3951** | **0.3870** | 0.6766 | **0.3768** | **0.0909** | **0.8087** | 0.6910 | 0.7832 | 0.7292 | **0.8096** | 0.7697 |
| cl_v6_fair | **0.4252** | **0.3302** | 0.6914 | **0.3517** | 0.0000 | **0.8101** | <span style="color:red"><strong>0.7229</strong></span> | 0.7785 | **0.7361** | **0.8109** | 0.7726 |
| cl_v6_tau01 | **0.4239** | 0.3231 | **0.7114** | <span style="color:red"><strong>0.3958</strong></span> | **0.0909** | <span style="color:red"><strong>0.8114</strong></span> | 0.6898 | 0.7818 | **0.7473** | 0.8070 | 0.7754 |
| cl_v6_tau02 | **0.4186** | **0.3601** | 0.6770 | **0.3823** | 0.0000 | **0.8053** | 0.6896 | 0.7812 | **0.7430** | **0.8098** | 0.7682 |
| cl_v6_tau03 | **0.4170** | **0.3422** | **0.6985** | 0.3269 | 0.0000 | **0.8094** | **0.6936** | 0.7765 | **0.7515** | **0.8114** | 0.7707 |
| cl_v7_fair | **0.4022** | **0.3420** | **0.7067** | **0.3503** | 0.0000 | **0.8094** | **0.7082** | <span style="color:red"><strong>0.7903</strong></span> | **0.7509** | **0.8130** | 0.7724 |

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
| cl_v6_tau01 | **0.5253** |
| cl_v6_tau02 | 0.5122 |
| cl_v6_tau03 | 0.5116 |
| cl_v7_fair | 0.5147 |

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
| cl_v6_fair | **0.6446** |
| cl_v6_tau01 | <span style="color:red"><strong>0.6552</strong></span> |
| cl_v6_tau02 | **0.6457** |
| cl_v6_tau03 | **0.6400** |
| cl_v7_fair | **0.6453** |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.0565 | **0.1519** | **0.1393** | **0.0870** | **0.1253** | 0.0714 | <span style="color:red"><strong>0.3040</strong></span> | **0.2220** | <span style="color:red"><strong>0.3109</strong></span> | 0.1067 | **0.2068** | **0.1379** |
| baseline | 0.0659 | 0.1184 | 0.0813 | 0.0444 | 0.1040 | 0.0833 | 0.2801 | 0.2114 | 0.2403 | 0.1235 | 0.1972 | 0.1220 |
| scGPT_human | **0.0660** | **0.1620** | <span style="color:red"><strong>0.2141</strong></span> | 0.0256 | **0.2269** | 0.0000 | 0.2788 | <span style="color:red"><strong>0.2737</strong></span> | **0.3018** | <span style="color:red"><strong>0.2033</strong></span> | 0.1923 | **0.2599** |
| v4_bias_rec_best | 0.0448 | 0.0995 | 0.0651 | **0.0952** | **0.1266** | **0.1250** | 0.2409 | 0.1305 | **0.2559** | 0.1200 | 0.1108 | **0.2465** |
| v4_plain_best | **0.1009** | 0.1131 | **0.0966** | **0.0923** | **0.2286** | 0.0769 | 0.2123 | 0.2009 | **0.2691** | **0.1266** | <span style="color:red"><strong>0.2477</strong></span> | **0.2409** |
| v4_type_pe_best | <span style="color:red"><strong>0.1039</strong></span> | 0.0909 | **0.0982** | **0.0667** | 0.1027 | 0.0714 | 0.2213 | **0.2635** | 0.2231 | **0.1238** | **0.2183** | **0.2061** |
| scconcept | **0.0688** | 0.0563 | 0.0526 | 0.0227 | **0.1215** | 0.0714 | 0.0528 | 0.0442 | 0.1051 | 0.0746 | 0.0632 | 0.0824 |
| scconcept_encoded | 0.0619 | 0.0429 | 0.0336 | 0.0385 | 0.0667 | 0.0000 | 0.0263 | 0.0759 | 0.0437 | 0.0429 | 0.0423 | 0.0843 |
| cl_scratch_v5 | 0.0628 | **0.1481** | **0.1806** | **0.0513** | <span style="color:red"><strong>0.2456</strong></span> | 0.0833 | 0.2653 | **0.2492** | **0.2716** | 0.1184 | 0.1942 | **0.2228** |
| cl_v6_fair | 0.0633 | 0.1136 | 0.0720 | **0.0889** | **0.1200** | **0.1429** | 0.1932 | 0.1724 | **0.2594** | **0.1333** | 0.1818 | **0.1843** |
| cl_v6_tau01 | **0.0676** | **0.1369** | **0.1535** | **0.0816** | **0.1336** | **0.1429** | 0.2452 | **0.2139** | **0.2591** | 0.1233 | 0.1939 | <span style="color:red"><strong>0.2601</strong></span> |
| cl_v6_tau02 | 0.0648 | <span style="color:red"><strong>0.1691</strong></span> | **0.1008** | **0.0714** | **0.2395** | <span style="color:red"><strong>0.1538</strong></span> | 0.2523 | **0.2332** | **0.2851** | **0.1566** | 0.1843 | **0.2267** |
| cl_v6_tau03 | **0.0699** | 0.0988 | **0.1398** | **0.0976** | **0.2394** | <span style="color:red"><strong>0.1538</strong></span> | 0.2734 | **0.2171** | **0.2526** | **0.1392** | 0.1649 | **0.1988** |
| cl_v7_fair | **0.0739** | 0.1047 | **0.1699** | <span style="color:red"><strong>0.1242</strong></span> | **0.1723** | 0.0769 | 0.2307 | **0.2226** | **0.2570** | **0.1467** | 0.1221 | **0.1747** |

##### Aggregate mean across Non-Specific 500-gene datasets

Latent variables: metric=F1, negative_protocol=full_candidate, network_group=Non-Specific, dataset_size=500, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.1295** |
| baseline | 0.1172 |
| scGPT_human | **0.1541** |
| v4_bias_rec_best | **0.1361** |
| v4_plain_best | **0.1418** |
| v4_type_pe_best | **0.1370** |
| scconcept | 0.0586 |
| scconcept_encoded | 0.0474 |
| cl_scratch_v5 | **0.1455** |
| cl_v6_fair | **0.1392** |
| cl_v6_tau01 | **0.1598** |
| cl_v6_tau02 | <span style="color:red"><strong>0.1685</strong></span> |
| cl_v6_tau03 | **0.1509** |
| cl_v7_fair | **0.1416** |

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
| cl_v6_tau01 | **0.1755** |
| cl_v6_tau02 | **0.1878** |
| cl_v6_tau03 | **0.1900** |
| cl_v7_fair | **0.1710** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | <span style="color:red"><strong>0.3551</strong></span> | **0.1837** | **0.4408** | 0.4948 | 0.4039 | 0.3480 | 0.5028 | **0.5592** | **0.3964** | 0.1676 | **0.3673** | 0.2254 |
| baseline | 0.2906 | 0.1538 | 0.4189 | 0.5383 | 0.4066 | 0.3519 | 0.5031 | 0.4766 | 0.3580 | <span style="color:red"><strong>0.2110</strong></span> | 0.3244 | 0.3500 |
| scGPT_human | 0.2786 | <span style="color:red"><strong>0.2000</strong></span> | **0.4377** | <span style="color:red"><strong>0.5559</strong></span> | **0.4438** | **0.4532** | **0.5211** | **0.5723** | **0.4182** | 0.1102 | <span style="color:red"><strong>0.3916</strong></span> | 0.3271 |
| v4_bias_rec_best | 0.2549 | 0.1273 | <span style="color:red"><strong>0.4495</strong></span> | 0.4634 | 0.3945 | **0.3761** | 0.4789 | **0.5479** | 0.3277 | 0.1682 | 0.2041 | 0.3036 |
| v4_plain_best | 0.2811 | **0.1754** | **0.4268** | 0.4381 | **0.4219** | <span style="color:red"><strong>0.5201</strong></span> | 0.4961 | **0.5132** | **0.4022** | 0.1646 | **0.3439** | 0.3455 |
| v4_type_pe_best | 0.2597 | **0.1569** | **0.4396** | 0.5177 | **0.4409** | **0.3797** | 0.4909 | **0.5392** | **0.4092** | 0.0638 | **0.3444** | <span style="color:red"><strong>0.4453</strong></span> |
| scconcept | 0.0448 | **0.1667** | 0.2163 | 0.0630 | 0.2042 | 0.0941 | 0.1503 | 0.0873 | 0.0733 | 0.0256 | 0.0857 | 0.1346 |
| scconcept_encoded | 0.0261 | 0.0870 | 0.0899 | 0.1080 | 0.1405 | 0.0429 | 0.0890 | 0.1093 | 0.0172 | 0.0233 | 0.0215 | 0.1311 |
| cl_scratch_v5 | 0.2249 | 0.1452 | **0.4423** | 0.4379 | **0.4199** | **0.4102** | <span style="color:red"><strong>0.5380</strong></span> | <span style="color:red"><strong>0.5834</strong></span> | **0.4313** | 0.1087 | **0.3348** | 0.3414 |
| cl_v6_fair | 0.2587 | **0.1667** | **0.4354** | 0.4247 | **0.4233** | **0.4361** | **0.5057** | **0.5467** | **0.4002** | 0.0727 | **0.3635** | **0.3589** |
| cl_v6_tau01 | 0.2726 | **0.1667** | 0.4172 | 0.4273 | <span style="color:red"><strong>0.4517</strong></span> | **0.4486** | **0.5343** | **0.5479** | **0.4117** | 0.0998 | **0.3458** | **0.3683** |
| cl_v6_tau02 | **0.2935** | 0.1525 | **0.4379** | 0.4621 | **0.4402** | **0.4294** | **0.5290** | **0.5613** | **0.4267** | 0.1775 | **0.3312** | **0.3887** |
| cl_v6_tau03 | 0.2786 | 0.1538 | **0.4481** | 0.4713 | **0.4203** | **0.4188** | 0.4922 | **0.5595** | **0.4033** | 0.1162 | **0.3368** | **0.3779** |
| cl_v7_fair | 0.2609 | 0.1290 | **0.4342** | 0.4909 | **0.4368** | **0.4314** | **0.5048** | **0.5114** | <span style="color:red"><strong>0.4371</strong></span> | 0.1347 | 0.2973 | **0.4061** |

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
| cl_v6_tau01 | 0.3431 |
| cl_v6_tau02 | **0.3619** |
| cl_v6_tau03 | **0.3496** |
| cl_v7_fair | **0.3506** |

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
| cl_v6_tau01 | **0.4055** |
| cl_v6_tau02 | **0.4097** |
| cl_v6_tau03 | **0.3966** |
| cl_v7_fair | **0.3952** |

## SPECIFICITY (Supplementary)

### Negative protocol: tf_stratified_1to10

Latent variables: metric=SPECIFICITY, negative_protocol=tf_stratified_1to10, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.8509** | 0.8505 | 0.8774 | 0.9059 | 0.9625 | 0.6394 | 0.7559 | **0.6873** | **0.6533** | **0.6168** | **0.6315** |
| baseline | 0.8470 | 0.8527 | 0.8868 | 0.9246 | 0.9875 | 0.6416 | <span style="color:red"><strong>0.7637</strong></span> | 0.6310 | 0.6326 | 0.6025 | 0.5820 |
| scGPT_human | <span style="color:red"><strong>0.8743</strong></span> | 0.8000 | 0.8722 | 0.9138 | **0.9938** | **0.6507** | 0.6934 | **0.6561** | **0.6395** | **0.6263** | **0.6094** |
| v4_bias_rec_best | 0.8431 | 0.8430 | 0.8851 | **0.9260** | 0.9688 | 0.6200 | 0.7383 | **0.6476** | **0.6519** | <span style="color:red"><strong>0.6485</strong></span> | **0.6263** |
| v4_plain_best | **0.8733** | 0.8161 | **0.8902** | <span style="color:red"><strong>0.9325</strong></span> | 0.9812 | 0.6216 | 0.7246 | **0.6756** | **0.6367** | **0.6136** | **0.6224** |
| v4_type_pe_best | **0.8665** | 0.8333 | 0.8756 | **0.9289** | **0.9938** | 0.6313 | 0.7363 | **0.6723** | 0.5843 | **0.6311** | **0.6328** |
| scconcept | 0.8095 | 0.8247 | 0.8302 | 0.9052 | <span style="color:red"><strong>1.0000</strong></span> | 0.6146 | 0.6387 | 0.6006 | 0.5953 | **0.6092** | 0.5247 |
| scconcept_encoded | 0.8212 | 0.7763 | 0.8559 | 0.9167 | 0.9750 | 0.6055 | 0.6602 | 0.6148 | 0.5677 | 0.5627 | 0.5169 |
| cl_scratch_v5 | **0.8577** | <span style="color:red"><strong>0.8559</strong></span> | 0.8868 | 0.9246 | 0.9875 | 0.6222 | 0.7168 | **0.6399** | <span style="color:red"><strong>0.6727</strong></span> | 0.6009 | **0.6302** |
| cl_v6_fair | **0.8567** | 0.8473 | **0.8885** | 0.9195 | 0.9812 | 0.6039 | 0.7012 | **0.6934** | 0.6064 | **0.6334** | **0.5990** |
| cl_v6_tau01 | 0.8445 | 0.8376 | **0.9005** | **0.9274** | **0.9938** | <span style="color:red"><strong>0.6642</strong></span> | 0.7344 | <span style="color:red"><strong>0.6979</strong></span> | **0.6492** | **0.6092** | <span style="color:red"><strong>0.6380</strong></span> |
| cl_v6_tau02 | **0.8509** | 0.8355 | **0.8911** | 0.9217 | 0.9875 | **0.6529** | 0.7324 | **0.6861** | **0.6340** | **0.6442** | **0.6250** |
| cl_v6_tau03 | **0.8533** | 0.8473 | **0.8928** | **0.9282** | 0.9875 | 0.6308 | 0.7324 | **0.6723** | 0.6174 | **0.6434** | **0.6133** |
| cl_v7_fair | **0.8509** | 0.8355 | <span style="color:red"><strong>0.9039</strong></span> | **0.9267** | 0.9875 | 0.6362 | 0.7188 | **0.6910** | 0.5939 | **0.6044** | **0.6107** |

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
| cl_v6_tau01 | **0.7706** |
| cl_v6_tau02 | 0.7629 |
| cl_v6_tau03 | 0.7596 |
| cl_v7_fair | 0.7493 |

##### Aggregate mean across Specific 1000-gene datasets

Latent variables: metric=SPECIFICITY, negative_protocol=tf_stratified_1to10, network_group=Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.7629** |
| baseline | 0.7556 |
| scGPT_human | **0.7656** |
| v4_bias_rec_best | **0.7617** |
| v4_plain_best | **0.7678** |
| v4_type_pe_best | **0.7676** |
| scconcept | 0.7282 |
| scconcept_encoded | 0.7295 |
| cl_scratch_v5 | 0.7553 |
| cl_v6_fair | **0.7659** |
| cl_v6_tau01 | **0.7740** |
| cl_v6_tau02 | <span style="color:red"><strong>0.7745</strong></span> |
| cl_v6_tau03 | **0.7701** |
| cl_v7_fair | **0.7689** |

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
| cl_v6_tau01 | 0.9610 | 0.9356 | **0.9582** | **0.9483** | **0.9663** | 0.9909 | **0.9653** | **0.9536** | 0.9597 | 0.9436 | 0.9669 | **0.9663** |
| cl_v6_tau02 | **0.9659** | 0.9371 | **0.9557** | 0.9431 | 0.9636 | 0.9909 | 0.9635 | **0.9378** | 0.9589 | 0.9513 | 0.9659 | **0.9630** |
| cl_v6_tau03 | **0.9703** | **0.9551** | **0.9521** | **0.9483** | 0.9578 | 0.9864 | **0.9671** | **0.9353** | 0.9619 | 0.9436 | 0.9649 | 0.9598 |
| cl_v7_fair | 0.9581 | 0.9476 | **0.9552** | **0.9603** | 0.9632 | 0.9909 | **0.9695** | **0.9502** | 0.9578 | 0.9538 | 0.9663 | 0.9598 |

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
| cl_v6_tau01 | 0.9564 |
| cl_v6_tau02 | 0.9539 |
| cl_v6_tau03 | 0.9547 |
| cl_v7_fair | **0.9605** |

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
| cl_v6_tau01 | 0.9629 |
| cl_v6_tau02 | 0.9622 |
| cl_v6_tau03 | 0.9624 |
| cl_v7_fair | 0.9617 |

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
| cl_v6_tau01 | 0.9550 | 0.9734 | 0.9698 | 0.9610 | 0.9687 | **0.9701** | 0.9648 | **0.9697** | 0.9581 | **0.9629** | 0.9591 | **0.9824** |
| cl_v6_tau02 | 0.9496 | 0.9703 | 0.9667 | 0.9602 | 0.9708 | **0.9686** | 0.9661 | **0.9746** | 0.9609 | **0.9548** | 0.9598 | **0.9809** |
| cl_v6_tau03 | 0.9550 | 0.9719 | 0.9707 | 0.9580 | 0.9679 | **0.9654** | 0.9640 | <span style="color:red"><strong>0.9762</strong></span> | 0.9589 | **0.9613** | 0.9625 | **0.9824** |
| cl_v7_fair | **0.9567** | **0.9797** | 0.9688 | 0.9557 | 0.9694 | 0.9591 | 0.9672 | **0.9713** | 0.9574 | **0.9694** | 0.9635 | **0.9838** |

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
| cl_v6_tau01 | **0.9699** |
| cl_v6_tau02 | **0.9682** |
| cl_v6_tau03 | **0.9692** |
| cl_v7_fair | **0.9698** |

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
| cl_v6_tau01 | 0.9626 |
| cl_v6_tau02 | 0.9623 |
| cl_v6_tau03 | 0.9632 |
| cl_v7_fair | 0.9638 |

### Negative protocol: full_candidate

Latent variables: metric=SPECIFICITY, negative_protocol=full_candidate, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.9269 | 0.9171 | 0.9319 | 0.9716 | **0.9978** | 0.7757 | 0.7638 | **0.7701** | <span style="color:red"><strong>0.6892</strong></span> | <span style="color:red"><strong>0.7449</strong></span> | **0.6045** |
| baseline | 0.9408 | 0.9257 | 0.9330 | 0.9733 | 0.9933 | 0.7806 | 0.7739 | 0.7487 | 0.6561 | 0.6973 | 0.5886 |
| scGPT_human | <span style="color:red"><strong>0.9450</strong></span> | 0.9051 | 0.9313 | 0.9622 | **0.9978** | **0.7935** | 0.7652 | **0.7856** | 0.6506 | **0.7026** | **0.6230** |
| v4_bias_rec_best | 0.9138 | 0.9229 | 0.9302 | <span style="color:red"><strong>0.9792</strong></span> | 0.9933 | **0.7928** | 0.7725 | **0.7637** | 0.6188 | **0.7097** | **0.6019** |
| v4_plain_best | 0.9220 | <span style="color:red"><strong>0.9320</strong></span> | **0.9426** | 0.9698 | 0.9933 | <span style="color:red"><strong>0.8011</strong></span> | **0.8014** | **0.7786** | 0.6312 | 0.6932 | 0.5873 |
| v4_type_pe_best | 0.9342 | **0.9280** | **0.9347** | **0.9762** | 0.9933 | 0.7668 | <span style="color:red"><strong>0.8261</strong></span> | **0.7699** | 0.6229 | 0.6826 | 0.5820 |
| scconcept | **0.9413** | 0.9183 | 0.9054 | 0.9592 | <span style="color:red"><strong>1.0000</strong></span> | 0.7754 | 0.7565 | 0.7468 | 0.6354 | 0.6546 | 0.5476 |
| scconcept_encoded | 0.9239 | 0.9154 | 0.9178 | 0.9680 | 0.9888 | 0.7681 | **0.7913** | 0.7414 | 0.5732 | 0.6805 | 0.5066 |
| cl_scratch_v5 | 0.9321 | 0.9217 | <span style="color:red"><strong>0.9499</strong></span> | 0.9721 | **0.9955** | 0.7711 | **0.7986** | **0.7755** | 0.6492 | **0.7044** | 0.5780 |
| cl_v6_fair | 0.9218 | 0.9206 | 0.9257 | **0.9751** | 0.9933 | **0.7875** | **0.7928** | <span style="color:red"><strong>0.8020</strong></span> | **0.6602** | **0.7013** | **0.5992** |
| cl_v6_tau01 | 0.9316 | 0.9154 | **0.9347** | 0.9692 | **0.9955** | **0.7928** | **0.7942** | **0.7792** | 0.6492 | **0.7318** | 0.5860 |
| cl_v6_tau02 | 0.9321 | 0.9114 | 0.9245 | 0.9677 | **0.9955** | **0.7997** | 0.7667 | **0.7870** | 0.6533 | **0.7131** | <span style="color:red"><strong>0.6243</strong></span> |
| cl_v6_tau03 | 0.9349 | 0.9154 | 0.9319 | **0.9760** | **0.9955** | 0.7777 | 0.7696 | **0.7896** | 0.6519 | 0.6923 | **0.5979** |
| cl_v7_fair | 0.9314 | 0.9137 | 0.9285 | **0.9774** | 0.9910 | **0.7915** | **0.7971** | **0.7904** | 0.6202 | 0.6823 | 0.5463 |

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
| cl_v6_tau01 | **0.7881** |
| cl_v6_tau02 | **0.7903** |
| cl_v6_tau03 | 0.7861 |
| cl_v7_fair | 0.7737 |

##### Aggregate mean across Specific 1000-gene datasets

Latent variables: metric=SPECIFICITY, negative_protocol=full_candidate, network_group=Specific, dataset_size=1000, classifier=aggregated(lr,mlp), aggregation=mean_across_datasets

| Embedding | Mean |
|---|---:|
| minus | **0.8535** |
| baseline | 0.8456 |
| scGPT_human | **0.8534** |
| v4_bias_rec_best | **0.8482** |
| v4_plain_best | **0.8512** |
| v4_type_pe_best | 0.8441 |
| scconcept | 0.8304 |
| scconcept_encoded | 0.8333 |
| cl_scratch_v5 | **0.8509** |
| cl_v6_fair | **0.8522** |
| cl_v6_tau01 | <span style="color:red"><strong>0.8565</strong></span> |
| cl_v6_tau02 | **0.8540** |
| cl_v6_tau03 | **0.8504** |
| cl_v7_fair | **0.8503** |

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
| cl_v6_tau01 | **0.9976** | 0.9901 | 0.9984 | 0.9950 | 0.9983 | 0.9994 | 0.9967 | <span style="color:red"><strong>0.9911</strong></span> | 0.9981 | **0.9926** | **0.9982** | **0.9934** |
| cl_v6_tau02 | **0.9976** | 0.9884 | 0.9989 | **0.9971** | 0.9971 | <span style="color:red"><strong>1.0000</strong></span> | 0.9969 | **0.9901** | 0.9982 | **0.9921** | **0.9982** | **0.9917** |
| cl_v6_tau03 | **0.9974** | 0.9914 | 0.9990 | **0.9971** | 0.9971 | <span style="color:red"><strong>1.0000</strong></span> | 0.9964 | <span style="color:red"><strong>0.9911</strong></span> | 0.9982 | **0.9915** | 0.9978 | 0.9900 |
| cl_v7_fair | **0.9972** | 0.9903 | 0.9982 | **0.9968** | 0.9974 | 0.9994 | 0.9971 | **0.9903** | 0.9982 | **0.9926** | **0.9986** | **0.9911** |

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
| cl_v6_tau01 | **0.9936** |
| cl_v6_tau02 | **0.9932** |
| cl_v6_tau03 | **0.9935** |
| cl_v7_fair | **0.9934** |

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
| cl_v6_tau01 | 0.9979 |
| cl_v6_tau02 | 0.9978 |
| cl_v6_tau03 | 0.9976 |
| cl_v7_fair | 0.9978 |

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
| cl_v6_tau01 | 0.9983 | 0.9976 | 0.9975 | **0.9915** | 0.9971 | 0.9931 | **0.9978** | **0.9954** | **0.9990** | **0.9964** | 0.9989 | **0.9973** |
| cl_v6_tau02 | 0.9983 | 0.9967 | 0.9973 | 0.9881 | 0.9965 | 0.9927 | **0.9981** | **0.9959** | 0.9990 | 0.9960 | **0.9991** | **0.9977** |
| cl_v6_tau03 | **0.9988** | 0.9958 | 0.9973 | 0.9884 | 0.9963 | 0.9919 | **0.9981** | **0.9963** | 0.9990 | 0.9960 | **0.9992** | **0.9981** |
| cl_v7_fair | 0.9985 | 0.9960 | 0.9968 | 0.9890 | 0.9966 | 0.9927 | **0.9980** | **0.9951** | 0.9988 | 0.9962 | 0.9990 | **0.9977** |

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
| cl_v6_tau01 | **0.9952** |
| cl_v6_tau02 | 0.9945 |
| cl_v6_tau03 | 0.9944 |
| cl_v7_fair | 0.9945 |

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
| cl_v6_tau01 | 0.9981 |
| cl_v6_tau02 | 0.9981 |
| cl_v6_tau03 | 0.9981 |
| cl_v7_fair | 0.9979 |

