import React, { useState } from 'react';
import './App.css';
import ResultDisplay from './components/ResultDisplay';
function App() {
  const [subreddit, setSubreddit] = useState('');
  const [keyword, setKeyword] = useState('');
  const [sentiment, setSentiment] = useState('');
  const [confidence, setConfidence] = useState('');

  const handleAnalyze = () => {
  
    setSentiment('Positive');
    setConfidence('0.85');
  };

  return (
    <div className="app-container">
      <video autoPlay loop muted className="background-video">
        <source src="https://videos.pexels.com/video-files/3248991/3248991-uhd_2560_1440_25fps.mp4" type="video/mp4" />
      </video>

      <div className="content">
        <h1>CrowdPulse: Reddit Sentiment Analysis</h1>
        <p>
        Explore Reddit sentiment in real-time. Enter keywords or subreddit names to see insights on user opinions, analyzed through VADER sentiment scores, comment length, and upvote counts. Powered by machine learning, CrowdPulse provides accurate sentiment predictions and interactive visualizations. </p>

        <div className="input-container">
          <input
            type="text"
            placeholder="Enter subreddit name"
            value={subreddit}
            onChange={(e) => setSubreddit(e.target.value)}
          />
          <input
            type="text"
            placeholder="Enter keyword"
            value={keyword}
            onChange={(e) => setKeyword(e.target.value)}
          />
        </div>

        <button className="analyze-button" onClick={handleAnalyze}>
          Run Analysis
        </button>

        <div className="result-display">


          {/* Display result and graphs */}
          <ResultDisplay sentiment={sentiment} confidence={confidence} />
        </div>
      </div>
    </div>
  );
}

export default App;