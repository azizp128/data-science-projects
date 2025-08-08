# **Project Overview**

This project demonstrates a **machine learning pipeline** that predicts whether an individual’s annual income exceeds **\$50K** based on demographic and employment attributes such as:

* **Age**
* **Workclass**
* **Education level**
* **Marital status**
* **Occupation**
* **Hours worked per week**
* And other relevant features from the [UCI Adult Income dataset](https://archive.ics.uci.edu/dataset/2/adult)

The model is built using **XGBoost** within a **scikit-learn pipeline** for preprocessing and training. It supports both **single predictions** via a form interface and **bulk predictions** via CSV uploads.

Beyond model training, the project also focuses on **deployment best practices**, showcasing how to serve ML models in production environments using **Flask** (Heroku deployment) and **Streamlit** (cloud-hosted interactive UI).

# **Key Features**

* **End-to-End ML Pipeline**: Includes data preprocessing, feature engineering, model training, evaluation, and persistence using `joblib`.
* **Custom Encoders**: Implements a `FrequencyEncoder` for categorical variables alongside ordinal, binary, and numeric transformations.
* **Interactive Web App**:

  * Single prediction interface
  * Bulk CSV upload and prediction
  * Downloadable prediction results
* **Cloud Deployment**: Deployed on both **Streamlit Cloud** and (previously) **Heroku**, demonstrating different hosting strategies.

# **Deployments**

## **Streamlit App**

[🔗 Launch Adult Income Prediction App](https://adult-income-prediction.streamlit.app/)

An interactive dashboard that allows users to input attributes or upload CSV files for instant predictions.

![Streamlit Web Page Screenshot](https://raw.githubusercontent.com/azizp128/data-science-projects/refs/heads/main/income-prediction/assets/streamlit-screenshot.png)

## **Heroku App** *(archived)*

A REST API implementation using Flask, hosted on Heroku, allowing programmatic income predictions via HTTP requests.

![Heroku Web Page Screenshot](https://raw.githubusercontent.com/azizp128/data-science-projects/refs/heads/main/income-prediction/assets/heroku-screenshot.png)

# **Tech Stack**

* **Python**: Data processing, model training, and deployment scripting
* **scikit-learn** & **XGBoost**: Machine learning and pipeline management
* **Pandas** & **NumPy**: Data wrangling and preprocessing
* **Streamlit**: Interactive UI for predictions
* **Flask**: API service for Heroku deployment
* **Joblib**: Model persistence
* **Heroku** & **Streamlit Cloud**: Cloud deployment platforms

# **Use Cases**

* Demonstrates deploying ML models for **tabular data classification**.
* Serves as a reference for **building custom preprocessing pipelines** in scikit-learn.
* Useful learning resource for **ML deployment comparisons** (API vs interactive UI).
