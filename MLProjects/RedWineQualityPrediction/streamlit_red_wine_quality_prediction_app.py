import os
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
import streamlit as st 

# Define the type of cell you are going to predict
wine_type = ['Low_quality','High_quality']

classifier = pickle.load(open('wine_quality_rfclassifier.pickle', 'rb'))



#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_wine(fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_so2,total_so2,density,ph_value,sulphates,alcohol):
    
    # Make a prediction
    myprediction = classifier.predict([[fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_so2,total_so2,
    density,ph_value,sulphates,alcohol]])[0]
    # preds = model_predict(model,file_path)
    if myprediction > 0.5:
        pred_class = 1
    else:
        pred_class = 0
    result = wine_type[pred_class]
    return result



def main():
    st.title("Fake News Classifier")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Fake News Classifier ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    fixed_acidity = st.text_input("fixed_acidity","input your values here")
    volatile_acidity = st.text_input("volatile_acidity","input your values here")
    citric_acid = st.text_input("citric_acid","input your values here")
    residual_sugar = st.text_input("residual_sugar","input your values here")
    chlorides = st.text_input("chlorides","input your values here")
    free_so2 = st.text_input("free_so2","input your values here")
    total_so2 = st.text_input("total_so2","input your values here")
    density = st.text_input("density","input your values here")
    ph_value = st.text_input("ph_value","input your values here")
    sulphates = st.text_input("sulphates","input your values here")
    alcohol = st.text_input("alcohol","input your values here")
    result=""
    if st.button("Predict"):
        result=predict_wine(fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_so2,
        total_so2,density,ph_value,sulphates,alcohol)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()

