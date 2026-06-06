# Perturbation Benchmark (Conference-style Tables)

Tables are regenerated from the merged `perturbation_results.csv` after every run, including incremental embedding runs.
Values are grouped by task and dataset; values better than baseline are black bold, and the best embedding value within each row is red bold.

## Task A: Perturbation classification accuracy

Metric: `accuracy` (higher is better). Values better than baseline are **black bold**; best values are <span style="color: red"><strong>red bold</strong></span>.

| dataset | clf | minus | baseline | scGPT_human | v4_bias_rec_best | v4_plain_best | v4_type_pe_best | scconcept | scconcept_encoded | cl_scratch_v5 | cl_v6_fair |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| adamson | lr | **0.2749±0.0043** | 0.2744±0.0055 | <span style="color: red"><strong>0.2895±0.0023</strong></span> | 0.2669±0.0042 | 0.2704±0.0019 | 0.2723±0.0056 | 0.2680±0.0048 | 0.2565±0.0056 | 0.2687±0.0050 | 0.2714±0.0046 |
| adamson | mlp | 0.2459±0.0019 | 0.2515±0.0047 | <span style="color: red"><strong>0.2784±0.0035</strong></span> | 0.2327±0.0040 | 0.2486±0.0024 | 0.2471±0.0050 | **0.2563±0.0038** | 0.1685±0.0043 | 0.2486±0.0019 | 0.2462±0.0030 |
| dixit | lr | <span style="color: red"><strong>0.1947±0.0036</strong></span> | 0.1928±0.0034 | 0.1842±0.0036 | **0.1944±0.0036** | **0.1935±0.0034** | **0.1937±0.0025** | 0.1816±0.0034 | 0.1861±0.0025 | 0.1912±0.0017 | **0.1933±0.0030** |
| dixit | mlp | **0.1999±0.0057** | 0.1985±0.0052 | 0.1964±0.0046 | **0.2021±0.0057** | **0.2000±0.0039** | 0.1985±0.0067 | 0.1933±0.0034 | 0.1856±0.0047 | 0.1984±0.0021 | <span style="color: red"><strong>0.2023±0.0029</strong></span> |
| norman | lr | **0.4782±0.0034** | 0.4716±0.0032 | <span style="color: red"><strong>0.5066±0.0043</strong></span> | **0.4734±0.0028** | 0.4663±0.0051 | **0.4725±0.0038** | **0.4815±0.0033** | **0.4944±0.0015** | 0.4694±0.0037 | 0.4680±0.0017 |
| norman | mlp | 0.4116±0.0021 | 0.4165±0.0040 | <span style="color: red"><strong>0.4706±0.0040</strong></span> | 0.3974±0.0048 | 0.4154±0.0041 | 0.4127±0.0022 | **0.4703±0.0036** | 0.3491±0.0044 | **0.4184±0.0032** | 0.4147±0.0040 |

## Task A: Perturbation classification macro F1

Metric: `f1_macro` (higher is better). Values better than baseline are **black bold**; best values are <span style="color: red"><strong>red bold</strong></span>.

| dataset | clf | minus | baseline | scGPT_human | v4_bias_rec_best | v4_plain_best | v4_type_pe_best | scconcept | scconcept_encoded | cl_scratch_v5 | cl_v6_fair |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| adamson | lr | 0.2436±0.0048 | 0.2445±0.0052 | <span style="color: red"><strong>0.2655±0.0033</strong></span> | 0.2346±0.0045 | 0.2413±0.0026 | 0.2425±0.0054 | 0.2422±0.0038 | 0.2277±0.0053 | 0.2387±0.0049 | 0.2410±0.0037 |
| adamson | mlp | 0.2101±0.0041 | 0.2198±0.0058 | <span style="color: red"><strong>0.2492±0.0045</strong></span> | 0.1960±0.0081 | 0.2148±0.0066 | 0.2103±0.0023 | **0.2265±0.0058** | 0.1369±0.0019 | 0.2113±0.0042 | 0.2172±0.0042 |
| dixit | lr | 0.0966±0.0029 | 0.0973±0.0029 | <span style="color: red"><strong>0.1112±0.0050</strong></span> | **0.0977±0.0028** | 0.0969±0.0038 | **0.0994±0.0036** | **0.1093±0.0035** | **0.1024±0.0031** | 0.0955±0.0024 | **0.0979±0.0022** |
| dixit | mlp | 0.0834±0.0072 | 0.0834±0.0053 | <span style="color: red"><strong>0.0891±0.0090</strong></span> | 0.0778±0.0042 | **0.0843±0.0073** | **0.0866±0.0038** | 0.0775±0.0011 | 0.0784±0.0052 | 0.0783±0.0063 | 0.0760±0.0042 |
| norman | lr | **0.4309±0.0038** | 0.4239±0.0021 | <span style="color: red"><strong>0.4624±0.0076</strong></span> | **0.4245±0.0036** | 0.4183±0.0044 | **0.4267±0.0031** | **0.4337±0.0034** | **0.4441±0.0031** | 0.4217±0.0026 | 0.4213±0.0029 |
| norman | mlp | 0.3596±0.0021 | 0.3649±0.0040 | **0.4188±0.0037** | 0.3423±0.0058 | 0.3611±0.0023 | 0.3603±0.0013 | <span style="color: red"><strong>0.4196±0.0049</strong></span> | 0.2849±0.0026 | **0.3682±0.0026** | 0.3634±0.0035 |

## Task B: Perturbation effect similarity (Spearman)

Metric: `spearman_r` (higher is better). Values better than baseline are **black bold**; best values are <span style="color: red"><strong>red bold</strong></span>.

| dataset | minus | baseline | scGPT_human | v4_bias_rec_best | v4_plain_best | v4_type_pe_best | scconcept | scconcept_encoded | cl_scratch_v5 | cl_v6_fair |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| adamson | <span style="color: red"><strong>0.1633</strong></span> | 0.1382 | 0.1323 | 0.1001 | 0.1152 | 0.1198 | 0.0306 | -0.0086 | 0.1352 | 0.1178 |
| dixit | **0.2499** | 0.2025 | <span style="color: red"><strong>0.3451</strong></span> | 0.1866 | **0.2172** | 0.1561 | 0.0719 | 0.1526 | **0.2716** | **0.2484** |
| norman | 0.0657 | <span style="color: red"><strong>0.1010</strong></span> | 0.0682 | 0.0635 | 0.0538 | 0.0424 | 0.0060 | -0.0306 | 0.0462 | 0.0497 |

## Task B: Perturbation effect similarity (Pearson)

Metric: `pearson_r` (higher is better). Values better than baseline are **black bold**; best values are <span style="color: red"><strong>red bold</strong></span>.

| dataset | minus | baseline | scGPT_human | v4_bias_rec_best | v4_plain_best | v4_type_pe_best | scconcept | scconcept_encoded | cl_scratch_v5 | cl_v6_fair |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| adamson | <span style="color: red"><strong>0.1738</strong></span> | 0.1418 | **0.1555** | 0.0977 | **0.1429** | **0.1475** | 0.0122 | 0.0239 | **0.1499** | 0.1306 |
| dixit | **0.3368** | 0.3086 | <span style="color: red"><strong>0.4053</strong></span> | **0.3285** | **0.3195** | 0.2966 | 0.0480 | 0.1513 | **0.3759** | **0.3466** |
| norman | 0.0490 | <span style="color: red"><strong>0.0831</strong></span> | 0.0476 | 0.0367 | 0.0436 | 0.0320 | 0.0108 | -0.0360 | 0.0366 | 0.0403 |

## Task C: Perturbation direction prediction (Pearson)

Metric: `pearson_r` (higher is better). Values better than baseline are **black bold**; best values are <span style="color: red"><strong>red bold</strong></span>.

| dataset | minus | baseline | scGPT_human | v4_bias_rec_best | v4_plain_best | v4_type_pe_best | scconcept | scconcept_encoded | cl_scratch_v5 | cl_v6_fair |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| adamson | **0.1294±0.3525** | 0.1006±0.4030 | <span style="color: red"><strong>0.1676±0.3616</strong></span> | **0.1473±0.3731** | 0.0751±0.3992 | **0.1097±0.3610** | 0.0152±0.2365 | 0.0932±0.4205 | **0.1236±0.3734** | 0.0840±0.3681 |
| dixit | 0.2459±0.6042 | 0.2683±0.5920 | 0.2109±0.6284 | <span style="color: red"><strong>0.3645±0.4926</strong></span> | **0.2704±0.5775** | 0.2087±0.6377 | 0.0275±0.3777 | 0.2011±0.4710 | **0.2904±0.6050** | **0.3404±0.5692** |
| norman | 0.0446±0.3844 | 0.1422±0.3693 | 0.0688±0.3710 | 0.0913±0.4080 | 0.0855±0.3532 | 0.0643±0.3467 | 0.0739±0.1782 | 0.0500±0.3570 | <span style="color: red"><strong>0.1472±0.3133</strong></span> | 0.1042±0.3435 |

## Task C: Perturbation direction prediction (MSE)

Metric: `mse` (lower is better). Values better than baseline are **black bold**; best values are <span style="color: red"><strong>red bold</strong></span>.

| dataset | minus | baseline | scGPT_human | v4_bias_rec_best | v4_plain_best | v4_type_pe_best | scconcept | scconcept_encoded | cl_scratch_v5 | cl_v6_fair |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| adamson | **1.2885** | 1.3902 | <span style="color: red"><strong>1.1143</strong></span> | 1.5714 | 1.4834 | **1.3561** | **1.3039** | 1.9604 | **1.3226** | 1.4353 |
| dixit | **1.2187** | 1.2440 | **1.1228** | <span style="color: red"><strong>1.0477</strong></span> | **1.1358** | 1.2516 | 1.2516 | 1.4201 | **1.0831** | **1.1140** |
| norman | 1.7565 | 1.4938 | **1.2932** | 1.9016 | 1.5994 | 1.7082 | <span style="color: red"><strong>1.1929</strong></span> | 2.0651 | **1.4913** | 1.6233 |

