# Backend - TF-IDF Keyword Extraction API

## Overview
This backend implements a RESTful API for keyword extraction using TF-IDF (Term Frequency-Inverse Document Frequency) technique. The API accepts text input and returns the top N keywords with their TF-IDF scores.

## Technology Stack
- **Framework**: Flask 3.0.0
- **ML Library**: scikit-learn (for TF-IDF vectorization)
- **NLP Library**: NLTK (for text preprocessing)
- **CORS**: flask-cors (for cross-origin requests)

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Navigate to backend directory**:
```bash
cd backend
```

2. **Create virtual environment (recommended)**:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Download NLTK data** (if not automatically downloaded):
```python
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
```

## Running the Backend

1. **Start the Flask server**:
```bash
python app.py
```

2. **The API will be available at**:
```
http://localhost:5000
```

3. **Health check endpoint**:
```
GET http://localhost:5000/api/health
```

## API Endpoints

### 1. Health Check
- **URL**: `/api/health`
- **Method**: `GET`
- **Response**:
```json
{
  "status": "healthy",
  "message": "TF-IDF Keyword Extraction API is running"
}
```

### 2. Extract Keywords
- **URL**: `/api/extract-keywords`
- **Method**: `POST`
- **Content-Type**: `application/json`

**Request Body**:
```json
{
  "text": "Your input text here",
  "top_n": 10
}
```

**Parameters**:
- `text` (required): Input text string for keyword extraction
- `top_n` (optional): Number of top keywords to extract (default: 10)

**Response (Success)**:
```json
{
  "keywords": [
    {"keyword": "machine", "score": 0.523456},
    {"keyword": "learning", "score": 0.489123}
  ],
  "count": 10,
  "extraction_time": 0.0234,
  "status": "success"
}
```

**Response (Error)**:
```json
{
  "error": "Error message here",
  "status": "error"
}
```

## Code Structure

### `app.py`
Main Flask application file containing:
- Flask app initialization
- CORS configuration
- API endpoint definitions
- Request/response handling

### `keyword_extractor.py`
Core keyword extraction module containing:
- `KeywordExtractor` class
- `preprocess_text()` method: Text preprocessing pipeline
- `extract_keywords()` method: TF-IDF based keyword extraction

## Preprocessing Pipeline

The text preprocessing follows these steps:

1. **Lowercasing**: Convert all text to lowercase
2. **Tokenization**: Split text into individual words/tokens
3. **Stopword Removal**: Remove common English stopwords (the, is, a, etc.)
4. **Lemmatization**: Convert words to their base/root form (running → run)

## TF-IDF Algorithm

**Term Frequency (TF)**: Frequency of a term in the document
```
TF(t, d) = (Number of times term t appears in document d) / (Total number of terms in document d)
```

**Inverse Document Frequency (IDF)**: Measure of how rare/common a term is
```
IDF(t) = log(Total number of documents / Number of documents containing term t)
```

**TF-IDF Score**: 
```
TF-IDF(t, d) = TF(t, d) × IDF(t)
```

Higher TF-IDF scores indicate terms that are:
- Frequent in the document (high TF)
- Rare across the corpus (high IDF)
- Therefore, more important/keyword-like

## Testing the API

### Using cURL:
```bash
curl -X POST http://localhost:5000/api/extract-keywords \
  -H "Content-Type: application/json" \
  -d '{"text": "Machine learning is a subset of artificial intelligence", "top_n": 5}'
```

### Using Python:
```python
import requests

url = "http://localhost:5000/api/extract-keywords"
data = {
    "text": "Machine learning is a subset of artificial intelligence",
    "top_n": 5
}
response = requests.post(url, json=data)
print(response.json())
```

## Error Handling

The API handles the following error cases:
- Empty text input
- Missing text parameter
- Invalid top_n value
- Server errors during processing

## Notes

- The API runs on port 5000 by default
- CORS is enabled to allow frontend communication
- Debug mode is enabled for development
- NLTK data is automatically downloaded on first run


