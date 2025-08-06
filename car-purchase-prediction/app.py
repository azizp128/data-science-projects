import streamlit as st
import joblib
import os
from pathlib import Path

# Set page config
st.set_page_config(
    page_title="Car Purchase Prediction",
    page_icon="🚗",
    layout="centered"
)

# Load the model
MODEL_PATH = Path(__file__).parent.parent / "assets" / "model" / "model.joblib"
model = joblib.load(MODEL_PATH)

def predict_purchase(age, gender, annual_salary):
    """Make prediction using the loaded model"""
    features = [[age, gender, annual_salary]]
    prediction = model.predict(features)
    return prediction[0]

def main():
    # Add custom CSS
    st.markdown("""
        <style>
        .main {
            padding: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # Title
    st.title("Car Purchase Prediction")
    st.subheader("Silahkan isi form di bawah ini")

    # Input forms
    age = st.number_input("Usia", min_value=0, max_value=100, value=25)
    gender = st.selectbox("Gender", options=[0, 1], 
                         format_func=lambda x: "Laki-laki" if x == 0 else "Perempuan")
    annual_salary = st.number_input("Gaji Tahunan (Dollar)", min_value=0, value=30000)

    # Prediction button
    if st.button("Predict"):
        result = predict_purchase(age, gender, annual_salary)
        
        # Display result
        if result == 1:
            st.success("Anda kemungkinan besar mampu membeli mobil! 🎉")
        else:
            st.error("Anda mungkin belum mampu membeli mobil saat ini. 😢")

if __name__ == "__main__":
    main()