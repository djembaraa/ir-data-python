from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import re

factory = StemmerFactory()
stemmer = factory.create_stemmer()

def clean_text(text):
    """
    Membersihkan teks: lowercase, hapus tanda baca, dan stemming.
    """
    if not text:
        return ""
    
    text = text.lower()
    
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    
    text = stemmer.stem(text)
    
    return text