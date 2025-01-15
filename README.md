# From Multiple-Choice to Extractive QA: A Case Study for English and Arabic

## Overview

This repository accompanies the paper *"From Multiple-Choice to Extractive QA: A Case Study for English and Arabic"* presented at the [31st International Conference on Computational Linguistics (COLING 2025)](https://coling2025.org/). It provides the dataset, code, and resources to facilitate the conversion of multiple-choice question answering (MCQA) datasets into extractive question answering (EQA) datasets.

The project includes:
- A parallel EQA dataset for English and Modern Standard Arabic (MSA).
- Annotation guidelines for EQA datasets.
- Tools and scripts for dataset preparation, annotation, and evaluation.

## Repository Structure

- **`Data/`**: Contains the datasets, including raw MCQA data, annotated EQA datasets, and supplementary materials.
- **`Guidelines/`**: Contains detailed annotation guidelines for creating EQA datasets for English and Arabic.
- **`Notebooks/`**: Jupyter notebooks for analysis and visualization of results.
- **`Results/`**: Contains evaluation results for various QA tasks and experimental configurations.
- **`Results_Translated/`**: Stores evaluation results for experiments conducted with translated datasets.
- **`Scripts/`**: Includes scripts for data preprocessing, annotation projection, and evaluation.
- **`Settings/`**: Contains configuration files for running experiments and evaluations.
- **`Settings_Translated/`**: Includes configuration files for experiments using translated data.

## Prerequisites

[PrimeQA](https://github.com/primeqa): This repository relies on the PrimeQA toolkit for evaluation and experimentation. 
Installation instructions for PrimeQA can be found [here](https://github.com/primeqa/primeqa?tab=readme-ov-file#%EF%B8%8F-getting-started).

## Dataset

### Description

- Parallel English-MSA dataset converted from BELEBELE MCQA to EQA format.
- Includes 329 QA pairs, with annotations for extractive spans.

### Access

The dataset is available in the `Data/` folder

---

## Results

| Passage | Question                   | **All** F1 | **All** EM | **All** F1ⁿ | **All** EMⁿ | **Sub** F1 | **Sub** EM | **Sub** F1ⁿ | **Sub** EMⁿ |
|---------|----------------------------|------------|------------|-------------|-------------|------------|------------|-------------|-------------|
| EN      | EN                         | 71.0       | 50.5       | 74.0        | 60.2        | 76.6       | 56.1       | 79.5        | 65.6        |
|         | MSA                        | 59.9       | 39.8       | 62.7        | 47.7        | 62.9       | 43.5       | 65.6        | 51.2        |
|         | DA--Iraqi                  | 44.5       | 27.7       | 46.2        | 31.3        | 46.0       | 29.5       | 47.8        | 33.0        |
|         | DA--Levantine              | 49.5       | 31.9       | 51.2        | 36.5        | 51.9       | 35.1       | 53.7        | 39.6        |
|         | DA--Gulf                   | 50.4       | 31.3       | 52.6        | 37.4        | 52.1       | 33.0       | 54.2        | 38.9        |
|         | DA--Morrocan               | 36.3       | 18.5       | 38.5        | 21.0        | 37.0       | 20.0       | 39.3        | 22.1        |
|         | DA--Egyptian               | 48.8       | 30.1       | 51.5        | 36.2        | 51.3       | 33.3       | 54.0        | 39.3        |
|         | *DA--Average*              | 45.9       | 27.9       | 48.0        | 32.5        | 47.7       | 30.2       | 49.8        | 34.6        |
|         | DA--Iraqi (T_EN)           | 59.8       | 39.2       | 62.7        | 46.8        | 64.2       | 42.8       | 67.2        | 50.9        |
|         | DA--Levantine (T_EN)       | 65.4       | 46.2       | 68.2        | 53.5        | 69.7       | 50.2       | 72.3        | 57.9        |
|         | DA--Gulf (T_EN)            | 65.4       | 43.8       | 68.2        | 52.9        | 69.5       | 48.1       | 72.2        | 57.2        |
|         | DA--Morrocan (T_EN)        | 63.0       | 41.0       | 65.7        | 49.5        | 67.0       | 44.9       | 69.6        | 53.0        |
|         | DA--Egyptian (T_EN)        | 65.7       | 45.0       | 68.7        | 53.8        | 70.0       | 49.5       | 72.9        | 58.2        |
|         | *DA--Average* (T_EN)       | 63.9       | 43.0       | 66.7        | 51.3        | 68.1       | 47.1       | 70.8        | 55.4        |
| MSA     | EN                         | 60.4       | 41.6       | 62.3        | 46.8        | 64.5       | 46.0       | 66.7        | 50.9        |
|         | MSA                        | 62.0       | 40.7       | 64.3        | 46.2        | 65.6       | 44.2       | 68.1        | 49.5        |
|         | DA--Iraqi                  | 50.3       | 32.2       | 51.2        | 35.0        | 54.2       | 36.1       | 55.6        | 39.3        |
|         | DA--Levantine              | 54.2       | 35.3       | 55.7        | 38.6        | 58.5       | 39.3       | 60.4        | 43.2        |
|         | DA--Gulf                   | 56.6       | 36.2       | 58.4        | 40.7        | 59.3       | 39.6       | 61.3        | 44.2        |
|         | DA--Morrocan               | 45.1       | 26.7       | 46.6        | 30.1        | 48.1       | 29.8       | 49.6        | 33.3        |
|         | DA--Egyptian               | 54.5       | 34.0       | 56.6        | 39.2        | 57.3       | 37.5       | 59.5        | 42.5        |
|         | *DA--Average*              | 52.1       | 32.9       | 53.7        | 36.7        | 55.5       | 36.5       | 57.3        | 40.5        |
|         | DA--Iraqi (T_MSA)          | 51.5       | 31.3       | 53.1        | 35.3        | 53.9       | 34.0       | 55.7        | 37.9        |
|         | DA--Levantine (T_MSA)      | 58.5       | 38.3       | 60.3        | 43.2        | 62.1       | 42.1       | 64.1        | 46.7        |
|         | DA--Gulf (T_MSA)           | 57.9       | 38.0       | 59.9        | 42.9        | 61.0       | 40.7       | 63.3        | 46.0        |
|         | DA--Morrocan (T_MSA)       | 56.5       | 36.2       | 58.6        | 42.6        | 59.4       | 39.3       | 61.5        | 45.3        |
|         | DA--Egyptian (T_MSA)       | 58.5       | 37.7       | 60.4        | 42.2        | 62.1       | 41.1       | 64.2        | 46.0        |
|         | *DA--Average* (T_MSA)      | 56.6       | 36.3       | 58.5        | 41.2        | 59.7       | 39.4       | 61.8        | 44.4        |

Monolingual and cross-lingual evaluation of BELEBELE-EQA shows strong performance in monolingual settings (EN-EN, MSA-MSA) and significant improvement with translation for dialectal Arabic. Results highlight the difficulty of cross-lingual and dialectal QA, emphasizing the value of the BELEBELE-EQA dataset for benchmarking multilingual QA systems. 

Please read a paper for detailed results.

---

## Citation

If you use this dataset or code, please cite:

```bibtex
@inproceedings{lynn_etal_2025_mcqa_to_eqa,
  title={From Multiple-Choice to Extractive QA: A Case Study for English and Arabic},
  author={Lynn, Teresa and Altakrori, Malik H. and Magdy, Samar M. and Das, Rocktim Jyoti and Lyu, Chenyang and Nasr, Mohamed and Samih, Younes and Chirkunov, Kirill and Aji, Alham Fikri and Nakov, Preslav and Godbole, Shantanu and Roukos, Salim and Florian, Radu and Habash, Nizar},
  booktitle={Proceedings of the 31st International Conference on Computational Linguistics (COLING 2025)},
  year={2025}
}
```

## Acknowledgments
This work is a result of a collaboration between [IBM](https://research.ibm.com/artificial-intelligence), [Mohamed bin Zayed University of Artificial Intelligence (MBZUAI)](https://mbzuai.ac.ae/), and [New York University Abu Dhabi (NYUAD)](https://nyuad.nyu.edu/).
Special thanks to the [BELEBELE dataset](https://github.com/facebookresearch/belebele) creators and the [PrimeQA](https://github.com/primeqa/primeqa) toolkit team.
