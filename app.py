#################################################
# Import Dependencies
#################################################

import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import numpy as np
import pickle

from flask import Flask, jsonify, request, render_template

#################################################
# Database Setup
#################################################



#################################################
# Flask Setup
#################################################

app = Flask(__name__)
model = pickle.load(open('rf_model.pkl','rb'))

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    """All available api routes"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0],2)

    return render_template('index.html', prediction_text='Home Value should be $ {}'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = requests.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)
    
if __name__==  '__main__':
    app.run(debug=True)

