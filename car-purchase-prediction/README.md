# Car Purchase Prediction Streamlit App

This repository contains a Streamlit application that helps users make car purchasing decisions. The application uses an XGBoost classification model to predict whether a person can afford a car based on their age, gender, and annual income. If the prediction is positive, it provides car recommendations, and if negative, it suggests potential career paths to increase income.

## Project Structure

```
car-purchase-prediction/
├── app.py              # Main Streamlit application
├── assets/
│   ├── car-images/    # Images of recommended cars
│   │   ├── Avanza.png
│   │   ├── brio.png
│   │   └── ...
│   ├── bg.jpg         # Background image
│   ├── car_data.csv   # Dataset used for training
│   ├── model.joblib   # Trained XGBoost model
│   └── notebook.ipynb # Model development notebook
└── requirements.txt    # Project dependencies
```

## Features

- Car purchase prediction using XGBoost classifier
- Interactive input form for user data
- Visual car recommendations with images and descriptions
- Career path suggestions for income improvement
- Cross-validated model with optimized F1-score and ROC-AUC
- Responsive Streamlit interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/car-purchase-prediction.git
cd car-purchase-prediction
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the Streamlit application:
```bash
streamlit run app.py
```

The app will open automatically in your default web browser at `http://localhost:8501`.

## Usage

1. Input your information:
   - Age (numeric value)
   - Gender (select Male or Female)
   - Annual Salary in USD

2. Click "Predict" to see the results

3. Based on the prediction:
   - If positive: View recommended cars with images and specifications
   - If negative: Explore suggested career paths with salary information

## Model Details

- Algorithm: XGBoost Classifier
- Features: Age, Gender, Annual Salary
- Metrics: Optimized for F1-score and ROC-AUC
- Validation: 10-fold cross-validation with 3 repeats
- Training data: 1000 samples with balanced class distribution
