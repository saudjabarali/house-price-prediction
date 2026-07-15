import pandas as pd
import streamlit as st
import joblib

st.write("App Started")

model=joblib.load("House_Price_Prediction_Model.jb")

st.title("House Price Prediction")
st.write("Enter the details of the house to predict its price.")

inputs=['OverallQual', 'GrLivArea', 'GarageCars', 'GarageArea', 'TotalBsmtSF',
       '1stFlrSF', 'FullBath', 'TotRmsAbvGrd', 'YearBuilt', 'YearRemodAdd',
       'GarageYrBlt', 'MasVnrArea', 'Fireplaces', 'BsmtFinSF1', 'Foundation',
       'LotFrontage', 'WoodDeckSF', '2ndFlrSF', 'OpenPorchSF', 'HalfBath',
       'LotArea', 'CentralAir']

input_data = {}
for feature in inputs:
    if feature == 'CentralAir':
        input_data[feature] = st.selectbox(f"Select {feature}", ['Y', 'N'])
    else:
        input_data[feature] = st.number_input(f"Enter {feature}", value=0,step=1.0 if feature in ['OverallQual', 'GarageCars', 'FullBath', 'TotRmsAbvGrd', 'YearBuilt', 'YearRemodAdd', 'GarageYrBlt', 'Fireplaces', 'HalfBath'] else 0.1)


if st.button("Predict Price"):
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)
    st.write(f"The predicted house price is: ${prediction[0]:,.2f}")