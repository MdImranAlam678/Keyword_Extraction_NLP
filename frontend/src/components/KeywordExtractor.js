import React, { useState } from 'react';
import axios from 'axios';
import './KeywordExtractor.css';
import LoadingSpinner from './LoadingSpinner';
import KeywordDisplay from './KeywordDisplay';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

const KeywordExtractor = () => {
  const [text, setText] = useState('');
  const [topN, setTopN] = useState(10);
  const [keywords, setKeywords] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [extractionTime, setExtractionTime] = useState(null);
  const [count, setCount] = useState(0);

  const handleExtract = async () => {
    // Validate input
    if (!text.trim()) {
      setError('Please enter some text to extract keywords.');
      return;
    }

    // Reset states
    setError('');
    setKeywords([]);
    setLoading(true);
    setExtractionTime(null);
    setCount(0);

    try {
      const response = await axios.post(`${API_URL}/api/extract-keywords`, {
        text: text,
        top_n: parseInt(topN) || 10
      });

      if (response.data.status === 'success') {
        setKeywords(response.data.keywords);
        setCount(response.data.count);
        setExtractionTime(response.data.extraction_time);
      } else {
        setError(response.data.error || 'Failed to extract keywords');
      }
    } catch (err) {
      if (err.response) {
        setError(err.response.data.error || 'Server error occurred');
      } else if (err.request) {
        setError('Unable to connect to server. Please make sure the backend is running.');
      } else {
        setError('An unexpected error occurred');
      }
    } finally {
      setLoading(false);
    }
  };

  const handleDownload = () => {
    if (keywords.length === 0) return;

    const content = keywords.map(k => `${k.keyword} (Score: ${k.score})`).join('\n');
    const blob = new Blob([content], { type: 'text/plain' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'extracted_keywords.txt';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    window.URL.revokeObjectURL(url);
  };

  const handleCopy = () => {
    if (keywords.length === 0) return;

    const content = keywords.map(k => k.keyword).join(', ');
    navigator.clipboard.writeText(content).then(() => {
      alert('Keywords copied to clipboard!');
    }).catch(() => {
      alert('Failed to copy to clipboard');
    });
  };

  return (
    <div className="keyword-extractor">
      <div className="extractor-container">
        {/* Input Section */}
        <div className="input-section">
          <label htmlFor="text-input" className="input-label">
            Enter Text for Keyword Extraction
          </label>
          <textarea
            id="text-input"
            className="text-input"
            placeholder="Paste or type your text here... For example: Machine learning is a subset of artificial intelligence that focuses on the development of algorithms and statistical models that enable computer systems to improve their performance on a specific task through experience."
            value={text}
            onChange={(e) => setText(e.target.value)}
            rows="8"
          />
          
          <div className="controls-row">
            <div className="top-n-control">
              <label htmlFor="top-n">Top N Keywords:</label>
              <input
                id="top-n"
                type="number"
                min="1"
                max="50"
                value={topN}
                onChange={(e) => setTopN(e.target.value)}
                className="top-n-input"
              />
            </div>
            
            <button
              className="extract-button"
              onClick={handleExtract}
              disabled={loading || !text.trim()}
            >
              {loading ? 'Extracting...' : '🔍 Extract Keywords (TF-IDF)'}
            </button>
          </div>
        </div>

        {/* Error Display */}
        {error && (
          <div className="error-message">
            <span className="error-icon">⚠️</span>
            {error}
          </div>
        )}

        {/* Loading Spinner */}
        {loading && <LoadingSpinner />}

        {/* Results Section */}
        {!loading && keywords.length > 0 && (
          <div className="results-section">
            <div className="results-header">
              <h2 className="results-title">Extracted Keywords</h2>
              <div className="results-stats">
                <span className="stat-item">
                  <strong>Count:</strong> {count}
                </span>
                {extractionTime && (
                  <span className="stat-item">
                    <strong>Time:</strong> {extractionTime}s
                  </span>
                )}
              </div>
            </div>

            <KeywordDisplay keywords={keywords} />

            <div className="action-buttons">
              <button
                className="action-button download-button"
                onClick={handleDownload}
              >
                📥 Download as .txt
              </button>
              <button
                className="action-button copy-button"
                onClick={handleCopy}
              >
                📋 Copy Keywords
              </button>
            </div>
          </div>
        )}

        {/* Empty State */}
        {!loading && keywords.length === 0 && !error && text.trim() && (
          <div className="empty-state">
            <p>Click "Extract Keywords" to see results</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default KeywordExtractor;


