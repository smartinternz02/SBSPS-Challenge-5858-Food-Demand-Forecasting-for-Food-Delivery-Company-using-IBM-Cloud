import pandas as pd
import numpy as np
import pickle
import os
from flask import Flask, request, render_template

app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = '2ece243aa5bfad295dca55d8b38cdbcd'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/home', methods=['GET'])
def about():
    return render_template('index.html')

@app.route('/pred', methods=['GET'])
def upload():
    return render_template('upload.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    print("[INFO] loading model...")

    with open("fdemand.pkl", "rb") as f:
        model = pickle.load(f)
    #model = pickle.load(open('fdemand.pkl', "rb").read())

    # make sure POST request
    if request.method == 'POST':
        y = request.form.values()
        input_features = []
        print(y)
        for x in y:
            if x.isnumeric():
                print(x)
                input_features.append(float(x))
        #input_features = [float(x) for x in y]
        print(input_features)
        features_value = [np.array(input_features)]
        print(features_value)
        features_name = ['homepage_featured', 'emailer_for_promotion', 'op_area', 'cuisine', 
        'city_code', 'region_code', 'category']
        prediction = model.predict(features_value)
        output = prediction[0]
        print(output)
        return render_template('upload.html', prediction_text=output)

    return render_template('upload.html')#, prediction_text=output)

if __name__ == '__main__':
    app.run()