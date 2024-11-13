import React from 'react';
import GraphSection from './GraphSection';

function ResultDisplay({ sentiment, confidence }) {
  return (
    <div>
      <h3>Sentiment: {sentiment || 'N/A'}</h3>
      <h3>Confidence Score: {confidence || 'N/A'}</h3>
        {/* Add GraphSection here */}
        <GraphSection sentimentData={{ positive: 120, neutral: 50, negative: 30 }} />
    </div>
  );
}

export default ResultDisplay;