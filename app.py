import streamlit as st
import pandas as pd
import numpy as np
import re
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential, load_model

# Fungsi untuk membersihkan teks
def clean_text(text):
    text = re.sub(r"<USERNAME>", "", text)
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"\d+", "", text)
    text = re.sub(r"[^\x00-\x7F]+", "", text)
    text = re.sub(r"[^a-zA-Z ]", "", text)
    text = text.lower().strip()
    return text

# Fungsi untuk memuat model dan tokenizer
@st.cache_resource
def load_sentiment_model():
    model = Sequential()
    model = load_model("sentiment_model.h5")  
    tokenizer = Tokenizer(num_words=5000)
    tokenizer.fit_on_texts(pd.read_csv("dataset_komentar_instagram_cyberbullying.csv")["Instagram Comment Text"])
    return model, tokenizer

# Aplikasi Streamlit
st.title("Sentimen Analisis Komentar Instagram")
st.write("Aplikasi ini menggunakan LSTM untuk memprediksi apakah komentar Instagram bernada positif atau negatif.")

# Input pengguna
user_input = st.text_area("Masukkan komentar Instagram di bawah:", "")

if st.button("Analisis Sentimen"):
    if user_input:
        # Preprocessing input pengguna
        cleaned_text = clean_text(user_input)
        model, tokenizer = load_sentiment_model()
        sequence = tokenizer.texts_to_sequences([cleaned_text])
        padded_sequence = pad_sequences(sequence, maxlen=100)
        
        # Prediksi menggunakan model
        prediction = model.predict(padded_sequence)
        sentiment = "Positif" if prediction[0][0] > 0.5 else "Negatif"
        st.write(f"**Prediksi Sentimen:** {sentiment}")
        st.write(f"**Probabilitas Sentimen Positif:** {prediction[0][0]:.2f}")
    else:
        st.warning("Silakan masukkan komentar untuk dianalisis.")

# Penjelasan tentang model dan dataset
st.sidebar.header("Tentang Aplikasi")
st.sidebar.write(
    """
    Aplikasi ini menggunakan model LSTM yang dilatih untuk menganalisis sentimen komentar Instagram.
    Dataset terdiri dari komentar yang telah dilabeli sebagai positif atau negatif.
    """
)
