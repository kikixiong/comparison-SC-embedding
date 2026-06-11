# AUROC matrices by setting (embedding × train_dataset)

## coverage_matched + lr | AUROC matrix (embedding × train_dataset)

| Embedding | hESC | hHep | mDC | mESC | mHSC-E | mHSC-GM | mHSC-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| baseline | 0.572801 ± 0.095904 | 0.606465 ± 0.095984 | 0.455866 ± 0.072504 | - | 0.616237 ± 0.063608 | 0.665098 ± 0.181737 | 0.637858 ± 0.079888 |
| cl_scratch_v5 | 0.565904 ± 0.049604 | <span style="color:red">0.645155 ± 0.076343</span> | 0.450350 ± 0.073520 | 0.504725 ± 0.000473 | 0.592867 ± 0.100674 | **<span style="color:red">0.727046 ± 0.053193</span>** | **<span style="color:red">0.654878 ± 0.087851</span>** |
| cl_v6_fair | <span style="color:red">0.600630 ± 0.069623</span> | <span style="color:red">0.616350 ± 0.107209</span> | <span style="color:red">0.463897 ± 0.054471</span> | 0.478057 ± 0.012114 | **<span style="color:red">0.685992 ± 0.088449</span>** | 0.590844 ± 0.137251 | 0.593472 ± 0.099238 |
| cl_v6_tau01 | <span style="color:red">0.588299 ± 0.148896</span> | <span style="color:red">0.668140 ± 0.072441</span> | 0.425598 ± 0.055725 | 0.488645 ± 0.000000 | 0.597669 ± 0.132358 | 0.660736 ± 0.103282 | 0.557236 ± 0.144278 |
| cl_v6_tau02 | <span style="color:red">0.601377 ± 0.062066</span> | <span style="color:red">0.660227 ± 0.059269</span> | 0.445660 ± 0.061017 | 0.488956 ± 0.009975 | <span style="color:red">0.635158 ± 0.103538</span> | <span style="color:red">0.668122 ± 0.116126</span> | 0.507281 ± 0.169679 |
| cl_v6_tau03 | <span style="color:red">0.580682 ± 0.080283</span> | 0.600391 ± 0.039939 | <span style="color:red">0.460829 ± 0.046374</span> | 0.465660 ± 0.027081 | 0.597534 ± 0.106080 | <span style="color:red">0.702711 ± 0.095098</span> | 0.588179 ± 0.104879 |
| cl_v7_fair | 0.551214 ± 0.103438 | <span style="color:red">0.654307 ± 0.042623</span> | 0.392192 ± 0.084288 | 0.470588 ± 0.040362 | <span style="color:red">0.629088 ± 0.128790</span> | <span style="color:red">0.665712 ± 0.104475</span> | 0.547812 ± 0.100768 |
| minus | 0.538287 ± 0.090779 | <span style="color:red">0.622459 ± 0.114272</span> | 0.422096 ± 0.042069 | 0.447429 ± 0.000000 | <span style="color:red">0.661075 ± 0.091408</span> | 0.616884 ± 0.128017 | 0.540959 ± 0.077186 |
| scGPT_human | 0.534877 ± 0.067002 | <span style="color:red">0.638484 ± 0.061569</span> | <span style="color:red">0.489473 ± 0.079884</span> | 0.524411 ± 0.006174 | 0.566923 ± 0.129015 | <span style="color:red">0.687710 ± 0.155369</span> | <span style="color:red">0.641737 ± 0.078573</span> |
| scconcept | 0.518378 ± 0.020535 | 0.472302 ± 0.048480 | <span style="color:red">0.484337 ± 0.025393</span> | 0.509360 ± 0.013125 | 0.486412 ± 0.153093 | 0.622873 ± 0.098509 | 0.500778 ± 0.109091 |
| scconcept_encoded | 0.516536 ± 0.064350 | 0.541091 ± 0.017586 | **<span style="color:red">0.492697 ± 0.044114</span>** | 0.472412 ± 0.025260 | 0.484951 ± 0.049247 | 0.519511 ± 0.122243 | 0.584743 ± 0.084424 |
| v4_bias_rec_best | **<span style="color:red">0.629138 ± 0.090133</span>** | **<span style="color:red">0.694859 ± 0.057545</span>** | 0.385741 ± 0.054991 | 0.441110 ± 0.000000 | 0.567922 ± 0.179594 | <span style="color:red">0.667506 ± 0.129366</span> | 0.588162 ± 0.107423 |
| v4_plain_best | 0.557859 ± 0.104800 | 0.565453 ± 0.084320 | 0.417433 ± 0.061242 | **0.525173 ± 0.000000** | <span style="color:red">0.621343 ± 0.066359</span> | 0.616200 ± 0.119604 | 0.600197 ± 0.109437 |
| v4_type_pe_best | <span style="color:red">0.620842 ± 0.102359</span> | <span style="color:red">0.647949 ± 0.093774</span> | 0.433231 ± 0.061365 | 0.462252 ± 0.053218 | 0.589208 ± 0.066879 | 0.658918 ± 0.132556 | 0.587938 ± 0.103190 |

## coverage_matched + mlp | AUROC matrix (embedding × train_dataset)

| Embedding | hESC | hHep | mDC | mESC | mHSC-E | mHSC-GM | mHSC-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| baseline | 0.560745 ± 0.091566 | 0.631932 ± 0.107575 | **0.491946 ± 0.070341** | **0.552330 ± 0.038376** | 0.633348 ± 0.087055 | 0.667305 ± 0.197956 | 0.654757 ± 0.123722 |
| cl_scratch_v5 | <span style="color:red">0.567489 ± 0.062183</span> | <span style="color:red">0.641864 ± 0.080236</span> | 0.482718 ± 0.049954 | 0.495353 ± 0.013859 | <span style="color:red">0.635246 ± 0.113568</span> | **<span style="color:red">0.742347 ± 0.065977</span>** | <span style="color:red">0.674478 ± 0.111258</span> |
| cl_v6_fair | <span style="color:red">0.574013 ± 0.081937</span> | 0.626102 ± 0.105858 | 0.476194 ± 0.049626 | 0.498091 ± 0.025301 | **<span style="color:red">0.672424 ± 0.133804</span>** | 0.627178 ± 0.132485 | 0.615408 ± 0.144408 |
| cl_v6_tau01 | <span style="color:red">0.580388 ± 0.117341</span> | <span style="color:red">0.651929 ± 0.093907</span> | 0.475952 ± 0.063879 | 0.493549 ± 0.015204 | 0.603018 ± 0.176673 | 0.644137 ± 0.166885 | 0.622027 ± 0.155136 |
| cl_v6_tau02 | <span style="color:red">0.582637 ± 0.065980</span> | <span style="color:red">0.665994 ± 0.056079</span> | 0.486852 ± 0.066042 | 0.492384 ± 0.035525 | <span style="color:red">0.662094 ± 0.127138</span> | <span style="color:red">0.720671 ± 0.106093</span> | 0.599642 ± 0.172642 |
| cl_v6_tau03 | <span style="color:red">0.579670 ± 0.078987</span> | 0.596513 ± 0.070773 | 0.470771 ± 0.011517 | 0.492929 ± 0.017407 | 0.619306 ± 0.116376 | <span style="color:red">0.713384 ± 0.111247</span> | <span style="color:red">0.676772 ± 0.094030</span> |
| cl_v7_fair | 0.532713 ± 0.111120 | 0.611366 ± 0.065546 | 0.422654 ± 0.052425 | 0.507370 ± 0.020919 | <span style="color:red">0.644519 ± 0.145955</span> | <span style="color:red">0.679673 ± 0.111697</span> | 0.599770 ± 0.130542 |
| minus | 0.543853 ± 0.073262 | 0.601319 ± 0.083281 | 0.469641 ± 0.026956 | 0.526787 ± 0.027517 | 0.630408 ± 0.121081 | 0.653428 ± 0.116076 | 0.530492 ± 0.193986 |
| scGPT_human | 0.531869 ± 0.030784 | 0.623765 ± 0.078095 | 0.483712 ± 0.042933 | 0.477627 ± 0.024807 | 0.586311 ± 0.141153 | <span style="color:red">0.711063 ± 0.147703</span> | **<span style="color:red">0.708876 ± 0.105036</span>** |
| scconcept | 0.506770 ± 0.033665 | 0.486868 ± 0.026602 | 0.484517 ± 0.033570 | 0.509755 ± 0.013408 | 0.481948 ± 0.106720 | 0.630245 ± 0.108730 | 0.514812 ± 0.130299 |
| scconcept_encoded | 0.518363 ± 0.076584 | 0.544207 ± 0.040155 | 0.490481 ± 0.055207 | 0.506650 ± 0.032081 | 0.473580 ± 0.047611 | 0.584664 ± 0.083494 | 0.586397 ± 0.106005 |
| v4_bias_rec_best | <span style="color:red">0.573053 ± 0.115255</span> | **<span style="color:red">0.670874 ± 0.090268</span>** | 0.429795 ± 0.099485 | 0.502049 ± 0.033707 | 0.584393 ± 0.114860 | <span style="color:red">0.696838 ± 0.124353</span> | <span style="color:red">0.664593 ± 0.169695</span> |
| v4_plain_best | 0.534783 ± 0.106356 | 0.579270 ± 0.089433 | 0.463640 ± 0.088996 | 0.504253 ± 0.015162 | <span style="color:red">0.637640 ± 0.094589</span> | 0.648232 ± 0.160691 | 0.638106 ± 0.115056 |
| v4_type_pe_best | **<span style="color:red">0.584415 ± 0.117681</span>** | 0.631652 ± 0.102530 | 0.449287 ± 0.050252 | 0.500850 ± 0.033808 | 0.593854 ± 0.124934 | <span style="color:red">0.684239 ± 0.149678</span> | 0.649062 ± 0.127934 |

## native + lr | AUROC matrix (embedding × train_dataset)

| Embedding | hESC | hHep | mDC | mESC | mHSC-E | mHSC-GM | mHSC-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| baseline | 0.567574 ± 0.044987 | 0.588666 ± 0.068592 | 0.465502 ± 0.030777 | 0.473813 ± 0.031004 | 0.606988 ± 0.080941 | 0.645408 ± 0.119639 | **0.617719 ± 0.082819** |
| cl_scratch_v5 | 0.558330 ± 0.081375 | <span style="color:red">0.597549 ± 0.093934</span> | <span style="color:red">0.485433 ± 0.061512</span> | **<span style="color:red">0.502494 ± 0.015279</span>** | <span style="color:red">0.619066 ± 0.090231</span> | 0.624642 ± 0.109976 | 0.598441 ± 0.086773 |
| cl_v6_fair | **<span style="color:red">0.591905 ± 0.073835</span>** | <span style="color:red">0.618057 ± 0.084288</span> | <span style="color:red">0.495195 ± 0.071116</span> | <span style="color:red">0.501399 ± 0.043440</span> | 0.606569 ± 0.075188 | 0.635930 ± 0.086409 | 0.566844 ± 0.099328 |
| cl_v6_tau01 | <span style="color:red">0.578064 ± 0.074633</span> | <span style="color:red">0.623917 ± 0.089238</span> | 0.465099 ± 0.059096 | <span style="color:red">0.480350 ± 0.041075</span> | <span style="color:red">0.613770 ± 0.082039</span> | <span style="color:red">0.656475 ± 0.089179</span> | 0.588851 ± 0.079660 |
| cl_v6_tau02 | <span style="color:red">0.574644 ± 0.066563</span> | <span style="color:red">0.624313 ± 0.084762</span> | 0.446225 ± 0.062348 | <span style="color:red">0.476921 ± 0.024723</span> | <span style="color:red">0.620033 ± 0.087433</span> | <span style="color:red">0.651178 ± 0.096311</span> | 0.585226 ± 0.084929 |
| cl_v6_tau03 | <span style="color:red">0.582526 ± 0.071982</span> | **<span style="color:red">0.624955 ± 0.084702</span>** | 0.464837 ± 0.073109 | 0.459289 ± 0.061880 | **<span style="color:red">0.624981 ± 0.083462</span>** | **<span style="color:red">0.656800 ± 0.088815</span>** | 0.576484 ± 0.081367 |
| cl_v7_fair | <span style="color:red">0.586525 ± 0.076528</span> | <span style="color:red">0.622833 ± 0.093051</span> | 0.444875 ± 0.065227 | <span style="color:red">0.484996 ± 0.022122</span> | <span style="color:red">0.619865 ± 0.077438</span> | <span style="color:red">0.653216 ± 0.093421</span> | 0.566423 ± 0.076226 |
| minus | 0.542271 ± 0.077633 | <span style="color:red">0.590098 ± 0.073550</span> | <span style="color:red">0.479308 ± 0.046970</span> | <span style="color:red">0.487117 ± 0.033962</span> | 0.599951 ± 0.100901 | <span style="color:red">0.653541 ± 0.096998</span> | 0.539185 ± 0.075558 |
| scGPT_human | <span style="color:red">0.573872 ± 0.057274</span> | <span style="color:red">0.613237 ± 0.092810</span> | 0.442193 ± 0.031659 | <span style="color:red">0.501204 ± 0.028623</span> | 0.602403 ± 0.078615 | <span style="color:red">0.655511 ± 0.142664</span> | 0.585843 ± 0.093548 |
| scconcept | 0.501247 ± 0.038014 | 0.517266 ± 0.015321 | **<span style="color:red">0.500901 ± 0.029360</span>** | <span style="color:red">0.496207 ± 0.012427</span> | 0.508204 ± 0.045429 | 0.580173 ± 0.091394 | 0.524134 ± 0.072956 |
| scconcept_encoded | 0.518870 ± 0.035321 | 0.531852 ± 0.030698 | <span style="color:red">0.495735 ± 0.042423</span> | <span style="color:red">0.485669 ± 0.038153</span> | 0.481859 ± 0.040840 | 0.558990 ± 0.059664 | 0.543047 ± 0.062006 |
| v4_bias_rec_best | 0.542225 ± 0.083712 | <span style="color:red">0.603045 ± 0.055492</span> | 0.421846 ± 0.038576 | 0.467692 ± 0.034058 | 0.599547 ± 0.067487 | <span style="color:red">0.654896 ± 0.088393</span> | 0.549489 ± 0.095671 |
| v4_plain_best | 0.551292 ± 0.066670 | <span style="color:red">0.597815 ± 0.056499</span> | 0.410016 ± 0.042833 | <span style="color:red">0.492087 ± 0.019020</span> | <span style="color:red">0.613894 ± 0.063917</span> | <span style="color:red">0.651094 ± 0.090599</span> | 0.592102 ± 0.100156 |
| v4_type_pe_best | <span style="color:red">0.574560 ± 0.073451</span> | <span style="color:red">0.597003 ± 0.087383</span> | 0.454122 ± 0.037099 | 0.460067 ± 0.033176 | 0.579184 ± 0.054519 | <span style="color:red">0.647633 ± 0.108639</span> | 0.598309 ± 0.099443 |

## native + mlp | AUROC matrix (embedding × train_dataset)

| Embedding | hESC | hHep | mDC | mESC | mHSC-E | mHSC-GM | mHSC-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| baseline | 0.589381 ± 0.077359 | 0.638565 ± 0.093845 | 0.455096 ± 0.052038 | 0.496473 ± 0.012913 | 0.627317 ± 0.091085 | **0.695296 ± 0.136307** | 0.656925 ± 0.124264 |
| cl_scratch_v5 | 0.586040 ± 0.091253 | 0.637121 ± 0.095746 | 0.454149 ± 0.052151 | <span style="color:red">0.497159 ± 0.014086</span> | 0.621620 ± 0.100869 | 0.675824 ± 0.117126 | 0.650466 ± 0.108019 |
| cl_v6_fair | **<span style="color:red">0.611384 ± 0.086500</span>** | <span style="color:red">0.654147 ± 0.089755</span> | 0.452546 ± 0.061916 | 0.493678 ± 0.013937 | 0.624987 ± 0.094747 | 0.664632 ± 0.121776 | 0.650614 ± 0.113479 |
| cl_v6_tau01 | <span style="color:red">0.601245 ± 0.090578</span> | **<span style="color:red">0.657973 ± 0.094729</span>** | 0.437793 ± 0.053744 | <span style="color:red">0.496866 ± 0.011434</span> | <span style="color:red">0.638084 ± 0.102464</span> | 0.681816 ± 0.117213 | 0.654391 ± 0.107704 |
| cl_v6_tau02 | <span style="color:red">0.599444 ± 0.092230</span> | <span style="color:red">0.657303 ± 0.099178</span> | 0.423663 ± 0.053886 | <span style="color:red">0.501744 ± 0.012594</span> | <span style="color:red">0.637928 ± 0.110045</span> | 0.675680 ± 0.123079 | 0.641608 ± 0.113664 |
| cl_v6_tau03 | <span style="color:red">0.608037 ± 0.090390</span> | <span style="color:red">0.656913 ± 0.093999</span> | 0.434951 ± 0.060216 | 0.488290 ± 0.019264 | **<span style="color:red">0.638847 ± 0.101970</span>** | 0.677215 ± 0.117500 | 0.637691 ± 0.111562 |
| cl_v7_fair | <span style="color:red">0.608283 ± 0.092569</span> | <span style="color:red">0.650672 ± 0.104438</span> | 0.443537 ± 0.062469 | 0.485813 ± 0.012087 | <span style="color:red">0.637679 ± 0.095036</span> | 0.676973 ± 0.113875 | 0.643478 ± 0.115519 |
| minus | 0.555700 ± 0.107026 | <span style="color:red">0.643832 ± 0.091779</span> | 0.421043 ± 0.047829 | <span style="color:red">0.500719 ± 0.009938</span> | 0.619611 ± 0.105442 | 0.673397 ± 0.123696 | 0.626425 ± 0.123256 |
| scGPT_human | 0.588493 ± 0.082541 | <span style="color:red">0.642113 ± 0.106073</span> | 0.451505 ± 0.036409 | 0.493698 ± 0.013953 | 0.610035 ± 0.095388 | 0.683590 ± 0.155978 | <span style="color:red">0.658452 ± 0.130020</span> |
| scconcept | 0.505594 ± 0.051975 | 0.516038 ± 0.011300 | <span style="color:red">0.498088 ± 0.031156</span> | <span style="color:red">0.499114 ± 0.015138</span> | 0.506137 ± 0.046439 | 0.589770 ± 0.104859 | 0.537489 ± 0.100232 |
| scconcept_encoded | 0.513832 ± 0.062915 | 0.531261 ± 0.043671 | **<span style="color:red">0.509602 ± 0.044355</span>** | **<span style="color:red">0.502753 ± 0.018559</span>** | 0.484169 ± 0.044161 | 0.587441 ± 0.078814 | 0.553164 ± 0.090915 |
| v4_bias_rec_best | 0.553704 ± 0.108361 | <span style="color:red">0.653278 ± 0.085206</span> | 0.401604 ± 0.059922 | 0.482484 ± 0.015696 | <span style="color:red">0.630942 ± 0.087494</span> | 0.693893 ± 0.117349 | 0.642876 ± 0.145958 |
| v4_plain_best | 0.571786 ± 0.098520 | <span style="color:red">0.649516 ± 0.099206</span> | 0.430538 ± 0.038359 | 0.495163 ± 0.008294 | <span style="color:red">0.629683 ± 0.093324</span> | 0.693141 ± 0.110615 | 0.634474 ± 0.123183 |
| v4_type_pe_best | <span style="color:red">0.609522 ± 0.093161</span> | <span style="color:red">0.642700 ± 0.111652</span> | 0.433243 ± 0.049737 | 0.494400 ± 0.010452 | 0.620860 ± 0.088273 | 0.688974 ± 0.132237 | **<span style="color:red">0.661621 ± 0.122412</span>** |

## strict + lr | AUROC matrix (embedding × train_dataset)

| Embedding | hESC | hHep | mDC | mESC | mHSC-E | mHSC-GM | mHSC-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| baseline | 0.546394 ± 0.072335 | 0.649652 ± 0.088779 | 0.546067 ± 0.084998 | 0.466407 ± 0.035904 | 0.649405 ± 0.148515 | 0.689158 ± 0.098649 | **0.672400 ± 0.053510** |
| cl_scratch_v5 | 0.512934 ± 0.088532 | **<span style="color:red">0.681569 ± 0.099708</span>** | <span style="color:red">0.546915 ± 0.133055</span> | **<span style="color:red">0.515654 ± 0.027998</span>** | <span style="color:red">0.649749 ± 0.155748</span> | <span style="color:red">0.701092 ± 0.105438</span> | 0.638574 ± 0.085672 |
| cl_v6_fair | 0.533102 ± 0.076083 | <span style="color:red">0.680239 ± 0.097145</span> | 0.532854 ± 0.150432 | <span style="color:red">0.500543 ± 0.012972</span> | 0.641405 ± 0.150594 | <span style="color:red">0.694956 ± 0.085941</span> | 0.604086 ± 0.095987 |
| cl_v6_tau01 | 0.523039 ± 0.086766 | <span style="color:red">0.674634 ± 0.097341</span> | 0.534584 ± 0.142816 | <span style="color:red">0.488419 ± 0.001517</span> | <span style="color:red">0.654042 ± 0.145311</span> | <span style="color:red">0.706309 ± 0.094180</span> | 0.613334 ± 0.069744 |
| cl_v6_tau02 | 0.535445 ± 0.075884 | <span style="color:red">0.670372 ± 0.095556</span> | 0.526364 ± 0.136625 | <span style="color:red">0.470931 ± 0.022367</span> | <span style="color:red">0.656402 ± 0.150016</span> | **<span style="color:red">0.713031 ± 0.095183</span>** | 0.594674 ± 0.074169 |
| cl_v6_tau03 | 0.530053 ± 0.082928 | <span style="color:red">0.673849 ± 0.099679</span> | 0.521231 ± 0.142059 | 0.417869 ± 0.012053 | <span style="color:red">0.653304 ± 0.148912</span> | <span style="color:red">0.708680 ± 0.091773</span> | 0.590643 ± 0.072209 |
| cl_v7_fair | 0.525837 ± 0.077079 | <span style="color:red">0.667701 ± 0.105366</span> | 0.519012 ± 0.126067 | <span style="color:red">0.488482 ± 0.058475</span> | 0.644494 ± 0.150942 | <span style="color:red">0.692576 ± 0.098978</span> | 0.626878 ± 0.081744 |
| minus | 0.538042 ± 0.069758 | <span style="color:red">0.660108 ± 0.107890</span> | 0.486872 ± 0.063442 | <span style="color:red">0.483568 ± 0.011213</span> | <span style="color:red">0.651015 ± 0.159526</span> | 0.661417 ± 0.160159 | 0.559346 ± 0.087418 |
| scGPT_human | <span style="color:red">0.550327 ± 0.069549</span> | 0.627864 ± 0.099213 | **<span style="color:red">0.551133 ± 0.107416</span>** | <span style="color:red">0.472113 ± 0.000693</span> | <span style="color:red">0.650124 ± 0.170832</span> | <span style="color:red">0.694440 ± 0.102640</span> | 0.624906 ± 0.086522 |
| scconcept | 0.498045 ± 0.048896 | 0.503659 ± 0.056714 | 0.531737 ± 0.060611 | <span style="color:red">0.474700 ± 0.007842</span> | 0.505624 ± 0.101907 | 0.591133 ± 0.087763 | 0.518783 ± 0.093874 |
| scconcept_encoded | 0.527791 ± 0.074731 | 0.527142 ± 0.078280 | 0.470689 ± 0.022472 | <span style="color:red">0.501814 ± 0.026075</span> | 0.471991 ± 0.107108 | 0.608391 ± 0.051441 | 0.572299 ± 0.061582 |
| v4_bias_rec_best | 0.533601 ± 0.072017 | 0.625468 ± 0.081629 | 0.451975 ± 0.038663 | 0.424144 ± 0.028932 | 0.637018 ± 0.125522 | 0.643611 ± 0.150941 | 0.524557 ± 0.108125 |
| v4_plain_best | <span style="color:red">0.548578 ± 0.095099</span> | <span style="color:red">0.662926 ± 0.102388</span> | 0.537148 ± 0.139089 | <span style="color:red">0.492872 ± 0.035139</span> | **<span style="color:red">0.661210 ± 0.126545</span>** | <span style="color:red">0.693575 ± 0.110082</span> | 0.642526 ± 0.098067 |
| v4_type_pe_best | **<span style="color:red">0.557867 ± 0.072431</span>** | 0.647034 ± 0.087295 | 0.495270 ± 0.125066 | <span style="color:red">0.477815 ± 0.022630</span> | 0.643562 ± 0.148150 | 0.672017 ± 0.088598 | 0.635300 ± 0.115403 |

## strict + mlp | AUROC matrix (embedding × train_dataset)

| Embedding | hESC | hHep | mDC | mESC | mHSC-E | mHSC-GM | mHSC-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| baseline | 0.539564 ± 0.092297 | 0.649912 ± 0.088968 | 0.545370 ± 0.092049 | **0.524766 ± 0.029826** | 0.640851 ± 0.145547 | 0.669915 ± 0.113296 | 0.672713 ± 0.098295 |
| cl_scratch_v5 | 0.504432 ± 0.106663 | <span style="color:red">0.678485 ± 0.103696</span> | **<span style="color:red">0.571045 ± 0.119104</span>** | 0.484159 ± 0.017317 | <span style="color:red">0.652910 ± 0.168670</span> | <span style="color:red">0.719301 ± 0.085146</span> | 0.659880 ± 0.096015 |
| cl_v6_fair | 0.516470 ± 0.113005 | **<span style="color:red">0.683601 ± 0.106052</span>** | <span style="color:red">0.554809 ± 0.126207</span> | 0.484086 ± 0.006501 | <span style="color:red">0.654680 ± 0.166520</span> | <span style="color:red">0.713060 ± 0.078382</span> | 0.672504 ± 0.094316 |
| cl_v6_tau01 | 0.512483 ± 0.116399 | <span style="color:red">0.677252 ± 0.102673</span> | <span style="color:red">0.551191 ± 0.114636</span> | 0.486283 ± 0.007627 | <span style="color:red">0.667354 ± 0.157785</span> | **<span style="color:red">0.722748 ± 0.079782</span>** | <span style="color:red">0.677233 ± 0.088505</span> |
| cl_v6_tau02 | 0.516531 ± 0.109380 | <span style="color:red">0.674588 ± 0.098836</span> | <span style="color:red">0.556230 ± 0.110691</span> | 0.483576 ± 0.009606 | <span style="color:red">0.660974 ± 0.168492</span> | <span style="color:red">0.722248 ± 0.090248</span> | 0.663582 ± 0.096700 |
| cl_v6_tau03 | 0.514761 ± 0.110829 | <span style="color:red">0.668527 ± 0.100632</span> | <span style="color:red">0.552676 ± 0.115700</span> | 0.485702 ± 0.011148 | <span style="color:red">0.662185 ± 0.161828</span> | <span style="color:red">0.722572 ± 0.082692</span> | 0.656935 ± 0.096785 |
| cl_v7_fair | 0.515949 ± 0.110460 | <span style="color:red">0.677525 ± 0.104186</span> | <span style="color:red">0.556656 ± 0.123284</span> | 0.488355 ± 0.005951 | <span style="color:red">0.651921 ± 0.168370</span> | <span style="color:red">0.705119 ± 0.094396</span> | **<span style="color:red">0.679102 ± 0.091977</span>** |
| minus | 0.520184 ± 0.090726 | <span style="color:red">0.667287 ± 0.103749</span> | 0.499238 ± 0.047813 | 0.518576 ± 0.051121 | <span style="color:red">0.653908 ± 0.169056</span> | 0.650532 ± 0.164998 | 0.613856 ± 0.111941 |
| scGPT_human | 0.538236 ± 0.062419 | 0.647803 ± 0.105611 | <span style="color:red">0.556882 ± 0.067955</span> | 0.487389 ± 0.016083 | 0.620379 ± 0.169277 | <span style="color:red">0.707967 ± 0.099709</span> | 0.642339 ± 0.116612 |
| scconcept | 0.508945 ± 0.035703 | 0.513146 ± 0.040891 | 0.536299 ± 0.035778 | 0.508682 ± 0.026249 | 0.498758 ± 0.112634 | 0.577979 ± 0.106679 | 0.524642 ± 0.120910 |
| scconcept_encoded | 0.532871 ± 0.076731 | 0.562288 ± 0.070333 | 0.488032 ± 0.055396 | 0.511881 ± 0.012458 | 0.488930 ± 0.095788 | 0.609228 ± 0.087404 | 0.572201 ± 0.089701 |
| v4_bias_rec_best | 0.515321 ± 0.115851 | <span style="color:red">0.665526 ± 0.085733</span> | 0.495014 ± 0.037847 | 0.520949 ± 0.016315 | **<span style="color:red">0.671080 ± 0.125348</span>** | 0.659435 ± 0.127249 | 0.653545 ± 0.100260 |
| v4_plain_best | 0.537543 ± 0.099047 | <span style="color:red">0.667050 ± 0.097665</span> | 0.542612 ± 0.108245 | 0.511988 ± 0.032387 | <span style="color:red">0.665418 ± 0.149602</span> | <span style="color:red">0.681283 ± 0.120577</span> | 0.643918 ± 0.108045 |
| v4_type_pe_best | **<span style="color:red">0.542737 ± 0.089153</span>** | <span style="color:red">0.652356 ± 0.084332</span> | 0.529605 ± 0.116000 | 0.523639 ± 0.039952 | <span style="color:red">0.655560 ± 0.147171</span> | <span style="color:red">0.671718 ± 0.131754</span> | 0.672061 ± 0.106765 |

## topology_matched + lr | AUROC matrix (embedding × train_dataset)

| Embedding | hESC | hHep | mDC | mESC | mHSC-E | mHSC-GM | mHSC-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| baseline | 0.539413 ± 0.115999 | 0.652570 ± 0.102318 | 0.528159 ± 0.103391 | 0.476179 ± 0.018829 | 0.638841 ± 0.127956 | 0.716262 ± 0.110168 | **0.649241 ± 0.060007** |
| cl_scratch_v5 | 0.530854 ± 0.140917 | <span style="color:red">0.679401 ± 0.110068</span> | <span style="color:red">0.555692 ± 0.137945</span> | **<span style="color:red">0.530163 ± 0.024326</span>** | 0.618288 ± 0.159436 | 0.713382 ± 0.057547 | 0.620687 ± 0.106716 |
| cl_v6_fair | 0.506853 ± 0.057413 | <span style="color:red">0.652579 ± 0.098444</span> | **<span style="color:red">0.567610 ± 0.134449</span>** | <span style="color:red">0.493435 ± 0.024068</span> | <span style="color:red">0.660815 ± 0.120363</span> | 0.645842 ± 0.082281 | 0.617331 ± 0.080590 |
| cl_v6_tau01 | 0.521567 ± 0.146361 | 0.652438 ± 0.086897 | 0.524869 ± 0.147437 | 0.453616 ± 0.030705 | <span style="color:red">0.648762 ± 0.139238</span> | 0.699751 ± 0.070584 | 0.599684 ± 0.086647 |
| cl_v6_tau02 | 0.504318 ± 0.100851 | <span style="color:red">0.669072 ± 0.092564</span> | <span style="color:red">0.528569 ± 0.128762</span> | 0.444069 ± 0.015268 | <span style="color:red">0.650087 ± 0.183839</span> | 0.660653 ± 0.090387 | 0.581023 ± 0.097285 |
| cl_v6_tau03 | <span style="color:red">0.551436 ± 0.068507</span> | <span style="color:red">0.681602 ± 0.113715</span> | <span style="color:red">0.528831 ± 0.123790</span> | 0.425560 ± 0.025922 | <span style="color:red">0.643224 ± 0.162798</span> | 0.700000 ± 0.092896 | 0.620470 ± 0.091276 |
| cl_v7_fair | <span style="color:red">0.551473 ± 0.075232</span> | **<span style="color:red">0.691615 ± 0.116537</span>** | 0.493241 ± 0.121227 | <span style="color:red">0.489305 ± 0.054528</span> | 0.621093 ± 0.184000 | 0.692385 ± 0.080179 | 0.628202 ± 0.078365 |
| minus | 0.504892 ± 0.104544 | <span style="color:red">0.673591 ± 0.104784</span> | 0.488385 ± 0.087939 | <span style="color:red">0.503047 ± 0.011447</span> | **<span style="color:red">0.670469 ± 0.132810</span>** | 0.646443 ± 0.126754 | 0.562436 ± 0.076431 |
| scGPT_human | **<span style="color:red">0.591511 ± 0.118918</span>** | 0.622348 ± 0.094635 | 0.507414 ± 0.125083 | <span style="color:red">0.510098 ± 0.002945</span> | <span style="color:red">0.650408 ± 0.168078</span> | **<span style="color:red">0.726155 ± 0.068792</span>** | 0.612493 ± 0.079370 |
| scconcept | 0.471272 ± 0.095505 | 0.506495 ± 0.060208 | <span style="color:red">0.537527 ± 0.053616</span> | 0.462337 ± 0.007403 | 0.526388 ± 0.089411 | 0.539366 ± 0.137875 | 0.555366 ± 0.076071 |
| scconcept_encoded | 0.506830 ± 0.121383 | 0.544021 ± 0.088602 | 0.429157 ± 0.037336 | <span style="color:red">0.512369 ± 0.017119</span> | 0.484313 ± 0.079395 | 0.616676 ± 0.066404 | 0.581991 ± 0.075935 |
| v4_bias_rec_best | 0.509160 ± 0.106546 | 0.652346 ± 0.101875 | 0.453712 ± 0.039063 | 0.411648 ± 0.025778 | 0.630419 ± 0.148195 | 0.681409 ± 0.084490 | 0.603872 ± 0.097448 |
| v4_plain_best | <span style="color:red">0.558196 ± 0.080342</span> | <span style="color:red">0.672496 ± 0.125186</span> | <span style="color:red">0.550606 ± 0.151490</span> | <span style="color:red">0.511076 ± 0.058515</span> | <span style="color:red">0.642861 ± 0.157318</span> | 0.657585 ± 0.117721 | 0.560525 ± 0.122711 |
| v4_type_pe_best | <span style="color:red">0.547080 ± 0.117313</span> | 0.627008 ± 0.111820 | 0.510499 ± 0.124956 | <span style="color:red">0.477377 ± 0.030387</span> | 0.636500 ± 0.142940 | 0.677554 ± 0.096061 | 0.620121 ± 0.142228 |

## topology_matched + mlp | AUROC matrix (embedding × train_dataset)

| Embedding | hESC | hHep | mDC | mESC | mHSC-E | mHSC-GM | mHSC-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| baseline | 0.529051 ± 0.163777 | 0.643814 ± 0.090749 | 0.539996 ± 0.102094 | 0.531777 ± 0.064358 | 0.629304 ± 0.151656 | 0.693425 ± 0.112324 | 0.648372 ± 0.114036 |
| cl_scratch_v5 | <span style="color:red">0.530441 ± 0.138460</span> | <span style="color:red">0.677553 ± 0.116719</span> | <span style="color:red">0.597911 ± 0.094727</span> | 0.484986 ± 0.027823 | <span style="color:red">0.640557 ± 0.171063</span> | 0.688112 ± 0.096423 | 0.625295 ± 0.113331 |
| cl_v6_fair | 0.493633 ± 0.100263 | <span style="color:red">0.668216 ± 0.108086</span> | **<span style="color:red">0.618083 ± 0.072793</span>** | 0.466169 ± 0.048138 | **<span style="color:red">0.664080 ± 0.136565</span>** | 0.683597 ± 0.078791 | 0.622933 ± 0.122662 |
| cl_v6_tau01 | 0.504466 ± 0.169429 | <span style="color:red">0.655904 ± 0.096723</span> | <span style="color:red">0.558858 ± 0.113427</span> | 0.456304 ± 0.053522 | <span style="color:red">0.651491 ± 0.153298</span> | 0.684920 ± 0.081749 | 0.628810 ± 0.115007 |
| cl_v6_tau02 | 0.490317 ± 0.119369 | <span style="color:red">0.665919 ± 0.099389</span> | <span style="color:red">0.568621 ± 0.107255</span> | 0.490248 ± 0.061126 | <span style="color:red">0.654308 ± 0.180939</span> | 0.672847 ± 0.091628 | 0.602138 ± 0.156326 |
| cl_v6_tau03 | <span style="color:red">0.548753 ± 0.091419</span> | <span style="color:red">0.657416 ± 0.101385</span> | <span style="color:red">0.572910 ± 0.102094</span> | 0.523046 ± 0.058888 | <span style="color:red">0.651784 ± 0.160689</span> | **<span style="color:red">0.712008 ± 0.090229</span>** | 0.637351 ± 0.116460 |
| cl_v7_fair | <span style="color:red">0.531455 ± 0.090965</span> | **<span style="color:red">0.698081 ± 0.106788</span>** | <span style="color:red">0.559208 ± 0.120554</span> | 0.451264 ± 0.040943 | <span style="color:red">0.635604 ± 0.180368</span> | <span style="color:red">0.695328 ± 0.088630</span> | **<span style="color:red">0.652428 ± 0.114763</span>** |
| minus | 0.494046 ± 0.103996 | <span style="color:red">0.676454 ± 0.102063</span> | 0.528935 ± 0.058141 | 0.515292 ± 0.052630 | <span style="color:red">0.641781 ± 0.150369</span> | 0.647675 ± 0.137182 | 0.601534 ± 0.113154 |
| scGPT_human | **<span style="color:red">0.567708 ± 0.097682</span>** | <span style="color:red">0.652524 ± 0.104264</span> | 0.527183 ± 0.081903 | 0.466438 ± 0.022401 | 0.610231 ± 0.175776 | 0.685215 ± 0.108406 | 0.613814 ± 0.124422 |
| scconcept | 0.502153 ± 0.067397 | 0.513968 ± 0.060344 | 0.526215 ± 0.035205 | 0.522853 ± 0.071128 | 0.517469 ± 0.073638 | 0.549577 ± 0.130228 | 0.531664 ± 0.102270 |
| scconcept_encoded | 0.497993 ± 0.133453 | 0.561845 ± 0.065195 | 0.425172 ± 0.040955 | 0.509924 ± 0.047865 | 0.494421 ± 0.084577 | 0.605695 ± 0.096370 | 0.591501 ± 0.090320 |
| v4_bias_rec_best | 0.518149 ± 0.141962 | <span style="color:red">0.686371 ± 0.107307</span> | 0.480520 ± 0.053072 | 0.531510 ± 0.048355 | <span style="color:red">0.639572 ± 0.136209</span> | 0.671941 ± 0.109615 | <span style="color:red">0.650950 ± 0.100569</span> |
| v4_plain_best | <span style="color:red">0.538557 ± 0.087057</span> | <span style="color:red">0.687802 ± 0.118479</span> | <span style="color:red">0.552645 ± 0.104935</span> | 0.463752 ± 0.036192 | 0.618853 ± 0.179083 | 0.670991 ± 0.118842 | 0.570045 ± 0.140456 |
| v4_type_pe_best | <span style="color:red">0.533110 ± 0.125849</span> | 0.624217 ± 0.114364 | <span style="color:red">0.547910 ± 0.087832</span> | **<span style="color:red">0.549992 ± 0.037092</span>** | 0.615831 ± 0.147537 | 0.667681 ± 0.140005 | 0.631967 ± 0.111538 |

## Aggregate mean across train datasets

Latent variables: metric=AUROC, task=transfer_v2, aggregation=mean_across_train_dataset_means, settings=coverage_matched + lr/coverage_matched + mlp/native + lr/native + mlp/strict + lr/strict + mlp/topology_matched + lr/topology_matched + mlp, train_dataset_count=7/7/7/7/7/7/7/7

Each cell is the mean of that embedding's per-train-dataset means from the setting-specific matrix above.

| Embedding | coverage_matched + lr | coverage_matched + mlp | native + lr | native + mlp | strict + lr | strict + mlp | topology_matched + lr | topology_matched + mlp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| baseline | **0.592388** | 0.598909 | 0.566524 | 0.594150 | 0.602783 | 0.606156 | 0.600095 | 0.602248 |
| cl_scratch_v5 | 0.591561 | **<span style="color:red">0.605642</span>** | <span style="color:red">0.569422</span> | 0.588911 | **<span style="color:red">0.606641</span>** | <span style="color:red">0.610030</span> | **<span style="color:red">0.606924</span>** | <span style="color:red">0.606408</span> |
| cl_v6_fair | 0.575606 | 0.584201 | **<span style="color:red">0.573700</span>** | 0.593141 | 0.598169 | <span style="color:red">0.611316</span> | 0.592066 | <span style="color:red">0.602387</span> |
| cl_v6_tau01 | 0.569475 | 0.581571 | <span style="color:red">0.572361</span> | **<span style="color:red">0.595453</span>** | 0.599194 | **<span style="color:red">0.613506</span>** | 0.585812 | 0.591536 |
| cl_v6_tau02 | 0.572397 | <span style="color:red">0.601468</span> | <span style="color:red">0.568363</span> | 0.591053 | 0.595317 | <span style="color:red">0.611104</span> | 0.576827 | 0.592057 |
| cl_v6_tau03 | 0.570855 | 0.592764 | <span style="color:red">0.569982</span> | 0.591706 | 0.585090 | <span style="color:red">0.609051</span> | 0.593018 | **<span style="color:red">0.614753</span>** |
| cl_v7_fair | 0.558702 | 0.571152 | <span style="color:red">0.568390</span> | 0.592348 | 0.594997 | <span style="color:red">0.610661</span> | 0.595330 | <span style="color:red">0.603338</span> |
| minus | 0.549884 | 0.565133 | 0.555924 | 0.577247 | 0.577195 | 0.589083 | 0.578466 | 0.586531 |
| scGPT_human | 0.583374 | 0.589032 | <span style="color:red">0.567752</span> | 0.589698 | 0.595844 | 0.600142 | <span style="color:red">0.602918</span> | 0.589016 |
| scconcept | 0.513491 | 0.516416 | 0.518305 | 0.521747 | 0.517669 | 0.524064 | 0.514107 | 0.523414 |
| scconcept_encoded | 0.515992 | 0.529192 | 0.516575 | 0.526032 | 0.525731 | 0.537919 | 0.525051 | 0.526650 |
| v4_bias_rec_best | 0.567777 | 0.588799 | 0.548391 | 0.579826 | 0.548625 | 0.597267 | 0.563224 | 0.597002 |
| v4_plain_best | 0.557666 | 0.572275 | 0.558329 | 0.586329 | <span style="color:red">0.605548</span> | <span style="color:red">0.607116</span> | 0.593335 | 0.586092 |
| v4_type_pe_best | 0.571477 | 0.584766 | 0.558697 | 0.593046 | 0.589838 | <span style="color:red">0.606811</span> | 0.585163 | 0.595815 |
