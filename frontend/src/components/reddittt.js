import React from 'react';

function AnalyzeButton({ onClick }) {
  return (
    <button onClick={onClick} style={{ padding: '10px 20px', margin: '10px 0' }}>
      Analyze Sentiment
    </button>
  );
}

export default AnalyzeButton;