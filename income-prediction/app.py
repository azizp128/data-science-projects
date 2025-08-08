import joblib
import streamlit as st
import pandas as pd
import shap
import os
import plotly.express as px
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from src.encoders import FrequencyEncoder

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Income Prediction",
    page_icon="💰",
    layout="centered"
)

# ------------------ CACHED LOADING ------------------
@st.cache_resource
def load_pipeline():
    model_path = os.path.join(os.path.dirname(__file__), 'src/pipeline.joblib')
    return joblib.load(model_path)

pipeline = load_pipeline()

@st.cache_resource
def get_shap_explainer(_model):
    return shap.Explainer(_model)

# ------------------ PREDICTION FUNCTIONS ------------------
def get_shap_values(df):
    model = pipeline.named_steps['classifier']
    processed_data = pipeline.named_steps['preprocessor'].transform(df)
    explainer = get_shap_explainer(model)
    shap_values = explainer(processed_data)
    
    feature_names = (
        ['age', 'capital-gain', 'capital-loss', 'hours-per-week'] +  
        ['education', 'gender'] +  
        ['workclass', 'marital-status', 'occupation', 'relationship', 'race', 'native-country']
    )
    return shap_values.values, feature_names

def predict(features):
    numeric_indices = [0, 8, 9, 10]
    if any(f is None or (i in numeric_indices and f < 0) for i, f in enumerate(features)):
        return {'error': "Please provide valid positive numbers for all numeric fields."}
    
    try:
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
        df = pd.DataFrame([feature_dict])
        output = int(pipeline.predict(df)[0])
        
        shap_values, feature_names = get_shap_values(df)
        
        return {
            'prediction': "Income > $50K" if output == 1 else "Income ≤ $50K",
            'probability': float(pipeline.predict_proba(df)[0][1]),
            'shap_values': shap_values,
            'feature_names': feature_names
        }
    except Exception as e:
        return {'error': f"Prediction error: {str(e)}"}

# ------------------ MAIN APP ------------------
def main():
    st.markdown("<h1 style='text-align:center'>Income Prediction 💰</h1><hr>", unsafe_allow_html=True)
    age = st.number_input("Age", min_value=0, max_value=100, value=None, placeholder="Your Age")
    education = st.selectbox("Education", ["Preschool", "1st-4th", "5th-6th", "7th-8th", "9th", "10th",
                                            "11th", "12th", "HS-grad", "Some-college", "Assoc-voc",
                                            "Assoc-acdm", "Bachelors", "Masters", "Doctorate"])
    occupation = st.selectbox("Occupation", ["Adm-clerical", "Armed-Forces", "Craft-repair", "Exec-managerial",
                                                "Farming-fishing", "Handlers-cleaners", "Machine-op-inspct",
                                                "Other-service", "Priv-house-serv", "Prof-specialty", "Protective-serv",
                                                "Sales", "Tech-support", "Transport-moving"])
    capital_gain = st.number_input("Capital Gain", min_value=0, max_value=99999, value=None, placeholder="[0-99999]")

    working_class = st.selectbox("Working Class", ["Federal-gov", "Local-gov", "Never-worked",
                                                    "Private", "Self-emp-inc", "Self-emp-not-inc",
                                                    "State-gov", "Without-pay"])
    marital_status = st.selectbox("Marital Status", ["Divorced", "Married-AF-spouse", "Married-civ-spouse",
                                                        "Married-spouse-absent", "Never-married", "Separated", "Widowed"])
    relationship = st.selectbox("Relationship", ["Husband", "Not-in-family", "Other-relative",
                                                    "Own-child", "Unmarried", "Wife"])
    capital_loss = st.number_input("Capital Loss", min_value=0, max_value=4356, value=None, placeholder="[0-4356]")

    race = st.selectbox("Race", ["Amer-Indian-Eskimo", "Asian-Pac-Islander", "Black", "Other", "White"])
    gender = st.selectbox("Gender", ["Male", "Female"])
    hours_per_week = st.number_input("Hours Per Week", min_value=0, max_value=99, value=None, placeholder="[1-99]")
    native_country = st.selectbox("Native Country", ["Cambodia", "Canada", "China", "Columbia", "Cuba", "Dominican-Republic",
                                                        "Ecuador", "El-Salvador", "England", "France", "Germany", "Greece",
                                                        "Guatemala", "Haiti", "Holand-Netherlands", "Honduras", "Hong-Kong",
                                                        "Hungary", "India", "Iran", "Ireland", "Italy", "Jamaica", "Japan",
                                                        "Laos", "Mexico", "Nicaragua", "Outlying-US(Guam-USVI-etc)", "Peru",
                                                        "Philippines", "Poland", "Portugal", "Puerto-Rico", "Scotland", "South",
                                                        "Taiwan", "Thailand", "Trinadad&Tobago", "United-States", "Vietnam", "Yugoslavia"])
    
    if st.button("Predict", use_container_width=True):
        features = [age, working_class, education, marital_status,
                    occupation, relationship, race, gender,
                    capital_gain, capital_loss, hours_per_week, native_country]
        result = predict(features)

        if 'error' in result:
            st.error(result['error'])
        else:
            prob = result['probability'] * 100
            prediction_text = result['prediction']

            # 🎯 Decision styling rules
            if prediction_text == "Income > $50K":
                decision_color = "#2E8B57"  # green
                decision_emoji = "💰"
                decision_text = "High Income Potential"
                description = "The model predicts this person is likely to earn more than $50K."
                action_text = "Consider targeting higher-paying opportunities."
            else:
                decision_color = "#B22222"  # red
                decision_emoji = "📉"
                decision_text = "Lower Income Potential"
                description = "The model predicts this person is likely to earn $50K or less."
                action_text = "Consider upskilling or exploring career changes."

            # Confidence level interpretation
            if prob >= 80:
                confidence_color = "green"
                confidence_emoji = "🎯"
                confidence_level = f"High Confidence ({prob:.1f}%)"
            elif 60 <= prob < 80:
                confidence_color = "#DAA520"  # gold
                confidence_emoji = "⚖️"
                confidence_level = f"Moderate Confidence ({prob:.1f}%)"
            else:
                confidence_color = "orange"
                confidence_emoji = "⚠️"
                confidence_level = f"Low Confidence ({prob:.1f}%)"

            # Styled result card
            st.markdown("### 🎯 Prediction Results")
            st.markdown(f"""
            <div style="text-align: center; padding: 20px; border-radius: 10px; 
                        background-color: rgba(128,128,128,0.1); margin: 10px 0;">
                <h4 style="color: {decision_color}; margin: 0;">{decision_emoji} {decision_text}</h4>
                <p style="font-size: 18px; margin: 10px 0;">{description}</p>
                <p style="color: {confidence_color}; font-weight: bold; margin: 5px 0;">
                    {confidence_emoji} {confidence_level}
                </p>
                <p style="font-style: italic; color: gray; margin: 5px 0;">
                    Recommendation: {action_text}
                </p>
            </div>
            """, unsafe_allow_html=True)

            # 📖 Interpretation Guide
            with st.expander("📖 How to Interpret This Result"):
                st.markdown("""
                **Confidence Levels:**
                - 🎯 **High Confidence (80%+)**: Strong prediction, safe to follow recommendation  
                - ⚖️ **Moderate Confidence (60-79%)**: Good prediction, consider additional factors  
                - ⚠️ **Low Confidence (<60%)**: Uncertain prediction, manual review recommended  

                **Recommendation Actions:**
                - ✅ **High Income Potential**: Focus on leveraging current skills and maximizing opportunities  
                - ❌ **Lower Income Potential**: Consider upskilling, retraining, or career change strategies  
                """)
            
            # Feature Importance Plot
            shap_df = pd.DataFrame({'Feature': result['feature_names'], 'Impact': result['shap_values'][0]})
            fig = px.bar(shap_df.sort_values('Impact'), x='Impact', y='Feature', orientation='h',
                         title='Feature Impact on Prediction', color='Impact',
                         color_continuous_scale=['red', 'green'])
            st.markdown("### Feature Importance")
            st.plotly_chart(fig, use_container_width=True)

    # === Bulk Upload ===
    st.header("📂 Bulk Income Prediction (CSV Upload)")

    # Sample CSV for reference
    st.subheader("📄 Sample Data Format")
    sample_data = pd.DataFrame({
        'age': [39, 50],
        'workclass': ['Private', 'Self-emp-not-inc'],
        'education': ['Bachelors', 'HS-grad'],
        'marital-status': ['Never-married', 'Married-civ-spouse'],
        'occupation': ['Adm-clerical', 'Exec-managerial'],
        'relationship': ['Not-in-family', 'Husband'],
        'race': ['White', 'White'],
        'gender': ['Male', 'Male'],
        'capital-gain': [2174, 0],
        'capital-loss': [0, 0],
        'hours-per-week': [40, 13],
        'native-country': ['United-States', 'United-States']
    })
    st.dataframe(sample_data.head())

    # Downloadable sample
    st.download_button(
        label="📥 Download Sample Data",
        data=sample_data.to_csv(index=False).encode('utf-8'),
        file_name='sample_bulk_income_prediction.csv',
        mime='text/csv',
    )

    # File uploader
    uploaded_file = st.file_uploader("Upload Data (.csv)", type=["csv"], key="bulk_file_upload")

    # Required columns
    REQUIRED_COLUMNS = [
        'age', 'workclass', 'education', 'marital-status', 'occupation',
        'relationship', 'race', 'gender', 'capital-gain', 'capital-loss',
        'hours-per-week', 'native-country'
    ]

    if uploaded_file is not None:
        try:
            df_bulk = pd.read_csv(uploaded_file)

            # Check columns
            missing_cols = set(REQUIRED_COLUMNS) - set(df_bulk.columns)
            if missing_cols:
                st.error(f"Missing required columns: {missing_cols}")
            else:
                st.subheader("Preview of Uploaded Data")
                st.dataframe(df_bulk.head())

                # Predictions
                with st.spinner("Processing and predicting..."):
                    results = []
                    for _, row in df_bulk.iterrows():
                        features = [
                            row['age'], row['workclass'], row['education'], row['marital-status'],
                            row['occupation'], row['relationship'], row['race'], row['gender'],
                            row['capital-gain'], row['capital-loss'], row['hours-per-week'], row['native-country']
                        ]
                        pred_result = predict(features)
                        if 'error' in pred_result:
                            results.append("Error")
                        else:
                            results.append(pred_result['prediction'])

                    df_bulk['Prediction'] = results
                    st.session_state['bulk_income_predictions'] = df_bulk

                # Show results
                st.success("✅ Bulk Prediction Completed")
                st.subheader("📊 Prediction Results")
                st.dataframe(df_bulk)

                # Download results
                st.download_button(
                    label="📥 Download Results as CSV",
                    data=df_bulk.to_csv(index=False).encode('utf-8'),
                    file_name='bulk_income_predictions.csv',
                    mime='text/csv',
                )

        except Exception as e:
            st.error(f"Error processing file: {e}")

    elif "bulk_income_predictions" in st.session_state:
        st.subheader("📊 Last Bulk Prediction")
        st.dataframe(st.session_state["bulk_income_predictions"])


if __name__ == "__main__":
    main()