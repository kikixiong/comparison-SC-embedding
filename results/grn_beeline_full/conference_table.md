# GRN BEELINE Full (Conference-style Tables)

说明：`-`表示该组合无结果；按列（同一dataset）比较：**加粗**表示优于baseline；<span style="color:red"><strong>红色加粗</strong></span>表示该列最优。
仅将`dataset`与`embedding`作为显式变量；其余设置作为表上方 latent variables 展示；`dataset_split`与`classifier`已聚合，不再展示拆分明细。

## AUROC (Main)

Latent variables: metric=AUROC, classifier=aggregated(lr,mlp), aggregation=mean

### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.8466 | 0.7901 | 0.8887 | **0.8427** | 0.7063 | **0.8959** | 0.8188 | <span style='color:red'><strong>0.8720</strong></span> | <span style='color:red'><strong>0.7789</strong></span> | <span style='color:red'><strong>0.8686</strong></span> | <span style='color:red'><strong>0.7912</strong></span> |
| baseline | <span style='color:red'><strong>0.8551</strong></span> | <span style='color:red'><strong>0.8211</strong></span> | 0.8954 | 0.8341 | 0.8136 | 0.8918 | 0.8317 | 0.8699 | 0.7676 | 0.8563 | 0.7790 |
| scGPT_human | 0.8356 | 0.7980 | 0.8794 | **0.8376** | 0.7464 | **0.8957** | 0.8075 | **0.8713** | 0.7609 | **0.8582** | 0.7740 |
| v4_bias_rec_best | 0.8528 | 0.8094 | 0.8929 | 0.8289 | 0.6085 | <span style='color:red'><strong>0.8962</strong></span> | <span style='color:red'><strong>0.8365</strong></span> | 0.8691 | **0.7760** | 0.8561 | **0.7815** |
| v4_plain_best | 0.8473 | 0.8125 | **0.8956** | 0.8302 | <span style='color:red'><strong>0.8237</strong></span> | **0.8949** | 0.8246 | **0.8718** | 0.7560 | **0.8622** | **0.7830** |
| v4_type_pe_best | 0.8550 | 0.8142 | <span style='color:red'><strong>0.8972</strong></span> | 0.8264 | 0.7386 | **0.8949** | **0.8323** | **0.8705** | 0.7633 | **0.8616** | **0.7894** |
| scconcept | 0.8123 | 0.7923 | 0.8531 | 0.7765 | 0.6723 | 0.8769 | 0.7742 | 0.8452 | 0.7282 | 0.8430 | 0.7237 |
| scconcept_encoded | 0.8327 | 0.7934 | 0.8539 | 0.8226 | 0.5379 | 0.8780 | 0.8083 | 0.8496 | 0.7275 | 0.8349 | 0.7103 |
| cl_scratch_v5 | 0.8511 | 0.8119 | 0.8907 | <span style='color:red'><strong>0.8501</strong></span> | 0.7011 | **0.8960** | **0.8342** | **0.8707** | **0.7697** | **0.8609** | 0.7723 |

### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.8847** | 0.8421 | <span style='color:red'><strong>0.8637</strong></span> | <span style='color:red'><strong>0.8364</strong></span> | **0.8695** | **0.6466** | 0.8713 | **0.8356** | 0.8371 | <span style='color:red'><strong>0.8085</strong></span> | 0.8296 | **0.8111** |
| baseline | 0.8815 | 0.8675 | 0.8460 | 0.7431 | 0.8598 | 0.6291 | <span style='color:red'><strong>0.8738</strong></span> | 0.8295 | 0.8481 | 0.7696 | 0.8317 | 0.7628 |
| scGPT_human | 0.8478 | 0.8578 | **0.8578** | **0.8039** | 0.8355 | **0.6659** | 0.8580 | **0.8534** | 0.8361 | **0.7975** | **0.8352** | <span style='color:red'><strong>0.8185</strong></span> |
| v4_bias_rec_best | 0.8701 | 0.8590 | 0.8284 | **0.8088** | **0.8638** | **0.6444** | 0.8587 | <span style='color:red'><strong>0.8609</strong></span> | **0.8518** | **0.7863** | 0.8115 | **0.8054** |
| v4_plain_best | **0.8927** | <span style='color:red'><strong>0.8770</strong></span> | **0.8511** | **0.7837** | <span style='color:red'><strong>0.8770</strong></span> | **0.6758** | 0.8602 | **0.8453** | 0.8378 | 0.7685 | **0.8350** | **0.7942** |
| v4_type_pe_best | <span style='color:red'><strong>0.8930</strong></span> | 0.8402 | **0.8543** | **0.7725** | **0.8691** | **0.6468** | 0.8696 | 0.8255 | <span style='color:red'><strong>0.8538</strong></span> | 0.7621 | **0.8344** | **0.7822** |
| scconcept | 0.8253 | 0.8304 | 0.7839 | **0.7608** | 0.7682 | 0.5622 | 0.8039 | 0.7460 | 0.7828 | 0.7543 | 0.8071 | 0.7466 |
| scconcept_encoded | 0.8490 | 0.7996 | 0.8074 | 0.7144 | 0.7331 | <span style='color:red'><strong>0.6779</strong></span> | 0.7851 | 0.7624 | 0.7675 | 0.7168 | 0.7825 | 0.7365 |
| cl_scratch_v5 | **0.8818** | **0.8738** | **0.8465** | **0.8050** | **0.8762** | **0.6441** | 0.8685 | **0.8406** | 0.8460 | 0.7583 | <span style='color:red'><strong>0.8485</strong></span> | **0.7661** |

### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.8263 | **0.8167** | **0.8859** | 0.9041 | **0.9012** | 0.8191 | **0.8930** | <span style='color:red'><strong>0.9281</strong></span> | **0.8740** | <span style='color:red'><strong>0.8612</strong></span> | **0.8768** | **0.8642** |
| baseline | 0.8297 | 0.7884 | 0.8806 | <span style='color:red'><strong>0.9180</strong></span> | 0.8974 | 0.8304 | 0.8895 | 0.8984 | 0.8680 | 0.7924 | 0.8595 | 0.8416 |
| scGPT_human | <span style='color:red'><strong>0.8468</strong></span> | **0.8337** | 0.8798 | 0.8955 | 0.8915 | **0.8691** | **0.8930** | **0.9091** | **0.8697** | **0.8133** | 0.8594 | **0.8664** |
| v4_bias_rec_best | **0.8302** | **0.8126** | **0.8820** | 0.9053 | **0.9002** | **0.8449** | 0.8869 | 0.8824 | 0.8561 | **0.8271** | **0.8650** | <span style='color:red'><strong>0.8820</strong></span> |
| v4_plain_best | 0.7986 | **0.8083** | **0.8827** | 0.8947 | **0.9020** | <span style='color:red'><strong>0.8795</strong></span> | 0.8856 | **0.9053** | 0.8594 | **0.8194** | **0.8649** | **0.8703** |
| v4_type_pe_best | **0.8351** | <span style='color:red'><strong>0.8501</strong></span> | <span style='color:red'><strong>0.8884</strong></span> | 0.9028 | <span style='color:red'><strong>0.9091</strong></span> | **0.8606** | <span style='color:red'><strong>0.9042</strong></span> | 0.8810 | <span style='color:red'><strong>0.8755</strong></span> | **0.8492** | <span style='color:red'><strong>0.8873</strong></span> | **0.8444** |
| scconcept | 0.7817 | 0.7538 | 0.8284 | 0.7815 | 0.8363 | 0.6936 | 0.8353 | 0.8159 | 0.7970 | 0.6515 | 0.7945 | 0.7588 |
| scconcept_encoded | 0.7344 | 0.7343 | 0.8200 | 0.7874 | 0.8251 | 0.7205 | 0.8258 | 0.7686 | 0.7847 | 0.6325 | 0.7621 | 0.7524 |
| cl_scratch_v5 | 0.8288 | **0.7917** | 0.8804 | 0.8987 | **0.9081** | **0.8669** | 0.8877 | **0.9091** | **0.8731** | **0.8479** | **0.8811** | **0.8692** |

## AUPRC (Main)

Latent variables: metric=AUPRC, classifier=aggregated(lr,mlp), aggregation=mean

### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.4524 | 0.3913 | 0.7572 | <span style='color:red'><strong>0.3969</strong></span> | 0.1186 | **0.8898** | 0.7526 | 0.8568 | <span style='color:red'><strong>0.8141</strong></span> | <span style='color:red'><strong>0.8920</strong></span> | <span style='color:red'><strong>0.8319</strong></span> |
| baseline | 0.4731 | 0.4199 | 0.7617 | 0.3837 | 0.2020 | 0.8828 | 0.7748 | 0.8578 | 0.7958 | 0.8793 | 0.8241 |
| scGPT_human | 0.4398 | **0.4321** | 0.7278 | 0.3654 | <span style='color:red'><strong>0.2153</strong></span> | <span style='color:red'><strong>0.8910</strong></span> | 0.7512 | 0.8569 | 0.7943 | **0.8809** | **0.8287** |
| v4_bias_rec_best | 0.4586 | 0.4097 | 0.7550 | 0.3728 | 0.0930 | **0.8886** | **0.7818** | 0.8553 | **0.7991** | **0.8811** | **0.8291** |
| v4_plain_best | **0.4797** | <span style='color:red'><strong>0.4374</strong></span> | <span style='color:red'><strong>0.7791</strong></span> | 0.3711 | 0.1687 | **0.8861** | 0.7683 | 0.8543 | 0.7868 | **0.8846** | **0.8257** |
| v4_type_pe_best | <span style='color:red'><strong>0.4848</strong></span> | 0.4081 | **0.7784** | 0.3567 | 0.1253 | **0.8875** | <span style='color:red'><strong>0.7882</strong></span> | 0.8529 | **0.8008** | **0.8827** | **0.8288** |
| scconcept | 0.3994 | 0.4073 | 0.6752 | 0.2678 | 0.1713 | 0.8649 | 0.6724 | 0.8200 | 0.7555 | 0.8646 | 0.7670 |
| scconcept_encoded | 0.4199 | 0.3832 | 0.6848 | 0.2778 | 0.0507 | 0.8673 | 0.7283 | 0.8272 | 0.7658 | 0.8563 | 0.7633 |
| cl_scratch_v5 | 0.4553 | **0.4357** | 0.7475 | **0.3898** | 0.1257 | **0.8884** | **0.7780** | <span style='color:red'><strong>0.8622</strong></span> | 0.7900 | **0.8833** | **0.8262** |

### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.1561 | 0.1894 | **0.1500** | **0.1191** | **0.2040** | **0.1220** | **0.2749** | **0.2480** | **0.2547** | **0.1889** | **0.2149** | **0.1901** |
| baseline | 0.1592 | <span style='color:red'><strong>0.2094</strong></span> | 0.1489 | 0.0739 | 0.1605 | 0.0909 | 0.2615 | 0.2024 | 0.2376 | 0.1491 | 0.1740 | 0.1400 |
| scGPT_human | 0.1341 | 0.1785 | 0.1449 | **0.1266** | **0.2078** | 0.0727 | **0.2685** | <span style='color:red'><strong>0.2601</strong></span> | **0.2390** | <span style='color:red'><strong>0.2697</strong></span> | **0.2335** | <span style='color:red'><strong>0.3191</strong></span> |
| v4_bias_rec_best | 0.1503 | 0.1646 | 0.1069 | <span style='color:red'><strong>0.1383</strong></span> | **0.1636** | **0.1129** | 0.2104 | **0.2367** | <span style='color:red'><strong>0.2615</strong></span> | 0.1367 | 0.1697 | **0.2149** |
| v4_plain_best | 0.1573 | 0.1930 | 0.1291 | **0.0964** | <span style='color:red'><strong>0.2224</strong></span> | **0.1074** | 0.2156 | **0.2044** | **0.2540** | 0.1381 | <span style='color:red'><strong>0.2359</strong></span> | **0.2197** |
| v4_type_pe_best | <span style='color:red'><strong>0.1729</strong></span> | 0.1714 | <span style='color:red'><strong>0.1668</strong></span> | **0.1046** | **0.1674** | **0.1433** | 0.2528 | **0.2426** | **0.2516** | 0.1467 | **0.1823** | **0.1990** |
| scconcept | 0.1264 | 0.1215 | 0.0876 | **0.0759** | 0.1000 | 0.0639 | 0.1239 | 0.0800 | 0.0828 | 0.1345 | 0.1183 | 0.1105 |
| scconcept_encoded | 0.1066 | 0.0954 | 0.0542 | 0.0495 | 0.0681 | 0.0310 | 0.0706 | 0.0874 | 0.0642 | 0.0741 | 0.0806 | 0.0904 |
| cl_scratch_v5 | 0.1563 | 0.1977 | **0.1528** | **0.1166** | **0.2195** | <span style='color:red'><strong>0.1668</strong></span> | <span style='color:red'><strong>0.2918</strong></span> | **0.2399** | 0.2338 | 0.1359 | **0.1915** | **0.1852** |

### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.2248** | **0.2445** | <span style='color:red'><strong>0.4365</strong></span> | 0.5104 | **0.4480** | 0.2443 | **0.5053** | **0.5506** | **0.3897** | **0.2356** | <span style='color:red'><strong>0.3569</strong></span> | **0.3361** |
| baseline | 0.2173 | 0.1923 | 0.4173 | 0.5467 | 0.4433 | 0.3374 | 0.4855 | 0.5366 | 0.3817 | 0.1408 | 0.3114 | 0.3210 |
| scGPT_human | 0.1940 | 0.1824 | **0.4276** | **0.5499** | **0.4557** | **0.4142** | **0.4900** | **0.5647** | 0.3446 | <span style='color:red'><strong>0.2386</strong></span> | **0.3186** | <span style='color:red'><strong>0.4327</strong></span> |
| v4_bias_rec_best | 0.2118 | 0.1654 | **0.4326** | <span style='color:red'><strong>0.5503</strong></span> | 0.4154 | **0.3629** | 0.4791 | **0.5760** | 0.3415 | **0.2221** | 0.3015 | **0.4103** |
| v4_plain_best | **0.2259** | 0.1516 | 0.4003 | 0.4769 | **0.4611** | <span style='color:red'><strong>0.4461</strong></span> | **0.4985** | <span style='color:red'><strong>0.5775</strong></span> | 0.3716 | **0.2088** | **0.3207** | **0.3924** |
| v4_type_pe_best | <span style='color:red'><strong>0.2471</strong></span> | <span style='color:red'><strong>0.2898</strong></span> | 0.4069 | 0.5140 | <span style='color:red'><strong>0.4924</strong></span> | **0.3709** | **0.5124** | 0.5224 | <span style='color:red'><strong>0.4081</strong></span> | **0.1811** | **0.3414** | **0.4059** |
| scconcept | 0.0799 | 0.1291 | 0.2081 | 0.1275 | 0.2469 | 0.0926 | 0.1848 | 0.1283 | 0.0615 | 0.0478 | 0.0876 | 0.1802 |
| scconcept_encoded | 0.0383 | 0.0699 | 0.1979 | 0.1294 | 0.2242 | 0.0845 | 0.1860 | 0.1015 | 0.0727 | 0.0444 | 0.0541 | 0.0945 |
| cl_scratch_v5 | 0.1923 | **0.2399** | 0.4006 | 0.5100 | **0.4670** | **0.3876** | <span style='color:red'><strong>0.5262</strong></span> | **0.5611** | **0.3836** | **0.1701** | **0.3290** | **0.3995** |

## PRECISION_AT_K (Supplementary)

Latent variables: metric=PRECISION_AT_K, classifier=aggregated(lr,mlp), aggregation=mean

### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.4554 | 0.4046 | 0.6903 | **0.4021** | 0.1500 | **0.8050** | 0.6786 | <span style='color:red'><strong>0.7794</strong></span> | <span style='color:red'><strong>0.7395</strong></span> | <span style='color:red'><strong>0.8124</strong></span> | <span style='color:red'><strong>0.7821</strong></span> |
| baseline | 0.4831 | 0.4220 | <span style='color:red'><strong>0.7071</strong></span> | 0.3846 | 0.2500 | 0.7983 | 0.6891 | 0.7723 | 0.7296 | 0.7996 | 0.7640 |
| scGPT_human | 0.4578 | **0.4306** | 0.6735 | **0.3951** | <span style='color:red'><strong>0.3500</strong></span> | **0.8047** | 0.6723 | **0.7737** | 0.7219 | **0.8010** | 0.7550 |
| v4_bias_rec_best | 0.4783 | **0.4277** | 0.6847 | 0.3811 | 0.1500 | **0.8017** | **0.6954** | **0.7729** | <span style='color:red'><strong>0.7395</strong></span> | 0.7981 | **0.7676** |
| v4_plain_best | <span style='color:red'><strong>0.5000</strong></span> | **0.4364** | 0.7034 | 0.3776 | 0.1000 | **0.8020** | **0.6912** | **0.7782** | 0.7219 | **0.8024** | **0.7694** |
| v4_type_pe_best | **0.4855** | **0.4277** | 0.6978 | 0.3671 | 0.2000 | <span style='color:red'><strong>0.8060</strong></span> | <span style='color:red'><strong>0.7059</strong></span> | **0.7776** | 0.7219 | **0.8043** | 0.7640 |
| scconcept | 0.4289 | <span style='color:red'><strong>0.4509</strong></span> | 0.6474 | 0.3287 | 0.1500 | 0.7809 | 0.6429 | 0.7513 | 0.7009 | 0.7884 | 0.7342 |
| scconcept_encoded | 0.4313 | 0.4162 | 0.6511 | 0.3217 | 0.0000 | 0.7832 | 0.6681 | 0.7549 | 0.7020 | 0.7829 | 0.7179 |
| cl_scratch_v5 | 0.4663 | **0.4393** | 0.6791 | <span style='color:red'><strong>0.4371</strong></span> | 0.1000 | **0.8020** | **0.6954** | 0.7717 | **0.7318** | **0.8036** | 0.7541 |

### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | <span style='color:red'><strong>0.2337</strong></span> | <span style='color:red'><strong>0.2558</strong></span> | **0.2108** | **0.1774** | **0.2553** | **0.1538** | **0.3228** | **0.2746** | **0.2746** | **0.2273** | <span style='color:red'><strong>0.2671</strong></span> | **0.1961** |
| baseline | 0.2308 | 0.2209 | 0.1863 | 0.0968 | 0.2163 | 0.1154 | 0.3122 | 0.2394 | 0.2676 | 0.1818 | 0.2453 | 0.1765 |
| scGPT_human | 0.1805 | 0.1860 | **0.1912** | **0.1290** | <span style='color:red'><strong>0.2908</strong></span> | 0.1154 | **0.3175** | <span style='color:red'><strong>0.2817</strong></span> | <span style='color:red'><strong>0.2782</strong></span> | <span style='color:red'><strong>0.2727</strong></span> | <span style='color:red'><strong>0.2671</strong></span> | <span style='color:red'><strong>0.3333</strong></span> |
| v4_bias_rec_best | 0.2130 | 0.1977 | 0.1814 | <span style='color:red'><strong>0.2097</strong></span> | **0.2411** | **0.1538** | 0.2804 | 0.2324 | **0.2746** | 0.1477 | 0.2298 | **0.2843** |
| v4_plain_best | 0.2308 | **0.2442** | **0.1912** | **0.1452** | **0.2837** | 0.1154 | 0.2804 | **0.2535** | 0.2641 | 0.1705 | **0.2547** | **0.2353** |
| v4_type_pe_best | 0.2278 | 0.2093 | <span style='color:red'><strong>0.2206</strong></span> | 0.0968 | **0.2234** | **0.1538** | 0.2937 | **0.2746** | **0.2746** | 0.1364 | 0.2174 | **0.2157** |
| scconcept | 0.1893 | 0.1047 | 0.1029 | 0.0968 | 0.1702 | 0.0385 | 0.1825 | 0.0915 | 0.0986 | 0.1364 | 0.1801 | 0.1667 |
| scconcept_encoded | 0.1509 | 0.0930 | 0.0686 | 0.0645 | 0.1241 | 0.0385 | 0.1032 | 0.1197 | 0.1092 | 0.1136 | 0.1242 | 0.1176 |
| cl_scratch_v5 | 0.2308 | **0.2326** | **0.1912** | 0.0968 | **0.2801** | <span style='color:red'><strong>0.1923</strong></span> | <span style='color:red'><strong>0.3333</strong></span> | **0.2606** | **0.2711** | 0.1818 | 0.2112 | **0.2353** |

### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.2669 | <span style='color:red'><strong>0.3571</strong></span> | <span style='color:red'><strong>0.4563</strong></span> | 0.4865 | <span style='color:red'><strong>0.5069</strong></span> | 0.3056 | 0.4975 | **0.5362** | 0.3723 | <span style='color:red'><strong>0.3462</strong></span> | <span style='color:red'><strong>0.3720</strong></span> | 0.3462 |
| baseline | 0.2857 | 0.1857 | 0.4476 | 0.5338 | 0.4585 | 0.4167 | 0.5025 | 0.5217 | 0.4078 | 0.1923 | 0.3384 | 0.3718 |
| scGPT_human | 0.2218 | **0.2286** | 0.4476 | 0.5270 | **0.4747** | <span style='color:red'><strong>0.4861</strong></span> | 0.4653 | **0.5435** | 0.3759 | **0.2308** | **0.3567** | **0.3846** |
| v4_bias_rec_best | 0.2556 | **0.2143** | 0.4454 | <span style='color:red'><strong>0.5405</strong></span> | **0.4724** | 0.4028 | 0.4876 | **0.5580** | 0.3511 | **0.2821** | **0.3598** | **0.4231** |
| v4_plain_best | 0.2707 | **0.2429** | 0.4105 | 0.4865 | **0.4931** | **0.4722** | **0.5050** | **0.5507** | 0.3723 | **0.2692** | **0.3476** | **0.4231** |
| v4_type_pe_best | <span style='color:red'><strong>0.3045</strong></span> | <span style='color:red'><strong>0.3571</strong></span> | 0.4214 | 0.5270 | **0.4977** | **0.4306** | <span style='color:red'><strong>0.5272</strong></span> | **0.5290** | <span style='color:red'><strong>0.4149</strong></span> | **0.2564** | <span style='color:red'><strong>0.3720</strong></span> | <span style='color:red'><strong>0.4359</strong></span> |
| scconcept | 0.1316 | 0.1571 | 0.2686 | 0.1622 | 0.3272 | 0.1250 | 0.2599 | 0.1884 | 0.1028 | 0.0513 | 0.1555 | 0.2179 |
| scconcept_encoded | 0.0677 | 0.1286 | 0.2533 | 0.1892 | 0.2972 | 0.1250 | 0.2550 | 0.1304 | 0.1277 | 0.0513 | 0.1067 | 0.1282 |
| cl_scratch_v5 | 0.2594 | **0.2571** | 0.4301 | 0.4932 | **0.4862** | <span style='color:red'><strong>0.4861</strong></span> | **0.5124** | <span style='color:red'><strong>0.5725</strong></span> | 0.3972 | **0.2436** | 0.3232 | **0.3974** |

## RECALL_AT_K (Supplementary)

Latent variables: metric=RECALL_AT_K, classifier=aggregated(lr,mlp), aggregation=mean

### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.4554 | 0.4046 | 0.6903 | **0.4021** | 0.1500 | **0.8050** | 0.6786 | <span style='color:red'><strong>0.7794</strong></span> | <span style='color:red'><strong>0.7395</strong></span> | <span style='color:red'><strong>0.8124</strong></span> | <span style='color:red'><strong>0.7821</strong></span> |
| baseline | 0.4831 | 0.4220 | <span style='color:red'><strong>0.7071</strong></span> | 0.3846 | 0.2500 | 0.7983 | 0.6891 | 0.7723 | 0.7296 | 0.7996 | 0.7640 |
| scGPT_human | 0.4578 | **0.4306** | 0.6735 | **0.3951** | <span style='color:red'><strong>0.3500</strong></span> | **0.8047** | 0.6723 | **0.7737** | 0.7219 | **0.8010** | 0.7550 |
| v4_bias_rec_best | 0.4783 | **0.4277** | 0.6847 | 0.3811 | 0.1500 | **0.8017** | **0.6954** | **0.7729** | <span style='color:red'><strong>0.7395</strong></span> | 0.7981 | **0.7676** |
| v4_plain_best | <span style='color:red'><strong>0.5000</strong></span> | **0.4364** | 0.7034 | 0.3776 | 0.1000 | **0.8020** | **0.6912** | **0.7782** | 0.7219 | **0.8024** | **0.7694** |
| v4_type_pe_best | **0.4855** | **0.4277** | 0.6978 | 0.3671 | 0.2000 | <span style='color:red'><strong>0.8060</strong></span> | <span style='color:red'><strong>0.7059</strong></span> | **0.7776** | 0.7219 | **0.8043** | 0.7640 |
| scconcept | 0.4289 | <span style='color:red'><strong>0.4509</strong></span> | 0.6474 | 0.3287 | 0.1500 | 0.7809 | 0.6429 | 0.7513 | 0.7009 | 0.7884 | 0.7342 |
| scconcept_encoded | 0.4313 | 0.4162 | 0.6511 | 0.3217 | 0.0000 | 0.7832 | 0.6681 | 0.7549 | 0.7020 | 0.7829 | 0.7179 |
| cl_scratch_v5 | 0.4663 | **0.4393** | 0.6791 | <span style='color:red'><strong>0.4371</strong></span> | 0.1000 | **0.8020** | **0.6954** | 0.7717 | **0.7318** | **0.8036** | 0.7541 |

### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | <span style='color:red'><strong>0.2337</strong></span> | <span style='color:red'><strong>0.2558</strong></span> | **0.2108** | **0.1774** | **0.2553** | **0.1538** | **0.3228** | **0.2746** | **0.2746** | **0.2273** | <span style='color:red'><strong>0.2671</strong></span> | **0.1961** |
| baseline | 0.2308 | 0.2209 | 0.1863 | 0.0968 | 0.2163 | 0.1154 | 0.3122 | 0.2394 | 0.2676 | 0.1818 | 0.2453 | 0.1765 |
| scGPT_human | 0.1805 | 0.1860 | **0.1912** | **0.1290** | <span style='color:red'><strong>0.2908</strong></span> | 0.1154 | **0.3175** | <span style='color:red'><strong>0.2817</strong></span> | <span style='color:red'><strong>0.2782</strong></span> | <span style='color:red'><strong>0.2727</strong></span> | <span style='color:red'><strong>0.2671</strong></span> | <span style='color:red'><strong>0.3333</strong></span> |
| v4_bias_rec_best | 0.2130 | 0.1977 | 0.1814 | <span style='color:red'><strong>0.2097</strong></span> | **0.2411** | **0.1538** | 0.2804 | 0.2324 | **0.2746** | 0.1477 | 0.2298 | **0.2843** |
| v4_plain_best | 0.2308 | **0.2442** | **0.1912** | **0.1452** | **0.2837** | 0.1154 | 0.2804 | **0.2535** | 0.2641 | 0.1705 | **0.2547** | **0.2353** |
| v4_type_pe_best | 0.2278 | 0.2093 | <span style='color:red'><strong>0.2206</strong></span> | 0.0968 | **0.2234** | **0.1538** | 0.2937 | **0.2746** | **0.2746** | 0.1364 | 0.2174 | **0.2157** |
| scconcept | 0.1893 | 0.1047 | 0.1029 | 0.0968 | 0.1702 | 0.0385 | 0.1825 | 0.0915 | 0.0986 | 0.1364 | 0.1801 | 0.1667 |
| scconcept_encoded | 0.1509 | 0.0930 | 0.0686 | 0.0645 | 0.1241 | 0.0385 | 0.1032 | 0.1197 | 0.1092 | 0.1136 | 0.1242 | 0.1176 |
| cl_scratch_v5 | 0.2308 | **0.2326** | **0.1912** | 0.0968 | **0.2801** | <span style='color:red'><strong>0.1923</strong></span> | <span style='color:red'><strong>0.3333</strong></span> | **0.2606** | **0.2711** | 0.1818 | 0.2112 | **0.2353** |

### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.2669 | <span style='color:red'><strong>0.3571</strong></span> | <span style='color:red'><strong>0.4563</strong></span> | 0.4865 | <span style='color:red'><strong>0.5069</strong></span> | 0.3056 | 0.4975 | **0.5362** | 0.3723 | <span style='color:red'><strong>0.3462</strong></span> | <span style='color:red'><strong>0.3720</strong></span> | 0.3462 |
| baseline | 0.2857 | 0.1857 | 0.4476 | 0.5338 | 0.4585 | 0.4167 | 0.5025 | 0.5217 | 0.4078 | 0.1923 | 0.3384 | 0.3718 |
| scGPT_human | 0.2218 | **0.2286** | 0.4476 | 0.5270 | **0.4747** | <span style='color:red'><strong>0.4861</strong></span> | 0.4653 | **0.5435** | 0.3759 | **0.2308** | **0.3567** | **0.3846** |
| v4_bias_rec_best | 0.2556 | **0.2143** | 0.4454 | <span style='color:red'><strong>0.5405</strong></span> | **0.4724** | 0.4028 | 0.4876 | **0.5580** | 0.3511 | **0.2821** | **0.3598** | **0.4231** |
| v4_plain_best | 0.2707 | **0.2429** | 0.4105 | 0.4865 | **0.4931** | **0.4722** | **0.5050** | **0.5507** | 0.3723 | **0.2692** | **0.3476** | **0.4231** |
| v4_type_pe_best | <span style='color:red'><strong>0.3045</strong></span> | <span style='color:red'><strong>0.3571</strong></span> | 0.4214 | 0.5270 | **0.4977** | **0.4306** | <span style='color:red'><strong>0.5272</strong></span> | **0.5290** | <span style='color:red'><strong>0.4149</strong></span> | **0.2564** | <span style='color:red'><strong>0.3720</strong></span> | <span style='color:red'><strong>0.4359</strong></span> |
| scconcept | 0.1316 | 0.1571 | 0.2686 | 0.1622 | 0.3272 | 0.1250 | 0.2599 | 0.1884 | 0.1028 | 0.0513 | 0.1555 | 0.2179 |
| scconcept_encoded | 0.0677 | 0.1286 | 0.2533 | 0.1892 | 0.2972 | 0.1250 | 0.2550 | 0.1304 | 0.1277 | 0.0513 | 0.1067 | 0.1282 |
| cl_scratch_v5 | 0.2594 | **0.2571** | 0.4301 | 0.4932 | **0.4862** | <span style='color:red'><strong>0.4861</strong></span> | **0.5124** | <span style='color:red'><strong>0.5725</strong></span> | 0.3972 | **0.2436** | 0.3232 | **0.3974** |

## F1 (Supplementary)

Latent variables: metric=F1, classifier=aggregated(lr,mlp), aggregation=mean

### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.3704 | **0.3859** | 0.6843 | **0.3472** | 0.0000 | **0.8081** | 0.6943 | **0.7846** | **0.7518** | <span style='color:red'><strong>0.8206</strong></span> | <span style='color:red'><strong>0.7927</strong></span> |
| baseline | 0.4376 | 0.3572 | 0.6999 | 0.2911 | 0.0769 | 0.8067 | 0.6979 | 0.7814 | 0.7417 | 0.7954 | 0.7706 |
| scGPT_human | <span style='color:red'><strong>0.4450</strong></span> | **0.3852** | 0.6829 | **0.3652** | <span style='color:red'><strong>0.0909</strong></span> | 0.8049 | 0.6749 | **0.7833** | 0.7299 | **0.8093** | 0.7629 |
| v4_bias_rec_best | 0.4146 | **0.3769** | 0.6842 | **0.3359** | 0.0625 | **0.8072** | <span style='color:red'><strong>0.7016</strong></span> | **0.7815** | <span style='color:red'><strong>0.7582</strong></span> | **0.8106** | 0.7700 |
| v4_plain_best | **0.4406** | **0.3736** | <span style='color:red'><strong>0.7116</strong></span> | **0.3116** | 0.0714 | **0.8076** | 0.6845 | **0.7873** | 0.7273 | **0.8071** | 0.7706 |
| v4_type_pe_best | 0.4372 | **0.3778** | 0.6951 | **0.3238** | 0.0000 | **0.8080** | **0.6995** | <span style='color:red'><strong>0.7899</strong></span> | **0.7563** | **0.8121** | **0.7837** |
| scconcept | 0.3992 | **0.3711** | 0.6510 | 0.2475 | <span style='color:red'><strong>0.0909</strong></span> | 0.7889 | 0.6409 | 0.7635 | 0.7115 | **0.7998** | 0.7447 |
| scconcept_encoded | 0.3150 | 0.3368 | 0.6586 | 0.2071 | 0.0000 | 0.7906 | 0.6626 | 0.7626 | 0.7210 | 0.7933 | 0.7319 |
| cl_scratch_v5 | 0.3982 | <span style='color:red'><strong>0.3916</strong></span> | 0.6689 | <span style='color:red'><strong>0.3695</strong></span> | 0.0769 | <span style='color:red'><strong>0.8103</strong></span> | 0.6964 | 0.7742 | **0.7444** | **0.8119** | 0.7645 |

### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.0733 | 0.1500 | 0.0667 | **0.0932** | **0.1542** | 0.0625 | **0.2877** | **0.2258** | <span style='color:red'><strong>0.2725</strong></span> | 0.1039 | **0.2180** | **0.1455** |
| baseline | 0.0747 | <span style='color:red'><strong>0.1682</strong></span> | 0.0840 | 0.0588 | 0.1024 | <span style='color:red'><strong>0.0714</strong></span> | 0.2616 | 0.1738 | 0.2227 | 0.1235 | 0.1738 | 0.1321 |
| scGPT_human | **0.1121** | 0.1194 | <span style='color:red'><strong>0.1075</strong></span> | 0.0250 | <span style='color:red'><strong>0.2733</strong></span> | 0.0000 | <span style='color:red'><strong>0.2955</strong></span> | <span style='color:red'><strong>0.2529</strong></span> | **0.2651** | <span style='color:red'><strong>0.2332</strong></span> | <span style='color:red'><strong>0.2750</strong></span> | <span style='color:red'><strong>0.2500</strong></span> |
| v4_bias_rec_best | 0.0521 | 0.0831 | 0.0538 | <span style='color:red'><strong>0.1222</strong></span> | **0.1145** | 0.0625 | 0.1488 | **0.1886** | **0.2706** | 0.1139 | 0.1451 | **0.2051** |
| v4_plain_best | <span style='color:red'><strong>0.1288</strong></span> | 0.1272 | 0.0667 | **0.0800** | **0.2040** | <span style='color:red'><strong>0.0714</strong></span> | 0.1584 | 0.1662 | **0.2668** | **0.1294** | **0.2356** | **0.1892** |
| v4_type_pe_best | **0.1004** | 0.0886 | **0.1008** | **0.0652** | **0.1305** | 0.0667 | 0.2504 | **0.2410** | **0.2620** | 0.0957 | 0.1304 | **0.1815** |
| scconcept | **0.1124** | 0.0556 | **0.0878** | 0.0233 | 0.0995 | 0.0667 | 0.1141 | 0.0305 | 0.0571 | 0.0882 | 0.0965 | 0.1016 |
| scconcept_encoded | 0.0570 | 0.0571 | 0.0318 | 0.0208 | 0.0674 | 0.0000 | 0.0247 | 0.0866 | 0.0365 | 0.0479 | 0.0439 | 0.0909 |
| cl_scratch_v5 | **0.0861** | 0.1651 | **0.0967** | **0.0779** | **0.2066** | <span style='color:red'><strong>0.0714</strong></span> | **0.2767** | **0.2164** | **0.2554** | **0.1250** | **0.1879** | **0.1805** |

### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | <span style='color:red'><strong>0.3041</strong></span> | 0.1346 | **0.4478** | 0.4606 | **0.4026** | 0.2053 | 0.4945 | **0.5244** | **0.4193** | <span style='color:red'><strong>0.1647</strong></span> | <span style='color:red'><strong>0.3609</strong></span> | 0.2714 |
| baseline | 0.2472 | 0.1600 | 0.3971 | 0.5443 | 0.3529 | 0.3089 | 0.5004 | 0.4649 | 0.3706 | 0.1000 | 0.3355 | 0.3200 |
| scGPT_human | 0.2313 | **0.1636** | <span style='color:red'><strong>0.4568</strong></span> | <span style='color:red'><strong>0.5575</strong></span> | <span style='color:red'><strong>0.4735</strong></span> | **0.3880** | 0.4827 | **0.5616** | 0.3692 | **0.1575** | 0.3193 | <span style='color:red'><strong>0.4375</strong></span> |
| v4_bias_rec_best | **0.2616** | 0.1429 | **0.4540** | **0.5531** | **0.4170** | **0.3508** | 0.4844 | **0.5707** | 0.3579 | **0.1607** | 0.2640 | **0.3577** |
| v4_plain_best | **0.2774** | <span style='color:red'><strong>0.1930</strong></span> | **0.4100** | 0.4429 | **0.4122** | <span style='color:red'><strong>0.4686</strong></span> | 0.4910 | **0.5104** | 0.3460 | **0.1540** | 0.3099 | 0.2824 |
| v4_type_pe_best | 0.2352 | 0.1429 | **0.4000** | 0.5330 | **0.4356** | **0.3895** | 0.4779 | **0.5304** | <span style='color:red'><strong>0.4275</strong></span> | 0.0810 | **0.3468** | 0.2414 |
| scconcept | 0.0622 | 0.1200 | 0.2136 | 0.0698 | 0.2220 | 0.0711 | 0.1560 | 0.0840 | 0.0463 | 0.0213 | 0.0831 | 0.1724 |
| scconcept_encoded | 0.0242 | 0.1000 | 0.1643 | 0.0930 | 0.1864 | 0.0423 | 0.1724 | 0.0727 | 0.0480 | 0.0213 | 0.0244 | 0.1071 |
| cl_scratch_v5 | 0.2435 | **0.1667** | **0.4018** | 0.4424 | **0.4185** | **0.3395** | <span style='color:red'><strong>0.5321</strong></span> | <span style='color:red'><strong>0.5746</strong></span> | **0.4212** | **0.1267** | **0.3359** | 0.3092 |

## SPECIFICITY (Supplementary)

Latent variables: metric=SPECIFICITY, classifier=aggregated(lr,mlp), aggregation=mean

### Specific

| Embedding | hESC_Specific_1000 | hESC_Specific_500 | hHep_Specific_1000 | mDC_Specific_1000 | mDC_Specific_500 | mHSC-E_Specific_1000 | mHSC-E_Specific_500 | mHSC-GM_Specific_1000 | mHSC-GM_Specific_500 | mHSC-L_Specific_1000 | mHSC-L_Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | **0.9354** | 0.8992 | **0.9361** | 0.9696 | 0.9955 | **0.7797** | **0.7645** | **0.7649** | 0.6288 | 0.7199 | 0.6129 |
| baseline | 0.9298 | 0.9237 | 0.9339 | <span style='color:red'><strong>0.9763</strong></span> | 0.9955 | 0.7722 | 0.7370 | 0.7449 | <span style='color:red'><strong>0.6425</strong></span> | <span style='color:red'><strong>0.7261</strong></span> | <span style='color:red'><strong>0.6496</strong></span> |
| scGPT_human | 0.9096 | 0.9151 | 0.9260 | 0.9652 | <span style='color:red'><strong>1.0000</strong></span> | <span style='color:red'><strong>0.7909</strong></span> | **0.8049** | **0.7593** | 0.6123 | 0.6960 | 0.5945 |
| v4_bias_rec_best | 0.9284 | 0.9231 | 0.9294 | 0.9760 | 0.9888 | **0.7859** | **0.7543** | **0.7593** | 0.6192 | 0.6991 | 0.5879 |
| v4_plain_best | **0.9340** | <span style='color:red'><strong>0.9248</strong></span> | 0.9322 | 0.9734 | 0.9933 | 0.7679 | <span style='color:red'><strong>0.8136</strong></span> | **0.7646** | 0.6301 | 0.7183 | 0.6050 |
| v4_type_pe_best | 0.9288 | **0.9243** | 0.9322 | 0.9760 | **0.9978** | **0.7892** | **0.8136** | **0.7525** | 0.5795 | 0.6981 | 0.5906 |
| scconcept | 0.9141 | 0.9226 | 0.9036 | 0.9582 | <span style='color:red'><strong>1.0000</strong></span> | 0.7672 | **0.7543** | 0.7317 | 0.6041 | 0.6898 | 0.5512 |
| scconcept_encoded | <span style='color:red'><strong>0.9382</strong></span> | 0.9174 | 0.9103 | 0.9734 | 0.9911 | 0.7584 | **0.7948** | 0.7416 | 0.5658 | 0.6804 | 0.5328 |
| cl_scratch_v5 | **0.9361** | 0.9214 | <span style='color:red'><strong>0.9367</strong></span> | 0.9754 | 0.9955 | **0.7830** | **0.7890** | <span style='color:red'><strong>0.7730</strong></span> | 0.6164 | 0.7025 | 0.5814 |

### Non-Specific

| Embedding | hESC_Non-Specific_1000 | hESC_Non-Specific_500 | hHep_Non-Specific_1000 | hHep_Non-Specific_500 | mDC_Non-Specific_1000 | mDC_Non-Specific_500 | mHSC-E_Non-Specific_1000 | mHSC-E_Non-Specific_500 | mHSC-GM_Non-Specific_1000 | mHSC-GM_Non-Specific_500 | mHSC-L_Non-Specific_1000 | mHSC-L_Non-Specific_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.9963 | **0.9931** | 0.9986 | **0.9956** | 0.9985 | 0.9988 | 0.9971 | 0.9893 | **0.9988** | **0.9924** | 0.9980 | **0.9931** |
| baseline | 0.9968 | 0.9920 | <span style='color:red'><strong>0.9990</strong></span> | 0.9951 | 0.9988 | <span style='color:red'><strong>1.0000</strong></span> | 0.9972 | 0.9895 | 0.9987 | 0.9921 | 0.9980 | 0.9901 |
| scGPT_human | 0.9916 | <span style='color:red'><strong>0.9956</strong></span> | 0.9940 | <span style='color:red'><strong>0.9974</strong></span> | 0.9930 | 0.9988 | 0.9943 | <span style='color:red'><strong>0.9922</strong></span> | 0.9961 | **0.9936** | 0.9957 | <span style='color:red'><strong>0.9945</strong></span> |
| v4_bias_rec_best | **0.9974** | 0.9918 | 0.9987 | <span style='color:red'><strong>0.9974</strong></span> | 0.9984 | 0.9988 | **0.9974** | 0.9880 | 0.9986 | **0.9924** | **0.9987** | **0.9920** |
| v4_plain_best | 0.9957 | **0.9953** | 0.9978 | **0.9956** | 0.9975 | <span style='color:red'><strong>1.0000</strong></span> | **0.9978** | 0.9887 | <span style='color:red'><strong>0.9990</strong></span> | 0.9912 | <span style='color:red'><strong>0.9990</strong></span> | **0.9923** |
| v4_type_pe_best | <span style='color:red'><strong>0.9974</strong></span> | 0.9918 | 0.9984 | **0.9965** | <span style='color:red'><strong>0.9990</strong></span> | 0.9994 | 0.9971 | 0.9885 | 0.9987 | 0.9880 | **0.9988** | **0.9926** |
| scconcept | 0.9944 | **0.9931** | 0.9940 | **0.9968** | 0.9967 | 0.9994 | 0.9962 | 0.9880 | 0.9959 | <span style='color:red'><strong>0.9947</strong></span> | 0.9965 | **0.9926** |
| scconcept_encoded | 0.9957 | **0.9934** | 0.9971 | **0.9954** | 0.9978 | 0.9994 | <span style='color:red'><strong>0.9978</strong></span> | 0.9847 | 0.9980 | 0.9909 | **0.9985** | **0.9920** |
| cl_scratch_v5 | 0.9967 | 0.9918 | 0.9986 | **0.9971** | 0.9969 | <span style='color:red'><strong>1.0000</strong></span> | 0.9969 | 0.9876 | 0.9983 | **0.9924** | 0.9980 | **0.9909** |

### STRING

| Embedding | hESC_STRING_1000 | hESC_STRING_500 | hHep_STRING_1000 | hHep_STRING_500 | mDC_STRING_1000 | mDC_STRING_500 | mHSC-E_STRING_1000 | mHSC-E_STRING_500 | mHSC-GM_STRING_1000 | mHSC-GM_STRING_500 | mHSC-L_STRING_1000 | mHSC-L_STRING_500 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minus | 0.9984 | 0.9982 | **0.9970** | **0.9928** | 0.9972 | **0.9932** | **0.9976** | **0.9956** | 0.9989 | **0.9978** | **0.9991** | **0.9981** |
| baseline | 0.9984 | <span style='color:red'><strong>0.9987</strong></span> | 0.9969 | 0.9895 | <span style='color:red'><strong>0.9980</strong></span> | 0.9928 | 0.9973 | 0.9947 | <span style='color:red'><strong>0.9992</strong></span> | 0.9970 | 0.9988 | 0.9977 |
| scGPT_human | 0.9954 | 0.9980 | 0.9952 | <span style='color:red'><strong>0.9941</strong></span> | 0.9947 | <span style='color:red'><strong>0.9972</strong></span> | 0.9956 | **0.9963** | 0.9961 | <span style='color:red'><strong>0.9996</strong></span> | 0.9976 | **0.9985** |
| v4_bias_rec_best | 0.9984 | 0.9976 | **0.9971** | **0.9914** | 0.9952 | 0.9916 | **0.9977** | **0.9965** | 0.9988 | **0.9976** | <span style='color:red'><strong>0.9993</strong></span> | 0.9973 |
| v4_plain_best | 0.9982 | 0.9980 | **0.9969** | 0.9857 | 0.9974 | 0.9920 | **0.9980** | **0.9958** | 0.9990 | **0.9982** | **0.9991** | 0.9973 |
| v4_type_pe_best | **0.9986** | <span style='color:red'><strong>0.9987</strong></span> | **0.9969** | 0.9892 | 0.9966 | **0.9936** | **0.9983** | **0.9960** | 0.9988 | **0.9976** | **0.9990** | <span style='color:red'><strong>0.9990</strong></span> |
| scconcept | 0.9970 | 0.9984 | 0.9963 | **0.9903** | 0.9957 | 0.9884 | 0.9971 | 0.9928 | 0.9975 | **0.9986** | 0.9980 | **0.9981** |
| scconcept_encoded | <span style='color:red'><strong>0.9989</strong></span> | 0.9982 | <span style='color:red'><strong>0.9978</strong></span> | **0.9899** | 0.9961 | 0.9872 | **0.9974** | 0.9942 | 0.9979 | **0.9986** | 0.9988 | 0.9977 |
| cl_scratch_v5 | **0.9985** | 0.9973 | 0.9966 | **0.9930** | 0.9972 | **0.9952** | <span style='color:red'><strong>0.9985</strong></span> | <span style='color:red'><strong>0.9972</strong></span> | 0.9989 | **0.9972** | **0.9992** | **0.9981** |

