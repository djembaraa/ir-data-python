import streamlit as st
import pandas as pd
from supabase import create_client, Client
from modules.search_engine import IRModel

st.set_page_config(page_title="Tugas IR Deploy", page_icon="🔍")

@st.cache_resource
def init_connection():
    url = st.secrets["supabase"]["url"]
    key = st.secrets["supabase"]["key"]
    return create_client(url, key)

supabase = init_connection()

@st.cache_data(ttl=600) 
def load_data():
    response = supabase.table('documents').select("*").execute()
    data = response.data
    return pd.DataFrame(data)

st.title("🔍 Sistem Temu Balik Informasi (IR)")
st.caption("Deploy Sederhana | Backend: Python & Scikit-learn | DB: Supabase")

try:
    df_docs = load_data()
    
    with st.expander("Lihat Database Dokumen (Supabase)"):
        st.dataframe(df_docs)

    if not df_docs.empty:
        model = IRModel(df_docs)
        
        query = st.text_input("Masukkan kata kunci pencarian:", placeholder="Contoh: sistem informasi")
        
        if query:
            st.write(f"Hasil pencarian untuk: **{query}**")
            
            results = model.search(query)
            
            if not results.empty:
                for index, row in results.iterrows():
                    st.success(f"**{row['title']}** (Score: {row['score']:.4f})")
                    st.write(row['content'])
                    st.divider()
            else:
                st.warning("Tidak ditemukan dokumen yang relevan.")
    else:
        st.error("Database kosong. Silakan isi data di Supabase.")

except Exception as e:
    st.error(f"Terjadi kesalahan koneksi atau code: {e}")

st.markdown("---")
st.markdown("Dibuat oleh: **Djembar Arafat** | Framework: Streamlit")