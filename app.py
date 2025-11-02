# ======================================================
# 🧮 Insurance Cost Prediction App (Streamlit)
# ======================================================

import streamlit as st
import numpy as np
import pandas as pd
import pickle

# ------------------------------------------------------
# Load the trained model
# ------------------------------------------------------
with open("insurance_model.pkl", "rb") as f:
    model = pickle.load(f)

# ------------------------------------------------------
# Streamlit Page Setup
# ------------------------------------------------------
st.set_page_config(page_title="Insurance Cost Prediction", page_icon="💰", layout="centered")

st.title("💰 Insurance Cost Prediction App")
st.markdown("Predict medical insurance charges based on personal attributes.")

st.divider()

# ------------------------------------------------------
# User Inputs
# ------------------------------------------------------
# ------------------------------------------------------
# User Inputs
# ------------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=18, max_value=100, value=30, step=1)
    sex = st.selectbox("Sex", ["male", "female"])

with col2:
    children = st.number_input("Number of Children", min_value=0, max_value=5, value=0, step=1)
    smoker = st.selectbox("Smoker", ["yes", "no"])

# -------------------------
# BMI or Calculate BMI
# -------------------------
st.divider()
st.subheader("🏋️ BMI (Body Mass Index)")

bmi_option = st.radio(
    "Do you know your BMI?",
    ("Yes, I know my BMI", "No, calculate it for me")
)

if bmi_option == "Yes, I know my BMI":
    bmi = st.number_input("Enter your BMI", min_value=10.0, max_value=60.0, value=25.0, step=0.1)
else:
    weight = st.number_input("Enter your weight (kg)", min_value=30.0, max_value=200.0, value=70.0, step=0.5)
    height = st.number_input("Enter your height (m)", min_value=1.0, max_value=2.5, value=1.7, step=0.01)
    bmi = weight / (height ** 2)
    st.write(f"📏 Calculated BMI: **{bmi:.2f}**")

# -------------------------
# Region input
# -------------------------
region = st.selectbox("Region", ["southeast", "southwest", "northeast", "northwest"])

st.divider()

# ------------------------------------------------------
# Prepare input for model
# ------------------------------------------------------
input_data = pd.DataFrame({
    'age': [age],
    'sex': [1 if sex == "male" else 0],
    'bmi': [bmi],
    'children': [children],
    'smoker': [1 if smoker == "yes" else 0],
    'region': [region]
})

# ------------------------------------------------------
# Prediction
# ------------------------------------------------------
if st.button("🔮 Predict Insurance Cost"):
    prediction = model.predict(input_data)[0]
    st.success(f"💵 Estimated Annual Insurance Cost: ₹{prediction:,.2f}")
    st.caption("⚙️ Model: Gradient Boosting Regressor with optimized preprocessing")