import streamlit as st

st.title("🚗 Simple Car MPG Predictor")

# 1. User inputs
weight = st.slider("Vehicle Weight (lbs)", 1500, 5000, 3000)
horsepower = st.slider("Horsepower", 40, 250, 100)
cylinders = st.selectbox("Cylinders", [4, 6, 8])

# 2. Predict button
if st.button("Predict MPG"):
    # Estimated MPG calculation formula
    mpg = 50 - (weight * 0.006) - (horsepower * 0.05) - (cylinders * 0.5)
    st.success(f"Estimated Fuel Efficiency: **{max(mpg, 5.0):.1f} MPG**")
