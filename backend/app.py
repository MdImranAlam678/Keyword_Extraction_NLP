"""
Flask Backend for TF-IDF Keyword Extraction
Main application file with API endpoints
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import time
from keyword_extractor import KeywordExtractor

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Initialize keyword extractor
extractor = KeywordExtractor()


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "message": "TF-IDF Keyword Extraction API is running"})


@app.route('/api/extract-keywords', methods=['POST'])
def extract_keywords():
    """
    Main endpoint for keyword extraction using TF-IDF
    
    Request Body:
        {
            "text": "Input text string",
            "top_n": 10 (optional, default: 10)
        }
    
    Returns:
        {
            "keywords": [{"keyword": "word", "score": 0.123}],
            "count": 10,
            "extraction_time": 0.045,
            "status": "success"
        }
    """
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Validate input
        if not data:
            return jsonify({
                "error": "No data provided",
                "status": "error"
            }), 400
        
        text = data.get('text', '').strip()
        top_n = data.get('top_n', 10)
        
        # Check if text is empty
        if not text:
            return jsonify({
                "error": "Text input is empty",
                "status": "error"
            }), 400
        
        # Validate top_n
        if not isinstance(top_n, int) or top_n <= 0:
            top_n = 10
        
        # Record start time
        start_time = time.time()
        
        # Extract keywords using TF-IDF
        keywords = extractor.extract_keywords(text, top_n=top_n)
        
        # Calculate extraction time
        extraction_time = round(time.time() - start_time, 4)
        
        # Prepare response
        response = {
            "keywords": keywords,
            "count": len(keywords),
            "extraction_time": extraction_time,
            "status": "success"
        }
        
        return jsonify(response), 200
        
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500


if __name__ == '__main__':
    print("Starting TF-IDF Keyword Extraction API...")
    print("API will be available at http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)


