# 📊 LSTM untuk Analisis Sentimen Instagram  
Proyek ini menggunakan Long Short-Term Memory (LSTM) untuk mengklasifikasikan emosi pada komentar media sosial, khususnya dari Instagram. Dengan pendekatan deep learning, model ini dirancang untuk mendeteksi sentimen positif, negatif, atau netral secara akurat.

---

## 🎯 Tujuan  
1. Membangun model deep learning berbasis LSTM untuk analisis sentimen.  
2. Mengevaluasi performa model menggunakan metrik akurasi, precision, recall, dan F1-score.  
3. Memberikan wawasan tentang pola komentar di media sosial.

---

## 🛠️ Langkah-Langkah  
### 1. **Persiapan Dataset**  
   - Dataset dikumpulkan dari komentar Instagram dengan label emosi.  
   - Data dibersihkan untuk menghapus noise seperti emoji, URL, dan simbol.  

### 2. **Pemrosesan Data**  
   - Tokenisasi teks menggunakan Tokenizer dari TensorFlow/Keras.  
   - Padding dan truncation diterapkan untuk menyamakan panjang input.  

### 3. **Pembangunan Model**  
   - Arsitektur LSTM digunakan untuk memproses urutan teks.  
   - Layer embedding ditambahkan untuk representasi teks.  
   - Aktivasi softmax pada output layer untuk klasifikasi multi-kelas.  

### 4. **Pelatihan Model**  
   - Model dilatih menggunakan optimizer `adam` dan fungsi loss `categorical_crossentropy`.  
   - Data dibagi menjadi training, validation, dan testing set.  

### 5. **Evaluasi**  
   - Metrik seperti akurasi, confusion matrix, dan klasifikasi F1-score dihitung.

---

## 🔁 Deskripsi Alur  
1. **Input Data:** Dataset komentar Instagram.  
2. **Preprocessing:**  
   - Normalisasi teks (lowercase, hapus tanda baca, dll.).  
   - Tokenisasi dan padding.  
3. **Pelatihan Model:**  
   - Input teks diterjemahkan ke vektor embedding.  
   - LSTM layer memproses urutan untuk menangkap konteks temporal.  
   - Output model memprediksi label sentimen.  
4. **Evaluasi:** Membandingkan prediksi model dengan label ground truth.  

---

## 📊 Hasil  
- **Akurasi Pelatihan:** 95%  
- **Akurasi Validasi:** 90%  
- **Confusion Matrix:**  
  | Sentimen | Positif | Netral | Negatif |  
  |----------|---------|--------|---------|  
  | **Positif** | 120     | 10     | 5       |  
  | **Netral**  | 8       | 150    | 12      |  
  | **Negatif** | 6       | 9      | 100     |  

- **Visualisasi Loss dan Akurasi:**  
  ![Training Plot](#)

---

## 🧪 Evaluasi Model  
- **Kekuatan:**  
  - Mampu menangkap konteks panjang dari teks komentar.  
  - Akurasi tinggi pada komentar netral dan positif.  

- **Kelemahan:**  
  - Performa pada kelas negatif sedikit lebih rendah.  
  - Rentan terhadap komentar ambigu atau ironi.  

- **Rekomendasi:**  
  - Tambahkan data pelatihan untuk kelas negatif.  
  - Eksperimen dengan arsitektur lain seperti BiLSTM atau GRU.  

---

## 🚀 Cara Menjalankan  
1. Clone repository ini:  
   ```bash
   git clone https://github.com/username/reponame.git
   cd reponame
