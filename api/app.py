#  flask used to create your web application  
#  request used to access data sent in http requests 
#   jsonify coverts data to json format for response 
#   pickle  used for loading machine learning model 
#   os used to manipulate with os for file operations 
# api/app.py
# Importing necessary modules
from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS for handling cross-origin requests
import pickle
import os

app = Flask(__name__)

# Enable CORS for the /predict route only from http://localhost:3000
CORS(app, resources={r"/predict": {"origins": "*"}})

# Load the model and vectorizer
model_path = os.path.join('model', 'model.pkl')
with open(model_path, 'rb') as f:
    vectorizer, model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    review = data['review']
    features = vectorizer.transform([review])
    prediction = model.predict(features)
    sentiment = 'positive' if prediction[0] == 1 else 'negative'
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    # Run the app on all available IPs on port 5000
    app.run(debug=True, host='0.0.0.0', port=5000)
