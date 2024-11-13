import React from 'react';
import { Pie, Bar } from 'react-chartjs-2';
import 'chart.js/auto';

const GraphSection = ({ sentimentData }) => {
  
  const sampleData = {
    positive: 120,
    neutral: 50,
    negative: 30,
  };

  const data = sentimentData || sampleData;

  
  const pieData = {
    labels: ['Positive', 'Neutral', 'Negative'],
    datasets: [
      {
        data: [data.positive, data.neutral, data.negative],
        backgroundColor: ['#36a2eb', '#ffcd56', '#ff6384'], 
        hoverBackgroundColor: ['#1e90ff', '#ffc107', '#ff4558'], 
      },
    ],
  };

  
  const barData = {
    labels: ['Positive', 'Neutral', 'Negative'],
    datasets: [
      {
        label: 'Sentiment Count',
        data: [data.positive, data.neutral, data.negative],
        backgroundColor: ['#36a2eb', '#ffcd56', '#ff6384'], 
      },
    ],
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.heading}>Sentiment Analysis Results</h1>
      <div style={styles.chartContainer}>
        <div style={styles.chart}>
          <Pie data={pieData} options={{ responsive: true }} />
        </div>
        <div style={styles.chart}>
          <Bar data={barData} options={{ responsive: true }} />
        </div>
      </div>
    </div>
  );
};

const styles = {
  container: {
    padding: '20px',
    backgroundColor: 'rgba(255, 255, 255, 0.8)', 
    borderRadius: '8px',
    boxShadow: '0 4px 10px rgba(0, 0, 0, 0.1)',
  },
  heading: {
    color: '#333',
    textAlign: 'center',
    marginBottom: '20px',
  },
  chartContainer: {
    display: 'flex',
    justifyContent: 'space-around',
  },
  chart: {
    width: '45%',
  },
};

export default GraphSection;