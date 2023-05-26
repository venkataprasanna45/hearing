from flask import Flask,render_template,request
import pickle
import numpy as np

model = pickle.load(open('model.pkl','rb'))
        qqqqqqq queue`````  queue   queue       queue`queueq    `                   `   `       `   `   q   `queue2 q`  `       queue`  3

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_placement():
    cgpa = float(request.form.get('age'))
    iq = int(request.form.get('physical_score'))

    # prediction
    result = model.predict(np.array([age,physcial_score]).reshape(1,2))

    if result[0] == 1:
        result = 'hearing is good'
    else:
        result = 'hearing is bad'

    return render_template('index.html',result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
