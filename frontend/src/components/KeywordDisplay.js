import React from 'react';
import './KeywordDisplay.css';

const KeywordDisplay = ({ keywords }) => {
  if (!keywords || keywords.length === 0) {
    return null;
  }

  // Calculate max score for normalization (for visual representation)
  const maxScore = Math.max(...keywords.map(k => k.score));

  return (
    <div className="keyword-display">
      <div className="keywords-grid">
        {keywords.map((item, index) => {
          // Calculate opacity based on score (higher score = more opaque)
          const opacity = 0.6 + (item.score / maxScore) * 0.4;
          
          return (
            <div
              key={index}
              className="keyword-card"
              style={{ opacity }}
            >
              <span className="keyword-rank">#{index + 1}</span>
              <span className="keyword-text">{item.keyword}</span>
              <span className="keyword-score">{item.score.toFixed(4)}</span>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default KeywordDisplay;


