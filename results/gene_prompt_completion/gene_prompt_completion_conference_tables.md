# Gene-Prompt Completion Conference Tables

Style: **bold** = best embedding within a row; *italic* = better than baseline embedding in the same row. Lower is better for MSE/MAE; higher is better for correlation/R2/ranking metrics.

## Data included

- Input rows: 8
- Successful rows: 8
- Metrics shown: mse, pearson_all, spearman_all, r2

## Main embedding comparison tables

Columns are the six fixed embeddings. **Bold** marks the best embedding in that row; *italic* marks better than the baseline embedding in that row. These tables are intentionally all in this one markdown file for direct paper-style inspection.

### Secondary: cell_holdout + ridge_pair

#### mse

| dataset / prompt_ratio | baseline | minus | scGPT_human | v4_bias_rec_best | v4_plain_best | v4_type_pe_best | scconcept | scconcept_encoded |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| ('test_data', 0.1) | 0.03015 | *0.0298* | **0.029** | *0.02992* | 0.03024 | 0.03031 | 0.03056 | *0.02927* |

#### pearson_all

| dataset / prompt_ratio | baseline | minus | scGPT_human | v4_bias_rec_best | v4_plain_best | v4_type_pe_best | scconcept | scconcept_encoded |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| ('test_data', 0.1) | 0.4924 | *0.5011* | **0.5205** | *0.4982* | 0.4900 | 0.4880 | 0.4814 | *0.5141* |

#### spearman_all

| dataset / prompt_ratio | baseline | minus | scGPT_human | v4_bias_rec_best | v4_plain_best | v4_type_pe_best | scconcept | scconcept_encoded |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| ('test_data', 0.1) | 0.2480 | *0.2515* | **0.2520** | *0.2497* | *0.2495* | *0.2499* | *0.2517* | *0.2514* |

#### r2

| dataset / prompt_ratio | baseline | minus | scGPT_human | v4_bias_rec_best | v4_plain_best | v4_type_pe_best | scconcept | scconcept_encoded |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| ('test_data', 0.1) | 0.2416 | *0.2503* | **0.2705** | *0.2475* | 0.2394 | 0.2375 | 0.2314 | *0.2637* |

## Conservative win/loss vs baselines

An embedding is counted as a conservative win only when ridge_pair beats both mean and knn_prompt on MSE for the same dataset/prompt/split.

| Embedding | wins | comparisons | win_rate |
|---|---:|---:|---:|
| baseline | 0.0 | 1.0 | 0.0 |
| minus | 0.0 | 1.0 | 0.0 |
| scGPT_human | 0.0 | 1.0 | 0.0 |
| scconcept | 0.0 | 1.0 | 0.0 |
| scconcept_encoded | 0.0 | 1.0 | 0.0 |
| v4_bias_rec_best | 0.0 | 1.0 | 0.0 |
| v4_plain_best | 0.0 | 1.0 | 0.0 |
| v4_type_pe_best | 0.0 | 1.0 | 0.0 |

## Interpretation rules

- The most direct embedding comparison is ridge_pair, because mean and knn_prompt do not use gene embeddings.
- Treat gains that appear only for MSE but not Pearson/Spearman as calibration-only improvements.
- Do not claim broad superiority from one dataset, one prompt ratio, or cell_holdout alone.
