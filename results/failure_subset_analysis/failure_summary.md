# Failure-subset analysis

This diagnostic report analyzes failure modes on top of existing benchmark CSVs. It should not be read as a new benchmark protocol or as evidence that any model is globally better across tasks.

## Main findings
- Metric-disagreement failures found: **2460**.
- Protocol-sensitivity rows summarized: **4200**.
- Low-positive / sparse GRN warnings: **722**.
- Topology/frequency summary rows: **150**.
- Margin-collapse rows: **0**.
- Model-specific vulnerability rows: **5581** comparing against `baseline` and `scGPT_human` where available.

Perturbation folds with n_test < 5 or n_train < 20 are treated as diagnostic only and excluded from headline failure tables.

## Top failure subsets
| embedding | comparator | task | metric | delta | setting |
|---|---|---|---:|---:|---|
| scconcept_encoded | scGPT_human | perturbation_regression | mse | 1.191 | dataset=norman;context=dataset::all;method=frozen_linear;fold_id=2;n_train=80;n_test=20 |
| scconcept_encoded | scGPT_human | perturbation_regression | mse | 1.181 | dataset=adamson;context=dataset::all;method=frozen_linear;fold_id=4;n_train=60;n_test=15 |
| scconcept_encoded | scGPT_human | perturbation_regression | mse | 1.159 | dataset=adamson;context=dataset::all;method=frozen_linear;fold_id=3;n_train=60;n_test=15 |
| scconcept_encoded | scGPT_human | perturbation_regression | mse | 1.148 | dataset=adamson;context=dataset::all;method=frozen_linear;fold_id=2;n_train=60;n_test=15 |
| scconcept_encoded | baseline | perturbation_regression | mse | 1.147 | dataset=adamson;context=dataset::all;method=frozen_linear;fold_id=4;n_train=60;n_test=15 |
| scconcept_encoded | scGPT_human | perturbation_regression | mse | 1.024 | dataset=norman;context=dataset::all;method=frozen_linear;fold_id=1;n_train=80;n_test=20 |
| scconcept_encoded | scGPT_human | perturbation_regression | mse | 1.001 | dataset=adamson;context=dataset::all;method=frozen_linear;setting_group=frozen_probe;n_pert_genes=75;target_dim=256;n_folds=5 |
| cl_scratch_v5 | baseline | grn | auroc | -1 | dataset=mHSC-E500->hHep500;setting=transfer;train_dataset=mHSC-E500;test_dataset=hHep500;clf=lr;coverage=457/500->487/500 |
| cl_scratch_v5 | baseline | grn | auroc | -1 | dataset=mHSC-E500->hHep500;setting=transfer;train_dataset=mHSC-E500;test_dataset=hHep500;clf=mlp;coverage=457/500->487/500 |
| cl_scratch_v5 | baseline | grn | auroc | -1 | dataset=mHSC-GM500->hHep500;setting=transfer;train_dataset=mHSC-GM500;test_dataset=hHep500;clf=mlp;coverage=449/500->487/500 |

## Protocol sensitivity summary
- Flagged protocol-sensitive cases: **2300**.
| embedding | metric | native | topology_matched | rank_native | rank_topology | flags |
|---|---|---:|---:|---:|---:|---|
| cl_v6_fair | auprc | 0.6744 | 0.4734 | 1 | 10 | native_win_topology_loss;rank_change>=2 |
| cl_scratch_v5 | auprc | 0.4726 | 0.8497 | 10 | 1 | rank_change>=2 |
| v4_type_pe_best | auprc | 0.7611 | 0.2011 | 1 | 10 | native_win_topology_loss;rank_change>=2 |
| minus | auprc | 0.4274 | 0.6442 | 10 | 1 | rank_change>=2 |
| cl_scratch_v5 | auprc | 0.5284 | 0.6965 | 1 | 10 | native_win_topology_loss;coverage_gain_strict_collapse;rank_change>=2 |
| scconcept_encoded | auprc | 0.5423 | 0.5957 | 10 | 1 | rank_change>=2 |
| scGPT_human | auprc | 0.5138 | 0.6399 | 10 | 1 | rank_change>=2 |
| v4_bias_rec_best | auprc | 0.4778 | 0.6 | 10 | 1 | rank_change>=2 |
| scconcept | auroc | 0.4952 | 0.5104 | 10 | 1 | rank_change>=2 |
| cl_scratch_v5 | auroc | 0.4394 | 0.741 | 10 | 1 | rank_change>=2 |

## Metric disagreement summary
- AUROC improves but AUPRC drops: **554** rows.
- AUROC improves but F1 drops: **1082** rows.
- AUROC improves but Precision@K drops: **824** rows.

| embedding | task | failure_type | primary_delta | secondary_delta | setting |
|---|---|---|---:|---:|---|
| scconcept | grn | AUROC improves but AUPRC drops | 0.01545 | -0.02651 | dataset=hHep500->mHSC-E500;setting=transfer;train_dataset=hHep500;test_dataset=mHSC-E500;clf=lr;coverage=487/500->457/500 |
| v4_plain_best | grn | AUROC improves but AUPRC drops | 0.008426 | -0.01938 | dataset=mHSC-E500;setting=in_domain;train_dataset=mHSC-E500;test_dataset=mHSC-E500;clf=lr;coverage=457/500 |
| scGPT_human | grn | AUROC improves but AUPRC drops | 0.002485 | -0.01727 | dataset=mHSC-E500;setting=in_domain;train_dataset=mHSC-E500;test_dataset=mHSC-E500;clf=mlp;coverage=457/500 |
| cl_scratch_v5 | grn | AUROC improves but AUPRC drops | 0.01335 | -0.01712 | dataset=mHSC-E500->mHSC-L500;setting=transfer;train_dataset=mHSC-E500;test_dataset=mHSC-L500;clf=mlp;coverage=457/500->442/500 |
| v4_plain_best | grn | AUROC improves but AUPRC drops | 0.001278 | -0.01367 | dataset=mHSC-L500->mHSC-GM500;setting=transfer;train_dataset=mHSC-L500;test_dataset=mHSC-GM500;clf=lr;coverage=442/500->449/500 |
| minus | grn | AUROC improves but AUPRC drops | 0.006763 | -0.01264 | dataset=hHep500->mHSC-E500;setting=transfer;train_dataset=hHep500;test_dataset=mHSC-E500;clf=lr;coverage=487/500->457/500 |
| v4_bias_rec_best | grn | AUROC improves but AUPRC drops | 0.01471 | -0.01261 | dataset=hHep500->mHSC-L500;setting=transfer;train_dataset=hHep500;test_dataset=mHSC-L500;clf=lr;coverage=487/500->442/500 |
| scGPT_human | grn | AUROC improves but AUPRC drops | 0.003297 | -0.01168 | dataset=mHSC-GM500;setting=in_domain;train_dataset=mHSC-GM500;test_dataset=mHSC-GM500;clf=mlp;coverage=449/500 |
| scconcept | grn | AUROC improves but AUPRC drops | 0.01141 | -0.01168 | dataset=mHSC-GM500->mHSC-E500;setting=transfer;train_dataset=mHSC-GM500;test_dataset=mHSC-E500;clf=mlp;coverage=449/500->457/500 |
| minus | grn | AUROC improves but AUPRC drops | 0.005063 | -0.007705 | dataset=mHSC-GM500;setting=in_domain;train_dataset=mHSC-GM500;test_dataset=mHSC-GM500;clf=lr;coverage=449/500 |

## Low-positive GRN warnings
- auprc_near_random: **18** rows.
- few_test_positives: **400** rows.
- high_negative_to_positive_ratio: **520** rows.
- low_positive_ratio: **500** rows.

These settings should be treated as diagnostic/stress-test subsets, not headline evidence, especially when AUPRC is close to the random positive-rate baseline.

## Topology/frequency-shift summary
| protocol | embedding | degree_bin | train_freq_bin | test_freq_bin | ratio_bin | mean_delta_auprc | n |
|---|---|---|---|---|---|---:|---:|
| coverage_matched | scconcept | high | high | medium | low | -0.1934 | 7 |
| topology_matched | scconcept_encoded | high | high | medium | low | -0.1365 | 6 |
| topology_matched | scconcept | medium | high | medium | low | -0.1335 | 15 |
| strict | scconcept | medium | high | medium | low | -0.1204 | 15 |
| coverage_matched | scconcept | medium | high | medium | low | -0.1151 | 16 |
| strict | scconcept | high | high | medium | low | -0.1114 | 6 |
| coverage_matched | scconcept_encoded | high | high | medium | low | -0.101 | 7 |
| strict | scconcept_encoded | high | high | high | low | -0.09844 | 33 |
| topology_matched | scGPT_human | high | high | medium | low | -0.09591 | 6 |
| strict | scconcept | high | high | high | low | -0.09141 | 33 |

## Margin-collapse summary
No source/target score-statistic pairs were available; margin deltas were not fabricated from target-only score summaries.

## Recommended interpretation
- Do not declare a model globally better because it wins one metric or one protocol.
- Treat AUROC gains paired with AUPRC/F1/Precision@K losses as suspicious: global separability may improve while positive retrieval worsens.
- Treat native gains that disappear under topology-matched evaluation as protocol-sensitive rather than robust.
- Treat very sparse GRN settings and near-random AUPRC as stress tests; they are useful for diagnosing instability but weak as headline evidence.
- Use recurring topology/frequency and score-collapse failures to motivate task-aware contrastive objectives, especially perturbation-effect contrastive losses and GRN topology-aware edge contrastive losses.

## Warnings
- Margin-collapse analysis found target score statistics but no source/train score statistics; source-target deltas were not fabricated.

