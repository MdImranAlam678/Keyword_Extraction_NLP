# Quick Start Guide - TF-IDF Keyword Extraction

## 🚀 Get Started in 5 Minutes

### Step 1: Backend Setup (Terminal 1)

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

✅ Backend running at `http://localhost:5000`

### Step 2: Frontend Setup (Terminal 2)

```bash
cd frontend
npm install
npm start
```

✅ Frontend running at `http://localhost:3000`

### Step 3: Use the Application

1. Open `http://localhost:3000` in your browser
2. Enter text in the textarea
3. Click "Extract Keywords (TF-IDF)"
4. View results!

## 📝 Sample Text to Test

```
Machine learning is a subset of artificial intelligence that focuses on the 
development of algorithms and statistical models that enable computer systems 
to improve their performance on a specific task through experience.
```

## ✅ Verify Installation

### Backend Test
```bash
curl http://localhost:5000/api/health
```

Expected: `{"status": "healthy", "message": "TF-IDF Keyword Extraction API is running"}`

### Frontend Test
- Open browser to `http://localhost:3000`
- You should see the keyword extraction interface

## 🐛 Common Issues

**Backend won't start?**
- Check Python version: `python3 --version` (need 3.8+)
- Activate virtual environment
- Install dependencies: `pip install -r requirements.txt`

**Frontend won't start?**
- Check Node version: `node --version` (need 14+)
- Install dependencies: `npm install`
- Clear cache: `npm cache clean --force`

**Can't connect to backend?**
- Make sure backend is running on port 5000
- Check browser console for errors
- Verify CORS is enabled in backend

## 📚 Need More Help?

- See [README.md](README.md) for full documentation
- See [INTEGRATION_GUIDE.md](INTEGRATION_GUIDE.md) for detailed setup
- See [API_DOCUMENTATION.md](API_DOCUMENTATION.md) for API details


