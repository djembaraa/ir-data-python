import streamlit as st
import pandas as pd
from supabase import create_client
from modules.search_engine import IRModel
import time

st.set_page_config(page_title="Search Engine IR", page_icon="✨", layout="centered")

st.markdown("""
<style>
    /* Import Font Modern */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Menghilangkan padding atas bawaan yang terlalu lebar */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 5rem;
    }

    /* Styling Input Box agar lebih 'Tactile' */
    .stTextInput input {
        border-radius: 12px !important;
        border: 1px solid #E0E0E0;
        padding: 12px 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
        transition: all 0.3s ease;
    }
    
    .stTextInput input:focus {
        border-color: #FF4B4B !important;
        box-shadow: 0 4px 12px rgba(255, 75, 75, 0.15) !important;
    }

    /* Styling Expander Database */
    .streamlit-expanderHeader {
        background-color: #F8F9FA;
        border-radius: 8px;
        font-size: 0.9rem;
    }

    /* Custom Footer */
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: white;
        text-align: center;
        padding: 15px;
        font-size: 0.8rem;
        color: #888;
        border-top: 1px solid #eee;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def init_connection():
    try:
        url = st.secrets["supabase"]["url"]
        key = st.secrets["supabase"]["key"]
        return create_client(url, key)
    except:
        return None

supabase = init_connection()

@st.cache_data(ttl=600)
def load_data():
    if not supabase:
        return pd.DataFrame()
    try:
        response = supabase.table('documents').select("*").execute()
        return pd.DataFrame(response.data)
    except Exception as e:
        return pd.DataFrame()


col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    st.title("✨ Smart Search")
    st.markdown(
        "<p style='text-align: left; color: #666; margin-top: -15px;'>Sistem Temu Balik Informasi berbasis <b>Cosine Similarity</b></p>", 
        unsafe_allow_html=True
    )

try:
    df_docs = load_data()

    with st.expander("Lihat Data Korpus (Database)"):
        if not df_docs.empty:
            st.dataframe(df_docs, use_container_width=True)
        else:
            st.info("Database kosong atau gagal terkoneksi.")

    st.divider()

    if not df_docs.empty:
        model = IRModel(df_docs)
        
        query = st.text_input("", placeholder="🔍 Ketik kata kunci (misal: 'teknologi informasi')...")
        
        if query:
            with st.spinner('Menganalisis relevansi dokumen...'):
                time.sleep(0.3)
                results = model.search(query)
            
            st.markdown(f"##### Hasil pencarian untuk: `'{query}'`")
            
            if not results.empty:
                for index, row in results.iterrows():
                    score_pct = row['score'] * 100
                    
                    with st.container(border=True):
                        c1, c2 = st.columns([5, 1])
                        
                        with c1:
                            st.subheader(row['title'])
                        with c2:
                            st.metric(label="Relevansi", value=f"{int(score_pct)}%")
                        
                        st.markdown(f"<div style='color: #444; line-height: 1.6;'>{row['content']}</div>", unsafe_allow_html=True)
                        
                        st.progress(row['score'], text=None)
            else:
                st.container(border=True).markdown("""
                <div style='text-align: center; padding: 20px;'>
                    <h3>🤷‍♂️</h3>
                    <p><b>Tidak ditemukan dokumen yang relevan.</b><br>
                    Coba gunakan kata kunci lain atau periksa typo.</p>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.error("Gagal memuat data dari Supabase. Cek koneksi internet atau API Key.")

except Exception as e:
    st.error(f"System Error: {e}")

st.markdown("""
<div class='footer'>
    Designed by <b>Djembar Arafat</b> &nbsp;|&nbsp; Information Retrieval 2025
</div>
""", unsafe_allow_html=True)