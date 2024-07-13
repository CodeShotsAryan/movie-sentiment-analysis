"use client"

import { useState } from 'react';
import axios from 'axios';

export default function Home() {
  const [review, setReview] = useState('');
  const [sentiment, setSentiment] = useState(null);
  console.log('API URL:', process.env.NEXT_PUBLIC_API_URL);

  const handlePredict = async () => {
    try {
      const response = await axios.post(`${process.env.NEXT_PUBLIC_API_URL}/predict`, { review });
      setSentiment(response.data.sentiment);
    } catch (error: any) {  // Explicitly typing error as 'any'
      if (error.response) {
        // Server responded with a status other than 200 range
        console.error("Server Error:", error.response.data);
      } else if (error.request) {
        // Request was made but no response received
        console.error("Network Error:", error.message);
      } else {
        // Something else happened while setting up the request
        console.error("Error:", error.message);
      }
    }
  };

  return (
    <div>
      <h1>AI Sentiment Analysis</h1>
      <input
        type="text"
        value={review}
        onChange={(e) => setReview(e.target.value)}
        placeholder="Enter movie review"
      />
      <button onClick={handlePredict}>Predict</button>
      {sentiment && <p>Sentiment: {sentiment}</p>}
    </div>
  );
}
