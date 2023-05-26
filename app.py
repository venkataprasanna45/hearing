from flask import Flask,render_template,url_for,request,redirect
import numpy as np
import pandas as pd
import joblib
import pickle
app = Flask(__name__)

model = joblib.load('model.pkl')




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_placement():
    age = float(request.form.get('age'))
    physical_score = float(request.form.get('physical_score'))

    # prediction
    result = model.predict(np.array([age,physical_score]).reshape(1,2))

    if result[0] == 1:
        result = 'hearing is good'
    else:
        result = 'hearing is bad'

    return render_template('index.html',result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
