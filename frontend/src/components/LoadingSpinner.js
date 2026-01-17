import React from 'react';
import './LoadingSpinner.css';

const LoadingSpinner = () => {
  return (
    <div className="loading-container">
      <div className="spinner"></div>
      <p className="loading-text">Processing text with TF-IDF algorithm...</p>
    </div>
  );
};

export default LoadingSpinner;


