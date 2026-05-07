import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("heart_model.pkl")

st.title("❤️ Heart Disease Prediction App")

st.write("Enter patient details below:")

age = st.number_input("Age", 1, 120)
sex = st.selectbox("Sex", [0, 1])
chest_pain_type = st.selectbox("Chest Pain Type", [0,1,2,3])
resting_blood_pressure = st.number_input("Resting Blood Pressure")
serum_cholesterol = st.number_input("Serum Cholesterol")
fasting_blood_sugar = st.selectbox("Fasting Blood Sugar > 120", [0,1])
resting_ekg_results = st.selectbox("Resting ECG Results", [0,1,2])
max_heart_rate = st.number_input("Max Heart Rate Achieved")
exercise_induced_angina = st.selectbox("Exercise Induced Angina", [0,1])
oldpeak = st.number_input("Oldpeak ST Depression")
slope = st.selectbox("Slope of Peak Exercise ST Segment", [0,1,2])
num_major_vessels = st.selectbox("Number of Major Vessels", [0,1,2,3])
thal = st.selectbox("Thal", [0,1,2])

if st.button("Predict"):

    features = np.array([[age, sex, chest_pain_type,
                          resting_blood_pressure,
                          serum_cholesterol,
                          fasting_blood_sugar,
                          resting_ekg_results,
                          max_heart_rate,
                          exercise_induced_angina,
                          oldpeak,
                          slope,
                          num_major_vessels,
                          thal]])

    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("⚠️ Heart Disease Detected")
    else:
        st.success("✅ No Heart Disease Detected")