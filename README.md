# TF-IDF Keyword Extraction - NLP Micro-Project

A complete full-stack web application for extracting keywords from text using the Term Frequency-Inverse Document Frequency (TF-IDF) algorithm. This project is designed for academic submission and demonstrates practical implementation of NLP concepts.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
- [Documentation](#documentation)
- [Screenshots](#screenshots)
- [Algorithm Explanation](#algorithm-explanation)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project implements a complete keyword extraction system that:
- Accepts text input from users
- Preprocesses the text (lowercasing, tokenization, stopword removal, lemmatization)
- Calculates TF-IDF scores for each term
- Extracts and ranks the top N keywords
- Displays results in a modern, user-friendly interface

## ✨ Features

### Backend Features
- ✅ RESTful API using Flask
- ✅ TF-IDF keyword extraction algorithm
- ✅ Comprehensive text preprocessing pipeline
- ✅ Error handling and validation
- ✅ CORS support for frontend integration

### Frontend Features
- ✅ Modern, responsive React UI
- ✅ Real-time keyword extraction
- ✅ Loading animations
- ✅ Error handling and validation
- ✅ Download keywords as .txt file
- ✅ Copy keywords to clipboard
- ✅ Configurable number of keywords (Top N)
- ✅ Display extraction time and keyword count

## 🛠 Technology Stack

### Backend
- **Python 3.8+**
- **Flask 3.0.0** - Web framework
- **scikit-learn 1.3.2** - TF-IDF vectorization
- **NLTK 3.8.1** - Text preprocessing
- **flask-cors 4.0.0** - CORS handling

### Frontend
- **React 18.2.0** - UI framework
- **Axios 1.6.0** - HTTP client
- **CSS3** - Styling (Flexbox, Grid)

## 📁 Project Structure

```
keywordExtractionNLP/
├── backend/
│   ├── app.py                    # Flask application
│   ├── keyword_extractor.py     # TF-IDF implementation
│   ├── requirements.txt          # Python dependencies
│   └── README.md                 # Backend documentation
│
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── KeywordExtractor.js
│   │   │   ├── KeywordDisplay.js
│   │   │   └── LoadingSpinner.js
│   │   ├── App.js
│   │   └── index.js
│   ├── package.json
│   └── README.md                 # Frontend documentation
│
├── INTEGRATION_GUIDE.md          # Integration instructions
├── API_DOCUMENTATION.md          # API reference
├── ARCHITECTURE.md               # System architecture
├── ACADEMIC_EXPLANATION.md       # Academic documentation
├── SAMPLE_INPUT_OUTPUT.md        # Sample examples
└── README.md                     # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Node.js 14.0 or higher
- npm or yarn

### Step 1: Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the server
python app.py
```

The backend will run on `http://localhost:5000`

### Step 2: Frontend Setup

Open a new terminal:

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start the development server
npm start
```

The frontend will open automatically at `http://localhost:3000`

### Step 3: Use the Application

1. Enter text in the textarea
2. Set the number of keywords (Top N)
3. Click "Extract Keywords (TF-IDF)"
4. View the extracted keywords with their scores
5. Download or copy the keywords as needed

## 📚 Documentation

### Detailed Documentation Files

1. **[Backend README](backend/README.md)** - Backend setup and API details
2. **[Frontend README](frontend/README.md)** - Frontend setup and features
3. **[Integration Guide](INTEGRATION_GUIDE.md)** - Complete integration instructions
4. **[API Documentation](API_DOCUMENTATION.md)** - Complete API reference
5. **[Architecture](ARCHITECTURE.md)** - System architecture and diagrams
6. **[Academic Explanation](ACADEMIC_EXPLANATION.md)** - Academic documentation
7. **[Sample Input/Output](SAMPLE_INPUT_OUTPUT.md)** - Example inputs and outputs

## 🔬 Algorithm Explanation

### TF-IDF (Term Frequency-Inverse Document Frequency)

**Term Frequency (TF)**:
```
TF(t, d) = (Number of times term t appears in document d) / (Total number of terms in document d)
```

**Inverse Document Frequency (IDF)**:
```
IDF(t) = log(Total number of documents / Number of documents containing term t)
```

**TF-IDF Score**:
```
TF-IDF(t, d) = TF(t, d) × IDF(t)
```

### Preprocessing Pipeline

1. **Lowercasing**: Convert all text to lowercase
2. **Tokenization**: Split text into individual words
3. **Stopword Removal**: Remove common words (the, is, a, etc.)
4. **Lemmatization**: Convert words to base form (running → run)

### Time Complexity
- **Overall**: O(n + m × v + v log v)
  - n = number of characters
  - m = number of tokens
  - v = vocabulary size

### Space Complexity
- **Overall**: O(n + m + v)

## 🎨 Screenshots

### Main Interface
- Clean, modern design with gradient background
- Large text input area
- Responsive layout for all screen sizes

### Results Display
- Grid layout showing keyword cards
- Each card displays rank, keyword, and TF-IDF score
- Visual opacity based on score importance

## 📝 API Endpoints

### Health Check
```
GET http://localhost:5000/api/health
```

### Extract Keywords
```
POST http://localhost:5000/api/extract-keywords
Content-Type: application/json

Body:
{
  "text": "Your text here",
  "top_n": 10
}
```

See [API_DOCUMENTATION.md](API_DOCUMENTATION.md) for complete API reference.

## 🧪 Testing

### Test Backend
```bash
# Health check
curl http://localhost:5000/api/health

# Extract keywords
curl -X POST http://localhost:5000/api/extract-keywords \
  -H "Content-Type: application/json" \
  -d '{"text": "Machine learning is fascinating", "top_n": 5}'
```

### Test Frontend
1. Start both backend and frontend
2. Enter sample text
3. Verify keywords are extracted and displayed
4. Test download and copy functionality

## 🐛 Troubleshooting

### Backend Issues
- **ModuleNotFoundError**: Make sure virtual environment is activated and dependencies are installed
- **Port 5000 in use**: Change port in `app.py`
- **NLTK data missing**: Run `python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"`

### Frontend Issues
- **Cannot connect to backend**: Verify backend is running on port 5000
- **CORS errors**: Check that `flask-cors` is installed
- **npm install fails**: Clear cache with `npm cache clean --force`

See [INTEGRATION_GUIDE.md](INTEGRATION_GUIDE.md) for detailed troubleshooting.

## 📊 Use Cases

1. **Document Summarization**: Extract key terms from documents
2. **Content Tagging**: Automatically tag articles and blog posts
3. **SEO Optimization**: Identify important keywords for web content
4. **Academic Research**: Extract key terms from research papers
5. **Information Retrieval**: Improve search functionality

## 🎓 Academic Information

This project is designed for:
- **Subject**: Natural Language Processing (NLP)
- **Semester**: 7th Semester Computer Science Engineering
- **Technique**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Type**: Micro-Project

### Project Deliverables
- ✅ Complete backend implementation
- ✅ Complete frontend implementation
- ✅ API documentation
- ✅ Integration guide
- ✅ Architecture diagrams
- ✅ Academic explanation
- ✅ Sample input/output examples

## 🔮 Future Enhancements

- Multi-document TF-IDF
- N-gram keyword extraction (phrases)
- Support for multiple languages
- Advanced preprocessing (NER, POS tagging)
- Keyword visualization charts
- Batch processing
- API authentication

## 📄 License

This project is created for academic purposes.

## 👨‍💻 Author

7th Semester Computer Science Engineering Student

## 🙏 Acknowledgments

- scikit-learn for TF-IDF implementation
- NLTK for text preprocessing tools
- React and Flask communities

---

**Note**: This project uses only TF-IDF for keyword extraction. No other methods (RAKE, TextRank, etc.) are implemented, as per requirements.


