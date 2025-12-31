import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .preprocessor import clean_text

class IRModel:
    def __init__(self, data_frame):
        """
        Inisialisasi model dengan data dari database.
        data_frame harus punya kolom 'content'.
        """
        self.df = data_frame
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = None
        self._build_model()

    def _build_model(self):
        self.df['clean_content'] = self.df['content'].apply(clean_text)
        
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df['clean_content'])

    def search(self, query):
        clean_query = clean_text(query)
        
        query_vec = self.vectorizer.transform([clean_query])
        
        similarity_scores = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        
        results = self.df.copy()
        results['score'] = similarity_scores
        
        final_results = results[results['score'] > 0].sort_values(by='score', ascending=False)
        
        return final_results