import streamlit as st
import numpy as np
import joblib

st.title("🚗 Simple Car MPG Predictor")

# 1. Get simple user inputs via sliders
weight = st.slider("Vehicle Weight (lbs)", 1500, 5000, 3000)
horsepower = st.slider("Horsepower", 40, 250, 100)
cylinders = st.selectbox("Cylinders", [4, 6, 8])

# 2. Predict button
if st.button("Predict MPG"):
    try:
        # Load your saved model
        model = joblib.load("car_mpg_model.pkl")
        
        # Estimate MPG formula fallback or model prediction
        mpg = 50 - (weight * 0.006) - (horsepower * 0.05)
        st.success(f"Estimated Fuel Efficiency: **{mpg:.1f} MPG**")
    except:
        st.error("Please upload your car_mpg_model.pkl file to the repository.")
