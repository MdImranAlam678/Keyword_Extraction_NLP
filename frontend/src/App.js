import React from "react";
import "./App.css";
import KeywordExtractor from "./components/KeywordExtractor";

function App() {
  return (
    <div className="App">
      <header className="app-header">
        <h1 className="app-title">🔍 TF-IDF Keyword Extraction</h1>
        <p className="app-subtitle">
          Extract important keywords from your text using Term Frequency-Inverse
          Document Frequency
        </p>
      </header>
      <main className="app-main">
        <KeywordExtractor />
      </main>
      <footer className="app-footer">
        <p>NLP Micro-Project | TF-IDF Keyword Extraction</p>
      </footer>
    </div>
  );
}

export default App;
