import streamlit as st 
import joblib 

#load the joblib model 
model_nb = joblib.load('exp-salary')

#user input 
st.title("SALARY EXPECTATION")
ip = st.text_input("Enter your Year of Experience:")

#predict if the entered message is spam or ham 
op = model_nb.predict([ip])
if st.button('PREDICT'):
  st.title(op[0])  #prints the output as spam or ham 
           
  
