# System Architecture - TF-IDF Keyword Extraction

## 1. System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                         CLIENT LAYER                             │
│                                                                   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │              React Frontend Application                   │   │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │   │
│  │  │   Text Input │  │ Extract Btn  │  │  Results     │  │   │
│  │  │   Component  │  │  Component   │  │  Display     │  │   │
│  │  └──────────────┘  └──────────────┘  └──────────────┘  │   │
│  │                                                           │   │
│  │  ┌──────────────────────────────────────────────────┐    │   │
│  │  │         Axios HTTP Client                        │    │   │
│  │  └──────────────────────────────────────────────────┘    │   │
│  └──────────────────────────────────────────────────────────┘   │
│                          │                                       │
│                          │ HTTP/REST API                         │
│                          │ (JSON Request/Response)                │
└──────────────────────────┼───────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                        SERVER LAYER                             │
│                                                                   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │              Flask Backend Application                    │   │
│  │  ┌────────────────────────────────────────────────────┐  │   │
│  │  │              API Endpoints                          │  │   │
│  │  │  - GET  /api/health                                 │  │   │
│  │  │  - POST /api/extract-keywords                       │  │   │
│  │  └────────────────────────────────────────────────────┘  │   │
│  │                                                           │   │
│  │  ┌────────────────────────────────────────────────────┐  │   │
│  │  │         Request Handler & Validator                 │  │   │
│  │  └────────────────────────────────────────────────────┘  │   │
│  └──────────────────────────────────────────────────────────┘   │
│                          │                                       │
└──────────────────────────┼───────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                      PROCESSING LAYER                            │
│                                                                   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │         KeywordExtractor Class                           │   │
│  │                                                           │   │
│  │  ┌────────────────────────────────────────────────────┐  │   │
│  │  │     Preprocessing Pipeline                          │  │   │
│  │  │  1. Lowercasing                                     │  │   │
│  │  │  2. Tokenization (NLTK)                             │  │   │
│  │  │  3. Stopword Removal (NLTK)                         │  │   │
│  │  │  4. Lemmatization (NLTK)                            │  │   │
│  │  └────────────────────────────────────────────────────┘  │   │
│  │                                                           │   │
│  │  ┌────────────────────────────────────────────────────┐  │   │
│  │  │     TF-IDF Vectorization (scikit-learn)            │  │   │
│  │  │  - Term Frequency Calculation                       │  │   │
│  │  │  - Inverse Document Frequency Calculation          │  │   │
│  │  │  - TF-IDF Score Computation                         │  │   │
│  │  └────────────────────────────────────────────────────┘  │   │
│  │                                                           │   │
│  │  ┌────────────────────────────────────────────────────┐  │   │
│  │  │     Keyword Ranking & Selection                     │  │   │
│  │  │  - Sort by TF-IDF scores (descending)              │  │   │
│  │  │  - Extract top N keywords                           │  │   │
│  │  └────────────────────────────────────────────────────┘  │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

## 2. Data Flow Diagram (DFD)

### Level 0 (Context Diagram)

```
┌─────────────┐
│             │
│    User     │
│             │
└──────┬──────┘
       │
       │ Text Input
       │
       ▼
┌─────────────────────────────────────┐
│                                     │
│   TF-IDF Keyword Extraction System  │
│                                     │
└──────┬──────────────────────────────┘
       │
       │ Extracted Keywords
       │
       ▼
┌─────────────┐
│             │
│    User     │
│             │
└─────────────┘
```

### Level 1 (Process Decomposition)

```
┌─────────────┐
│             │
│    User     │
│             │
└──────┬──────┘
       │
       │ Text Input
       │
       ▼
┌─────────────────────┐
│  1.0                │
│  Frontend           │
│  (React)            │
└──────┬──────────────┘
       │
       │ HTTP POST Request
       │ (JSON: {text, top_n})
       │
       ▼
┌─────────────────────┐
│  2.0                │
│  Backend API        │
│  (Flask)            │
└──────┬──────────────┘
       │
       │ Preprocessed Text
       │
       ▼
┌─────────────────────┐
│  3.0                │
│  Text Preprocessing │
│  (NLTK)             │
└──────┬──────────────┘
       │
       │ Clean Tokens
       │
       ▼
┌─────────────────────┐
│  4.0                │
│  TF-IDF Calculation │
│  (scikit-learn)     │
└──────┬──────────────┘
       │
       │ TF-IDF Scores
       │
       ▼
┌─────────────────────┐
│  5.0                │
│  Keyword Ranking    │
│  & Selection        │
└──────┬──────────────┘
       │
       │ Top N Keywords
       │
       ▼
┌─────────────────────┐
│  2.0                │
│  Backend API        │
│  (Response)         │
└──────┬──────────────┘
       │
       │ HTTP Response
       │ (JSON: {keywords, count, time})
       │
       ▼
┌─────────────────────┐
│  1.0                │
│  Frontend           │
│  (Display Results)  │
└──────┬──────────────┘
       │
       │ Display Keywords
       │
       ▼
┌─────────────┐
│             │
│    User     │
│             │
└─────────────┘
```

## 3. Use Case Diagram

```
                    ┌─────────────────────────────┐
                    │                             │
                    │   Keyword Extraction        │
                    │   System                    │
                    │                             │
                    └─────────────────────────────┘
                              │
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        │                     │                     │
        ▼                     ▼                     ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│               │    │               │    │               │
│  Enter Text   │    │ Extract       │    │  View         │
│               │    │ Keywords      │    │  Keywords     │
│               │    │               │    │               │
└───────────────┘    └───────────────┘    └───────────────┘
        │                     │                     │
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              │
                              │
                    ┌─────────▼─────────┐
                    │                   │
                    │      User         │
                    │                   │
                    └───────────────────┘

Additional Use Cases:
┌─────────────────────┐
│  Download Keywords  │
│  (as .txt file)     │
└─────────────────────┘

┌─────────────────────┐
│  Copy Keywords      │
│  (to clipboard)     │
└─────────────────────┘

┌─────────────────────┐
│  Configure Top N    │
│  (number of keywords)│
└─────────────────────┘
```

## 4. Component Interaction Diagram

```
┌──────────────┐
│   React App  │
└──────┬───────┘
       │
       │ 1. User enters text
       │
       ▼
┌─────────────────────┐
│ KeywordExtractor    │
│ Component           │
└──────┬──────────────┘
       │
       │ 2. handleExtract()
       │
       ▼
┌─────────────────────┐
│  Axios HTTP Client   │
└──────┬───────────────┘
       │
       │ 3. POST /api/extract-keywords
       │    {text, top_n}
       │
       ▼
┌─────────────────────┐
│  Flask App          │
│  (app.py)           │
└──────┬──────────────┘
       │
       │ 4. extract_keywords()
       │
       ▼
┌─────────────────────┐
│ KeywordExtractor    │
│ Class               │
└──────┬──────────────┘
       │
       │ 5. preprocess_text()
       │
       ▼
┌─────────────────────┐
│  NLTK Preprocessing │
│  - Tokenization     │
│  - Stopword Removal │
│  - Lemmatization    │
└──────┬──────────────┘
       │
       │ 6. Preprocessed text
       │
       ▼
┌─────────────────────┐
│  TF-IDF Vectorizer  │
│  (scikit-learn)     │
└──────┬──────────────┘
       │
       │ 7. TF-IDF scores
       │
       ▼
┌─────────────────────┐
│  Keyword Ranking    │
│  & Selection        │
└──────┬──────────────┘
       │
       │ 8. Top N keywords
       │
       ▼
┌─────────────────────┐
│  Flask Response     │
│  {keywords, count,  │
│   time, status}     │
└──────┬──────────────┘
       │
       │ 9. HTTP Response
       │
       ▼
┌─────────────────────┐
│  React Component    │
│  Updates State      │
└──────┬──────────────┘
       │
       │ 10. Display Results
       │
       ▼
┌─────────────────────┐
│  KeywordDisplay     │
│  Component          │
└─────────────────────┘
```

## 5. Database Schema

**Note**: This system does not use a database. All processing is done in-memory.

## 6. Technology Stack

### Frontend

- **React 18.2.0**: UI framework
- **Axios 1.6.0**: HTTP client
- **CSS3**: Styling

### Backend

- **Flask 3.0.0**: Web framework
- **flask-cors 4.0.0**: CORS handling
- **scikit-learn 1.3.2**: TF-IDF vectorization
- **NLTK 3.8.1**: Text preprocessing
- **NumPy 1.24.3**: Numerical operations

## 7. Deployment Architecture

### Development Environment

```
┌──────────────┐         ┌──────────────┐
│   Browser    │────────▶│   React Dev  │
│              │         │   Server     │
│  localhost:  │         │  localhost:  │
│    3000      │         │    3000      │
└──────────────┘         └──────┬───────┘
                                │
                                │ API Calls
                                │
                                ▼
                        ┌──────────────┐
                        │  Flask Dev   │
                        │   Server     │
                        │  localhost:  │
                        │    5000      │
                        └──────────────┘
```

### Production Environment

```
┌──────────────┐         ┌──────────────┐
│   Browser    │────────▶│   Nginx/     │
│              │         │   Apache     │
│  https://    │         │   (Static)   │
│  domain.com  │         └──────────────┘
└──────────────┘
                                │
                                │ API Calls
                                │
                                ▼
                        ┌──────────────┐
                        │  Gunicorn/   │
                        │  uWSGI       │
                        │  (WSGI)      │
                        └──────┬───────┘
                                │
                                ▼
                        ┌──────────────┐
                        │  Flask App   │
                        │  (Backend)   │
                        └──────────────┘
```

