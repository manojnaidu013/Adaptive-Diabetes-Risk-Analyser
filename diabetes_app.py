import streamlit as st
import pickle
import pandas as pd

with open("diabetes_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("ADAPTIVE DIABETES PREDICTION MODEL")

st.markdown("""
This app predicts the risk of diabetes based on the user-provided symptoms.
Please provide the following details to check your diabetes risk.
""")

age = st.slider("Age", 10, 100, 30)
gender = st.selectbox("Gender", ["Male", "Female"])
polyuria = st.selectbox("Polyuria (Excessive Urination)", ["Yes", "No"])
polydipsia = st.selectbox("Polydipsia (Excessive Thirst)", ["Yes", "No"])
sudden_weight_loss = st.selectbox("Sudden Weight Loss", ["Yes", "No"])
weakness = st.selectbox("Weakness", ["Yes", "No"])
polyphagia = st.selectbox("Polyphagia (Excessive Hunger)", ["Yes", "No"])
genital_thrush = st.selectbox("Genital Thrush", ["Yes", "No"])
visual_blurring = st.selectbox("Visual Blurring", ["Yes", "No"])
itching = st.selectbox("Itching", ["Yes", "No"])
irritability = st.selectbox("Irritability", ["Yes", "No"])
delayed_healing = st.selectbox("Delayed Healing", ["Yes", "No"])
partial_paresis = st.selectbox("Partial Paresis", ["Yes", "No"])
muscle_stiffness = st.selectbox("Muscle Stiffness", ["Yes", "No"])
alopecia = st.selectbox("Alopecia (Hair Loss)", ["Yes", "No"])
obesity = st.selectbox("Obesity", ["Yes", "No"])

inputs = pd.DataFrame({
    "Age": [age],
    "Gender": [1 if gender == "Male" else 0],
    "Polyuria": [1 if polyuria == "Yes" else 0],
    "Polydipsia": [1 if polydipsia == "Yes" else 0],
    "sudden weight loss": [1 if sudden_weight_loss == "Yes" else 0],
    "weakness": [1 if weakness == "Yes" else 0],
    "Polyphagia": [1 if polyphagia == "Yes" else 0],
    "Genital thrush": [1 if genital_thrush == "Yes" else 0],
    "visual blurring": [1 if visual_blurring == "Yes" else 0],
    "Itching": [1 if itching == "Yes" else 0],
    "Irritability": [1 if irritability == "Yes" else 0],
    "delayed healing": [1 if delayed_healing == "Yes" else 0],
    "partial paresis": [1 if partial_paresis == "Yes" else 0],
    "muscle stiffness": [1 if muscle_stiffness == "Yes" else 0],
    "Alopecia": [1 if alopecia == "Yes" else 0],
    "Obesity": [1 if obesity == "Yes" else 0]
})


if st.button("Predict Diabetes Risk"):
    prediction = model.predict(inputs)[0]
    risk = "Positive (High Risk)" if prediction == 1 else "Negative (Low Risk)"
    st.subheader(f"Prediction: {risk}")
