# Write-up 6: Project Proposal

**Name:** Krishna Sharma  
**Student ID:** ksharma2  
**Date:** 12/4/2025  

---

## Overview

Write-Up 6 for Project 2.

---

## Content

1. Project Overview

- Overarching Goal: The objective of the project is to predict natural killer (NK) cell infiltration into the tumor microenvironments of human tumors by analyzing bulk RNA-seq data using ML methods. Specifically, this project will classify tumors by their NK cell abudance and build a model that can predict NK cell infiltration into tumors.

- Rationale: Despite the advances of immunotherapy, solid tumors are especially difficult to treat due to their heterogeneous TME and reprogramming of immune cells, such that many immunotherapies are not effective in certain patients. NK cells offer a unique approach to combat solid tumors through their anti-tumor cytotoxicity and not needing prior antigen exposure, unlike T cells. NK cells are improperly understood in their ability to infiltrate tumors and what gene signatures may be associated with their exclusion. NK cells are understudied compared to T cells and their low infiltration are associated with poor prognosis in cancer patients.

- Specific Aims:
AIM 1: Develop a pre-processing pipeline that can obtain TCGA bulk RNA-seq gene expression data, extract features, normalize the data and prepare the data for training a model. The expected outcome is to have a script that can take the raw data and process it for model training. There could be difficulties with obtaining datatypes that are easily readable and there could be challenges with choosing a normalization method. These can be addressed on a case by case basis and by deciding statistical methods beforehand.

AIM 2: Train a machine learning model that can predict NK cell infiltration into tumors from bulk RNA-seq data. Using deconvolutional methods and tools (like CIBERSORTx), we will classify training/test data by NK cell infiltration scoring. Then build a regression model to predict NK cell infiltraton. A potential problem could be with the model overfitting the data and the parameters need to be tuned. In this case, we can use regularized models and reduce dimensionality.

2. Data

- Dataset description: use TCGA Bulk RNA-seq data which includes data across several cancer types (pan-cancer) or specific types. We can use a specific solid tumor dataset, such as HNSC, which has a little over 520 samples to start and then generalize to pan cancer (over 10,000 samples). We can take the data from UCSC Xena browser which has the data processed as STAR-Counts or STAR-TPM in a csv.

- Data Suitability: The data is suitable because NK cells can be identified based on the rna data. It is optimal for downstream processing since we already have TPM values.

- Storage and Data Management: We call the dataset directly from UCSC for the lesser datasets. If needed, then we can use the Stanford cluster (SCG). Can be shared with collaborators by directing to TCGA.

3. Environment

- Coding Environment: Use python from Jupyter notebook that is on the local machine. If not, SCG for bigger jobs.

- Dependencies: Can download the scikit-learn library for ML analysis. We can download numpy and pandas for the pre-processing. We can download seaborn for visualizing the data in graphs/plots. We cna download xgboost for gradient boosting.

- Reproducibility: Store code on a Git repo with a clean directory. Can have a conda environment with a yml file.

4. Pipeline:

- Algorithms and methods: First load the TCGA gene expression data in and process to make TCM. Log transform and normalize the data. Filter by p-values. Apply CIBERSORTx infiltration data. Create NK cell infiltration scores for different groups. Apply regression to predict NK cell infiltration score. Use random forest regression model or gradient boosting regressor.

- Scalability and Efficiency: To ensure the pipeline works efficiently, add directories that download processed data at each step. Use feature reduced data for initial memory usage and model training. Split the data into train/test once. Chunk the dataset for usage before training.

5. Machine Learning

- Task Definition: Supervised learning by classification of tumors being NK-high or NK-low depending on infiltration per the gene expression signatures from the bulk RNA-seq.

- Feature Representation: The data will be normalized and converted to TPM and be log transformed. We will filter out non-variable genes and those with non-significant p values. Perform PCA to get dimensional reduction. There will be some 5000 genes or so of interest and perhaps 15-100 features for dimensions from PCA.

- Model Selection: Apply Gradient Boosting, Logistic Regression, and Random Forest. Logistic regression is effective for data with many dimensions, gradient boosting is easier to change parameters and is used as a standard, and Random forest will obtain any non-linear relationships.

- Generalization Strategy: Train/test split. Try with different cancer subtypes.

- Evaluation Metrics: Evaluate based on pearson correlation, accuracy, precision, and ROC/AUC. Pearson correlation provides a biologically relevant alignment of prediction and actual NK cell infiltration for the regression. For the classification, accuracy and precision are key to ensure the model is effective. ROC/AUC is important for classification tasks in binary situations and to avoid false positives.



You can use some text formating, lists, and tables to imporve the write-up readability
#### **Text Formatting**

You can make text **bold**, *italic*, or even ***bold and italic*** for emphasis.

#### **Lists**

**Unordered list:**
- Apple  
- Banana  
- Cherry  

**Ordered list:**
1. First step  
2. Second step  
3. Third step  

#### **Table Example**

| Tool | Description         | Example Command        |
|------|---------------------|------------------------|
| `ls` | Lists files         | `ls -la`               |
| `grep` | Searches text     | `grep "pattern" file.txt` |
| `wc` | Counts words/lines  | `wc -l filename.txt`   |

Code snippets and images are highly recommended to document your work.

#### **Code Examples**

**Inline code example:** Use the `print()` function to display text.  

**Code block example:**

```bash
# Example command line code
echo "Hello, Markdown!"
```

```python
# Example Python code
for i in range(3):
    print("Iteration:", i)
```

For longer script, you can say something like, `script1.py` contains functions for reading fasta file. Ideally, all codes you run should be saved in corresponding files. 


#### **Image Example**

![Example placeholder image](./snyderlab.png)

#### **Link Example**

Learn more about Markdown syntax here:  
[Markdown Guide](https://www.markdownguide.org/basic-syntax/)

---


## Acknowledgement

