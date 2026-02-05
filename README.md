# Per-era luminosity calculation [CMS analysis]

This workflow computes per-era integrated luminosities using `brilcalc` on `lxplus`.

For Run 2 UL datasets, the official golden JSONs are not provided per era. Therefore, they are manually split into eras using the run-number ranges corresponding to each data-taking period. The run ranges were taken from [PdmVDataReprocessing < CMS < TWiki](https://twiki.cern.ch/twiki/bin/view/CMS/PdmVDataReprocessing).

For each year in Run 2, the sum of the per-era luminosities agrees with the values recommended by [LUM TWiki](https://twiki.cern.ch/twiki/bin/view/CMS/LumiRecommendationsRun3). In the case of Run 3, some eras are not recommended for use in analysis.

## Sources

Source for the golden JSON files:
- 2016: [Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON](https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions16/13TeV/Legacy_2016/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt)
- 2017:  [Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON](https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions17/13TeV/Legacy_2017/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt)
- 2018: [Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON](https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions18/13TeV/Legacy_2018/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt)
- 2022: [2022C](https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions22/Cert_Collisions2022_eraC_355862_357482_Golden.json), [2022D](https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions22/Cert_Collisions2022_eraD_357538_357900_Golden.json), [2022E](https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions22/Cert_Collisions2022_eraE_359022_360331_Golden.json), [2022F](https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions22/Cert_Collisions2022_eraF_360390_362167_Golden.json), [2022G](https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions22/Cert_Collisions2022_eraG_362433_362760_Golden.json)
- 2023: [2023C](https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions23/Cert_Collisions2023_eraC_367095_368823_Golden.json), [2023D](https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions23/Cert_Collisions2023_eraD_369803_370790_Golden.json)

Source for run numbers for each era in Run 2:
- 2016: [PdmVDataReprocessingUL2016](https://twiki.cern.ch/twiki/bin/view/CMS/PdmVDataReprocessingUL2016)
- 2017: [PdmVDataReprocessingUL2017](https://twiki.cern.ch/twiki/bin/view/CMS/PdmVDataReprocessingUL2017)
- 2018: [PdmVDataReprocessingUL2018](https://twiki.cern.ch/twiki/bin/view/CMS/PdmVDataReprocessingUL2018)

## How to run

Split a golden JSON into eras using the corresponding run-number map:
```bash
python3 split.json --json goldenJSONs/Legacy_2016.json  --run runs/2016.json
```

Verify that `brilcalc` tool  is correctly set up:
```bash
brilcalc lumi \
--normtag /cvmfs/cms-bril.cern.ch/cms-lumi-pog/Normtags/normtag_PHYSICS.json \
-u /fb \
-i goldenJSONs/Legacy_2016.json
```
Compute luminosity for a specific year (e.g. 2022):
```bash
python3 calculate.py --filter 2022
```


## Results

### 2016

Pre-VFP eras:
| Era       | Lumi (fb$^{-1}$) | From POG  |
| :-------- | ----------------:|:---------:|
| B_ver2    |    5.82942773    | ---   |
| C         |    2.60167810    | ---   |
| D         |    4.28603180    | ---   |
| E         |    4.06597475    | ---   |
| FHIPM     |    2.71848926    | ---   |
| **Total** | **19.50160251**  | ---   |

Source (POG): https://twiki.cern.ch/twiki/bin/view/CMS/LumiRecommendationsRun2#Luminosity_for_pp_13_TeV_data_20

Post-VFP eras:
| Era       | Lumi (fb$^{-1}$) | From POG  |
| :-------- | ----------------:|:---------:|
| F         |     0.41877119   | ---   |
| G         |     7.65326123   | ---   |
| H         |     8.74011930   | ---   |
| **Total** | **16.81215172**  | ---   |

Total (preVFP + postVFP) = 36.313753344 fb$^{-1}$ <br>
POG recommended value: 36.31 fb$^{-1}$<br>
Source (POG): https://twiki.cern.ch/twiki/bin/view/CMS/LumiRecommendationsRun2#Luminosity_for_pp_13_TeV_data_20

### 2017
| Era       | Lumi (fb$^{-1}$) | From POG  |
| :-------- | ----------------:|:---------:|
| B         |  4.88086683      | ---   |
| C         |  9.72563826      | ---   |
| D         |  4.31371476      | ---   |
| E         |  9.42009453      | ---   |
| F         | 13.72791429      | ---   |
| **Total** | **42.06822866**  | 42.07 |

Source (POG): https://twiki.cern.ch/twiki/bin/view/CMS/LumiRecommendationsRun2#Luminosity_for_pp_13_TeV_data_20

### 2018

| Era       | Lumi (fb$^{-1}$) | From POG  |
| :-------- | ----------------:|:---------:|
| A         | 13.961196585     | ---       |
| B         |  7.028282919     | ---       |
| C         |  6.872940971     | ---       |
| D         | 31.698842046     | ---       |
| **Total** | **59.56126252**  | 59.56     |

Source (POG): https://twiki.cern.ch/twiki/bin/view/CMS/LumiRecommendationsRun2#Luminosity_for_pp_13_TeV_data_20

### 2022

Pre-EE eras:
| Era       | Lumi (fb$^{-1}$) | From PdmV |
| :-------- | ----------------:| ---------:|
| C         | 5.010409015      | 5.0104    |
| D         | 2.970045130      | 2.9700    |
| **Total** | **7.980454145**  | ---       |

Post-EE eras:
| Era       | Lumi (fb$^{-1}$) | From PdmV |
| :-------- | ----------------:| ---------:|
| E         |  5.80695521      | 	5.8070   |
| F         | 17.78190146      | 17.7819   |
| G         |  3.08275303      |	3.0828   |
| **Total** | **26.67160970**  | ---       |

Source (PdMV): https://twiki.cern.ch/twiki/bin/view/CMS/PdmVRun3Analysis#DATA_AN4

### 2023

| Era       | Lumi (fb$^{-1}$) | From PdmV |
| :-------- | ----------------:| ---------:|
| C (preBPix)   | 18.06265911  | 18.063    |
| D (postBPix)  |  9.69313005  | 	9.693    |

Source (PdMV): https://twiki.cern.ch/twiki/bin/view/CMS/PdmVRun3Analysis#DATA_AN2

## Conclusion

Use the following luminosities while working with the Run 2 and Run 3 datasets. The numbers are expressed in pb$^{-1}$.

| campaign         | Lumi (pb$^-1$) |
| :--------------- | --------------:|
| 2016preVFP_UL    | 19501.60251    |
| 2016postVFP_UL   | 16812.15172    |
| 2017_UL          | 42068.22866    |
| 2018_UL          | 59561.26252    |
| Run3Summer22     |  7980.45414    |
| Run3Summer22EE   | 26671.60970    |
| Run3Summer23     | 18062.65911    |
| Run3Summer23BPix |  9693.13005    |
