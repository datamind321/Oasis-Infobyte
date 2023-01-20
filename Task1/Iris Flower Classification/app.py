import streamlit as st
import pickle 
from win32com.client import Dispatch
import numpy as np
from sklearn.linear_model import LogisticRegression
model = pickle.load(open('iris.pkl','rb'))
model2 = pickle.load(open('iris_linear.pkl','rb'))
model3 = pickle.load(open('iris_svm.pkl','rb'))


def predict(num):
    if num<0.5:
        speak("Iris Setosa")
        
        return "Iris-Setosa"
    elif num <1.5:
        speak("Iris Virginica")
        return 'Iris-Virginica'
    else:
        speak("Iris Versicolor")
        return 'Iris-Versicolor'
def speak(text):
	speak=Dispatch(("SAPI.SpVoice"))
	speak.Speak(text)

    
        

def main():
    st.title("Welcome to Iris Flower Prediction App")
    activities=['Linear Regression','Logistic Regression','SVM']
    option=st.sidebar.selectbox("Which model would you like to use ?",activities)
    st.subheader(option)
    a = st.slider(' Select Sepal Length in cm',0.0,10.0)
    b = st.slider(' Select Sepal width in cm',0.0,10.0)
    c = st.slider(' Select Petal Length in cm',0.0,10.0)
    d = st.slider(' Select Petal Width in cm',0.0,10.0)
    inputs = [[a,b,c,d]]
    if st.button("Predict"):
        if option=="Linear Regression":
            st.success(predict(model2.predict(inputs)))
        elif option=="Logistic Regression":
            st.success(predict(model.predict(inputs)))
        elif option=="SVM":
            st.success(predict(model3.predict(inputs)))
        if predict=="Iris-Setosa":
            st.image('setosa.png')
        elif predict=="Iris-Virginica":
            st.image('verginica.png')
        else:
            st.image('versicolor.png')
        
if __name__=="__main__":
    main()
        

    
