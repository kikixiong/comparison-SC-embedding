# GRN BEELINE Full Diagnostics

Diagnostics are scoped to the GRN BEELINE full benchmark only.

## Files

- `dataset_class_balance.csv`: per-dataset split sizes, positive ratios, and the random-ranking AUPRC baseline.
- `metric_summary_by_network_embedding.csv`: metric summaries by network group, embedding, and classifier.

## Class-balance summary

| dataset | network_group | n_genes | test_n_positive | test_n_negative | test_positive_ratio | random_auprc_baseline |
| --- | --- | --- | --- | --- | --- | --- |
| hESC_Specific_500 | Specific | 500 | 173 | 878 | 0.164605 | 0.164605 |
| hESC_Specific_1000 | Specific | 1000 | 415 | 2136 | 0.162681 | 0.162681 |
| hESC_Non-Specific_500 | Non-Specific | 500 | 43 | 1823 | 0.023044 | 0.023044 |
| hESC_Non-Specific_1000 | Non-Specific | 1000 | 169 | 9563 | 0.017365 | 0.017365 |
| hESC_STRING_500 | STRING | 500 | 35 | 2764 | 0.012504 | 0.012504 |
| hESC_STRING_1000 | STRING | 1000 | 133 | 12378 | 0.010631 | 0.010631 |
| hHep_Specific_1000 | Specific | 1000 | 268 | 892 | 0.231034 | 0.231034 |
| hHep_Non-Specific_500 | Non-Specific | 500 | 31 | 1722 | 0.017684 | 0.017684 |
| hHep_Non-Specific_1000 | Non-Specific | 1000 | 102 | 8703 | 0.011584 | 0.011584 |
| hHep_STRING_500 | STRING | 500 | 74 | 2372 | 0.030253 | 0.030253 |
| hHep_STRING_1000 | STRING | 1000 | 229 | 12048 | 0.018653 | 0.018653 |
| mDC_Specific_500 | Specific | 500 | 10 | 224 | 0.042735 | 0.042735 |
| mDC_Specific_1000 | Specific | 1000 | 143 | 1710 | 0.077172 | 0.077172 |
| mDC_Non-Specific_500 | Non-Specific | 500 | 13 | 806 | 0.015873 | 0.015873 |
| mDC_Non-Specific_1000 | Non-Specific | 1000 | 141 | 8896 | 0.015603 | 0.015603 |
| mDC_STRING_500 | STRING | 500 | 36 | 1247 | 0.028059 | 0.028059 |
| mDC_STRING_1000 | STRING | 1000 | 217 | 9048 | 0.023421 | 0.023421 |
| mHSC-E_Specific_500 | Specific | 500 | 238 | 346 | 0.407534 | 0.407534 |
| mHSC-E_Specific_1000 | Specific | 1000 | 1490 | 1523 | 0.494524 | 0.494524 |
| mHSC-E_Non-Specific_500 | Non-Specific | 500 | 71 | 2381 | 0.028956 | 0.028956 |
| mHSC-E_Non-Specific_1000 | Non-Specific | 1000 | 189 | 10930 | 0.016998 | 0.016998 |
| mHSC-E_STRING_500 | STRING | 500 | 69 | 2846 | 0.023671 | 0.023671 |
| mHSC-E_STRING_1000 | STRING | 1000 | 202 | 12075 | 0.016454 | 0.016454 |
| mHSC-GM_Specific_500 | Specific | 500 | 453 | 365 | 0.553790 | 0.553790 |
| mHSC-GM_Specific_1000 | Specific | 1000 | 1695 | 1780 | 0.487770 | 0.487770 |
| mHSC-GM_Non-Specific_500 | Non-Specific | 500 | 44 | 1707 | 0.025128 | 0.025128 |
| mHSC-GM_Non-Specific_1000 | Non-Specific | 1000 | 142 | 10985 | 0.012762 | 0.012762 |
| mHSC-GM_STRING_500 | STRING | 500 | 39 | 2531 | 0.015175 | 0.015175 |
| mHSC-GM_STRING_1000 | STRING | 1000 | 141 | 13064 | 0.010678 | 0.010678 |
| mHSC-L_Specific_500 | Specific | 500 | 553 | 381 | 0.592077 | 0.592077 |
| mHSC-L_Specific_1000 | Specific | 1000 | 2098 | 1610 | 0.565804 | 0.565804 |
| mHSC-L_Non-Specific_500 | Non-Specific | 500 | 51 | 1816 | 0.027317 | 0.027317 |
| mHSC-L_Non-Specific_1000 | Non-Specific | 1000 | 161 | 11421 | 0.013901 | 0.013901 |
| mHSC-L_STRING_500 | STRING | 500 | 39 | 2408 | 0.015938 | 0.015938 |
| mHSC-L_STRING_1000 | STRING | 1000 | 164 | 15126 | 0.010726 | 0.010726 |

