# Sistem Temu Balik Informasi (IR Search Engine)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)
![Supabase](https://img.shields.io/badge/Database-Supabase-green)

Aplikasi "Sistem Temu Balik Informasi" sederhana yang dibangun untuk memenuhi tugas mata kuliah **Information Retrieval**. Aplikasi ini mengimplementasikan algoritma **Cosine Similarity** dan **TF-IDF** untuk mencari relevansi dokumen, serta menggunakan library **Sastrawi** untuk proses stemming Bahasa Indonesia.

## Fitur Utama

* **Algoritma TF-IDF & Cosine Similarity:** Menghitung skor kemiripan antara query pencarian dan dokumen secara matematis.
* **Stemming Bahasa Indonesia:** Menggunakan library `Sastrawi` untuk mengubah kata berimbuhan menjadi kata dasar agar pencarian lebih akurat (Pre-processing).
* **Database Terintegrasi:** Dokumen disimpan dan diambil secara *real-time* dari **Supabase (PostgreSQL)**, bukan hardcode array.
* **Modern UI/UX:** Antarmuka web bersih dan responsif menggunakan **Streamlit** dengan pendekatan desain *Gestalt Principles* (Card layout, clean typography).
* **Modular Code:** Struktur kode dipisah antara logika (*backend*) dan tampilan (*frontend*) untuk kemudahan maintenance.

## Teknologi yang Digunakan

* **Bahasa:** Python
* **Framework Web:** Streamlit
* **Machine Learning:** Scikit-learn (TF-IDF, Cosine Similarity)
* **NLP:** NLTK & Sastrawi
* **Database:** Supabase-py

## Struktur Folder

```bash
├── modules/
│   ├── preprocessing.py    # Logika Stemming & Cleaning Teks
│   └── search_engine.py    # Logika TF-IDF & Perhitungan Skor
├── .streamlit/
│   └── secrets.toml        # Konfigurasi API Key (Local only)
├── app.py                  # File Utama (Frontend UI)
├── requirements.txt        # Daftar Library Dependencies
└── README.md               # Dokumentasi Proyek

##  Instalasi & Menjalankan di Local

### 1. Clone Repository
git clone [[https://github.com/USERNAME_KAMU/NAMA_REPO_KAMU.git](https://github.com/djembaraa/ir-data-python.git)]([https://github.com/USERNAME_KAMU/NAMA_REPO_KAMU.git](https://github.com/djembaraa/ir-data-python.git))
cd ir-data-python

### 2. Buat Virtual Environment
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Config
# File: .streamlit/secrets.toml

[supabase]
url = "MASUKKAN_SUPABASE_URL_KAMU"
key = "MASUKKAN_SUPABASE_ANON_KEY_KAMU"

### 5. Run Development
streamlit run app.py
