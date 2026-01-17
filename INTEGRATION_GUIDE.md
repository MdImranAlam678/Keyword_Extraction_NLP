# Integration Guide - TF-IDF Keyword Extraction

## Overview

This guide explains how to integrate and run the complete TF-IDF Keyword Extraction system, including both backend and frontend components.

## System Architecture

```
┌─────────────────┐         HTTP/REST API         ┌─────────────────┐
│                 │  ───────────────────────────>  │                 │
│   React         │                                │   Flask         │
│   Frontend      │  <───────────────────────────  │   Backend       │
│   (Port 3000)   │         JSON Response          │   (Port 5000)   │
│                 │                                │                 │
└─────────────────┘                                └─────────────────┘
                                                           │
                                                           │
                                                           ▼
                                                  ┌─────────────────┐
                                                  │  TF-IDF         │
                                                  │  Processor      │
                                                  │  (NLTK,         │
                                                  │   scikit-learn) │
                                                  └─────────────────┘
```

## Prerequisites

### Backend Requirements

- Python 3.8 or higher
- pip (Python package manager)

### Frontend Requirements

- Node.js 14.0 or higher
- npm or yarn package manager

## Step-by-Step Setup

### Step 1: Backend Setup

1. **Navigate to backend directory**:

```bash
cd backend
```

2. **Create virtual environment** (recommended):

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Start the backend server**:

```bash
python app.py
```

5. **Verify backend is running**:
   - Open browser: `http://localhost:5000/api/health`
   - Should see: `{"status": "healthy", "message": "TF-IDF Keyword Extraction API is running"}`

### Step 2: Frontend Setup

1. **Open a new terminal window**

2. **Navigate to frontend directory**:

```bash
cd frontend
```

3. **Install dependencies**:

```bash
npm install
```

4. **Start the frontend development server**:

```bash
npm start
```

5. **The application will automatically open** at `http://localhost:3000`

### Step 3: Verify Integration

1. **Backend should be running** on `http://localhost:5000`
2. **Frontend should be running** on `http://localhost:3000`
3. **Test the application**:
   - Enter some text in the textarea
   - Click "Extract Keywords (TF-IDF)"
   - Verify keywords are displayed

## API Configuration

### Default Configuration

- **Backend URL**: `http://localhost:5000`
- **Frontend URL**: `http://localhost:3000`

### Changing API URL

If your backend runs on a different URL/port:

1. **Create `.env` file** in `frontend/` directory:

```
REACT_APP_API_URL=http://your-backend-url:port
```

2. **Restart the frontend server**

## CORS Configuration

CORS (Cross-Origin Resource Sharing) is already configured in the backend:

```python
from flask_cors import CORS
app = Flask(__name__)
CORS(app)  # Allows requests from frontend
```

This allows the React frontend (running on port 3000) to communicate with the Flask backend (running on port 5000).

## API Endpoints

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

## Troubleshooting

### Backend Issues

**Problem**: `ModuleNotFoundError` or import errors

- **Solution**: Make sure virtual environment is activated and all dependencies are installed

**Problem**: Port 5000 already in use

- **Solution**: Change port in `app.py`:
  ```python
  app.run(debug=True, host='0.0.0.0', port=5001)  # Change to 5001
  ```

**Problem**: NLTK data not found

- **Solution**: Run:
  ```python
  python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
  ```

### Frontend Issues

**Problem**: `npm install` fails

- **Solution**: Clear npm cache: `npm cache clean --force` and try again

**Problem**: Cannot connect to backend

- **Solution**:
  1. Verify backend is running
  2. Check API URL in `.env` file
  3. Check browser console for CORS errors

**Problem**: Port 3000 already in use

- **Solution**: React will prompt to use a different port, or set:
  ```bash
  PORT=3001 npm start
  ```

### Integration Issues

**Problem**: CORS errors in browser console

- **Solution**: Verify `flask-cors` is installed and `CORS(app)` is called in `app.py`

**Problem**: API returns 404

- **Solution**: Check that backend endpoint URL matches frontend API calls

## Production Deployment

### Backend Deployment

1. **Disable debug mode** in `app.py`:

```python
app.run(debug=False, host='0.0.0.0', port=5000)
```

2. **Use production WSGI server** (e.g., Gunicorn):

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Frontend Deployment

1. **Build production bundle**:

```bash
cd frontend
npm run build
```

2. **Serve the `build/` folder** using:

   - Nginx
   - Apache
   - Any static file server

3. **Update API URL** in production environment

## Testing the Complete System

### Manual Testing Steps

1. **Start backend**: `cd backend && python app.py`
2. **Start frontend**: `cd frontend && npm start`
3. **Test with sample text**:
   ```
   Machine learning is a subset of artificial intelligence that focuses on
   the development of algorithms and statistical models that enable computer
   systems to improve their performance on a specific task through experience.
   ```
4. **Verify**:
   - Keywords are extracted
   - Scores are displayed
   - Download works
   - Copy works
   - Loading animation appears
   - Error handling works (try empty text)

## Network Configuration

### Local Development

- Backend: `http://localhost:5000`
- Frontend: `http://localhost:3000`
- No additional configuration needed

### Remote Access

- Backend: `http://your-ip:5000`
- Frontend: `http://your-ip:3000`
- Update `.env` file with backend IP address

## Security Considerations

1. **CORS**: Currently allows all origins (for development). In production, restrict to specific domains:

   ```python
   CORS(app, resources={r"/api/*": {"origins": "https://yourdomain.com"}})
   ```

2. **Input Validation**: Backend validates input, but consider adding:

   - Maximum text length limits
   - Rate limiting
   - Input sanitization

3. **Error Messages**: Avoid exposing internal errors to frontend in production

## Support

For issues or questions:

1. Check backend logs in terminal
2. Check browser console for frontend errors
3. Verify all dependencies are installed
4. Ensure both servers are running
