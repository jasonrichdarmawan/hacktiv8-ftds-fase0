# rencana awal dan saat ini

rencana awal: per repository per fase.

rencana sekarang: 1 repository untuk fase 0 - 2.

dampaknya adalah: folder fase 1 -> `x_fase1`

# penting

- [Hypothesis Testing null hypothesis and alternative hypothesis](week02_day04/am/am.ipynb)
- [Find the most influential people with Eigendecomposition](week02_day05_libur/latihan_live_code/Math_Solving_Cases.ipynb)
- [Recommendation System with Cosine Similarity & Feature Selection](week03_day01/pm/P0W3D1PM_Math_&_Stats_Solving_cases.ipynb)
- [Feature Selection dengan corrcoef](week02_day03/pm/d2am.ipynb)

# feature selection

![](./images/How-to-Choose-Feature-Selection-Methods-For-Machine-Learning%20(1).webp)

## probably important

- [Linear Regression and Logistic Regression technical know how](./x_fase1/week01_day03/am/Linreg_Logreg.ipynb)

- [Linear Regression](./x_fase1/week01_day03/am/P1W1D3AM_Linear_Regression.ipynb)
- [Logistic Regression](./x_fase1/week01_day03/pm/P1W1D3PM_Logistic_Regression.ipynb)

- [simpler explanation of logistic regression](./x_fase1/week01_day03/pm/playground/logistic_regression.ipynb)

- [imbalanced dataset](./x_fase1/week01_day03/ngc1/h8dsft_LogisticRegression.ipynb)
  - careful, this suffer from overfitting because [RandomOverSampler](https://stackoverflow.com/questions/51064462/process-for-oversampling-data-for-imbalanced-binary-classification)
  - careful, this suffer from data leakage. i will fix this later with cross validation.

## reference

- [L2 Ridge try to minimize coefficient, L1 Lasso to force coefficient to zero, ElasticNet do L2 -> L1 by ratio](https://towardsdatascience.com/linear-regression-models-4a3d14b8d368)

- [accuracy, precision, recall, f1-score](https://medium.com/analytics-vidhya/confusion-matrix-accuracy-precision-recall-f1-score-ade299cf63cd)
  - accuracy 0.97 
    
    this model guess (class 1, 2, 3) correctly 97% of the time, 3% incorrectly.
    - high accuracy does not mean good model. probably the model just guess everything as class 1. the other 3% of the data is class 2 and 3.
  
  - precision class 1 0.97 
    
    this model guess class 1 correctly 97% of the time (including false positive)

    - false positive class 1 = guessing class 2 as class 1.
    - high precision does not mean good model. probably the model just guess everything as class 1. the other 3% of the data is class 2 and 3.
  
  - recall class 1 0.97
    
    this model recognize class 1 97% of the time. 3% of the time, the model unable to recognize class 1.
  
  - f1-score
    ```
    f1-score = 2 * precision * recall
                   ------------------
                   precision + recall
    ```