# Batch-Correction Conference Tables

Style: **bold** marks the best embedding within a row. Values are mean±std across seeds; higher is better for all displayed metrics.

## Data included

- Input rows: 270
- Successful rows: 180
- Datasets: Immune_Human, PBMC_10K
- Correction methods: linear_residual, none
- Metrics shown: Overall, AvgBIO, AvgBATCH, NMI_label, ARI_label, ASW_label, ASW_batch, GraphConn

## Overall embedding ranking

| embedding | rank | Overall | AvgBIO | AvgBATCH | conservative_score |
| --- | --- | --- | --- | --- | --- |
| minus | 1 | 0.6091 | 0.3681 | 0.9707 | 0.3681 |
| v4_plain_best | 2 | 0.6043 | 0.3647 | 0.9637 | 0.3647 |
| scGPT_human | 3 | 0.6024 | 0.3558 | 0.9722 | 0.3558 |
| scconcept | 4 | 0.6004 | 0.3519 | 0.9732 | 0.3519 |
| cl_scratch_v5 | 5 | 0.5981 | 0.3576 | 0.9587 | 0.3576 |
| v4_type_pe_best | 6 | 0.5966 | 0.3537 | 0.961 | 0.3537 |
| baseline | 7 | 0.5902 | 0.3421 | 0.9625 | 0.3421 |
| v4_bias_rec_best | 8 | 0.5781 | 0.3223 | 0.9619 | 0.3223 |
| scconcept_encoded | 9 | 0.5021 | 0.2018 | 0.9527 | 0.2018 |

## Overall by dataset and correction method

| dataset / correction_method | baseline | minus | cl_scratch_v5 | scGPT_human | scconcept | scconcept_encoded | v4_bias_rec_best | v4_plain_best | v4_type_pe_best |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Immune_Human / linear_residual | 0.561±0.002 | **0.583±0.004** | 0.566±0.003 | 0.573±0.003 | 0.533±0.005 | 0.409±0.000 | 0.544±0.002 | 0.571±0.005 | 0.567±0.004 |
| Immune_Human / none | 0.535±0.002 | **0.568±0.002** | 0.538±0.006 | 0.554±0.007 | 0.546±0.001 | 0.379±0.001 | 0.521±0.003 | 0.552±0.006 | 0.544±0.006 |
| PBMC_10K / linear_residual | 0.633±0.000 | 0.644±0.000 | 0.646±0.010 | 0.642±0.000 | **0.659±0.000** | 0.610±0.000 | 0.623±0.000 | 0.647±0.001 | 0.638±0.000 |
| PBMC_10K / none | 0.633±0.001 | 0.642±0.000 | 0.641±0.001 | 0.641±0.000 | **0.664±0.012** | 0.611±0.000 | 0.624±0.000 | 0.647±0.001 | 0.637±0.000 |

## AvgBIO by dataset and correction method

| dataset / correction_method | baseline | minus | cl_scratch_v5 | scGPT_human | scconcept | scconcept_encoded | v4_bias_rec_best | v4_plain_best | v4_type_pe_best |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Immune_Human / linear_residual | 0.282±0.004 | **0.309±0.006** | 0.286±0.006 | 0.293±0.005 | 0.255±0.008 | 0.065±0.001 | 0.255±0.003 | 0.294±0.008 | 0.288±0.006 |
| Immune_Human / none | 0.257±0.003 | **0.301±0.003** | 0.278±0.010 | 0.280±0.012 | 0.257±0.001 | 0.005±0.001 | 0.233±0.004 | 0.288±0.010 | 0.281±0.011 |
| PBMC_10K / linear_residual | 0.414±0.000 | 0.432±0.001 | 0.437±0.017 | 0.426±0.000 | **0.443±0.000** | 0.369±0.000 | 0.400±0.000 | 0.439±0.002 | 0.424±0.000 |
| PBMC_10K / none | 0.415±0.001 | 0.430±0.000 | 0.429±0.001 | 0.424±0.001 | **0.452±0.020** | 0.369±0.000 | 0.401±0.000 | 0.438±0.001 | 0.422±0.001 |

## AvgBATCH by dataset and correction method

| dataset / correction_method | baseline | minus | cl_scratch_v5 | scGPT_human | scconcept | scconcept_encoded | v4_bias_rec_best | v4_plain_best | v4_type_pe_best |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Immune_Human / linear_residual | 0.979±0.000 | **0.994±0.000** | 0.987±0.000 | 0.992±0.000 | 0.950±0.000 | 0.925±0.000 | 0.978±0.000 | 0.986±0.000 | 0.987±0.000 |
| Immune_Human / none | 0.951±0.000 | 0.967±0.000 | 0.928±0.000 | 0.964±0.000 | **0.978±0.000** | 0.940±0.000 | 0.954±0.000 | 0.949±0.000 | 0.938±0.000 |
| PBMC_10K / linear_residual | 0.960±0.000 | 0.962±0.000 | 0.960±0.000 | 0.966±0.000 | **0.982±0.000** | 0.972±0.000 | 0.958±0.000 | 0.960±0.000 | 0.960±0.000 |
| PBMC_10K / none | 0.960±0.000 | 0.960±0.000 | 0.960±0.000 | 0.967±0.000 | **0.983±0.000** | 0.973±0.000 | 0.958±0.000 | 0.960±0.000 | 0.960±0.000 |

## Best correction method per embedding

| embedding | best_correction_method | Overall | n |
| --- | --- | --- | --- |
| baseline | linear_residual | 0.597±0.038 | 10 |
| minus | linear_residual | 0.613±0.032 | 10 |
| cl_scratch_v5 | linear_residual | 0.606±0.043 | 10 |
| scGPT_human | linear_residual | 0.607±0.037 | 10 |
| scconcept | none | 0.605±0.063 | 10 |
| scconcept_encoded | linear_residual | 0.509±0.106 | 10 |
| v4_bias_rec_best | linear_residual | 0.584±0.042 | 10 |
| v4_plain_best | linear_residual | 0.609±0.040 | 10 |
| v4_type_pe_best | linear_residual | 0.603±0.038 | 10 |

## Auxiliary metric rankings

Mean metric values across all successful datasets, correction methods, and seeds.

| embedding | NMI_label | ARI_label | ASW_label | ASW_batch | GraphConn |
| --- | --- | --- | --- | --- | --- |
| baseline | 0.5452 | 0.3531 | 0.1279 | 0.9897 | 0.9353 |
| minus | 0.5797 | 0.3793 | 0.1454 | 0.9976 | 0.9438 |
| cl_scratch_v5 | 0.5636 | 0.3734 | 0.1359 | 0.9885 | 0.929 |
| scGPT_human | 0.5652 | 0.3715 | 0.1308 | 0.9929 | 0.9515 |
| scconcept | 0.5867 | 0.4251 | 0.0439 | 0.9999 | 0.9465 |
| scconcept_encoded | 0.3634 | 0.2447 | -0.0027 | 0.9994 | 0.906 |
| v4_bias_rec_best | 0.5185 | 0.3366 | 0.1118 | 0.9939 | 0.9299 |
| v4_plain_best | 0.5713 | 0.3773 | 0.1453 | 0.9913 | 0.936 |
| v4_type_pe_best | 0.5589 | 0.3684 | 0.1337 | 0.9905 | 0.9315 |

## Interpretation rules

- Prefer embeddings that jointly improve Overall, AvgBIO, and AvgBATCH rather than a single metric.
- Compare embeddings within the same dataset and correction method row to avoid mixing correction effects with embedding effects.
- Treat the best-correction table as a workflow-selection summary, not as evidence that one correction method is universally optimal.

