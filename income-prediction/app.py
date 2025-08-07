import pickle
import streamlit as st
import pandas as pd
import shap
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

# Custom Frequency Encoder
class FrequencyEncoder(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.freq_maps = {}
    
    def fit(self, X, y=None):
        self.freq_maps = {}
        # Handle both DataFrame and array inputs
        if hasattr(X, 'columns'):
            for col in X.columns:
                freqs = X[col].value_counts(normalize=True)
                self.freq_maps[col] = freqs
        else:
            # If X is an array, create column names
            X_df = pd.DataFrame(X)
            for col in X_df.columns:
                freqs = X_df[col].value_counts(normalize=True)
                self.freq_maps[col] = freqs
        return self

    def transform(self, X):
        # Handle both DataFrame and array inputs
        if hasattr(X, 'columns'):
            X_out = X.copy()
            for col in X.columns:
                if col in self.freq_maps:
                    X_out[col] = X_out[col].map(self.freq_maps[col]).fillna(0)
        else:
            # Convert array to DataFrame for processing
            X_df = pd.DataFrame(X)
            X_out = X_df.copy()
            for col in X_df.columns:
                if col in self.freq_maps:
                    X_out[col] = X_out[col].map(self.freq_maps[col]).fillna(0)
            X_out = X_out.values  # Convert back to array
        
        return X_out

def get_shap_values(df):
    """Get SHAP values and feature names for interpretation"""
    # Get the model from pipeline
    model = pipeline.named_steps['classifier']
    # Get preprocessed data
    processed_data = pipeline.named_steps['preprocessor'].transform(df)
    
    # Initialize JS visualization for notebook environment
    shap.initjs()
    
    # Calculate SHAP values
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(processed_data)
    
    # Get feature names after preprocessing
    feature_names = (
        ['age', 'capital-gain', 'capital-loss', 'hours-per-week'] +  # numeric
        ['education'] +  # ordinal
        ['gender'] +  # binary
        ['workclass', 'marital-status', 'occupation', 'relationship', 'race', 'native-country']  # nominal
    )
    
    return shap_values, feature_names

def get_recommendations(df, shap_values, feature_names):
    """Generate recommendations based on SHAP values"""
    recommendations = []
    
    # Get all features sorted by importance
    feature_importance = np.abs(shap_values[0])
    sorted_indices = np.argsort(feature_importance)
    
    # Examine all features
    for idx in sorted_indices:
        feature = feature_names[idx]
        shap_value = shap_values[0][idx]
        
        # Add recommendations based on feature importance and values
        if shap_value < 0:  # Negative impact on income prediction
            if feature == 'education':
                recommendations.append("Consider pursuing higher education to potentially increase income.")
            elif feature == 'hours-per-week':
                if df['hours-per-week'].values[0] < 40:
                    recommendations.append("Consider increasing work hours if possible.")
                else:
                    recommendations.append("Your current work hours are good for income potential.")
            elif feature == 'occupation':
                recommendations.append("Consider exploring opportunities in higher-paying occupations or career advancement.")
            elif feature == 'capital-gain':
                if df['capital-gain'].values[0] < 1000:
                    recommendations.append("Look into investment opportunities to increase capital gains.")
            elif feature == 'workclass':
                recommendations.append("Consider exploring opportunities in different sectors or self-employment.")
            elif feature == 'age':
                recommendations.append("Consider gaining more work experience or skills development.")
        else:  # Positive impact on income prediction
            if feature == 'education':
                recommendations.append("Your education level positively impacts your income potential.")
            elif feature == 'occupation':
                recommendations.append("Your current occupation shows good income potential.")
            elif feature == 'capital-gain':
                recommendations.append("Your investment strategy appears to be working well.")
    
    # Limit to top 3 most relevant recommendations
    recommendations = recommendations[:3]
                
    return recommendations

# loading in the model to predict on the data (now includes preprocessing)
with open('assets/model.pkl', 'rb') as model_file:
    pipeline = pickle.load(model_file)


def page_style():
    return st.markdown(
    """
    <h1 style="text-align: center; font-family: sans-serif;">
    Income Prediction
    </h1>
    <hr>
    """,
        unsafe_allow_html=True
    )


def predict(features):
    """
    Predict income category using the pipeline and provide explanations
    """
    # Convert features to format expected by model
    feature_dict = {
        'age': features[0],
        'workclass': features[1], 
        'education': features[2],
        'marital-status': features[3],
        'occupation': features[4],
        'relationship': features[5],
        'race': features[6],
        'gender': features[7],
        'capital-gain': features[8],
        'capital-loss': features[9],
        'hours-per-week': features[10],
        'native-country': features[11]
    }
    
    # Convert dictionary to DataFrame
    df = pd.DataFrame([feature_dict])
    
    # Make prediction
    prediction = pipeline.predict(df)
    output = int(prediction[0])
    
    # Get SHAP values and recommendations
    shap_values, feature_names = get_shap_values(df)
    recommendations = get_recommendations(df, shap_values, feature_names)
    
    # Create result dictionary
    result = {
        'prediction': "Income > $50K" if output == 1 else "Income ≤ $50K",
        'probability': float(pipeline.predict_proba(df)[0][1]),
        'recommendations': recommendations,
        'shap_values': shap_values,
        'feature_names': feature_names
    }
    
    return result


def main():
    page_style()

    age = st.number_input(label="Age", placeholder="Your Age",
                          value=None, min_value=0, max_value=100)
    working_class = st.selectbox(
        label="Working Class", index=0,
        options=("Federal-gov", "Local-gov", "Never-worked",
                 "Private", "Self-emp-inc", "Self-emp-not-inc",
                 "State-gov", "Without-pay"))
    education = st.selectbox(
        label="Education", index=0,
        options=("Preschool", "1st-4th", "5th-6th", "7th-8th", "9th", "10th",
                "11th", "12th", "HS-grad", "Some-college", "Assoc-voc",
                "Assoc-acdm", "Bachelors", "Masters", "Doctorate"))
    marital_status = st.selectbox(
        label="Marital Status", index=0,
        options=("Divorced", "Married-AF-spouse", "Married-civ-spouse",
                 "Married-spouse-absent", "Never-married", "Separated",
                 "Widowed"))
    occupation = st.selectbox(
        label="Occupation", index=0,
        options=("Adm-clerical", "Armed-Forces", "Craft-repair", "Exec-managerial",
                 "Farming-fishing", "Handlers-cleaners", "Machine-op-inspct",
                 "Other-service", "Priv-house-serv", "Prof-specialty", "Protective-serv",
                 "Sales", "Tech-support", "Transport-moving"))
    relationship = st.selectbox(
        label="Relationship", index=0,
        options=("Husband", "Not-in-family", "Other-relative",
                 "Own-child", "Unmarried", "Wife"))
    race = st.selectbox(
        label="Race", index=0,
        options=("Amer-Indian-Eskimo", "Asian-Pac-Islander",
                 "Black", "Other", "White"))
    gender = st.selectbox(label="Gender", index=0,
                          options=("Male", "Female"))
    capital_gain = st.number_input(
        "Capital Gain", placeholder="[0-99999]", min_value=0, max_value=99999, value=None)
    capital_loss = st.number_input(
        "Capital Loss", placeholder="[0-4356]", min_value=0, max_value=4356, value=None)
    hours_per_week = st.number_input(
        "Hours Per Week", placeholder="[1-99]", min_value=0, max_value=99, value=None)
    native_country = st.selectbox(
        label="Native Country", index=0,
        options=("Cambodia", "Canada", "China",
                 "Columbia", "Cuba", "Dominican-Republic",
                 "Ecuador", "El-Salvador", "England",
                 "France", "Germany", "Greece",
                 "Guatemala", "Haiti", "Holand-Netherlands",
                 "Honduras", "Hong-Kong", "Hungary",
                 "India", "Iran", "Ireland", "Italy",
                 "Jamaica", "Japan", "Laos", "Mexico",
                 "Nicaragua", "Outlying-US(Guam-USVI-etc)", "Peru",
                 "Philippines", "Poland", "Portugal", "Puerto-Rico",
                 "Scotland", "South", "Taiwan", "Thailand",
                 "Trinadad&Tobago", "United-States", "Vietnam", "Yugoslavia"))

    result = ""
    if st.button("Predict", use_container_width=True):
        features = [age, working_class, education, marital_status,
                   occupation, relationship, race, gender,
                   capital_gain, capital_loss, hours_per_week, native_country]
        result = predict(features)
        
    if result:
        # Display prediction with probability
        pred_text = result['prediction']
        prob = result['probability'] * 100
        st.markdown(f"""
        ## Prediction Result
        <div style='padding: 20px; border-radius: 10px; border: 2px solid red; text-align: center;'>
            <h4>{pred_text}</h4>
            <p>Confidence: {prob:.1f}%</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Display SHAP values
        st.markdown("## Feature Importance")
        shap_values = result['shap_values']
        feature_names = result['feature_names']
        
        # Create a simple bar plot of SHAP values
        st.bar_chart(
            pd.DataFrame(
                shap_values[0],
                index=feature_names,
                columns=['Impact']
            ).sort_values('Impact', ascending=True)
        )

        # Display recommendations
        if result['recommendations']:
            st.markdown("""
            ## Recommendations
            <div style='border-radius: 10px;'>
            """, unsafe_allow_html=True)
            for rec in result['recommendations']:
                st.markdown(f"- {rec}")
            st.markdown("</div>", unsafe_allow_html=True)


if __name__ == '__main__':
    main()