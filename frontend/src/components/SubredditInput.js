import React from 'react';

function SubredditInput({ value, onChange }) {
  return (
    <div>
      <label>Enter a subreddit name:</label>
      <input
        type="text"
        value={value}
        onChange={onChange}
        placeholder="e.g., AskReddit"
        style={{ width: '100%', padding: '10px', margin: '10px 0' }}
      />
    </div>
  );
}

export default SubredditInput;