import streamlit as st
import joblib
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load trained model
model = joblib.load("model.pkl")

# Title of your app
st.title("Fish Classifier: Blue Fish vs. Orange Fish")

# User input features in sidebar
st.sidebar.header("Input Features")
water_depth = st.sidebar.slider("Water Depth (meters, scaled)", -5.0, 5.0, 0.0)
temp = st.sidebar.slider("Temperature (°C, scaled)", -5.0, 5.0, 0.0)

# Prepare input for prediction
input_features = np.array([[water_depth, temp]])

# Prediction
if st.sidebar.button("Predict"):
    prediction = model.predict(input_features)[0]
    probability = model.predict_proba(input_features)[0]
    st.write(f"### Prediction: {'Orange Fish' if prediction == 1 else 'Blue Fish'}")
    st.write(f"Probability of Blue Fish: {probability[0]:.2f}")
    st.write(f"Probability of Orange Fish: {probability[1]:.2f}")

# Optional data visualization
if st.checkbox("Show Data Visualization"):
    df = pd.read_csv("data.csv")
    fig, ax = plt.subplots()
    sns.scatterplot(x="water_depth", y="temp", hue="target", palette={0: "blue", 1: "orange"}, data=df, ax=ax)
    ax.scatter(water_depth, temp, color="red", s=100, label="User Input", marker="x")
    ax.legend(labels=["Blue Fish", "Orange Fish", "User Input"])
    st.pyplot(fig)