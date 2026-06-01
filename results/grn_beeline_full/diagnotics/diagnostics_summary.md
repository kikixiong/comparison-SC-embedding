# GRN BEELINE Full Diagnostics

Diagnostics are scoped to the GRN BEELINE full benchmark only.

## Files

- `dataset_class_balance.csv`: per-dataset split sizes, positive ratios, random-ranking AUPRC baseline, and network-context retention diagnostics.
- `metric_summary_by_network_embedding.csv`: metric summaries by network group, negative protocol, embedding, classifier, AUPRC lift, and pair-space separability diagnostics.

## Class-balance summary

| dataset | network_group | negative_protocol | n_genes | n_edges_raw | n_edges_after_expression_filter | n_positive_edges_after_filter | hvg_edge_retention | test_n_positive | test_n_negative | test_positive_ratio | test_negative_to_positive_ratio | random_auprc_baseline |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| hESC_Specific_500 | Specific | tf_stratified_1to10 | 500 | 436563 | 213597 | 712 | 0.003333 | 169 | 465 | 0.266562 | 2.751479 | 0.266562 |
| hESC_Specific_500 | Specific | full_candidate | 500 | 436563 | 213597 | 712 | 0.003333 | 169 | 875 | 0.161877 | 5.177515 | 0.161877 |
| hESC_Specific_1000 | Specific | tf_stratified_1to10 | 1000 | 436563 | 213597 | 1768 | 0.008277 | 412 | 1026 | 0.286509 | 2.490291 | 0.286509 |
| hESC_Specific_1000 | Specific | full_candidate | 1000 | 436563 | 213597 | 1768 | 0.008277 | 412 | 2128 | 0.162205 | 5.165049 | 0.162205 |
| hESC_Non-Specific_500 | Non-Specific | tf_stratified_1to10 | 500 | 386293 | 81353 | 151 | 0.001856 | 42 | 334 | 0.111702 | 7.952381 | 0.111702 |
| hESC_Non-Specific_500 | Non-Specific | full_candidate | 500 | 386293 | 81353 | 151 | 0.001856 | 42 | 1810 | 0.022678 | 43.095238 | 0.022678 |
| hESC_Non-Specific_1000 | Non-Specific | tf_stratified_1to10 | 1000 | 386293 | 81353 | 625 | 0.007683 | 161 | 1230 | 0.115744 | 7.639752 | 0.115744 |
| hESC_Non-Specific_1000 | Non-Specific | full_candidate | 1000 | 386293 | 81353 | 625 | 0.007683 | 161 | 9529 | 0.016615 | 59.186335 | 0.016615 |
| hESC_STRING_500 | STRING | tf_stratified_1to10 | 500 | 198285 | 113697 | 95 | 0.001671 | 32 | 320 | 0.090909 | 10.000000 | 0.090909 |
| hESC_STRING_500 | STRING | full_candidate | 500 | 198285 | 113697 | 95 | 0.001671 | 32 | 2745 | 0.011523 | 85.781250 | 0.011523 |
| hESC_STRING_1000 | STRING | tf_stratified_1to10 | 1000 | 198285 | 113697 | 411 | 0.007230 | 119 | 1190 | 0.090909 | 10.000000 | 0.090909 |
| hESC_STRING_1000 | STRING | full_candidate | 1000 | 198285 | 113697 | 411 | 0.007230 | 119 | 12344 | 0.009548 | 103.731092 | 0.009548 |
| hHep_Specific_1000 | Specific | tf_stratified_1to10 | 1000 | 342862 | 252595 | 1145 | 0.004533 | 266 | 583 | 0.313310 | 2.191729 | 0.313310 |
| hHep_Specific_1000 | Specific | full_candidate | 1000 | 342862 | 252595 | 1145 | 0.004533 | 266 | 888 | 0.230503 | 3.338346 | 0.230503 |
| hHep_Non-Specific_500 | Non-Specific | tf_stratified_1to10 | 500 | 386293 | 78471 | 92 | 0.001172 | 29 | 290 | 0.090909 | 10.000000 | 0.090909 |
| hHep_Non-Specific_500 | Non-Specific | full_candidate | 500 | 386293 | 78471 | 92 | 0.001172 | 29 | 1710 | 0.016676 | 58.965517 | 0.016676 |
| hHep_Non-Specific_1000 | Non-Specific | tf_stratified_1to10 | 1000 | 386293 | 78471 | 348 | 0.004435 | 97 | 970 | 0.090909 | 10.000000 | 0.090909 |
| hHep_Non-Specific_1000 | Non-Specific | full_candidate | 1000 | 386293 | 78471 | 348 | 0.004435 | 97 | 8672 | 0.011062 | 89.402062 | 0.011062 |
| hHep_STRING_500 | STRING | tf_stratified_1to10 | 500 | 198285 | 141539 | 256 | 0.003617 | 67 | 666 | 0.091405 | 9.940299 | 0.091405 |
| hHep_STRING_500 | STRING | full_candidate | 500 | 198285 | 141539 | 256 | 0.003617 | 67 | 2362 | 0.027583 | 35.253731 | 0.027583 |
| hHep_STRING_1000 | STRING | tf_stratified_1to10 | 1000 | 198285 | 141539 | 824 | 0.011643 | 215 | 2150 | 0.090909 | 10.000000 | 0.090909 |
| hHep_STRING_1000 | STRING | full_candidate | 1000 | 198285 | 141539 | 824 | 0.011643 | 215 | 12018 | 0.017575 | 55.897674 | 0.017575 |
| mDC_Specific_500 | Specific | tf_stratified_1to10 | 500 | 30658 | 12182 | 33 | 0.002709 | 8 | 80 | 0.090909 | 10.000000 | 0.090909 |
| mDC_Specific_500 | Specific | full_candidate | 500 | 30658 | 12182 | 33 | 0.002709 | 8 | 223 | 0.034632 | 27.875000 | 0.034632 |
| mDC_Specific_1000 | Specific | tf_stratified_1to10 | 1000 | 30658 | 12182 | 596 | 0.048925 | 140 | 696 | 0.167464 | 4.971429 | 0.167464 |
| mDC_Specific_1000 | Specific | full_candidate | 1000 | 30658 | 12182 | 596 | 0.048925 | 140 | 1705 | 0.075881 | 12.178571 | 0.075881 |
| mDC_Non-Specific_500 | Non-Specific | tf_stratified_1to10 | 500 | 100139 | 24546 | 33 | 0.001344 | 11 | 110 | 0.090909 | 10.000000 | 0.090909 |
| mDC_Non-Specific_500 | Non-Specific | full_candidate | 500 | 100139 | 24546 | 33 | 0.001344 | 11 | 800 | 0.013564 | 72.727273 | 0.013564 |
| mDC_Non-Specific_1000 | Non-Specific | tf_stratified_1to10 | 1000 | 100139 | 24546 | 492 | 0.020044 | 129 | 1290 | 0.090909 | 10.000000 | 0.090909 |
| mDC_Non-Specific_1000 | Non-Specific | full_candidate | 1000 | 100139 | 24546 | 492 | 0.020044 | 129 | 8870 | 0.014335 | 68.759690 | 0.014335 |
| mDC_STRING_500 | STRING | tf_stratified_1to10 | 500 | 157134 | 60928 | 125 | 0.004103 | 33 | 318 | 0.094017 | 9.636364 | 0.094017 |
| mDC_STRING_500 | STRING | full_candidate | 500 | 157134 | 60928 | 125 | 0.004103 | 33 | 1240 | 0.025923 | 37.575758 | 0.025923 |
| mDC_STRING_1000 | STRING | tf_stratified_1to10 | 1000 | 157134 | 60928 | 817 | 0.026819 | 209 | 2090 | 0.090909 | 10.000000 | 0.090909 |
| mDC_STRING_1000 | STRING | full_candidate | 1000 | 157134 | 60928 | 817 | 0.026819 | 209 | 9023 | 0.022639 | 43.172249 | 0.022639 |
| mHSC-E_Specific_500 | Specific | tf_stratified_1to10 | 500 | 1078888 | 108816 | 1008 | 0.009263 | 235 | 256 | 0.478615 | 1.089362 | 0.478615 |
| mHSC-E_Specific_500 | Specific | full_candidate | 500 | 1078888 | 108816 | 1008 | 0.009263 | 235 | 345 | 0.405172 | 1.468085 | 0.405172 |
| mHSC-E_Specific_1000 | Specific | tf_stratified_1to10 | 1000 | 1078888 | 108816 | 6427 | 0.059063 | 1482 | 929 | 0.614683 | 0.626856 | 0.614683 |
| mHSC-E_Specific_1000 | Specific | full_candidate | 1000 | 1078888 | 108816 | 6427 | 0.059063 | 1482 | 1518 | 0.494000 | 1.024291 | 0.494000 |
| mHSC-E_Non-Specific_500 | Non-Specific | tf_stratified_1to10 | 500 | 100139 | 6876 | 248 | 0.036067 | 66 | 603 | 0.098655 | 9.136364 | 0.098655 |
| mHSC-E_Non-Specific_500 | Non-Specific | full_candidate | 500 | 100139 | 6876 | 248 | 0.036067 | 66 | 2364 | 0.027160 | 35.818182 | 0.027160 |
| mHSC-E_Non-Specific_1000 | Non-Specific | tf_stratified_1to10 | 1000 | 100139 | 6876 | 691 | 0.100494 | 178 | 1658 | 0.096950 | 9.314607 | 0.096950 |
| mHSC-E_Non-Specific_1000 | Non-Specific | full_candidate | 1000 | 100139 | 6876 | 691 | 0.100494 | 178 | 10898 | 0.016071 | 61.224719 | 0.016071 |
| mHSC-E_STRING_500 | STRING | tf_stratified_1to10 | 500 | 157134 | 10832 | 228 | 0.042097 | 62 | 610 | 0.092262 | 9.838710 | 0.092262 |
| mHSC-E_STRING_500 | STRING | full_candidate | 500 | 157134 | 10832 | 228 | 0.042097 | 62 | 2830 | 0.021438 | 45.645161 | 0.021438 |
| mHSC-E_STRING_1000 | STRING | tf_stratified_1to10 | 1000 | 157134 | 10832 | 702 | 0.129616 | 186 | 1860 | 0.090909 | 10.000000 | 0.090909 |
| mHSC-E_STRING_1000 | STRING | full_candidate | 1000 | 157134 | 10832 | 702 | 0.129616 | 186 | 12045 | 0.015207 | 64.758065 | 0.015207 |
| mHSC-GM_Specific_500 | Specific | tf_stratified_1to10 | 500 | 1078888 | 108816 | 1941 | 0.017837 | 448 | 362 | 0.553086 | 0.808036 | 0.553086 |
| mHSC-GM_Specific_500 | Specific | full_candidate | 500 | 1078888 | 108816 | 1941 | 0.017837 | 448 | 362 | 0.553086 | 0.808036 | 0.553086 |
| mHSC-GM_Specific_1000 | Specific | tf_stratified_1to10 | 1000 | 1078888 | 108816 | 7310 | 0.067178 | 1689 | 1233 | 0.578029 | 0.730018 | 0.578029 |
| mHSC-GM_Specific_1000 | Specific | full_candidate | 1000 | 1078888 | 108816 | 7310 | 0.067178 | 1689 | 1775 | 0.487587 | 1.050918 | 0.487587 |
| mHSC-GM_Non-Specific_500 | Non-Specific | tf_stratified_1to10 | 500 | 100139 | 6876 | 143 | 0.020797 | 39 | 390 | 0.090909 | 10.000000 | 0.090909 |
| mHSC-GM_Non-Specific_500 | Non-Specific | full_candidate | 500 | 100139 | 6876 | 143 | 0.020797 | 39 | 1699 | 0.022440 | 43.564103 | 0.022440 |
| mHSC-GM_Non-Specific_1000 | Non-Specific | tf_stratified_1to10 | 1000 | 100139 | 6876 | 493 | 0.071699 | 137 | 1326 | 0.093643 | 9.678832 | 0.093643 |
| mHSC-GM_Non-Specific_1000 | Non-Specific | full_candidate | 1000 | 100139 | 6876 | 493 | 0.071699 | 137 | 10944 | 0.012364 | 79.883212 | 0.012364 |
| mHSC-GM_STRING_500 | STRING | tf_stratified_1to10 | 500 | 157134 | 10832 | 101 | 0.018648 | 31 | 310 | 0.090909 | 10.000000 | 0.090909 |
| mHSC-GM_STRING_500 | STRING | full_candidate | 500 | 157134 | 10832 | 101 | 0.018648 | 31 | 2512 | 0.012190 | 81.032258 | 0.012190 |
| mHSC-GM_STRING_1000 | STRING | tf_stratified_1to10 | 1000 | 157134 | 10832 | 455 | 0.084010 | 129 | 1290 | 0.090909 | 10.000000 | 0.090909 |
| mHSC-GM_STRING_1000 | STRING | full_candidate | 1000 | 157134 | 10832 | 455 | 0.084010 | 129 | 13022 | 0.009809 | 100.945736 | 0.009809 |
| mHSC-L_Specific_500 | Specific | tf_stratified_1to10 | 500 | 1078888 | 108816 | 2373 | 0.021807 | 550 | 384 | 0.588865 | 0.698182 | 0.588865 |
| mHSC-L_Specific_500 | Specific | full_candidate | 500 | 1078888 | 108816 | 2373 | 0.021807 | 550 | 378 | 0.592672 | 0.687273 | 0.592672 |
| mHSC-L_Specific_1000 | Specific | tf_stratified_1to10 | 1000 | 1078888 | 108816 | 9051 | 0.083177 | 2087 | 1259 | 0.623730 | 0.603258 | 0.623730 |
| mHSC-L_Specific_1000 | Specific | full_candidate | 1000 | 1078888 | 108816 | 9051 | 0.083177 | 2087 | 1607 | 0.564970 | 0.770005 | 0.564970 |
| mHSC-L_Non-Specific_500 | Non-Specific | tf_stratified_1to10 | 500 | 100139 | 6876 | 177 | 0.025742 | 46 | 460 | 0.090909 | 10.000000 | 0.090909 |
| mHSC-L_Non-Specific_500 | Non-Specific | full_candidate | 500 | 100139 | 6876 | 177 | 0.025742 | 46 | 1807 | 0.024825 | 39.282609 | 0.024825 |
| mHSC-L_Non-Specific_1000 | Non-Specific | tf_stratified_1to10 | 1000 | 100139 | 6876 | 570 | 0.082897 | 153 | 1497 | 0.092727 | 9.784314 | 0.092727 |
| mHSC-L_Non-Specific_1000 | Non-Specific | full_candidate | 1000 | 100139 | 6876 | 570 | 0.082897 | 153 | 11390 | 0.013255 | 74.444444 | 0.013255 |
| mHSC-L_STRING_500 | STRING | tf_stratified_1to10 | 500 | 157134 | 10832 | 116 | 0.021418 | 34 | 340 | 0.090909 | 10.000000 | 0.090909 |
| mHSC-L_STRING_500 | STRING | full_candidate | 500 | 157134 | 10832 | 116 | 0.021418 | 34 | 2396 | 0.013992 | 70.470588 | 0.013992 |
| mHSC-L_STRING_1000 | STRING | tf_stratified_1to10 | 1000 | 157134 | 10832 | 512 | 0.094535 | 148 | 1480 | 0.090909 | 10.000000 | 0.090909 |
| mHSC-L_STRING_1000 | STRING | full_candidate | 1000 | 157134 | 10832 | 512 | 0.094535 | 148 | 15081 | 0.009718 | 101.898649 | 0.009718 |

