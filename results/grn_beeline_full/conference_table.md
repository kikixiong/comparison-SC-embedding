# GRN BEELINE Full (Conference-style Tables)

说明：`-`表示该组合无结果；按列（同一dataset）比较：**加粗**表示优于baseline；<span style="color:red"><strong>红色加粗</strong></span>表示该列最优。
仅将`dataset`与`embedding`作为显式变量；其余设置作为表上方 latent variables 展示；`dataset_split`与`classifier`已聚合，不再展示拆分明细。

## AUROC (Main)

### Negative protocol: tf_stratified_1to10

Latent variables: metric=AUROC, negative_protocol=tf_stratified_1to10, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.7004 | 0.6687 | 0.8490 | 0.6981 | 0.5172 | <span style='color:red'><strong>0.8352</strong></span> | **0.7881** | <span style='color:red'><strong>0.8248</strong></span> | **0.7770** | **0.8265** | <span style='color:red'><strong>0.8020</strong></span> |
| baseline | <span style='color:red'><strong>0.7217</strong></span> | 0.6884 | <span style='color:red'><strong>0.8645</strong></span> | 0.7041 | <span style='color:red'><strong>0.6492</strong></span> | 0.8327 | 0.7802 | 0.8135 | 0.7479 | 0.8154 | 0.7720 |
| scGPT_human | 0.7086 | 0.6812 | 0.8379 | 0.6972 | 0.5750 | 0.8254 | 0.7571 | 0.8116 | **0.7670** | <span style='color:red'><strong>0.8275</strong></span> | 0.7698 |
| v4_bias_rec_best | 0.7042 | 0.6717 | 0.8591 | 0.6940 | 0.3836 | **0.8333** | 0.7745 | **0.8163** | <span style='color:red'><strong>0.7883</strong></span> | **0.8217** | **0.7779** |
| v4_plain_best | 0.7120 | 0.6567 | 0.8580 | **0.7180** | 0.6016 | 0.8305 | 0.7528 | **0.8176** | **0.7522** | **0.8193** | **0.7916** |
| v4_type_pe_best | 0.7116 | <span style='color:red'><strong>0.7099</strong></span> | 0.8596 | 0.6987 | 0.5125 | 0.8325 | <span style='color:red'><strong>0.7957</strong></span> | **0.8163** | **0.7601** | **0.8248** | **0.7855** |
| scconcept | 0.6249 | 0.6441 | 0.7970 | 0.6512 | 0.4531 | 0.8021 | 0.7257 | 0.7707 | 0.7090 | 0.8121 | 0.7066 |
| scconcept_encoded | 0.6572 | 0.6381 | 0.7945 | 0.6816 | 0.4297 | 0.7990 | 0.7435 | 0.7700 | 0.7272 | 0.7935 | 0.7046 |
| cl_scratch_v5 | 0.6992 | **0.6986** | 0.8587 | <span style='color:red'><strong>0.7196</strong></span> | 0.5398 | 0.8291 | **0.7890** | **0.8167** | **0.7752** | **0.8192** | **0.7727** |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.6678 | 0.6145 | **0.6785** | **0.7065** | **0.7966** | 0.6132 | 0.7799 | 0.7200 | **0.7364** | 0.6205 | **0.7315** | 0.6830 |
| baseline | 0.6683 | 0.6235 | 0.6782 | 0.6607 | 0.7864 | <span style='color:red'><strong>0.7388</strong></span> | <span style='color:red'><strong>0.7976</strong></span> | 0.7327 | 0.7245 | 0.6547 | 0.7229 | 0.6925 |
| scGPT_human | 0.6394 | **0.6331** | <span style='color:red'><strong>0.7047</strong></span> | <span style='color:red'><strong>0.7178</strong></span> | 0.7677 | 0.6963 | 0.7678 | <span style='color:red'><strong>0.7780</strong></span> | **0.7425** | <span style='color:red'><strong>0.7107</strong></span> | **0.7426** | **0.7174** |
| v4_bias_rec_best | 0.6350 | 0.5756 | 0.6679 | **0.6845** | 0.7839 | 0.7190 | 0.7726 | **0.7568** | **0.7541** | **0.6702** | **0.7297** | **0.6998** |
| v4_plain_best | 0.6640 | <span style='color:red'><strong>0.6442</strong></span> | **0.6991** | **0.6951** | <span style='color:red'><strong>0.8062</strong></span> | 0.7326 | 0.7749 | **0.7599** | 0.6902 | 0.6280 | 0.7005 | **0.7219** |
| v4_type_pe_best | <span style='color:red'><strong>0.6829</strong></span> | 0.5817 | 0.6591 | 0.5546 | **0.7981** | 0.7190 | 0.7825 | 0.7305 | **0.7491** | 0.6281 | <span style='color:red'><strong>0.7483</strong></span> | <span style='color:red'><strong>0.7597</strong></span> |
| scconcept | 0.5374 | 0.5681 | 0.5923 | 0.5559 | 0.6508 | 0.5157 | 0.6326 | 0.5130 | 0.6633 | **0.6696** | 0.6536 | 0.5894 |
| scconcept_encoded | 0.5441 | 0.5226 | 0.6119 | 0.5181 | 0.6020 | 0.6260 | 0.6527 | 0.5934 | 0.6461 | 0.5951 | 0.6946 | 0.5888 |
| cl_scratch_v5 | 0.6626 | 0.5998 | **0.6847** | **0.6853** | **0.7973** | 0.6744 | 0.7851 | 0.7154 | <span style='color:red'><strong>0.7558</strong></span> | 0.6334 | **0.7442** | **0.7309** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.8007 | 0.6105 | **0.8814** | **0.9081** | **0.8829** | **0.7928** | **0.9037** | <span style='color:red'><strong>0.9210</strong></span> | 0.8391 | **0.8363** | 0.8201 | **0.8423** |
| baseline | 0.8066 | 0.6697 | 0.8689 | 0.9048 | 0.8765 | 0.7720 | 0.8907 | 0.8952 | 0.8664 | 0.7448 | 0.8325 | 0.8173 |
| scGPT_human | <span style='color:red'><strong>0.8403</strong></span> | <span style='color:red'><strong>0.7591</strong></span> | **0.8775** | **0.9115** | 0.8633 | <span style='color:red'><strong>0.8710</strong></span> | **0.9003** | **0.9208** | **0.8705** | **0.7589** | **0.8475** | 0.8067 |
| v4_bias_rec_best | 0.8007 | **0.6981** | **0.8769** | 0.9038 | 0.8644 | **0.8612** | **0.9050** | 0.8877 | 0.8490 | **0.8254** | **0.8441** | <span style='color:red'><strong>0.8565</strong></span> |
| v4_plain_best | 0.7803 | **0.6944** | **0.8735** | **0.9086** | **0.8800** | **0.7966** | **0.8976** | **0.8962** | 0.8330 | **0.7636** | **0.8346** | **0.8274** |
| v4_type_pe_best | **0.8270** | **0.7240** | <span style='color:red'><strong>0.8827</strong></span> | <span style='color:red'><strong>0.9121</strong></span> | <span style='color:red'><strong>0.8926</strong></span> | **0.7842** | <span style='color:red'><strong>0.9122</strong></span> | 0.8827 | 0.8628 | <span style='color:red'><strong>0.8374</strong></span> | <span style='color:red'><strong>0.8559</strong></span> | **0.8349** |
| scconcept | 0.6642 | **0.7209** | 0.7761 | 0.7654 | 0.7643 | 0.6176 | 0.7623 | 0.7145 | 0.7043 | 0.5745 | 0.7065 | 0.7011 |
| scconcept_encoded | 0.6473 | **0.6960** | 0.7672 | 0.6745 | 0.7460 | 0.6478 | 0.6898 | 0.6649 | 0.6809 | 0.5950 | 0.7030 | 0.6732 |
| cl_scratch_v5 | **0.8099** | 0.6685 | **0.8826** | **0.9069** | **0.8855** | 0.7654 | **0.8924** | **0.9093** | <span style='color:red'><strong>0.8758</strong></span> | **0.7874** | **0.8526** | **0.8363** |

### Negative protocol: full_candidate

Latent variables: metric=AUROC, negative_protocol=full_candidate, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.8420 | 0.7997 | 0.8916 | 0.8154 | 0.7021 | **0.8983** | 0.8177 | **0.8736** | **0.7732** | <span style='color:red'><strong>0.8702</strong></span> | **0.7957** |
| baseline | 0.8548 | <span style='color:red'><strong>0.8241</strong></span> | 0.8973 | <span style='color:red'><strong>0.8366</strong></span> | 0.8515 | 0.8926 | 0.8321 | 0.8724 | 0.7633 | 0.8587 | 0.7857 |
| scGPT_human | 0.8420 | 0.8024 | 0.8779 | 0.8366 | 0.7912 | **0.8967** | 0.8032 | 0.8708 | 0.7590 | **0.8598** | 0.7696 |
| v4_bias_rec_best | 0.8547 | 0.8159 | **0.8983** | 0.8123 | 0.6732 | <span style='color:red'><strong>0.8996</strong></span> | **0.8329** | 0.8667 | <span style='color:red'><strong>0.7805</strong></span> | 0.8583 | 0.7799 |
| v4_plain_best | 0.8532 | 0.8090 | <span style='color:red'><strong>0.8988</strong></span> | 0.8087 | <span style='color:red'><strong>0.8517</strong></span> | **0.8992** | 0.8306 | **0.8737** | 0.7602 | **0.8604** | 0.7842 |
| v4_type_pe_best | <span style='color:red'><strong>0.8608</strong></span> | 0.8161 | **0.8976** | 0.8174 | 0.7654 | **0.8963** | **0.8330** | 0.8722 | 0.7614 | **0.8608** | <span style='color:red'><strong>0.7959</strong></span> |
| scconcept | 0.8265 | 0.8039 | 0.8424 | 0.7669 | 0.6766 | 0.8792 | 0.7806 | 0.8482 | 0.7263 | 0.8427 | 0.7158 |
| scconcept_encoded | 0.8312 | 0.7982 | 0.8410 | 0.8195 | 0.6115 | 0.8797 | 0.8003 | 0.8511 | 0.7275 | 0.8411 | 0.7136 |
| cl_scratch_v5 | 0.8357 | 0.8085 | 0.8958 | 0.8342 | 0.6906 | **0.8976** | <span style='color:red'><strong>0.8394</strong></span> | <span style='color:red'><strong>0.8744</strong></span> | **0.7682** | **0.8597** | 0.7787 |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.8906** | **0.8460** | <span style='color:red'><strong>0.8513</strong></span> | <span style='color:red'><strong>0.8318</strong></span> | **0.8732** | **0.6444** | <span style='color:red'><strong>0.8718</strong></span> | **0.8408** | 0.8301 | 0.7985 | 0.8247 | **0.8292** |
| baseline | 0.8865 | 0.8450 | 0.8405 | 0.7533 | 0.8687 | 0.6128 | 0.8697 | 0.8306 | 0.8431 | 0.8032 | 0.8384 | 0.7872 |
| scGPT_human | 0.8661 | **0.8584** | 0.8369 | **0.8094** | 0.8545 | <span style='color:red'><strong>0.7449</strong></span> | 0.8611 | **0.8579** | 0.8410 | 0.8030 | 0.8383 | **0.8484** |
| v4_bias_rec_best | 0.8778 | 0.8418 | 0.8214 | **0.7937** | 0.8635 | **0.6719** | 0.8587 | <span style='color:red'><strong>0.8646</strong></span> | **0.8508** | <span style='color:red'><strong>0.8315</strong></span> | 0.8242 | **0.8423** |
| v4_plain_best | <span style='color:red'><strong>0.8984</strong></span> | **0.8665** | **0.8497** | **0.7972** | **0.8748** | **0.6904** | 0.8663 | **0.8423** | **0.8482** | 0.7833 | 0.8269 | <span style='color:red'><strong>0.8491</strong></span> |
| v4_type_pe_best | **0.8964** | <span style='color:red'><strong>0.8680</strong></span> | **0.8466** | **0.7722** | 0.8680 | **0.6781** | 0.8651 | 0.8206 | <span style='color:red'><strong>0.8598</strong></span> | 0.7935 | <span style='color:red'><strong>0.8449</strong></span> | **0.8336** |
| scconcept | 0.8412 | 0.8381 | 0.7886 | **0.7818** | 0.7650 | 0.5705 | 0.7993 | 0.7146 | 0.7988 | 0.7612 | 0.8093 | 0.7455 |
| scconcept_encoded | 0.8456 | 0.7989 | 0.7940 | 0.7166 | 0.7387 | **0.6547** | 0.8008 | 0.7486 | 0.7631 | 0.7112 | 0.7802 | 0.7335 |
| cl_scratch_v5 | **0.8901** | **0.8568** | 0.8258 | 0.7512 | <span style='color:red'><strong>0.8776</strong></span> | **0.6580** | **0.8698** | **0.8419** | **0.8505** | 0.7774 | **0.8441** | **0.8141** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.8427 | 0.7640 | <span style='color:red'><strong>0.9021</strong></span> | 0.9037 | 0.9026 | **0.8602** | 0.8889 | <span style='color:red'><strong>0.9322</strong></span> | 0.8761 | **0.8521** | **0.8633** | <span style='color:red'><strong>0.8690</strong></span> |
| baseline | 0.8491 | 0.7796 | 0.8906 | <span style='color:red'><strong>0.9174</strong></span> | 0.9029 | 0.8596 | 0.8894 | 0.9076 | 0.8807 | 0.8289 | 0.8617 | 0.8545 |
| scGPT_human | 0.8379 | <span style='color:red'><strong>0.8775</strong></span> | **0.8972** | 0.9034 | 0.8920 | **0.8740** | **0.8916** | **0.9243** | 0.8778 | 0.7866 | 0.8580 | 0.8367 |
| v4_bias_rec_best | 0.8331 | **0.7964** | 0.8879 | 0.8990 | 0.8963 | **0.8674** | **0.8923** | 0.8989 | 0.8600 | **0.8325** | 0.8611 | **0.8648** |
| v4_plain_best | 0.8144 | **0.7925** | **0.8912** | 0.8978 | 0.9019 | **0.8869** | 0.8877 | 0.8949 | 0.8782 | 0.8209 | **0.8667** | **0.8669** |
| v4_type_pe_best | <span style='color:red'><strong>0.8520</strong></span> | **0.8115** | **0.8994** | 0.9087 | <span style='color:red'><strong>0.9064</strong></span> | **0.8709** | <span style='color:red'><strong>0.9053</strong></span> | 0.8955 | <span style='color:red'><strong>0.8828</strong></span> | <span style='color:red'><strong>0.8571</strong></span> | <span style='color:red'><strong>0.8865</strong></span> | **0.8553** |
| scconcept | 0.7705 | 0.7560 | 0.8494 | 0.7898 | 0.8353 | 0.7048 | 0.8361 | 0.8260 | 0.8154 | 0.6765 | 0.7940 | 0.7690 |
| scconcept_encoded | 0.7440 | 0.7258 | 0.8011 | 0.7920 | 0.8203 | 0.7396 | 0.8026 | 0.7942 | 0.7830 | 0.6602 | 0.7258 | 0.7562 |
| cl_scratch_v5 | 0.8363 | 0.7565 | 0.8884 | 0.8873 | 0.8992 | <span style='color:red'><strong>0.8907</strong></span> | 0.8881 | **0.9202** | 0.8742 | **0.8390** | **0.8826** | **0.8670** |

## AUPRC (Main)

### Negative protocol: tf_stratified_1to10

Latent variables: metric=AUPRC, negative_protocol=tf_stratified_1to10, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.4650 | 0.3945 | 0.7451 | **0.3619** | 0.1333 | 0.8919 | 0.7811 | <span style='color:red'><strong>0.8685</strong></span> | <span style='color:red'><strong>0.8067</strong></span> | <span style='color:red'><strong>0.8898</strong></span> | <span style='color:red'><strong>0.8501</strong></span> |
| baseline | <span style='color:red'><strong>0.4835</strong></span> | 0.4243 | <span style='color:red'><strong>0.7670</strong></span> | 0.3602 | 0.1704 | <span style='color:red'><strong>0.8923</strong></span> | 0.7898 | 0.8572 | 0.7764 | 0.8772 | 0.8176 |
| scGPT_human | 0.4802 | **0.4285** | 0.7351 | 0.3572 | <span style='color:red'><strong>0.2207</strong></span> | 0.8837 | 0.7621 | 0.8556 | **0.7924** | **0.8894** | **0.8225** |
| v4_bias_rec_best | 0.4585 | 0.4214 | 0.7518 | **0.3826** | 0.0860 | 0.8908 | 0.7745 | **0.8638** | **0.7960** | **0.8811** | **0.8260** |
| v4_plain_best | 0.4798 | 0.4018 | 0.7629 | <span style='color:red'><strong>0.3959</strong></span> | **0.1827** | 0.8894 | 0.7579 | **0.8621** | **0.7821** | **0.8782** | **0.8421** |
| v4_type_pe_best | 0.4798 | **0.4297** | 0.7618 | **0.3605** | 0.1540 | 0.8917 | <span style='color:red'><strong>0.7987</strong></span> | **0.8601** | **0.7913** | **0.8867** | **0.8339** |
| scconcept | 0.3888 | 0.3954 | 0.6809 | 0.3012 | **0.2064** | 0.8665 | 0.7010 | 0.8135 | 0.7500 | 0.8733 | 0.7585 |
| scconcept_encoded | 0.4057 | 0.3606 | 0.6534 | 0.2921 | 0.0943 | 0.8606 | 0.7328 | 0.8178 | 0.7561 | 0.8560 | 0.7590 |
| cl_scratch_v5 | 0.4542 | <span style='color:red'><strong>0.4427</strong></span> | 0.7550 | **0.3953** | 0.1421 | 0.8897 | 0.7853 | **0.8648** | **0.8056** | **0.8809** | **0.8183** |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.2320 | 0.2242 | 0.2621 | **0.2301** | **0.4104** | 0.2820 | **0.3718** | **0.3439** | **0.3494** | 0.2333 | **0.3089** | **0.2885** |
| baseline | 0.2374 | 0.2264 | 0.2795 | 0.2235 | 0.3821 | <span style='color:red'><strong>0.4860</strong></span> | 0.3613 | 0.3365 | 0.3182 | 0.2759 | 0.2754 | 0.2731 |
| scGPT_human | 0.2205 | <span style='color:red'><strong>0.2417</strong></span> | <span style='color:red'><strong>0.3495</strong></span> | <span style='color:red'><strong>0.3189</strong></span> | **0.4045** | 0.3009 | 0.3451 | <span style='color:red'><strong>0.4245</strong></span> | <span style='color:red'><strong>0.3821</strong></span> | <span style='color:red'><strong>0.4093</strong></span> | <span style='color:red'><strong>0.3398</strong></span> | <span style='color:red'><strong>0.4063</strong></span> |
| v4_bias_rec_best | 0.2096 | 0.1685 | 0.2234 | **0.2520** | 0.3757 | 0.4168 | 0.3392 | **0.3569** | **0.3773** | 0.2345 | **0.3012** | **0.2849** |
| v4_plain_best | 0.2217 | 0.2072 | **0.2848** | **0.2739** | 0.3634 | 0.3879 | 0.3552 | **0.3510** | **0.3241** | 0.2636 | 0.2686 | **0.3602** |
| v4_type_pe_best | <span style='color:red'><strong>0.2613</strong></span> | 0.1588 | **0.2883** | 0.1879 | **0.3830** | 0.3758 | 0.3478 | **0.3618** | **0.3420** | 0.2751 | **0.3195** | **0.4016** |
| scconcept | 0.1722 | 0.1743 | 0.2014 | 0.1349 | 0.2010 | 0.1560 | 0.1714 | 0.1179 | 0.1970 | 0.2357 | 0.2031 | 0.1576 |
| scconcept_encoded | 0.1504 | 0.1383 | 0.1830 | 0.1524 | 0.1656 | 0.1747 | 0.1742 | 0.1390 | 0.1852 | 0.1567 | 0.2009 | 0.1564 |
| cl_scratch_v5 | **0.2484** | 0.2197 | **0.2848** | **0.2268** | <span style='color:red'><strong>0.4347</strong></span> | 0.3722 | <span style='color:red'><strong>0.3903</strong></span> | 0.3223 | **0.3613** | 0.2240 | **0.3041** | **0.3479** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.3987 | 0.2852 | 0.5399 | **0.6128** | 0.5500 | 0.3464 | **0.6288** | **0.6565** | 0.4859 | **0.4456** | **0.4728** | **0.5042** |
| baseline | 0.4246 | 0.3138 | <span style='color:red'><strong>0.5550</strong></span> | 0.5806 | 0.5681 | 0.3583 | 0.6204 | 0.6304 | 0.5454 | 0.2662 | 0.4644 | 0.5012 |
| scGPT_human | <span style='color:red'><strong>0.4582</strong></span> | <span style='color:red'><strong>0.4131</strong></span> | 0.5272 | <span style='color:red'><strong>0.6196</strong></span> | 0.5268 | <span style='color:red'><strong>0.5559</strong></span> | <span style='color:red'><strong>0.6414</strong></span> | <span style='color:red'><strong>0.7016</strong></span> | <span style='color:red'><strong>0.5736</strong></span> | **0.2765** | <span style='color:red'><strong>0.5303</strong></span> | <span style='color:red'><strong>0.5406</strong></span> |
| v4_bias_rec_best | 0.3750 | 0.2451 | 0.5446 | 0.5664 | 0.5390 | **0.4608** | 0.6081 | **0.6503** | 0.4925 | <span style='color:red'><strong>0.5121</strong></span> | 0.4639 | **0.5402** |
| v4_plain_best | 0.3816 | 0.2748 | 0.5222 | 0.5799 | 0.5659 | **0.4109** | **0.6315** | **0.6477** | 0.4807 | **0.3074** | **0.4702** | **0.5344** |
| v4_type_pe_best | 0.4219 | **0.3834** | 0.5233 | 0.5784 | <span style='color:red'><strong>0.6014</strong></span> | 0.3546 | **0.6237** | **0.6341** | 0.5332 | **0.4569** | **0.4793** | 0.4936 |
| scconcept | 0.2093 | **0.3983** | 0.2853 | 0.2428 | 0.3274 | 0.2151 | 0.2896 | 0.2626 | 0.2125 | 0.1382 | 0.2414 | 0.3028 |
| scconcept_encoded | 0.1569 | 0.2549 | 0.2707 | 0.1792 | 0.2800 | 0.2170 | 0.2152 | 0.1849 | 0.1922 | 0.1365 | 0.2030 | 0.2433 |
| cl_scratch_v5 | 0.4113 | **0.3297** | 0.5369 | 0.5372 | 0.5639 | **0.4101** | 0.6182 | **0.6893** | **0.5594** | **0.3313** | **0.4983** | 0.4692 |

### Negative protocol: full_candidate

Latent variables: metric=AUPRC, negative_protocol=full_candidate, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.4392 | 0.3885 | 0.7633 | 0.3678 | 0.1196 | **0.8914** | 0.7493 | **0.8577** | <span style='color:red'><strong>0.8097</strong></span> | <span style='color:red'><strong>0.8932</strong></span> | **0.8338** |
| baseline | 0.4586 | 0.4212 | 0.7653 | <span style='color:red'><strong>0.3847</strong></span> | <span style='color:red'><strong>0.1930</strong></span> | 0.8812 | 0.7737 | 0.8571 | 0.7946 | 0.8818 | 0.8295 |
| scGPT_human | 0.4440 | 0.4162 | 0.7275 | 0.3744 | 0.1727 | <span style='color:red'><strong>0.8922</strong></span> | 0.7445 | 0.8563 | 0.7873 | **0.8825** | 0.8262 |
| v4_bias_rec_best | 0.4570 | 0.4159 | **0.7699** | 0.3441 | 0.1298 | **0.8912** | 0.7719 | 0.8518 | **0.7972** | **0.8823** | **0.8306** |
| v4_plain_best | **0.4739** | 0.4159 | <span style='color:red'><strong>0.7825</strong></span> | 0.3406 | 0.1651 | **0.8900** | **0.7760** | **0.8589** | 0.7870 | **0.8837** | 0.8280 |
| v4_type_pe_best | <span style='color:red'><strong>0.4836</strong></span> | <span style='color:red'><strong>0.4271</strong></span> | **0.7819** | 0.3294 | 0.1315 | **0.8887** | **0.7888** | 0.8551 | **0.7989** | **0.8837** | <span style='color:red'><strong>0.8436</strong></span> |
| scconcept | 0.4082 | 0.4115 | 0.6711 | 0.2498 | 0.1838 | 0.8671 | 0.6769 | 0.8226 | 0.7487 | 0.8634 | 0.7617 |
| scconcept_encoded | 0.4094 | 0.3858 | 0.6720 | 0.2890 | 0.0609 | 0.8681 | 0.7163 | 0.8298 | 0.7596 | 0.8613 | 0.7722 |
| cl_scratch_v5 | 0.4514 | 0.4189 | 0.7645 | 0.3663 | 0.1078 | **0.8887** | <span style='color:red'><strong>0.7903</strong></span> | <span style='color:red'><strong>0.8637</strong></span> | 0.7899 | **0.8830** | **0.8318** |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.1548** | 0.2019 | **0.1446** | **0.1237** | **0.2209** | **0.1332** | **0.2591** | **0.2519** | <span style='color:red'><strong>0.2683</strong></span> | 0.1488 | **0.2069** | **0.1677** |
| baseline | 0.1545 | <span style='color:red'><strong>0.2235</strong></span> | 0.1155 | 0.0906 | 0.1818 | 0.1265 | 0.2530 | 0.2107 | 0.2330 | 0.1621 | 0.1758 | 0.1387 |
| scGPT_human | 0.1514 | 0.2007 | <span style='color:red'><strong>0.2079</strong></span> | <span style='color:red'><strong>0.1301</strong></span> | <span style='color:red'><strong>0.2389</strong></span> | 0.0798 | **0.2567** | <span style='color:red'><strong>0.2685</strong></span> | **0.2600** | <span style='color:red'><strong>0.2106</strong></span> | **0.2007** | <span style='color:red'><strong>0.3169</strong></span> |
| v4_bias_rec_best | 0.1514 | 0.1783 | 0.1020 | **0.1244** | 0.1786 | 0.1227 | 0.2232 | **0.2353** | **0.2507** | 0.1573 | 0.1574 | **0.2603** |
| v4_plain_best | **0.1676** | 0.1891 | **0.1222** | **0.1270** | **0.2157** | 0.0791 | 0.2217 | 0.1853 | **0.2580** | 0.1506 | <span style='color:red'><strong>0.2341</strong></span> | **0.2768** |
| v4_type_pe_best | <span style='color:red'><strong>0.1715</strong></span> | 0.2045 | **0.1448** | **0.1047** | 0.1798 | 0.1172 | 0.2429 | **0.2299** | **0.2551** | **0.1991** | **0.2087** | **0.2655** |
| scconcept | 0.1303 | 0.1346 | 0.0736 | 0.0760 | 0.1067 | 0.0653 | 0.0797 | 0.0703 | 0.1017 | 0.0972 | 0.0989 | 0.0883 |
| scconcept_encoded | 0.1120 | 0.0925 | 0.0645 | 0.0473 | 0.0749 | 0.0233 | 0.0758 | 0.0824 | 0.0711 | 0.0721 | 0.0753 | 0.0888 |
| cl_scratch_v5 | **0.1668** | 0.2183 | **0.1643** | **0.1012** | **0.2320** | <span style='color:red'><strong>0.1342</strong></span> | <span style='color:red'><strong>0.2738</strong></span> | **0.2562** | **0.2407** | 0.1296 | **0.1908** | **0.2543** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | <span style='color:red'><strong>0.2633</strong></span> | 0.1699 | 0.4407 | 0.5099 | 0.4361 | **0.3563** | <span style='color:red'><strong>0.5105</strong></span> | **0.5577** | **0.3614** | **0.2107** | <span style='color:red'><strong>0.3464</strong></span> | **0.3080** |
| baseline | 0.2484 | 0.1700 | <span style='color:red'><strong>0.4466</strong></span> | 0.5505 | 0.4565 | 0.3554 | 0.4971 | 0.5255 | 0.3591 | 0.1569 | 0.2994 | 0.2705 |
| scGPT_human | 0.2283 | <span style='color:red'><strong>0.3573</strong></span> | 0.4324 | <span style='color:red'><strong>0.5691</strong></span> | 0.4391 | **0.3946** | **0.5010** | <span style='color:red'><strong>0.6067</strong></span> | **0.3843** | **0.1887** | **0.3409** | **0.3400** |
| v4_bias_rec_best | 0.2085 | 0.1344 | 0.4212 | 0.4852 | 0.4315 | **0.4145** | 0.4764 | **0.5641** | 0.3162 | <span style='color:red'><strong>0.2221</strong></span> | 0.2651 | **0.3476** |
| v4_plain_best | 0.2453 | 0.1652 | 0.4215 | 0.4862 | **0.4592** | <span style='color:red'><strong>0.4771</strong></span> | **0.5005** | **0.5474** | **0.3872** | **0.1908** | **0.3289** | **0.3299** |
| v4_type_pe_best | 0.2393 | 0.1532 | 0.4336 | 0.5148 | <span style='color:red'><strong>0.4832</strong></span> | **0.3867** | 0.4932 | **0.5644** | **0.3800** | **0.1678** | **0.3237** | <span style='color:red'><strong>0.4148</strong></span> |
| scconcept | 0.0477 | 0.1494 | 0.2499 | 0.1498 | 0.2192 | 0.0989 | 0.1407 | 0.1256 | 0.0968 | 0.0506 | 0.0995 | 0.1544 |
| scconcept_encoded | 0.0397 | 0.0820 | 0.1287 | 0.1374 | 0.1909 | 0.0749 | 0.1380 | 0.1323 | 0.0586 | 0.0357 | 0.0422 | 0.1117 |
| cl_scratch_v5 | 0.2191 | 0.1639 | 0.4326 | 0.4888 | 0.4558 | **0.4251** | **0.5021** | **0.5903** | <span style='color:red'><strong>0.3954</strong></span> | 0.1408 | **0.3157** | **0.3411** |

## AUPRC_LIFT (Main)

AUPRC_LIFT normalizes AUPRC by the random-ranking baseline, which equals the test positive ratio. It indicates how many times better the model ranks true edges compared with random expectation.

### Negative protocol: tf_stratified_1to10

Latent variables: metric=AUPRC_LIFT, negative_protocol=tf_stratified_1to10, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 1.6231 | 1.4798 | 2.3781 | **2.1612** | 1.4666 | 1.4510 | 1.6319 | <span style='color:red'><strong>1.5025</strong></span> | <span style='color:red'><strong>1.4585</strong></span> | <span style='color:red'><strong>1.4266</strong></span> | <span style='color:red'><strong>1.4437</strong></span> |
| baseline | <span style='color:red'><strong>1.6875</strong></span> | 1.5918 | <span style='color:red'><strong>2.4479</strong></span> | 2.1510 | 1.8741 | <span style='color:red'><strong>1.4517</strong></span> | 1.6501 | 1.4830 | 1.4038 | 1.4064 | 1.3884 |
| scGPT_human | 1.6759 | **1.6075** | 2.3461 | 2.1330 | <span style='color:red'><strong>2.4280</strong></span> | 1.4376 | 1.5923 | 1.4802 | **1.4326** | **1.4259** | **1.3968** |
| v4_bias_rec_best | 1.6005 | 1.5808 | 2.3994 | **2.2847** | 0.9464 | 1.4492 | 1.6182 | **1.4944** | **1.4391** | **1.4127** | **1.4027** |
| v4_plain_best | 1.6748 | 1.5072 | 2.4350 | <span style='color:red'><strong>2.3639</strong></span> | **2.0096** | 1.4469 | 1.5835 | **1.4914** | **1.4141** | **1.4079** | **1.4301** |
| v4_type_pe_best | 1.6745 | **1.6119** | 2.4316 | **2.1530** | 1.6936 | 1.4507 | <span style='color:red'><strong>1.6687</strong></span> | **1.4879** | **1.4308** | **1.4216** | **1.4162** |
| scconcept | 1.3569 | 1.4832 | 2.1732 | 1.7988 | **2.2700** | 1.4096 | 1.4646 | 1.4074 | 1.3560 | 1.4002 | 1.2880 |
| scconcept_encoded | 1.4161 | 1.3528 | 2.0856 | 1.7441 | 1.0371 | 1.4001 | 1.5311 | 1.4149 | 1.3671 | 1.3725 | 1.2889 |
| cl_scratch_v5 | 1.5852 | <span style='color:red'><strong>1.6610</strong></span> | 2.4098 | **2.3603** | 1.5633 | 1.4475 | 1.6408 | **1.4962** | **1.4565** | **1.4124** | **1.3895** |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 2.0042 | 2.0069 | 2.8828 | **2.5311** | **4.5139** | 3.1021 | **3.8354** | **3.4864** | **3.7316** | 2.5658 | **3.3316** | **3.1731** |
| baseline | 2.0513 | 2.0267 | 3.0748 | 2.4581 | 4.2026 | <span style='color:red'><strong>5.3455</strong></span> | 3.7265 | 3.4110 | 3.3983 | 3.0352 | 2.9695 | 3.0039 |
| scGPT_human | 1.9048 | <span style='color:red'><strong>2.1635</strong></span> | <span style='color:red'><strong>3.8448</strong></span> | <span style='color:red'><strong>3.5077</strong></span> | **4.4492** | 3.3104 | 3.5596 | <span style='color:red'><strong>4.3025</strong></span> | <span style='color:red'><strong>4.0799</strong></span> | <span style='color:red'><strong>4.5025</strong></span> | <span style='color:red'><strong>3.6645</strong></span> | <span style='color:red'><strong>4.4697</strong></span> |
| v4_bias_rec_best | 1.8105 | 1.5089 | 2.4578 | **2.7725** | 4.1325 | 4.5844 | 3.4986 | **3.6173** | **4.0287** | 2.5797 | **3.2483** | **3.1344** |
| v4_plain_best | 1.9154 | 1.8547 | **3.1326** | **3.0125** | 3.9970 | 4.2674 | 3.6633 | **3.5574** | **3.4610** | 2.8991 | 2.8969 | **3.9621** |
| v4_type_pe_best | <span style='color:red'><strong>2.2572</strong></span> | 1.4216 | **3.1712** | 2.0674 | **4.2127** | 4.1343 | 3.5879 | **3.6671** | **3.6522** | 3.0259 | **3.4455** | **4.4172** |
| scconcept | 1.4882 | 1.5608 | 2.2150 | 1.4840 | 2.2108 | 1.7165 | 1.7677 | 1.1953 | 2.1035 | 2.5925 | 2.1907 | 1.7336 |
| scconcept_encoded | 1.2991 | 1.2381 | 2.0127 | 1.6768 | 1.8215 | 1.9217 | 1.7965 | 1.4094 | 1.9781 | 1.7233 | 2.1670 | 1.7204 |
| cl_scratch_v5 | **2.1463** | 1.9672 | **3.1325** | **2.4946** | <span style='color:red'><strong>4.7814</strong></span> | 4.0940 | <span style='color:red'><strong>4.0256</strong></span> | 3.2674 | **3.8583** | 2.4641 | **3.2799** | **3.8264** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 4.3854 | 3.1370 | 5.9394 | **6.7044** | 6.0503 | 3.6847 | **6.9166** | **7.1154** | 5.3451 | **4.9012** | **5.2011** | **5.5463** |
| baseline | 4.6705 | 3.4515 | <span style='color:red'><strong>6.1055</strong></span> | 6.3516 | 6.2492 | 3.8111 | 6.8247 | 6.8332 | 5.9997 | 2.9282 | 5.1084 | 5.5136 |
| scGPT_human | <span style='color:red'><strong>5.0404</strong></span> | <span style='color:red'><strong>4.5445</strong></span> | 5.7987 | <span style='color:red'><strong>6.7782</strong></span> | 5.7950 | <span style='color:red'><strong>5.9130</strong></span> | <span style='color:red'><strong>7.0553</strong></span> | <span style='color:red'><strong>7.6041</strong></span> | <span style='color:red'><strong>6.3091</strong></span> | **3.0416** | <span style='color:red'><strong>5.8332</strong></span> | <span style='color:red'><strong>5.9468</strong></span> |
| v4_bias_rec_best | 4.1250 | 2.6962 | 5.9905 | 6.1965 | 5.9288 | **4.9016** | 6.6890 | **7.0487** | 5.4173 | <span style='color:red'><strong>5.6332</strong></span> | 5.1024 | **5.9422** |
| v4_plain_best | 4.1976 | 3.0224 | 5.7441 | 6.3440 | 6.2249 | **4.3708** | **6.9469** | **7.0201** | 5.2877 | **3.3819** | **5.1725** | **5.8783** |
| v4_type_pe_best | 4.6408 | **4.2178** | 5.7559 | 6.3281 | <span style='color:red'><strong>6.6157</strong></span> | 3.7716 | **6.8602** | **6.8724** | 5.8650 | **5.0261** | **5.2723** | 5.4293 |
| scconcept | 2.3026 | **4.3818** | 3.1388 | 2.6563 | 3.6019 | 2.2880 | 3.1853 | 2.8457 | 2.3371 | 1.5200 | 2.6557 | 3.3309 |
| scconcept_encoded | 1.7258 | 2.8039 | 2.9773 | 1.9600 | 3.0796 | 2.3077 | 2.3671 | 2.0046 | 2.1141 | 1.5014 | 2.2331 | 2.6758 |
| cl_scratch_v5 | 4.5242 | **3.6271** | 5.9062 | 5.8773 | 6.2025 | **4.3622** | 6.8003 | **7.4710** | **6.1534** | **3.6438** | **5.4814** | 5.1616 |

### Negative protocol: full_candidate

Latent variables: metric=AUPRC_LIFT, negative_protocol=full_candidate, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 2.7079 | 2.3997 | 3.3116 | 4.8466 | 3.4526 | **1.8046** | 1.8493 | **1.7590** | <span style='color:red'><strong>1.4639</strong></span> | <span style='color:red'><strong>1.5810</strong></span> | **1.4068** |
| baseline | 2.8276 | 2.6017 | 3.3203 | <span style='color:red'><strong>5.0696</strong></span> | <span style='color:red'><strong>5.5715</strong></span> | 1.7837 | 1.9096 | 1.7578 | 1.4367 | 1.5609 | 1.3997 |
| scGPT_human | 2.7372 | 2.5710 | 3.1560 | 4.9334 | 4.9854 | <span style='color:red'><strong>1.8060</strong></span> | 1.8375 | 1.7562 | 1.4235 | **1.5621** | 1.3940 |
| v4_bias_rec_best | 2.8172 | 2.5692 | **3.3401** | 4.5353 | 3.7470 | **1.8040** | 1.9051 | 1.7470 | **1.4413** | **1.5617** | **1.4014** |
| v4_plain_best | **2.9214** | 2.5694 | <span style='color:red'><strong>3.3948</strong></span> | 4.4889 | 4.7659 | **1.8016** | **1.9153** | **1.7615** | 1.4229 | **1.5641** | 1.3971 |
| v4_type_pe_best | <span style='color:red'><strong>2.9813</strong></span> | <span style='color:red'><strong>2.6383</strong></span> | **3.3923** | 4.3404 | 3.7961 | **1.7989** | **1.9468** | 1.7538 | **1.4445** | **1.5642** | <span style='color:red'><strong>1.4234</strong></span> |
| scconcept | 2.5169 | 2.5419 | 2.9115 | 3.2919 | 5.3065 | 1.7554 | 1.6706 | 1.6872 | 1.3536 | 1.5283 | 1.2851 |
| scconcept_encoded | 2.5242 | 2.3836 | 2.9154 | 3.8090 | 1.7571 | 1.7572 | 1.7680 | 1.7018 | 1.3733 | 1.5246 | 1.3028 |
| cl_scratch_v5 | 2.7832 | 2.5877 | 3.3167 | 4.8272 | 3.1130 | **1.7991** | <span style='color:red'><strong>1.9505</strong></span> | <span style='color:red'><strong>1.7714</strong></span> | 1.4281 | **1.5630** | **1.4035** |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **9.3147** | 8.9030 | **13.0763** | **7.4170** | **15.4089** | **9.8176** | **16.1215** | **9.2746** | <span style='color:red'><strong>21.6974</strong></span> | 6.6323 | **15.6081** | **6.7548** |
| baseline | 9.3012 | <span style='color:red'><strong>9.8550</strong></span> | 10.4433 | 5.4356 | 12.6841 | 9.3292 | 15.7458 | 7.7592 | 18.8433 | 7.2224 | 13.2607 | 5.5884 |
| scGPT_human | 9.1115 | 8.8506 | <span style='color:red'><strong>18.7911</strong></span> | <span style='color:red'><strong>7.8038</strong></span> | <span style='color:red'><strong>16.6627</strong></span> | 5.8807 | **15.9744** | <span style='color:red'><strong>9.8867</strong></span> | **21.0316** | <span style='color:red'><strong>9.3851</strong></span> | **15.1446** | <span style='color:red'><strong>12.7637</strong></span> |
| v4_bias_rec_best | 9.1110 | 7.8635 | 9.2224 | **7.4618** | 12.4601 | 9.0440 | 13.8877 | **8.6620** | **20.2765** | 7.0108 | 11.8768 | **10.4858** |
| v4_plain_best | **10.0900** | 8.3404 | **11.0457** | **7.6157** | **15.0506** | 5.8328 | 13.7982 | 6.8233 | **20.8712** | 6.7131 | <span style='color:red'><strong>17.6623</strong></span> | **11.1487** |
| v4_type_pe_best | <span style='color:red'><strong>10.3207</strong></span> | 9.0156 | **13.0913** | **6.2757** | 12.5456 | 8.6422 | 15.1114 | **8.4660** | **20.6348** | **8.8739** | **15.7418** | **10.6961** |
| scconcept | 7.8424 | 5.9363 | 6.6508 | 4.5599 | 7.4418 | 4.8148 | 4.9595 | 2.5866 | 8.2279 | 4.3336 | 7.4649 | 3.5562 |
| scconcept_encoded | 6.7415 | 4.0800 | 5.8311 | 2.8376 | 5.2268 | 1.7161 | 4.7187 | 3.0320 | 5.7471 | 3.2120 | 5.6804 | 3.5756 |
| cl_scratch_v5 | **10.0390** | 9.6253 | **14.8518** | **6.0696** | **16.1839** | <span style='color:red'><strong>9.8926</strong></span> | <span style='color:red'><strong>17.0393</strong></span> | **9.4331** | **19.4713** | 5.7753 | **14.3934** | **10.2454** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | <span style='color:red'><strong>27.5724</strong></span> | 14.7483 | 25.0754 | 18.4848 | 19.2620 | **13.7444** | <span style='color:red'><strong>33.5703</strong></span> | **26.0161** | **36.8470** | **17.2883** | <span style='color:red'><strong>35.6446</strong></span> | **22.0118** |
| baseline | 26.0197 | 14.7561 | <span style='color:red'><strong>25.4086</strong></span> | 19.9594 | 20.1643 | 13.7115 | 32.6912 | 24.5131 | 36.6067 | 12.8669 | 30.8046 | 19.3318 |
| scGPT_human | 23.9111 | <span style='color:red'><strong>31.0030</strong></span> | 24.6001 | <span style='color:red'><strong>20.6329</strong></span> | 19.3948 | **15.2234** | **32.9451** | <span style='color:red'><strong>28.3019</strong></span> | **39.1794** | **15.4809** | **35.0796** | **24.3012** |
| v4_bias_rec_best | 21.8359 | 11.6616 | 23.9656 | 17.5895 | 19.0591 | **15.9911** | 31.3245 | **26.3110** | 32.2372 | <span style='color:red'><strong>18.2161</strong></span> | 27.2789 | **24.8432** |
| v4_plain_best | 25.6916 | 14.3332 | 23.9796 | 17.6248 | **20.2817** | <span style='color:red'><strong>18.4030</strong></span> | **32.9133** | **25.5315** | **39.4743** | **15.6527** | **33.8483** | **23.5815** |
| v4_type_pe_best | 25.0587 | 13.2936 | 24.6724 | 18.6629 | <span style='color:red'><strong>21.3439</strong></span> | **14.9156** | 32.4320 | **26.3256** | **38.7361** | **13.7625** | **33.3117** | <span style='color:red'><strong>29.6484</strong></span> |
| scconcept | 4.9998 | 12.9653 | 14.2204 | 5.4316 | 9.6833 | 3.8137 | 9.2512 | 5.8602 | 9.8655 | 4.1476 | 10.2398 | 11.0357 |
| scconcept_encoded | 4.1623 | 7.1172 | 7.3228 | 4.9799 | 8.4336 | 2.8898 | 9.0736 | 6.1720 | 5.9760 | 2.9303 | 4.3421 | 7.9866 |
| cl_scratch_v5 | 22.9494 | 14.2246 | 24.6123 | 17.7213 | 20.1329 | **16.4004** | **33.0155** | **27.5360** | <span style='color:red'><strong>40.3130</strong></span> | 11.5530 | **32.4867** | **24.3785** |

## PRECISION_AT_K (Supplementary)

### Negative protocol: tf_stratified_1to10

Latent variables: metric=PRECISION_AT_K, negative_protocol=tf_stratified_1to10, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.4745 | 0.3905 | 0.6861 | 0.3714 | 0.1875 | 0.8003 | 0.7128 | <span style='color:red'><strong>0.7877</strong></span> | **0.7277** | **0.8016** | <span style='color:red'><strong>0.7700</strong></span> |
| baseline | 0.4745 | 0.4231 | 0.6992 | 0.3750 | 0.1875 | 0.8016 | <span style='color:red'><strong>0.7149</strong></span> | 0.7774 | 0.7188 | 0.7944 | 0.7491 |
| scGPT_human | <span style='color:red'><strong>0.4842</strong></span> | 0.4172 | 0.6617 | **0.3786** | <span style='color:red'><strong>0.2500</strong></span> | <span style='color:red'><strong>0.8030</strong></span> | 0.6851 | 0.7738 | **0.7277** | <span style='color:red'><strong>0.8038</strong></span> | **0.7509** |
| v4_bias_rec_best | 0.4660 | 0.4083 | 0.6955 | **0.3893** | 0.0625 | 0.7993 | 0.7021 | 0.7753 | <span style='color:red'><strong>0.7533</strong></span> | **0.8014** | **0.7591** |
| v4_plain_best | **0.4782** | 0.4172 | <span style='color:red'><strong>0.7011</strong></span> | <span style='color:red'><strong>0.3964</strong></span> | 0.1875 | 0.7979 | 0.6915 | **0.7818** | 0.7154 | **0.7980** | **0.7645** |
| v4_type_pe_best | **0.4757** | **0.4497** | 0.6992 | 0.3643 | 0.0625 | 0.7979 | 0.7149 | **0.7798** | **0.7333** | **0.7985** | **0.7600** |
| scconcept | 0.4005 | 0.4024 | 0.6523 | 0.3143 | 0.1875 | 0.7817 | 0.6511 | 0.7487 | 0.6808 | **0.7978** | 0.7118 |
| scconcept_encoded | 0.4211 | 0.4024 | 0.6335 | 0.3500 | 0.0625 | 0.7797 | 0.6681 | 0.7460 | 0.6953 | 0.7849 | 0.7027 |
| cl_scratch_v5 | 0.4612 | <span style='color:red'><strong>0.4527</strong></span> | 0.6823 | **0.3821** | <span style='color:red'><strong>0.2500</strong></span> | 0.7976 | 0.6915 | 0.7741 | **0.7321** | **0.7973** | **0.7564** |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.2609 | <span style='color:red'><strong>0.2381</strong></span> | 0.2938 | **0.2586** | **0.4457** | 0.3182 | <span style='color:red'><strong>0.4045</strong></span> | 0.3258 | **0.3540** | **0.3077** | **0.3333** | 0.2500 |
| baseline | 0.2857 | 0.2024 | 0.2990 | 0.2069 | 0.3915 | <span style='color:red'><strong>0.4545</strong></span> | 0.3792 | 0.3485 | 0.3212 | 0.2821 | 0.3137 | 0.2717 |
| scGPT_human | 0.2360 | **0.2143** | <span style='color:red'><strong>0.3351</strong></span> | <span style='color:red'><strong>0.3276</strong></span> | **0.4302** | 0.3182 | **0.3876** | <span style='color:red'><strong>0.4242</strong></span> | **0.3723** | <span style='color:red'><strong>0.4103</strong></span> | <span style='color:red'><strong>0.3529</strong></span> | **0.3804** |
| v4_bias_rec_best | 0.2391 | 0.1905 | 0.2732 | **0.2931** | **0.4070** | <span style='color:red'><strong>0.4545</strong></span> | 0.3371 | 0.3182 | <span style='color:red'><strong>0.4088</strong></span> | 0.2821 | **0.3170** | **0.2826** |
| v4_plain_best | 0.2453 | 0.2024 | **0.3093** | **0.2931** | 0.3566 | 0.3636 | **0.3876** | **0.3636** | **0.3358** | 0.2821 | 0.3039 | **0.3478** |
| v4_type_pe_best | <span style='color:red'><strong>0.3106</strong></span> | 0.1786 | **0.3093** | 0.1897 | **0.4225** | <span style='color:red'><strong>0.4545</strong></span> | 0.3596 | **0.3788** | 0.3212 | 0.2564 | **0.3301** | <span style='color:red'><strong>0.4130</strong></span> |
| scconcept | 0.1677 | 0.1786 | 0.1856 | 0.1897 | 0.2519 | 0.1818 | 0.1854 | 0.1136 | 0.2372 | 0.2436 | 0.2288 | 0.1848 |
| scconcept_encoded | 0.1304 | 0.1548 | 0.1804 | 0.1207 | 0.2132 | 0.2727 | 0.2022 | 0.1515 | 0.2080 | 0.2179 | 0.2255 | 0.1522 |
| cl_scratch_v5 | 0.2857 | **0.2262** | 0.2990 | **0.2414** | <span style='color:red'><strong>0.4496</strong></span> | 0.4091 | <span style='color:red'><strong>0.4045</strong></span> | 0.3182 | **0.3796** | 0.2436 | **0.3170** | **0.3913** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.4076 | 0.2812 | 0.5070 | **0.5448** | **0.5789** | **0.4091** | **0.5914** | 0.6048 | 0.4612 | **0.4516** | **0.4662** | **0.4706** |
| baseline | 0.4286 | 0.3281 | <span style='color:red'><strong>0.5302</strong></span> | 0.5373 | 0.5694 | 0.3636 | 0.5806 | 0.6210 | 0.5233 | 0.1935 | 0.4561 | 0.4412 |
| scGPT_human | **0.4580** | **0.3750** | 0.5116 | <span style='color:red'><strong>0.5970</strong></span> | 0.5407 | <span style='color:red'><strong>0.5758</strong></span> | **0.6048** | **0.6371** | <span style='color:red'><strong>0.5271</strong></span> | **0.2742** | <span style='color:red'><strong>0.5034</strong></span> | **0.4706** |
| v4_bias_rec_best | 0.3908 | 0.3125 | <span style='color:red'><strong>0.5302</strong></span> | **0.5821** | 0.5359 | **0.4394** | 0.5699 | <span style='color:red'><strong>0.6532</strong></span> | 0.4612 | <span style='color:red'><strong>0.4839</strong></span> | 0.4426 | <span style='color:red'><strong>0.5441</strong></span> |
| v4_plain_best | 0.3866 | **0.3594** | 0.4977 | **0.5597** | 0.5526 | **0.4091** | **0.6048** | <span style='color:red'><strong>0.6532</strong></span> | 0.4574 | **0.3226** | 0.4291 | **0.4706** |
| v4_type_pe_best | <span style='color:red'><strong>0.4622</strong></span> | **0.3750** | 0.4953 | **0.5597** | **0.5909** | **0.4242** | <span style='color:red'><strong>0.6156</strong></span> | **0.6290** | 0.4845 | **0.4677** | **0.4865** | **0.4853** |
| scconcept | 0.2395 | <span style='color:red'><strong>0.3906</strong></span> | 0.3233 | 0.3209 | 0.3995 | 0.2576 | 0.3038 | 0.3145 | 0.2558 | 0.1290 | 0.3007 | 0.3235 |
| scconcept_encoded | 0.2101 | 0.2344 | 0.3140 | 0.1642 | 0.3230 | 0.2273 | 0.2634 | 0.2097 | 0.2481 | 0.1129 | 0.2635 | 0.2500 |
| cl_scratch_v5 | 0.3992 | 0.3281 | 0.5116 | 0.5149 | <span style='color:red'><strong>0.5909</strong></span> | **0.4697** | **0.6048** | <span style='color:red'><strong>0.6532</strong></span> | 0.5155 | **0.3226** | 0.4561 | 0.4412 |

### Negative protocol: full_candidate

Latent variables: metric=PRECISION_AT_K, negative_protocol=full_candidate, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.4757** | 0.3905 | 0.7011 | 0.3929 | <span style='color:red'><strong>0.1875</strong></span> | **0.8050** | 0.6723 | 0.7774 | **0.7344** | <span style='color:red'><strong>0.8115</strong></span> | <span style='color:red'><strong>0.7836</strong></span> |
| baseline | 0.4709 | 0.4172 | <span style='color:red'><strong>0.7124</strong></span> | 0.4071 | <span style='color:red'><strong>0.1875</strong></span> | 0.7966 | 0.6830 | 0.7783 | 0.7288 | 0.8028 | 0.7636 |
| scGPT_human | **0.4733** | **0.4467** | 0.6748 | 0.3964 | <span style='color:red'><strong>0.1875</strong></span> | **0.8026** | 0.6681 | 0.7765 | 0.7243 | **0.8043** | 0.7482 |
| v4_bias_rec_best | **0.4769** | **0.4260** | 0.7011 | 0.3429 | 0.0625 | <span style='color:red'><strong>0.8080</strong></span> | **0.6872** | 0.7715 | <span style='color:red'><strong>0.7400</strong></span> | 0.7976 | 0.7591 |
| v4_plain_best | **0.4818** | **0.4231** | 0.7030 | 0.3357 | 0.1250 | **0.8074** | **0.7043** | <span style='color:red'><strong>0.7792</strong></span> | 0.7221 | 0.7990 | 0.7627 |
| v4_type_pe_best | <span style='color:red'><strong>0.4964</strong></span> | **0.4408** | 0.6880 | 0.3536 | <span style='color:red'><strong>0.1875</strong></span> | **0.8033** | <span style='color:red'><strong>0.7064</strong></span> | **0.7786** | 0.7266 | **0.8038** | **0.7736** |
| scconcept | 0.4393 | <span style='color:red'><strong>0.4497</strong></span> | 0.6391 | 0.3071 | <span style='color:red'><strong>0.1875</strong></span> | 0.7868 | 0.6404 | 0.7555 | 0.7143 | 0.7877 | 0.7255 |
| scconcept_encoded | 0.4223 | **0.4231** | 0.6523 | 0.3464 | 0.0000 | 0.7861 | 0.6596 | 0.7543 | 0.6987 | 0.7873 | 0.7227 |
| cl_scratch_v5 | 0.4636 | 0.4142 | 0.6805 | <span style='color:red'><strong>0.4107</strong></span> | <span style='color:red'><strong>0.1875</strong></span> | **0.8013** | **0.6957** | 0.7783 | **0.7288** | 0.8019 | 0.7618 |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.2236** | **0.2738** | **0.1804** | **0.1724** | **0.2868** | <span style='color:red'><strong>0.1818</strong></span> | **0.3174** | **0.2803** | **0.2737** | **0.1795** | **0.2549** | 0.1630 |
| baseline | 0.2112 | 0.2619 | 0.1546 | 0.1552 | 0.2481 | 0.1364 | 0.3006 | 0.2576 | 0.2518 | 0.1667 | 0.2320 | 0.1957 |
| scGPT_human | 0.1957 | 0.2143 | <span style='color:red'><strong>0.2320</strong></span> | <span style='color:red'><strong>0.1897</strong></span> | <span style='color:red'><strong>0.3062</strong></span> | 0.0909 | **0.3090** | **0.2955** | <span style='color:red'><strong>0.2956</strong></span> | <span style='color:red'><strong>0.2564</strong></span> | <span style='color:red'><strong>0.2582</strong></span> | **0.2826** |
| v4_bias_rec_best | **0.2174** | 0.2024 | **0.2062** | <span style='color:red'><strong>0.1897</strong></span> | **0.2674** | 0.1364 | 0.2809 | 0.2500 | **0.2664** | **0.2308** | 0.2222 | **0.2935** |
| v4_plain_best | <span style='color:red'><strong>0.2391</strong></span> | 0.2500 | **0.1856** | <span style='color:red'><strong>0.1897</strong></span> | **0.2868** | 0.1364 | 0.2809 | 0.2424 | **0.2664** | **0.1795** | **0.2516** | <span style='color:red'><strong>0.3261</strong></span> |
| v4_type_pe_best | **0.2267** | <span style='color:red'><strong>0.2738</strong></span> | **0.1907** | 0.1207 | **0.2674** | 0.1364 | 0.2978 | **0.2727** | <span style='color:red'><strong>0.2956</strong></span> | **0.2179** | <span style='color:red'><strong>0.2582</strong></span> | **0.3043** |
| scconcept | 0.1863 | 0.1548 | 0.0979 | 0.0690 | 0.1899 | 0.0455 | 0.1292 | 0.0682 | 0.1387 | 0.1410 | 0.1667 | 0.1630 |
| scconcept_encoded | 0.1335 | 0.0714 | 0.0928 | 0.0517 | 0.1279 | 0.0000 | 0.1236 | 0.1212 | 0.1058 | 0.0769 | 0.1242 | 0.1087 |
| cl_scratch_v5 | **0.2329** | 0.2619 | **0.2062** | 0.1207 | **0.2946** | <span style='color:red'><strong>0.1818</strong></span> | <span style='color:red'><strong>0.3202</strong></span> | <span style='color:red'><strong>0.3106</strong></span> | <span style='color:red'><strong>0.2956</strong></span> | 0.1667 | 0.2059 | <span style='color:red'><strong>0.3261</strong></span> |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | <span style='color:red'><strong>0.3025</strong></span> | 0.2031 | <span style='color:red'><strong>0.4698</strong></span> | 0.5075 | <span style='color:red'><strong>0.4976</strong></span> | **0.4242** | **0.5081** | **0.5484** | 0.3643 | <span style='color:red'><strong>0.2903</strong></span> | <span style='color:red'><strong>0.3682</strong></span> | **0.3382** |
| baseline | 0.2815 | 0.2031 | 0.4558 | 0.5522 | 0.4785 | 0.3939 | 0.5054 | 0.5081 | 0.3837 | 0.2258 | 0.3176 | 0.3235 |
| scGPT_human | **0.2857** | <span style='color:red'><strong>0.3438</strong></span> | 0.4535 | <span style='color:red'><strong>0.5597</strong></span> | 0.4617 | **0.4848** | 0.4839 | <span style='color:red'><strong>0.5968</strong></span> | <span style='color:red'><strong>0.4031</strong></span> | **0.2581** | **0.3649** | **0.3382** |
| v4_bias_rec_best | 0.2815 | 0.1875 | **0.4605** | 0.5075 | 0.4641 | **0.4091** | 0.4946 | **0.5565** | 0.3256 | **0.2903** | **0.3243** | **0.4118** |
| v4_plain_best | 0.2731 | **0.2188** | 0.4372 | 0.4627 | 0.4641 | <span style='color:red'><strong>0.5152</strong></span> | **0.5081** | **0.5161** | **0.3915** | **0.2581** | **0.3277** | **0.3529** |
| v4_type_pe_best | **0.2983** | 0.2031 | 0.4488 | 0.5373 | **0.4904** | **0.4242** | 0.5054 | **0.5645** | **0.3876** | **0.2258** | **0.3412** | <span style='color:red'><strong>0.4265</strong></span> |
| scconcept | 0.0882 | **0.2188** | 0.2977 | 0.1940 | 0.2919 | 0.1364 | 0.2097 | 0.1694 | 0.1318 | 0.0323 | 0.1385 | 0.1765 |
| scconcept_encoded | 0.0714 | 0.1719 | 0.1837 | 0.2015 | 0.2990 | 0.0758 | 0.2016 | 0.1452 | 0.1008 | 0.0806 | 0.0642 | 0.1618 |
| cl_scratch_v5 | 0.2773 | **0.2344** | 0.4535 | 0.4851 | **0.4952** | **0.4848** | <span style='color:red'><strong>0.5188</strong></span> | <span style='color:red'><strong>0.5968</strong></span> | **0.3992** | 0.1935 | **0.3243** | **0.3676** |

## RECALL_AT_K (Supplementary)

### Negative protocol: tf_stratified_1to10

Latent variables: metric=RECALL_AT_K, negative_protocol=tf_stratified_1to10, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.4745 | 0.3905 | 0.6861 | 0.3714 | 0.1875 | 0.8003 | 0.7128 | <span style='color:red'><strong>0.7877</strong></span> | **0.7277** | **0.8016** | <span style='color:red'><strong>0.7700</strong></span> |
| baseline | 0.4745 | 0.4231 | 0.6992 | 0.3750 | 0.1875 | 0.8016 | <span style='color:red'><strong>0.7149</strong></span> | 0.7774 | 0.7188 | 0.7944 | 0.7491 |
| scGPT_human | <span style='color:red'><strong>0.4842</strong></span> | 0.4172 | 0.6617 | **0.3786** | <span style='color:red'><strong>0.2500</strong></span> | <span style='color:red'><strong>0.8030</strong></span> | 0.6851 | 0.7738 | **0.7277** | <span style='color:red'><strong>0.8038</strong></span> | **0.7509** |
| v4_bias_rec_best | 0.4660 | 0.4083 | 0.6955 | **0.3893** | 0.0625 | 0.7993 | 0.7021 | 0.7753 | <span style='color:red'><strong>0.7533</strong></span> | **0.8014** | **0.7591** |
| v4_plain_best | **0.4782** | 0.4172 | <span style='color:red'><strong>0.7011</strong></span> | <span style='color:red'><strong>0.3964</strong></span> | 0.1875 | 0.7979 | 0.6915 | **0.7818** | 0.7154 | **0.7980** | **0.7645** |
| v4_type_pe_best | **0.4757** | **0.4497** | 0.6992 | 0.3643 | 0.0625 | 0.7979 | 0.7149 | **0.7798** | **0.7333** | **0.7985** | **0.7600** |
| scconcept | 0.4005 | 0.4024 | 0.6523 | 0.3143 | 0.1875 | 0.7817 | 0.6511 | 0.7487 | 0.6808 | **0.7978** | 0.7118 |
| scconcept_encoded | 0.4211 | 0.4024 | 0.6335 | 0.3500 | 0.0625 | 0.7797 | 0.6681 | 0.7460 | 0.6953 | 0.7849 | 0.7027 |
| cl_scratch_v5 | 0.4612 | <span style='color:red'><strong>0.4527</strong></span> | 0.6823 | **0.3821** | <span style='color:red'><strong>0.2500</strong></span> | 0.7976 | 0.6915 | 0.7741 | **0.7321** | **0.7973** | **0.7564** |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.2609 | <span style='color:red'><strong>0.2381</strong></span> | 0.2938 | **0.2586** | **0.4457** | 0.3182 | <span style='color:red'><strong>0.4045</strong></span> | 0.3258 | **0.3540** | **0.3077** | **0.3333** | 0.2500 |
| baseline | 0.2857 | 0.2024 | 0.2990 | 0.2069 | 0.3915 | <span style='color:red'><strong>0.4545</strong></span> | 0.3792 | 0.3485 | 0.3212 | 0.2821 | 0.3137 | 0.2717 |
| scGPT_human | 0.2360 | **0.2143** | <span style='color:red'><strong>0.3351</strong></span> | <span style='color:red'><strong>0.3276</strong></span> | **0.4302** | 0.3182 | **0.3876** | <span style='color:red'><strong>0.4242</strong></span> | **0.3723** | <span style='color:red'><strong>0.4103</strong></span> | <span style='color:red'><strong>0.3529</strong></span> | **0.3804** |
| v4_bias_rec_best | 0.2391 | 0.1905 | 0.2732 | **0.2931** | **0.4070** | <span style='color:red'><strong>0.4545</strong></span> | 0.3371 | 0.3182 | <span style='color:red'><strong>0.4088</strong></span> | 0.2821 | **0.3170** | **0.2826** |
| v4_plain_best | 0.2453 | 0.2024 | **0.3093** | **0.2931** | 0.3566 | 0.3636 | **0.3876** | **0.3636** | **0.3358** | 0.2821 | 0.3039 | **0.3478** |
| v4_type_pe_best | <span style='color:red'><strong>0.3106</strong></span> | 0.1786 | **0.3093** | 0.1897 | **0.4225** | <span style='color:red'><strong>0.4545</strong></span> | 0.3596 | **0.3788** | 0.3212 | 0.2564 | **0.3301** | <span style='color:red'><strong>0.4130</strong></span> |
| scconcept | 0.1677 | 0.1786 | 0.1856 | 0.1897 | 0.2519 | 0.1818 | 0.1854 | 0.1136 | 0.2372 | 0.2436 | 0.2288 | 0.1848 |
| scconcept_encoded | 0.1304 | 0.1548 | 0.1804 | 0.1207 | 0.2132 | 0.2727 | 0.2022 | 0.1515 | 0.2080 | 0.2179 | 0.2255 | 0.1522 |
| cl_scratch_v5 | 0.2857 | **0.2262** | 0.2990 | **0.2414** | <span style='color:red'><strong>0.4496</strong></span> | 0.4091 | <span style='color:red'><strong>0.4045</strong></span> | 0.3182 | **0.3796** | 0.2436 | **0.3170** | **0.3913** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.4076 | 0.2812 | 0.5070 | **0.5448** | **0.5789** | **0.4091** | **0.5914** | 0.6048 | 0.4612 | **0.4516** | **0.4662** | **0.4706** |
| baseline | 0.4286 | 0.3281 | <span style='color:red'><strong>0.5302</strong></span> | 0.5373 | 0.5694 | 0.3636 | 0.5806 | 0.6210 | 0.5233 | 0.1935 | 0.4561 | 0.4412 |
| scGPT_human | **0.4580** | **0.3750** | 0.5116 | <span style='color:red'><strong>0.5970</strong></span> | 0.5407 | <span style='color:red'><strong>0.5758</strong></span> | **0.6048** | **0.6371** | <span style='color:red'><strong>0.5271</strong></span> | **0.2742** | <span style='color:red'><strong>0.5034</strong></span> | **0.4706** |
| v4_bias_rec_best | 0.3908 | 0.3125 | <span style='color:red'><strong>0.5302</strong></span> | **0.5821** | 0.5359 | **0.4394** | 0.5699 | <span style='color:red'><strong>0.6532</strong></span> | 0.4612 | <span style='color:red'><strong>0.4839</strong></span> | 0.4426 | <span style='color:red'><strong>0.5441</strong></span> |
| v4_plain_best | 0.3866 | **0.3594** | 0.4977 | **0.5597** | 0.5526 | **0.4091** | **0.6048** | <span style='color:red'><strong>0.6532</strong></span> | 0.4574 | **0.3226** | 0.4291 | **0.4706** |
| v4_type_pe_best | <span style='color:red'><strong>0.4622</strong></span> | **0.3750** | 0.4953 | **0.5597** | **0.5909** | **0.4242** | <span style='color:red'><strong>0.6156</strong></span> | **0.6290** | 0.4845 | **0.4677** | **0.4865** | **0.4853** |
| scconcept | 0.2395 | <span style='color:red'><strong>0.3906</strong></span> | 0.3233 | 0.3209 | 0.3995 | 0.2576 | 0.3038 | 0.3145 | 0.2558 | 0.1290 | 0.3007 | 0.3235 |
| scconcept_encoded | 0.2101 | 0.2344 | 0.3140 | 0.1642 | 0.3230 | 0.2273 | 0.2634 | 0.2097 | 0.2481 | 0.1129 | 0.2635 | 0.2500 |
| cl_scratch_v5 | 0.3992 | 0.3281 | 0.5116 | 0.5149 | <span style='color:red'><strong>0.5909</strong></span> | **0.4697** | **0.6048** | <span style='color:red'><strong>0.6532</strong></span> | 0.5155 | **0.3226** | 0.4561 | 0.4412 |

### Negative protocol: full_candidate

Latent variables: metric=RECALL_AT_K, negative_protocol=full_candidate, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.4757** | 0.3905 | 0.7011 | 0.3929 | <span style='color:red'><strong>0.1875</strong></span> | **0.8050** | 0.6723 | 0.7774 | **0.7344** | <span style='color:red'><strong>0.8115</strong></span> | <span style='color:red'><strong>0.7836</strong></span> |
| baseline | 0.4709 | 0.4172 | <span style='color:red'><strong>0.7124</strong></span> | 0.4071 | <span style='color:red'><strong>0.1875</strong></span> | 0.7966 | 0.6830 | 0.7783 | 0.7288 | 0.8028 | 0.7636 |
| scGPT_human | **0.4733** | **0.4467** | 0.6748 | 0.3964 | <span style='color:red'><strong>0.1875</strong></span> | **0.8026** | 0.6681 | 0.7765 | 0.7243 | **0.8043** | 0.7482 |
| v4_bias_rec_best | **0.4769** | **0.4260** | 0.7011 | 0.3429 | 0.0625 | <span style='color:red'><strong>0.8080</strong></span> | **0.6872** | 0.7715 | <span style='color:red'><strong>0.7400</strong></span> | 0.7976 | 0.7591 |
| v4_plain_best | **0.4818** | **0.4231** | 0.7030 | 0.3357 | 0.1250 | **0.8074** | **0.7043** | <span style='color:red'><strong>0.7792</strong></span> | 0.7221 | 0.7990 | 0.7627 |
| v4_type_pe_best | <span style='color:red'><strong>0.4964</strong></span> | **0.4408** | 0.6880 | 0.3536 | <span style='color:red'><strong>0.1875</strong></span> | **0.8033** | <span style='color:red'><strong>0.7064</strong></span> | **0.7786** | 0.7266 | **0.8038** | **0.7736** |
| scconcept | 0.4393 | <span style='color:red'><strong>0.4497</strong></span> | 0.6391 | 0.3071 | <span style='color:red'><strong>0.1875</strong></span> | 0.7868 | 0.6404 | 0.7555 | 0.7143 | 0.7877 | 0.7255 |
| scconcept_encoded | 0.4223 | **0.4231** | 0.6523 | 0.3464 | 0.0000 | 0.7861 | 0.6596 | 0.7543 | 0.6987 | 0.7873 | 0.7227 |
| cl_scratch_v5 | 0.4636 | 0.4142 | 0.6805 | <span style='color:red'><strong>0.4107</strong></span> | <span style='color:red'><strong>0.1875</strong></span> | **0.8013** | **0.6957** | 0.7783 | **0.7288** | 0.8019 | 0.7618 |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.2236** | **0.2738** | **0.1804** | **0.1724** | **0.2868** | <span style='color:red'><strong>0.1818</strong></span> | **0.3174** | **0.2803** | **0.2737** | **0.1795** | **0.2549** | 0.1630 |
| baseline | 0.2112 | 0.2619 | 0.1546 | 0.1552 | 0.2481 | 0.1364 | 0.3006 | 0.2576 | 0.2518 | 0.1667 | 0.2320 | 0.1957 |
| scGPT_human | 0.1957 | 0.2143 | <span style='color:red'><strong>0.2320</strong></span> | <span style='color:red'><strong>0.1897</strong></span> | <span style='color:red'><strong>0.3062</strong></span> | 0.0909 | **0.3090** | **0.2955** | <span style='color:red'><strong>0.2956</strong></span> | <span style='color:red'><strong>0.2564</strong></span> | <span style='color:red'><strong>0.2582</strong></span> | **0.2826** |
| v4_bias_rec_best | **0.2174** | 0.2024 | **0.2062** | <span style='color:red'><strong>0.1897</strong></span> | **0.2674** | 0.1364 | 0.2809 | 0.2500 | **0.2664** | **0.2308** | 0.2222 | **0.2935** |
| v4_plain_best | <span style='color:red'><strong>0.2391</strong></span> | 0.2500 | **0.1856** | <span style='color:red'><strong>0.1897</strong></span> | **0.2868** | 0.1364 | 0.2809 | 0.2424 | **0.2664** | **0.1795** | **0.2516** | <span style='color:red'><strong>0.3261</strong></span> |
| v4_type_pe_best | **0.2267** | <span style='color:red'><strong>0.2738</strong></span> | **0.1907** | 0.1207 | **0.2674** | 0.1364 | 0.2978 | **0.2727** | <span style='color:red'><strong>0.2956</strong></span> | **0.2179** | <span style='color:red'><strong>0.2582</strong></span> | **0.3043** |
| scconcept | 0.1863 | 0.1548 | 0.0979 | 0.0690 | 0.1899 | 0.0455 | 0.1292 | 0.0682 | 0.1387 | 0.1410 | 0.1667 | 0.1630 |
| scconcept_encoded | 0.1335 | 0.0714 | 0.0928 | 0.0517 | 0.1279 | 0.0000 | 0.1236 | 0.1212 | 0.1058 | 0.0769 | 0.1242 | 0.1087 |
| cl_scratch_v5 | **0.2329** | 0.2619 | **0.2062** | 0.1207 | **0.2946** | <span style='color:red'><strong>0.1818</strong></span> | <span style='color:red'><strong>0.3202</strong></span> | <span style='color:red'><strong>0.3106</strong></span> | <span style='color:red'><strong>0.2956</strong></span> | 0.1667 | 0.2059 | <span style='color:red'><strong>0.3261</strong></span> |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | <span style='color:red'><strong>0.3025</strong></span> | 0.2031 | <span style='color:red'><strong>0.4698</strong></span> | 0.5075 | <span style='color:red'><strong>0.4976</strong></span> | **0.4242** | **0.5081** | **0.5484** | 0.3643 | <span style='color:red'><strong>0.2903</strong></span> | <span style='color:red'><strong>0.3682</strong></span> | **0.3382** |
| baseline | 0.2815 | 0.2031 | 0.4558 | 0.5522 | 0.4785 | 0.3939 | 0.5054 | 0.5081 | 0.3837 | 0.2258 | 0.3176 | 0.3235 |
| scGPT_human | **0.2857** | <span style='color:red'><strong>0.3438</strong></span> | 0.4535 | <span style='color:red'><strong>0.5597</strong></span> | 0.4617 | **0.4848** | 0.4839 | <span style='color:red'><strong>0.5968</strong></span> | <span style='color:red'><strong>0.4031</strong></span> | **0.2581** | **0.3649** | **0.3382** |
| v4_bias_rec_best | 0.2815 | 0.1875 | **0.4605** | 0.5075 | 0.4641 | **0.4091** | 0.4946 | **0.5565** | 0.3256 | **0.2903** | **0.3243** | **0.4118** |
| v4_plain_best | 0.2731 | **0.2188** | 0.4372 | 0.4627 | 0.4641 | <span style='color:red'><strong>0.5152</strong></span> | **0.5081** | **0.5161** | **0.3915** | **0.2581** | **0.3277** | **0.3529** |
| v4_type_pe_best | **0.2983** | 0.2031 | 0.4488 | 0.5373 | **0.4904** | **0.4242** | 0.5054 | **0.5645** | **0.3876** | **0.2258** | **0.3412** | <span style='color:red'><strong>0.4265</strong></span> |
| scconcept | 0.0882 | **0.2188** | 0.2977 | 0.1940 | 0.2919 | 0.1364 | 0.2097 | 0.1694 | 0.1318 | 0.0323 | 0.1385 | 0.1765 |
| scconcept_encoded | 0.0714 | 0.1719 | 0.1837 | 0.2015 | 0.2990 | 0.0758 | 0.2016 | 0.1452 | 0.1008 | 0.0806 | 0.0642 | 0.1618 |
| cl_scratch_v5 | 0.2773 | **0.2344** | 0.4535 | 0.4851 | **0.4952** | **0.4848** | <span style='color:red'><strong>0.5188</strong></span> | <span style='color:red'><strong>0.5968</strong></span> | **0.3992** | 0.1935 | **0.3243** | **0.3676** |

## F1 (Supplementary)

### Negative protocol: tf_stratified_1to10

Latent variables: metric=F1, negative_protocol=tf_stratified_1to10, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.4112 | 0.3411 | 0.6818 | **0.3448** | **0.0667** | 0.8064 | 0.7007 | <span style='color:red'><strong>0.7902</strong></span> | **0.7283** | <span style='color:red'><strong>0.8092</strong></span> | **0.7751** |
| baseline | 0.4139 | 0.3452 | 0.7008 | 0.3303 | 0.0000 | 0.8091 | 0.7154 | 0.7880 | 0.7260 | 0.8046 | 0.7557 |
| scGPT_human | 0.3972 | **0.4212** | 0.6740 | **0.3332** | **0.1000** | 0.8040 | 0.6921 | 0.7777 | **0.7321** | **0.8085** | **0.7562** |
| v4_bias_rec_best | 0.4109 | **0.3544** | 0.6939 | **0.3491** | 0.0000 | 0.8066 | 0.7009 | 0.7849 | <span style='color:red'><strong>0.7682</strong></span> | **0.8051** | **0.7605** |
| v4_plain_best | <span style='color:red'><strong>0.4225</strong></span> | **0.3870** | <span style='color:red'><strong>0.7106</strong></span> | 0.3263 | 0.0000 | <span style='color:red'><strong>0.8096</strong></span> | 0.6887 | 0.7860 | 0.7201 | **0.8079** | <span style='color:red'><strong>0.7841</strong></span> |
| v4_type_pe_best | 0.4112 | <span style='color:red'><strong>0.4346</strong></span> | 0.6945 | 0.3255 | **0.1000** | 0.8048 | <span style='color:red'><strong>0.7171</strong></span> | 0.7819 | **0.7446** | **0.8057** | **0.7732** |
| scconcept | 0.3638 | **0.3604** | 0.6522 | 0.2080 | <span style='color:red'><strong>0.1111</strong></span> | 0.7911 | 0.6617 | 0.7599 | 0.6802 | 0.8035 | 0.7283 |
| scconcept_encoded | 0.3678 | **0.3917** | 0.6434 | 0.2431 | 0.0000 | 0.7885 | 0.6680 | 0.7545 | 0.7191 | 0.8017 | 0.7354 |
| cl_scratch_v5 | 0.3903 | **0.3911** | 0.6822 | <span style='color:red'><strong>0.3501</strong></span> | **0.0909** | 0.8057 | 0.6980 | 0.7837 | **0.7315** | **0.8083** | 0.7521 |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.1231 | 0.1237 | 0.1584 | **0.2024** | <span style='color:red'><strong>0.4034</strong></span> | 0.2500 | <span style='color:red'><strong>0.4072</strong></span> | **0.3490** | **0.3212** | 0.1765 | **0.2898** | 0.2521 |
| baseline | 0.1438 | 0.1294 | 0.2669 | 0.1387 | 0.3374 | 0.4000 | 0.3584 | 0.3416 | 0.2710 | 0.2113 | 0.2000 | 0.2628 |
| scGPT_human | <span style='color:red'><strong>0.2101</strong></span> | <span style='color:red'><strong>0.2163</strong></span> | <span style='color:red'><strong>0.3010</strong></span> | <span style='color:red'><strong>0.2735</strong></span> | **0.3799** | 0.0714 | 0.3365 | <span style='color:red'><strong>0.4125</strong></span> | **0.3374** | <span style='color:red'><strong>0.3463</strong></span> | <span style='color:red'><strong>0.3377</strong></span> | **0.3287** |
| v4_bias_rec_best | 0.0980 | 0.0633 | 0.1789 | **0.2154** | 0.2510 | 0.1538 | 0.3087 | 0.3108 | <span style='color:red'><strong>0.3538</strong></span> | 0.1512 | **0.2616** | 0.2482 |
| v4_plain_best | **0.2090** | 0.0617 | 0.2523 | **0.1874** | **0.3588** | 0.2667 | 0.3415 | 0.3370 | **0.2996** | 0.1999 | **0.2321** | **0.2897** |
| v4_type_pe_best | **0.1922** | 0.0964 | 0.1786 | **0.1481** | **0.3658** | <span style='color:red'><strong>0.4734</strong></span> | 0.3157 | 0.2957 | **0.3127** | 0.1897 | **0.3005** | <span style='color:red'><strong>0.3719</strong></span> |
| scconcept | 0.1363 | 0.0972 | 0.1713 | 0.1020 | 0.2059 | 0.0000 | 0.1095 | 0.0682 | 0.1971 | 0.1548 | 0.1647 | 0.1279 |
| scconcept_encoded | 0.0721 | 0.0894 | 0.1301 | 0.0727 | 0.1982 | 0.0588 | 0.1584 | 0.0909 | 0.1572 | 0.1095 | **0.2027** | 0.1172 |
| cl_scratch_v5 | 0.1362 | **0.1529** | 0.2308 | 0.1240 | **0.4027** | 0.1875 | **0.3624** | 0.3187 | **0.3462** | 0.1713 | **0.2587** | **0.3260** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.3958 | 0.2344 | 0.5099 | 0.5311 | 0.5449 | **0.1964** | **0.5757** | 0.5704 | 0.4559 | **0.4036** | 0.4245 | 0.3983 |
| baseline | 0.4143 | 0.2794 | <span style='color:red'><strong>0.5273</strong></span> | 0.5546 | 0.5598 | 0.1857 | 0.5693 | 0.6133 | 0.5038 | 0.1549 | 0.4297 | 0.4153 |
| scGPT_human | <span style='color:red'><strong>0.4283</strong></span> | 0.2453 | 0.5104 | <span style='color:red'><strong>0.5907</strong></span> | 0.5254 | <span style='color:red'><strong>0.5667</strong></span> | <span style='color:red'><strong>0.6074</strong></span> | 0.6013 | **0.5073** | 0.1250 | <span style='color:red'><strong>0.4960</strong></span> | <span style='color:red'><strong>0.5000</strong></span> |
| v4_bias_rec_best | 0.3862 | 0.1974 | 0.5197 | **0.5676** | 0.5268 | **0.4089** | **0.5729** | 0.6006 | 0.4538 | <span style='color:red'><strong>0.4618</strong></span> | 0.3383 | **0.4411** |
| v4_plain_best | 0.3945 | 0.2794 | 0.4669 | **0.5609** | 0.5594 | **0.2714** | **0.6069** | <span style='color:red'><strong>0.6426</strong></span> | 0.4512 | **0.1864** | 0.4227 | 0.3994 |
| v4_type_pe_best | **0.4231** | 0.2464 | 0.4799 | **0.5752** | <span style='color:red'><strong>0.5683</strong></span> | **0.2464** | **0.6055** | **0.6354** | 0.4665 | **0.3294** | **0.4569** | 0.3187 |
| scconcept | 0.1246 | <span style='color:red'><strong>0.3855</strong></span> | 0.2441 | 0.1661 | 0.3542 | 0.1400 | 0.2707 | 0.1917 | 0.1373 | 0.0577 | 0.2418 | 0.2105 |
| scconcept_encoded | 0.1107 | 0.1818 | 0.2548 | 0.1090 | 0.2326 | 0.1129 | 0.1758 | 0.1591 | 0.1811 | 0.0189 | 0.2338 | 0.1930 |
| cl_scratch_v5 | 0.3748 | 0.2542 | 0.4931 | 0.4861 | **0.5634** | **0.2615** | **0.5984** | **0.6144** | <span style='color:red'><strong>0.5116</strong></span> | **0.1613** | **0.4457** | 0.3855 |

### Negative protocol: full_candidate

Latent variables: metric=F1, negative_protocol=full_candidate, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.4005** | **0.3528** | **0.7037** | **0.3294** | 0.0000 | **0.8092** | 0.6816 | 0.7819 | **0.7403** | **0.8113** | <span style='color:red'><strong>0.7929</strong></span> |
| baseline | 0.3603 | 0.3236 | 0.6966 | 0.3276 | 0.0833 | 0.8008 | 0.6925 | <span style='color:red'><strong>0.7890</strong></span> | 0.7357 | 0.8072 | 0.7794 |
| scGPT_human | 0.3049 | <span style='color:red'><strong>0.4341</strong></span> | 0.6639 | <span style='color:red'><strong>0.3891</strong></span> | **0.1000** | **0.8068** | 0.6779 | 0.7771 | 0.7277 | **0.8104** | 0.7598 |
| v4_bias_rec_best | <span style='color:red'><strong>0.4451</strong></span> | **0.3712** | 0.6853 | 0.3008 | 0.0833 | **0.8107** | **0.6988** | 0.7780 | <span style='color:red'><strong>0.7584</strong></span> | **0.8077** | 0.7781 |
| v4_plain_best | **0.4368** | **0.3629** | <span style='color:red'><strong>0.7117</strong></span> | 0.3171 | 0.0833 | **0.8074** | <span style='color:red'><strong>0.7046</strong></span> | 0.7840 | 0.7352 | **0.8096** | 0.7708 |
| v4_type_pe_best | **0.4219** | **0.3801** | 0.6883 | 0.3212 | 0.0000 | <span style='color:red'><strong>0.8112</strong></span> | 0.6834 | 0.7858 | **0.7416** | <span style='color:red'><strong>0.8132</strong></span> | 0.7761 |
| scconcept | 0.2696 | **0.3932** | 0.6570 | 0.2354 | <span style='color:red'><strong>0.1111</strong></span> | 0.7908 | 0.6406 | 0.7633 | 0.7167 | 0.8023 | 0.7407 |
| scconcept_encoded | 0.3526 | **0.3801** | 0.6665 | 0.2657 | 0.0000 | 0.7916 | 0.6582 | 0.7639 | 0.7192 | 0.7983 | 0.7374 |
| cl_scratch_v5 | **0.3951** | **0.3870** | 0.6766 | **0.3768** | **0.0909** | **0.8087** | 0.6910 | 0.7832 | 0.7292 | **0.8096** | 0.7697 |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.0565 | **0.1519** | **0.1393** | **0.0870** | **0.1253** | 0.0714 | <span style='color:red'><strong>0.3040</strong></span> | **0.2220** | <span style='color:red'><strong>0.3109</strong></span> | 0.1067 | **0.2068** | **0.1379** |
| baseline | 0.0659 | 0.1184 | 0.0813 | 0.0444 | 0.1040 | 0.0833 | 0.2801 | 0.2114 | 0.2403 | 0.1235 | 0.1972 | 0.1220 |
| scGPT_human | **0.0660** | <span style='color:red'><strong>0.1620</strong></span> | <span style='color:red'><strong>0.2141</strong></span> | 0.0256 | **0.2269** | 0.0000 | 0.2788 | <span style='color:red'><strong>0.2737</strong></span> | **0.3018** | <span style='color:red'><strong>0.2033</strong></span> | 0.1923 | <span style='color:red'><strong>0.2599</strong></span> |
| v4_bias_rec_best | 0.0448 | 0.0995 | 0.0651 | <span style='color:red'><strong>0.0952</strong></span> | **0.1266** | <span style='color:red'><strong>0.1250</strong></span> | 0.2409 | 0.1305 | **0.2559** | 0.1200 | 0.1108 | **0.2465** |
| v4_plain_best | **0.1009** | 0.1131 | **0.0966** | **0.0923** | **0.2286** | 0.0769 | 0.2123 | 0.2009 | **0.2691** | **0.1266** | <span style='color:red'><strong>0.2477</strong></span> | **0.2409** |
| v4_type_pe_best | <span style='color:red'><strong>0.1039</strong></span> | 0.0909 | **0.0982** | **0.0667** | 0.1027 | 0.0714 | 0.2213 | **0.2635** | 0.2231 | **0.1238** | **0.2183** | **0.2061** |
| scconcept | **0.0688** | 0.0563 | 0.0526 | 0.0227 | **0.1215** | 0.0714 | 0.0528 | 0.0442 | 0.1051 | 0.0746 | 0.0632 | 0.0824 |
| scconcept_encoded | 0.0619 | 0.0429 | 0.0336 | 0.0385 | 0.0667 | 0.0000 | 0.0263 | 0.0759 | 0.0437 | 0.0429 | 0.0423 | 0.0843 |
| cl_scratch_v5 | 0.0628 | **0.1481** | **0.1806** | **0.0513** | <span style='color:red'><strong>0.2456</strong></span> | 0.0833 | 0.2653 | **0.2492** | **0.2716** | 0.1184 | 0.1942 | **0.2228** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | <span style='color:red'><strong>0.3551</strong></span> | **0.1837** | **0.4408** | 0.4948 | 0.4039 | 0.3480 | 0.5028 | **0.5592** | **0.3964** | 0.1676 | **0.3673** | 0.2254 |
| baseline | 0.2906 | 0.1538 | 0.4189 | 0.5383 | 0.4066 | 0.3519 | 0.5031 | 0.4766 | 0.3580 | <span style='color:red'><strong>0.2110</strong></span> | 0.3244 | 0.3500 |
| scGPT_human | 0.2786 | <span style='color:red'><strong>0.2000</strong></span> | **0.4377** | <span style='color:red'><strong>0.5559</strong></span> | <span style='color:red'><strong>0.4438</strong></span> | **0.4532** | **0.5211** | **0.5723** | **0.4182** | 0.1102 | <span style='color:red'><strong>0.3916</strong></span> | 0.3271 |
| v4_bias_rec_best | 0.2549 | 0.1273 | <span style='color:red'><strong>0.4495</strong></span> | 0.4634 | 0.3945 | **0.3761** | 0.4789 | **0.5479** | 0.3277 | 0.1682 | 0.2041 | 0.3036 |
| v4_plain_best | 0.2811 | **0.1754** | **0.4268** | 0.4381 | **0.4219** | <span style='color:red'><strong>0.5201</strong></span> | 0.4961 | **0.5132** | **0.4022** | 0.1646 | **0.3439** | 0.3455 |
| v4_type_pe_best | 0.2597 | **0.1569** | **0.4396** | 0.5177 | **0.4409** | **0.3797** | 0.4909 | **0.5392** | **0.4092** | 0.0638 | **0.3444** | <span style='color:red'><strong>0.4453</strong></span> |
| scconcept | 0.0448 | **0.1667** | 0.2163 | 0.0630 | 0.2042 | 0.0941 | 0.1503 | 0.0873 | 0.0733 | 0.0256 | 0.0857 | 0.1346 |
| scconcept_encoded | 0.0261 | 0.0870 | 0.0899 | 0.1080 | 0.1405 | 0.0429 | 0.0890 | 0.1093 | 0.0172 | 0.0233 | 0.0215 | 0.1311 |
| cl_scratch_v5 | 0.2249 | 0.1452 | **0.4423** | 0.4379 | **0.4199** | **0.4102** | <span style='color:red'><strong>0.5380</strong></span> | <span style='color:red'><strong>0.5834</strong></span> | <span style='color:red'><strong>0.4313</strong></span> | 0.1087 | **0.3348** | 0.3414 |

## SPECIFICITY (Supplementary)

### Negative protocol: tf_stratified_1to10

Latent variables: metric=SPECIFICITY, negative_protocol=tf_stratified_1to10, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.8509** | 0.8505 | 0.8774 | 0.9059 | 0.9625 | 0.6394 | 0.7559 | <span style='color:red'><strong>0.6873</strong></span> | **0.6533** | **0.6168** | **0.6315** |
| baseline | 0.8470 | 0.8527 | 0.8868 | 0.9246 | 0.9875 | 0.6416 | <span style='color:red'><strong>0.7637</strong></span> | 0.6310 | 0.6326 | 0.6025 | 0.5820 |
| scGPT_human | <span style='color:red'><strong>0.8743</strong></span> | 0.8000 | 0.8722 | 0.9138 | **0.9938** | <span style='color:red'><strong>0.6507</strong></span> | 0.6934 | **0.6561** | **0.6395** | **0.6263** | **0.6094** |
| v4_bias_rec_best | 0.8431 | 0.8430 | 0.8851 | **0.9260** | 0.9688 | 0.6200 | 0.7383 | **0.6476** | **0.6519** | <span style='color:red'><strong>0.6485</strong></span> | **0.6263** |
| v4_plain_best | **0.8733** | 0.8161 | <span style='color:red'><strong>0.8902</strong></span> | <span style='color:red'><strong>0.9325</strong></span> | 0.9812 | 0.6216 | 0.7246 | **0.6756** | **0.6367** | **0.6136** | **0.6224** |
| v4_type_pe_best | **0.8665** | 0.8333 | 0.8756 | **0.9289** | **0.9938** | 0.6313 | 0.7363 | **0.6723** | 0.5843 | **0.6311** | <span style='color:red'><strong>0.6328</strong></span> |
| scconcept | 0.8095 | 0.8247 | 0.8302 | 0.9052 | <span style='color:red'><strong>1.0000</strong></span> | 0.6146 | 0.6387 | 0.6006 | 0.5953 | **0.6092** | 0.5247 |
| scconcept_encoded | 0.8212 | 0.7763 | 0.8559 | 0.9167 | 0.9750 | 0.6055 | 0.6602 | 0.6148 | 0.5677 | 0.5627 | 0.5169 |
| cl_scratch_v5 | **0.8577** | <span style='color:red'><strong>0.8559</strong></span> | 0.8868 | 0.9246 | 0.9875 | 0.6222 | 0.7168 | **0.6399** | <span style='color:red'><strong>0.6727</strong></span> | 0.6009 | **0.6302** |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.9610 | 0.9356 | <span style='color:red'><strong>0.9624</strong></span> | **0.9534** | 0.9636 | 0.9909 | 0.9557 | **0.9461** | **0.9691** | 0.9603 | 0.9726 | **0.9750** |
| baseline | 0.9610 | 0.9521 | 0.9515 | 0.9448 | 0.9651 | 0.9909 | 0.9647 | 0.9295 | 0.9653 | 0.9641 | 0.9726 | 0.9620 |
| scGPT_human | 0.9203 | **0.9611** | 0.9479 | **0.9690** | 0.9601 | 0.9909 | 0.9581 | <span style='color:red'><strong>0.9693</strong></span> | 0.9555 | **0.9705** | 0.9446 | <span style='color:red'><strong>0.9859</strong></span> |
| v4_bias_rec_best | **0.9622** | 0.9521 | **0.9521** | 0.9414 | <span style='color:red'><strong>0.9717</strong></span> | <span style='color:red'><strong>1.0000</strong></span> | 0.9593 | **0.9337** | <span style='color:red'><strong>0.9713</strong></span> | 0.9564 | 0.9716 | 0.9522 |
| v4_plain_best | 0.9459 | 0.9476 | **0.9572** | **0.9534** | 0.9651 | <span style='color:red'><strong>1.0000</strong></span> | **0.9665** | **0.9320** | **0.9661** | 0.9564 | 0.9703 | **0.9674** |
| v4_type_pe_best | <span style='color:red'><strong>0.9720</strong></span> | 0.9506 | **0.9526** | **0.9707** | 0.9616 | 0.9682 | **0.9662** | **0.9395** | 0.9540 | 0.9590 | 0.9723 | **0.9641** |
| scconcept | 0.9301 | <span style='color:red'><strong>0.9656</strong></span> | 0.9490 | <span style='color:red'><strong>0.9741</strong></span> | 0.9349 | **0.9955** | 0.9469 | **0.9502** | 0.9427 | <span style='color:red'><strong>0.9744</strong></span> | 0.9395 | **0.9685** |
| scconcept_encoded | 0.9500 | 0.9326 | 0.9510 | **0.9621** | 0.9484 | 0.9727 | 0.9499 | **0.9428** | 0.9472 | 0.9615 | 0.9466 | **0.9674** |
| cl_scratch_v5 | **0.9663** | **0.9551** | **0.9536** | **0.9707** | **0.9663** | 0.9909 | <span style='color:red'><strong>0.9707</strong></span> | **0.9328** | 0.9600 | 0.9603 | <span style='color:red'><strong>0.9733</strong></span> | **0.9685** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.9534 | 0.9734 | 0.9642 | 0.9625 | 0.9684 | **0.9811** | 0.9667 | **0.9705** | 0.9605 | **0.9645** | **0.9662** | 0.9706 |
| baseline | 0.9563 | 0.9734 | <span style='color:red'><strong>0.9709</strong></span> | 0.9625 | <span style='color:red'><strong>0.9718</strong></span> | 0.9623 | <span style='color:red'><strong>0.9699</strong></span> | 0.9689 | 0.9636 | 0.9532 | 0.9649 | 0.9794 |
| scGPT_human | <span style='color:red'><strong>0.9626</strong></span> | <span style='color:red'><strong>0.9875</strong></span> | 0.9602 | <span style='color:red'><strong>0.9662</strong></span> | 0.9608 | 0.9591 | 0.9616 | <span style='color:red'><strong>0.9762</strong></span> | <span style='color:red'><strong>0.9647</strong></span> | <span style='color:red'><strong>0.9823</strong></span> | 0.9571 | **0.9853** |
| v4_bias_rec_best | 0.9462 | 0.9547 | 0.9665 | **0.9640** | 0.9675 | 0.9465 | 0.9656 | **0.9713** | **0.9643** | **0.9581** | <span style='color:red'><strong>0.9689</strong></span> | <span style='color:red'><strong>0.9882</strong></span> |
| v4_plain_best | 0.9555 | 0.9734 | 0.9647 | **0.9647** | 0.9708 | **0.9717** | 0.9675 | **0.9713** | 0.9593 | **0.9726** | 0.9564 | **0.9868** |
| v4_type_pe_best | 0.9525 | 0.9688 | 0.9679 | 0.9617 | 0.9711 | **0.9701** | 0.9653 | 0.9672 | 0.9578 | **0.9677** | **0.9659** | <span style='color:red'><strong>0.9882</strong></span> |
| scconcept | 0.9454 | **0.9781** | 0.9553 | 0.9542 | 0.9514 | <span style='color:red'><strong>0.9843</strong></span> | 0.9497 | **0.9713** | 0.9516 | **0.9710** | 0.9436 | **0.9838** |
| scconcept_encoded | 0.9471 | **0.9797** | 0.9607 | 0.9550 | 0.9665 | **0.9654** | 0.9645 | 0.9590 | 0.9496 | **0.9661** | 0.9500 | **0.9824** |
| cl_scratch_v5 | 0.9466 | **0.9812** | 0.9651 | 0.9602 | 0.9691 | **0.9764** | 0.9669 | 0.9639 | 0.9589 | **0.9661** | 0.9618 | 0.9750 |

### Negative protocol: full_candidate

Latent variables: metric=SPECIFICITY, negative_protocol=full_candidate, classifier=aggregated(lr,mlp), aggregation=mean

#### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.9269 | 0.9171 | 0.9319 | 0.9716 | **0.9978** | 0.7757 | 0.7638 | **0.7701** | <span style='color:red'><strong>0.6892</strong></span> | <span style='color:red'><strong>0.7449</strong></span> | **0.6045** |
| baseline | 0.9408 | 0.9257 | 0.9330 | 0.9733 | 0.9933 | 0.7806 | 0.7739 | 0.7487 | 0.6561 | 0.6973 | 0.5886 |
| scGPT_human | <span style='color:red'><strong>0.9450</strong></span> | 0.9051 | 0.9313 | 0.9622 | **0.9978** | **0.7935** | 0.7652 | <span style='color:red'><strong>0.7856</strong></span> | 0.6506 | **0.7026** | <span style='color:red'><strong>0.6230</strong></span> |
| v4_bias_rec_best | 0.9138 | 0.9229 | 0.9302 | <span style='color:red'><strong>0.9792</strong></span> | 0.9933 | **0.7928** | 0.7725 | **0.7637** | 0.6188 | **0.7097** | **0.6019** |
| v4_plain_best | 0.9220 | <span style='color:red'><strong>0.9320</strong></span> | **0.9426** | 0.9698 | 0.9933 | <span style='color:red'><strong>0.8011</strong></span> | **0.8014** | **0.7786** | 0.6312 | 0.6932 | 0.5873 |
| v4_type_pe_best | 0.9342 | **0.9280** | **0.9347** | **0.9762** | 0.9933 | 0.7668 | <span style='color:red'><strong>0.8261</strong></span> | **0.7699** | 0.6229 | 0.6826 | 0.5820 |
| scconcept | **0.9413** | 0.9183 | 0.9054 | 0.9592 | <span style='color:red'><strong>1.0000</strong></span> | 0.7754 | 0.7565 | 0.7468 | 0.6354 | 0.6546 | 0.5476 |
| scconcept_encoded | 0.9239 | 0.9154 | 0.9178 | 0.9680 | 0.9888 | 0.7681 | **0.7913** | 0.7414 | 0.5732 | 0.6805 | 0.5066 |
| cl_scratch_v5 | 0.9321 | 0.9217 | <span style='color:red'><strong>0.9499</strong></span> | 0.9721 | **0.9955** | 0.7711 | **0.7986** | **0.7755** | 0.6492 | **0.7044** | 0.5780 |

#### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.9969** | 0.9931 | 0.9980 | 0.9959 | 0.9988 | 0.9988 | 0.9964 | **0.9898** | **0.9988** | **0.9912** | **0.9986** | **0.9928** |
| baseline | 0.9967 | 0.9931 | <span style='color:red'><strong>0.9990</strong></span> | 0.9959 | 0.9989 | <span style='color:red'><strong>1.0000</strong></span> | 0.9971 | 0.9892 | 0.9987 | 0.9906 | 0.9978 | 0.9903 |
| scGPT_human | 0.9935 | <span style='color:red'><strong>0.9945</strong></span> | 0.9935 | **0.9971** | 0.9946 | 0.9988 | 0.9953 | <span style='color:red'><strong>0.9907</strong></span> | 0.9954 | **0.9921** | 0.9960 | <span style='color:red'><strong>0.9947</strong></span> |
| v4_bias_rec_best | <span style='color:red'><strong>0.9980</strong></span> | 0.9923 | 0.9983 | **0.9971** | 0.9985 | 0.9981 | 0.9961 | 0.9873 | **0.9988** | **0.9921** | <span style='color:red'><strong>0.9990</strong></span> | **0.9906** |
| v4_plain_best | **0.9973** | **0.9939** | 0.9974 | 0.9944 | 0.9979 | 0.9994 | 0.9965 | 0.9858 | **0.9989** | **0.9912** | **0.9989** | **0.9939** |
| v4_type_pe_best | **0.9975** | 0.9923 | 0.9982 | **0.9962** | <span style='color:red'><strong>0.9990</strong></span> | 0.9988 | **0.9975** | 0.9879 | <span style='color:red'><strong>0.9992</strong></span> | 0.9900 | **0.9980** | **0.9914** |
| scconcept | 0.9950 | 0.9931 | 0.9942 | 0.9956 | 0.9966 | 0.9988 | 0.9967 | 0.9858 | 0.9957 | <span style='color:red'><strong>0.9932</strong></span> | 0.9963 | **0.9911** |
| scconcept_encoded | 0.9959 | 0.9914 | 0.9973 | 0.9939 | 0.9978 | 0.9988 | <span style='color:red'><strong>0.9979</strong></span> | 0.9856 | 0.9983 | **0.9918** | **0.9987** | **0.9917** |
| cl_scratch_v5 | **0.9974** | 0.9925 | 0.9979 | <span style='color:red'><strong>0.9977</strong></span> | 0.9971 | <span style='color:red'><strong>1.0000</strong></span> | 0.9968 | 0.9873 | 0.9977 | **0.9918** | **0.9979** | **0.9911** |

#### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.9984 | <span style='color:red'><strong>0.9985</strong></span> | 0.9971 | **0.9917** | 0.9965 | **0.9944** | **0.9979** | 0.9949 | 0.9981 | **0.9972** | **0.9992** | **0.9979** |
| baseline | 0.9987 | 0.9978 | 0.9979 | 0.9903 | <span style='color:red'><strong>0.9972</strong></span> | 0.9935 | 0.9977 | 0.9949 | 0.9990 | 0.9962 | 0.9990 | 0.9967 |
| scGPT_human | 0.9962 | <span style='color:red'><strong>0.9985</strong></span> | 0.9953 | <span style='color:red'><strong>0.9930</strong></span> | 0.9941 | <span style='color:red'><strong>0.9964</strong></span> | 0.9953 | <span style='color:red'><strong>0.9968</strong></span> | 0.9963 | <span style='color:red'><strong>0.9992</strong></span> | 0.9977 | <span style='color:red'><strong>0.9990</strong></span> |
| v4_bias_rec_best | 0.9983 | 0.9971 | 0.9959 | **0.9905** | 0.9967 | 0.9903 | 0.9976 | **0.9959** | <span style='color:red'><strong>0.9991</strong></span> | **0.9970** | <span style='color:red'><strong>0.9993</strong></span> | **0.9973** |
| v4_plain_best | <span style='color:red'><strong>0.9990</strong></span> | 0.9973 | 0.9970 | 0.9877 | 0.9968 | 0.9927 | **0.9979** | **0.9959** | 0.9989 | **0.9984** | **0.9993** | **0.9971** |
| v4_type_pe_best | **0.9988** | **0.9980** | 0.9974 | **0.9909** | 0.9965 | 0.9915 | **0.9980** | **0.9956** | **0.9990** | **0.9974** | 0.9990 | **0.9983** |
| scconcept | 0.9970 | 0.9976 | 0.9971 | 0.9886 | 0.9957 | 0.9847 | 0.9968 | 0.9926 | 0.9973 | **0.9986** | 0.9981 | **0.9977** |
| scconcept_encoded | **0.9988** | **0.9982** | <span style='color:red'><strong>0.9984</strong></span> | 0.9892 | 0.9965 | 0.9863 | <span style='color:red'><strong>0.9982</strong></span> | 0.9926 | 0.9984 | **0.9974** | 0.9988 | **0.9969** |
| cl_scratch_v5 | **0.9989** | 0.9962 | 0.9971 | **0.9915** | 0.9970 | **0.9944** | 0.9974 | **0.9958** | **0.9990** | **0.9966** | 0.9989 | **0.9971** |

