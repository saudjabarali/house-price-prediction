import pandas as pd
import streamlit as st
import joblib

# Load the trained model
model = joblib.load("House_Price_Prediction_Model.jb")

# Title
st.title("🏠 House Price Prediction")
st.write("Enter the details of the house to predict its price.")

# Feature names
inputs = [
    'OverallQual', 'GrLivArea', 'GarageCars', 'GarageArea', 'TotalBsmtSF',
    '1stFlrSF', 'FullBath', 'TotRmsAbvGrd', 'YearBuilt', 'YearRemodAdd',
    'GarageYrBlt', 'MasVnrArea', 'Fireplaces', 'BsmtFinSF1', 'Foundation',
    'LotFrontage', 'WoodDeckSF', '2ndFlrSF', 'OpenPorchSF', 'HalfBath',
    'LotArea', 'CentralAir'
]

# Integer features
integer_features = [
    'OverallQual',
    'GarageCars',
    'FullBath',
    'TotRmsAbvGrd',
    'YearBuilt',
    'YearRemodAdd',
    'GarageYrBlt',
    'Fireplaces',
    'HalfBath'
]

input_data = {}

# Input widgets
for feature in inputs:

    if feature == "CentralAir":
        input_data[feature] = st.selectbox(
            "Central Air",
            ["Y", "N"]
        )

    elif feature in integer_features:
        input_data[feature] = st.number_input(
            f"Enter {feature}",
            value=0,
            step=1
        )

    else:
        input_data[feature] = st.number_input(
            f"Enter {feature}",
            value=0.0,
            step=0.1
        )

# Prediction button
if st.button("Predict Price"):

    # Convert CentralAir
    input_data["CentralAir"] = 1 if input_data["CentralAir"] == "Y" else 0

    # Create DataFrame
    input_df = pd.DataFrame([input_data])

    # Prediction
    prediction = model.predict(input_df)

    st.success(f"🏡 Predicted House Price: ${prediction[0]:,.2f}")