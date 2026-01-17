# Frontend - TF-IDF Keyword Extraction

## Overview
A modern, responsive React application for extracting keywords from text using TF-IDF technique. The frontend communicates with the Flask backend API to process text and display extracted keywords.

## Technology Stack
- **Framework**: React 18.2.0
- **HTTP Client**: Axios 1.6.0
- **Styling**: CSS3 with Flexbox and Grid
- **Build Tool**: Create React App

## Installation

### Prerequisites
- Node.js 14.0 or higher
- npm or yarn package manager

### Steps

1. **Navigate to frontend directory**:
```bash
cd frontend
```

2. **Install dependencies**:
```bash
npm install
```

## Running the Frontend

1. **Start the development server**:
```bash
npm start
```

2. **The application will open automatically at**:
```
http://localhost:3000
```

3. **Make sure the backend is running** on `http://localhost:5000`

## Configuration

### API URL
The frontend connects to the backend API. By default, it uses:
```
http://localhost:5000
```

To change the API URL, create a `.env` file in the frontend directory:
```
REACT_APP_API_URL=http://your-backend-url:port
```

## Features

### 1. Text Input
- Large textarea for entering text
- Placeholder text with example
- Real-time input validation

### 2. Keyword Extraction
- "Extract Keywords (TF-IDF)" button
- Configurable "Top N" keywords (1-50)
- Loading animation during processing

### 3. Results Display
- Grid layout showing extracted keywords
- Each keyword card displays:
  - Rank (#1, #2, etc.)
  - Keyword text
  - TF-IDF score
- Visual opacity based on score (higher score = more prominent)

### 4. Statistics
- Count of extracted keywords
- Extraction time in seconds

### 5. Actions
- **Download**: Save keywords as .txt file
- **Copy**: Copy keywords to clipboard

### 6. Error Handling
- Empty input validation
- Server connection errors
- API error messages
- User-friendly error display

## Project Structure

```
frontend/
├── public/
│   └── index.html
├── src/
│   ├── components/
│   │   ├── KeywordExtractor.js      # Main component
│   │   ├── KeywordExtractor.css
│   │   ├── KeywordDisplay.js         # Keywords display component
│   │   ├── KeywordDisplay.css
│   │   ├── LoadingSpinner.js         # Loading animation
│   │   └── LoadingSpinner.css
│   ├── App.js                        # Root component
│   ├── App.css
│   ├── index.js                      # Entry point
│   └── index.css                     # Global styles
├── package.json
└── README.md
```

## Component Details

### KeywordExtractor
Main component that handles:
- Text input state
- API calls to backend
- Error handling
- Download and copy functionality

### KeywordDisplay
Displays extracted keywords in a grid layout with:
- Rank indicators
- Keyword text
- TF-IDF scores
- Visual styling based on score

### LoadingSpinner
Shows animated spinner during API processing.

## API Integration

The frontend makes POST requests to:
```
POST http://localhost:5000/api/extract-keywords
```

Request body:
```json
{
  "text": "Input text",
  "top_n": 10
}
```

Response:
```json
{
  "keywords": [
    {"keyword": "word", "score": 0.123}
  ],
  "count": 10,
  "extraction_time": 0.0234,
  "status": "success"
}
```

## Building for Production

1. **Build the production bundle**:
```bash
npm run build
```

2. **The build folder will contain optimized production files**

3. **Serve the build folder** using any static file server:
```bash
# Using serve
npx serve -s build

# Using Python
cd build && python -m http.server 8000
```

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Responsive Design

The application is fully responsive and works on:
- Desktop (1920px+)
- Tablet (768px - 1024px)
- Mobile (320px - 767px)

## Notes

- The frontend uses functional components with React Hooks
- Axios is used for HTTP requests
- CSS is used for styling (no external UI libraries)
- The design is modern and clean, suitable for academic submission


