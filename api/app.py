#  flask used to create your web application  
#  request used to access data sent in http requests 
#   jsonify coverts data to json format for response 
#   pickle  used for loading machine learning model 
#   os used to manipulate with os for file operations 
from flask import Flask , request , jsonify  
import pickle 
import os

app = Flask(__name__) 

#load the machine learning model 

model_path = os.path.join('model','model.pkl')
with open(model_path,'rb') as f :
    model = pickle.load(f)

# define prediciton endpoints ok ?
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = data['features']
    prediction = model.predict([features])
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)