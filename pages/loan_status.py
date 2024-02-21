import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the pre-built model
model = joblib.load('LOAN/Model.pkl')

# Streamlit UI
st.title("Loan Status Prediction")

st.write("Please provide the following details to predict the loan status:")

# Input fields
married = st.selectbox("Marital Status", ["Married", "Single"])
dependents = st.number_input("Number of Dependents", min_value=0, max_value=10, value=0)
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
credit_history = st.selectbox("Credit History", [0.0, 1.0])
gender = st.radio("Gender", ["Male", "Female"])
property_area = st.selectbox("Property Area", ["Rural", "Semiurban", "Urban"])
total_income = st.number_input("Total Income", min_value=0.0, value=0.0)
emi = st.number_input("EMI", min_value=0.0, value=0.0)
balance_income = st.number_input("Balance Income", min_value=0.0, value=0.0)

# Mapping categorical values to integers
gender_mapping = {"Male": 1, "Female": 0}
property_mapping = {"Rural": 1, "Semiurban": 2, "Urban": 3}
education_mapping = {"Graduate": 1, "Not Graduate": 0}
self_employed_mapping = {"Yes": 1, "No": 0}
married_mapping = {"Married": 1, "Single": 0}

# Prepare input data
input_data = pd.DataFrame({
    'Married': [married_mapping[married]],
    'Dependents': [dependents],
    'Education': [education_mapping[education]],
    'Self_Employed': [self_employed_mapping[self_employed]],
    'Credit_History': [credit_history],
    'Gender_Female': [gender == "Female"],
    'Gender_Male': [gender == "Male"],
    'Property_Area_Rural': False,#[property_area == "Rural"],
    'Property_Area_Semiurban': False,#[property_area == "Semiurban"],
    'Property_Area_Urban': True,#[property_area == "Urban"],
    'TotalIncome': [total_income],
    'EMI': [emi],
    'BalanceIncome': [balance_income]
})

# Predict button
if st.button("Predict Loan Status"):
    prediction = model.predict(input_data)
    st.write("Loan Status:", prediction[0])

    if prediction[0] != 0:
        st.success("You are eligible for the loan!!")
    else:
        st.error("You are not eligible for the loan!!")
