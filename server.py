from flask import Flask
import pickle
from flask import request
from flask_socketio import SocketIO
from flask_cors import CORS, cross_origin
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
import re

def preprocess(text):
    text = text.lower()
    text = re.sub('[^a-zA-Z]',' ',text)
    return text


app = Flask(__name__)

model = pickle.load(open('model_covid.pkl','rb'))



@app.route("/")
@cross_origin()
def hello():
    return "Hello, World!"

@app.route('/submit',methods=['POST'])
@cross_origin()
def submit_model():
	datas = request.get_json()
	msg= datas['msg']
	ans = model.predict([msg])
	return ans[0]



if __name__ == '__main__':
    app.run(host='127.0.0.1',port=4455,debug=True) 
