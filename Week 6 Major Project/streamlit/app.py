import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

# Load trained model
@st.cache_resource
def load_model():
    return joblib.load("../Model/credit_card_fraud_detection_model.pkl")

model = load_model()

st.title("Credit Card Fraud Detection")

# Define the input features
feature_names = [
    "Time", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10",
    "V11", "V12", "V13", "V14", "V15", "V16", "V17", "V18", "V19", "V20",
    "V21", "V22", "V23", "V24", "V25", "V26", "V27", "V28", "Amount"
]

# Collect user inputs via number inputs
inputs = {}
for feature in feature_names:
    if feature in ['Time', 'Amount']:
        try:
            inputs[feature] = float(st.text_input(f"{feature}"))
        except ValueError:
            inputs[feature] = 0.0
    else:
        inputs[feature] = st.slider(f"{feature}", format="%.2f", min_value=-10.0, max_value=10.0, value=0.0)

# Preprocessing scaler statistics from training data 
def preprocess_input(data):
    df = pd.DataFrame([data])
    df['Amount'] = StandardScaler().fit_transform(df['Amount'].values.reshape(-1,1))
    df['Time'] = StandardScaler().fit_transform(df['Time'].values.reshape(-1,1))
    return df

if st.button("Predict Fraud"):
    # Preprocess the input
    input_df = preprocess_input(inputs)

    # Predict using the loaded model
    prediction = model.predict(input_df)[0]
    prediction_prob = model.predict_proba(input_df)[0][1]

    if prediction == 1:
        st.error(f"Warning! Fraud Detected with probability {prediction_prob:.4f}")
    else:
        st.success(f"Transaction is Normal. Probability of fraud: {prediction_prob:.4f}")
