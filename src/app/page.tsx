// frontend/pages/index.js
"use client";
import axios from "axios";
import { useState } from "react";

export default function Home() {
  const [review, setReview] = useState('');
  const [sentiment, setSentiment] = useState(null);
  console.log('API URL:', process.env.NEXT_PUBLIC_API_URL);

  const handlePredict = async () => {
    try {
      const response = await axios.post(`${process.env.NEXT_PUBLIC_API_URL}/predict`, { review });
      setSentiment(response.data.sentiment);
    } catch (error: any) {
      if (error.response) {
        console.error("Server Error:", error.response.data);
      } else if (error.request) {
        console.error("Network Error:", error.message);
      } else {
        console.error("Error:", error.message);
      }
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <div className="bg-white p-8 rounded-lg shadow-lg max-w-md w-full">
        <h1 className="text-2xl font-bold mb-6 text-center text-gray-800">AI Sentiment Analysis</h1>
        <input
          type="text"
          value={review}
          onChange={(e) => setReview(e.target.value)}
          placeholder="Enter movie review"
          className="w-full p-3 border border-gray-300 rounded-lg mb-4"
        />
        <button
          onClick={handlePredict}
          className="w-full bg-blue-500 text-white p-3 rounded-lg hover:bg-blue-600 transition"
        >
          Predict
        </button>
        {sentiment && (
          <p className="mt-4 text-center text-lg text-gray-700">
            Sentiment: <span className={`font-bold ${sentiment === 'positive' ? 'text-green-500' : 'text-red-500'}`}>{sentiment}</span>
          </p>
        )}
      </div>
    </div>
  );
}
