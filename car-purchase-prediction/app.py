import streamlit as st
import joblib
import os
from pathlib import Path
import numpy as np
import pandas as pd

# Set page config
st.set_page_config(
    page_title="Car Purchase Prediction",
    page_icon="🚗",
    layout="centered"
)

# Add background image
bg_path = Path(__file__).parent / "assets" / "bg.jpg"
if bg_path.exists():
    with open(bg_path, "rb") as f:
        image_bytes = f.read()
    st.image(image_bytes)

# Load the model with proper error handling
@st.cache_resource
def load_model():
    try:
        MODEL_PATH = Path(__file__).parent / "assets" / "model.joblib"
        if not MODEL_PATH.exists():
            st.error(f"Model file not found at {MODEL_PATH}")
            return None
        return joblib.load(MODEL_PATH)
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

model = load_model()

def predict_purchase(age, gender, annual_salary):
    """Make prediction using the loaded model"""
    if model is None:
        return None
    try:
        # Create features DataFrame with exact column names from training
        features = pd.DataFrame([[age, gender, annual_salary]], 
                              columns=['Age', 'Gender', 'AnnualSalary'])
        
        prediction = model.predict(features)
        return prediction[0]
    except Exception as e:
        st.error(f"Prediction error: {str(e)}")
        st.write("Feature names mismatch. Expected:", model.feature_names_in_)
        return None

def show_result_0():
    """Display content for prediction result 0"""
    st.error("Anda belum sesuai untuk membeli mobil.")
    st.write("Berikut pekerjaan yang bisa anda lakukan untuk mencari penghasilan tambahan, atau bahkan bisa menjadi pekerjaan utama anda!!")
    
    jobs = [
        {"title": "Admin Online Shop", "salary": "Rp3.500.000-Rp2.500.000"},
        {"title": "Anggota DPR", "salary": "Rp4.200.000/bulan + tunjangan"},
        {"title": "Anggota MPR", "salary": "Rp5.040.000/bulan"},
        {"title": "Direktur Pertamina", "salary": "Rp2,8 miliar/bulan"},
        {"title": "Menteri", "salary": "Rp18.648.000/bulan"},
        {"title": "Dokter Gigi", "salary": "Rp8.309.058/bulan"},
        {"title": "Influencer", "salary": "Rp22 juta/bulan"},
        {"title": "Manager", "salary": "Rp10.954.088/bulan"}
    ]
    
    for job in jobs:
        with st.expander(f"💼 {job['title']}"):
            st.write(f"Kisaran Gaji: {job['salary']}")

def show_result_1():
    """Display content for prediction result 1"""
    st.success("Anda telah cocok untuk membeli sebuah mobil!")
    st.write("Berikut rekomendasi mobil untuk pembelian pertama anda:")
    
    cars = [
        {
            "name": "Toyota Avanza",
            "price": "Rp240-308 juta",
            "image": "Avanza.png",
            "description": "Avanza E 1.3 tersedia mulai harga Rp. 240 juta hingga Rp. 254 jt. Sedangkan Avanza G 1.5 dimulai dari harga Rp. 267 juta hingga Rp. 281 juta dan Avanza G 1.5 TSS seharaga 308 juta."
        },
        {
            "name": "Hyundai Creta",
            "price": "Rp291,3-408,3 juta",
            "image": "creta.png",
            "description": "Harga Creta adalah antara Rp 291,3 Juta hingga Rp 408,3 Juta, Ada 6 varian yang tersedia dari Creta: Active MT, Trend MT, Trend IVT, Dynamic Black Edition, Style IVT dan Prime IVT."
        },
        {
            "name": "Honda Brio",
            "price": "Rp161-191 juta",
            "image": "brio.png",
            "description": "Siapa yang tidak mengetahui mobil keluarga satu ini, tidak hanya dengan kualitas yang oke apalagi dengan pengguna pertama, Honda Brio juga memiliki harga yang cukup ekonomis yakni berkisar antara 161juta-191juta untuk tipe S dan Type E."
        },
        {
            "name": "Honda Mobilio",
            "price": "Rp207-264 juta",
            "image": "mobilio.png",
            "description": "Honda Mobilio hadir dengan konsumsi bahan bakar lebih hemat dan performa yang selalu bisa diandalkan dengan Harga 207-264 juta anda dapat memiliki mobil dengan tipe Mobilio S, Mobilio E, Mobilio RS."
        },
        {
            "name": "Nissan Grand Livina",
            "price": "Rp218-318 juta",
            "image": "glivina.png",
            "description": "Nissan Livina adalah model MPV kompak yang diproduksi oleh produsen mobil Jepang Nissan. Ini diperkenalkan pada bulan Juli 2006 oleh Dongfeng Nissan di Guangzhou International Motor Show dan mulai dijual pada bulan Desember 2006. kini mobil tersebut bisa anda miliki dimulai dari Harga 218-318jutaa."
        },
        {
            "name": "Nissan Magnite",
            "price": "Rp272-300 juta",
            "image": "mg.png",
            "description": "Nissan Magnite hadir sebagai compact SUV yang berani dengan garis tubuh yang tangguh dan tampilan yang dinamis. Kemanapun anda pergi, Nissan Magnite akan selalu menjadi pusat perhatian yang membuat anda lebih percaya diri."
        },
        {
            "name": "Toyota Agya",
            "price": "Rp165-188 juta",
            "image": "agya.png",
            "description": "Toyota Agya merupakan mobil LCGC (low cost green car) yang menjadi andalan Toyota dan menarik perhatian banyak masyarakat, dengan harga 165-188 juta dan tipe AGYA G 1.2 M/T, AGYA G 1.2 A/T, AGYA G 1.2 M/T TRD."
        },
        {
            "name": "Toyota Calya",
            "price": "Rp161,7-184,4 juta",
            "image": "Toyota Calya.png",
            "description": "Walaupun harganya tak lagi murah, Toyota Calya tetap saja menjadi pilihan utama bagi mereka yang mencari dan mau membeli mobil pertama. Harga Calya antara Rp 161,7 Juta hingga Rp 184,4 Juta."
        }
    ]
    
    for car in cars:
        with st.expander(f"🚗 {car['name']} - {car['price']}"):
            # Load and display image
            image_path = Path(__file__).parent / "assets" / "car-images" / car['image']
            try:
                if image_path.exists():
                    # Try reading the image file first
                    with open(image_path, "rb") as f:
                        image_bytes = f.read()
                    st.image(image_bytes, 
                            caption=car['name'],
                            use_column_width=True)
                else:
                    st.warning(f"Image not found: {car['image']}")
                    st.write("Expected path:", image_path)
            except Exception as e:
                st.error(f"Error loading image: {str(e)}")
            
            # Display car description
            st.write(car['description'])

def main():
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
        if model is None:
            st.error("Model could not be loaded. Please check if the model file exists in the correct location.")
            return
            
        result = predict_purchase(age, gender, annual_salary)
        if result is not None:
            st.write("---")
            st.subheader("Hasil Prediksi")
            if result == 1:
                show_result_1()
            else:
                show_result_0()

if __name__ == "__main__":
    main()