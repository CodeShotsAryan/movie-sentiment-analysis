#  flask used to create your web application  
#  request used to access data sent in http requests 
#   jsonify coverts data to json format for response 
#   pickle  used for loading machine learning model 
#   os used to manipulate with os for file operations 
# api/app.py

from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)

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
    app.run(debug=True)
