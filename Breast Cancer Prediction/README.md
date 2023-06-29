# Summary of Breast Cancer Prediction Project:
The objective of this project was to predict breast cancer using classification models. The dataset used for this project was obtained from Kaggle https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data and is called the "Breast Cancer Wisconsin (Diagnostic) Data Set." The dataset contains various features computed from digitized images of fine needle aspirates (FNA) of breast mass. The features are used to predict whether the mass is **malignant (M)** or **benign (B)**.

Three classification algorithms, namely **Logistic Regression**, **Decision Tree**, and **Random Forest**, were employed for the breast cancer prediction task. After evaluating the models, it was found that the **Random Forest** algorithm yielded the best results.

## The project followed the following steps:

- **Data Collection**: The dataset was obtained from Kaggle, which provided a pre-processed version of the Breast Cancer Wisconsin dataset. The dataset consisted of features such as radius, texture, perimeter, area, smoothness, compactness, concavity, symmetry, and fractal dimension.

- **Data Preprocessing**: The dataset was examined for missing values, outliers, and any necessary data transformations. It was ensured that the data was in the correct format for model training.

- **Model Training**: Logistic Regression, Decision Tree, and Random Forest models were trained using the preprocessed dataset. Each model was fitted on the training data and learned the patterns and relationships between the features and the target variable.

- **Model Evaluation**: The trained models were evaluated using appropriate evaluation metrics such as accuracy, precision, recall, and F1-score. The performance of each model was assessed to determine its effectiveness in predicting breast cancer.

- **Comparison and Selection of Best Model**: After evaluating the models, it was observed that the Random Forest algorithm outperformed the Logistic Regression and Decision Tree models in terms of accuracy and other evaluation metrics. Therefore, the Random Forest model was chosen as the best model for breast cancer prediction in this project.

## Conclusion:
This project aimed to predict breast cancer using classification models. After evaluating the performance of Logistic Regression, Decision Tree, and Random Forest algorithms, the Random Forest model was found to provide the best results. The project highlights the importance of feature selection, model training, and evaluation in the context of breast cancer prediction. The chosen model can be further utilized for future predictions and potential clinical applications.
