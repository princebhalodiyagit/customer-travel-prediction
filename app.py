import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

st.title("Customer Travel Prediction")

age = st.number_input("Age", min_value=0, max_value=100)
frequent_flyer = st.selectbox("Frequent Flyer", [0, 1])
annual_income = st.selectbox("Annual Income Class", [0, 1, 2])
services_opted = st.number_input("Services Opted", min_value=0, max_value=10)
account_synced = st.selectbox("Account Synced To Social Media", [0, 1])
booked_hotel = st.selectbox("Booked Hotel Or Not", [0, 1])

if st.button("Predict"):
    input_data = np.array([[age, frequent_flyer, annual_income, services_opted, account_synced, booked_hotel]])
    result = model.predict(input_data)
    if result[0] == 1:
        st.success("Customer WILL Travel ✈️")
    else:
        st.error("Customer will NOT Travel ❌")