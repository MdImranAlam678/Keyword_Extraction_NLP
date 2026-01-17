"""
TF-IDF Keyword Extraction Module
Implements text preprocessing and TF-IDF based keyword extraction
"""

import re
import string
import ssl
from collections import Counter
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Handle SSL certificate issues when downloading NLTK resources
try:
    _create_unverified_https_context = ssl._create_unverified_context
    ssl._create_default_https_context = _create_unverified_https_context
except AttributeError:
    # SSL context overriding not supported (unlikely), proceed with defaults
    pass

# Download required NLTK data (will be done on first run)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', quiet=True)

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet', quiet=True)

try:
    nltk.data.find('corpora/omw-1.4')
except LookupError:
    nltk.download('omw-1.4', quiet=True)


class KeywordExtractor:
    """
    Class for extracting keywords from text using TF-IDF technique
    
    Methods:
        - preprocess_text: Cleans and preprocesses input text
        - extract_keywords: Extracts top N keywords using TF-IDF scores
    """
    
    def __init__(self):
        """Initialize the keyword extractor with preprocessing components"""
        # Initialize stopwords
        self.stop_words = set(stopwords.words('english'))
        
        # Initialize lemmatizer
        self.lemmatizer = WordNetLemmatizer()
        
        # Initialize TF-IDF vectorizer (will be fitted per document)
        self.vectorizer = None
    
    def preprocess_text(self, text):
        """
        Preprocesses input text through multiple steps:
        1. Lowercasing
        2. Tokenization
        3. Stopword removal
        4. Lemmatization
        
        Args:
            text (str): Raw input text
            
        Returns:
            str: Preprocessed text ready for TF-IDF vectorization
        """
        # Step 1: Lowercasing
        text = text.lower()
        
        # Step 2: Remove special characters and extra whitespace
        text = re.sub(r'[^\w\s]', ' ', text)
        text = re.sub(r'\s+', ' ', text)
        
        # Step 3: Tokenization
        tokens = word_tokenize(text)
        
        # Step 4: Remove stopwords and short words (length < 2)
        filtered_tokens = [
            token for token in tokens 
            if token not in self.stop_words and len(token) > 2
        ]
        
        # Step 5: Lemmatization
        lemmatized_tokens = [
            self.lemmatizer.lemmatize(token) for token in filtered_tokens
        ]
        
        # Join tokens back to string
        preprocessed_text = ' '.join(lemmatized_tokens)
        
        return preprocessed_text
    
    def extract_keywords(self, text, top_n=10):
        """
        Extracts top N keywords from input text using TF-IDF scores
        
        Algorithm:
        1. Preprocess the input text
        2. Create TF-IDF vectorizer and fit on the document
        3. Calculate TF-IDF scores for each term
        4. Extract top N terms with highest TF-IDF scores
        5. Return keywords with their scores
        
        Args:
            text (str): Input text for keyword extraction
            top_n (int): Number of top keywords to extract (default: 10)
            
        Returns:
            list: List of dictionaries containing keywords and their TF-IDF scores
                 Format: [{"keyword": "word", "score": 0.123}, ...]
        """
        # Step 1: Preprocess text
        preprocessed_text = self.preprocess_text(text)
        
        # Check if preprocessed text is empty
        if not preprocessed_text.strip():
            return []
        
        # Step 2: Initialize TF-IDF vectorizer
        # Using unigrams (single words) with min_df=1 to include all terms
        self.vectorizer = TfidfVectorizer(
            max_features=1000,  # Limit vocabulary size
            min_df=1,           # Minimum document frequency (at least once)
            max_df=1.0,         # Allow all terms (single document scenario)
            ngram_range=(1, 1), # Only unigrams (single words)
            smooth_idf=True     # Smooth IDF weights
        )
        
        # Step 3: Fit and transform the document
        # Since we're working with a single document, we treat it as a corpus
        # For single document TF-IDF, we use the document itself as the corpus
        tfidf_matrix = self.vectorizer.fit_transform([preprocessed_text])
        
        # Step 4: Get feature names (vocabulary)
        feature_names = self.vectorizer.get_feature_names_out()
        
        # Step 5: Extract TF-IDF scores for the document
        # Get the first (and only) row of the TF-IDF matrix
        tfidf_scores = tfidf_matrix.toarray()[0]
        
        # Step 6: Create list of (keyword, score) pairs
        keyword_scores = [
            (feature_names[i], float(tfidf_scores[i]))
            for i in range(len(feature_names))
            if tfidf_scores[i] > 0  # Only include terms with non-zero scores
        ]
        
        # Step 7: Sort by TF-IDF score in descending order
        keyword_scores.sort(key=lambda x: x[1], reverse=True)
        
        # Step 8: Extract top N keywords
        top_keywords = keyword_scores[:top_n]
        
        # Step 9: Format results
        result = [
            {
                "keyword": keyword,
                "score": round(score, 6)  # Round to 6 decimal places
            }
            for keyword, score in top_keywords
        ]
        
        return result


