#  flask used to create your web application  
#  request used to access data sent in http requests 
#   jsonify coverts data to json format for response 
#   pickle  used for loading machine learning model 
from flask import Flask , request , jsonify  
import pickle 
import os

app = Flask(__name__)
