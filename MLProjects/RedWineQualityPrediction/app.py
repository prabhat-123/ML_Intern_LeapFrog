import os
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from flask import url_for,request,Flask,redirect,render_template
from gevent.pywsgi import WSGIServer
from werkzeug.utils import secure_filename



# Define a Flask App
app = Flask(__name__)

# Define the type of cell you are going to predict
wine_type = ['Low_quality','High_quality']

classifier = pickle.load(open('wine_quality_rfclassifier.pickle', 'rb'))



@app.route('/',methods=['GET'])
def index():
    return render_template('./index.html')

@app.route('/',methods=['GET','POST'])
def upload():
    if request.method=='POST':
        fixed_acidity = request.form['fa']
        volatile_acidity = request.form['va']
        citric_acid = request.form['ca']
        residual_sugar = request.form['rs']
        chlorides = request.form['cls']
        free_so2 = request.form['fso2']
        total_so2 = request.form['tso2']
        density = request.form['dnsty']
        ph_value = request.form['ph']
        sulphates = request.form['sulph']
        alcohol = request.form['alc']
       
        # Make a prediction
        myprediction = classifier.predict([[fixed_acidity,volatile_acidity,citric_acid,
        residual_sugar,chlorides,free_so2,total_so2,density,ph_value,sulphates,alcohol]])[0]
        # preds = model_predict(model,file_path)
        if myprediction > 0.5:
            pred_class = 1
        else:
            pred_class = 0
        result = wine_type[pred_class]
        return render_template('./predict.html',result=result)
    else:
        return render_template('./index.html')

if __name__ == '__main__':
    app.run(debug=True)




