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

## Dataset

### Description

- Parallel English-MSA dataset converted from BELEBELE MCQA to EQA format.
- Includes 329 QA pairs, with annotations for extractive spans.

### Access

The dataset is available in the `Data/` folder

---

## Results

| Dataset              | F1   | EM   |
|----------------------|-------|-------|
| SQuAD               | 90.6 | 79.1 |
| BELEBELE-EQA (All)  | 71.0 | 50.5 |
| BELEBELE-EQA (Sub)  | 76.6 | 56.1 |

Detailed results in a paper.

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
