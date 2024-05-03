import streamlit as st
import pickle
import pandas as pd

with open('LR_reg.pkl', 'rb') as f:
    model = pickle.load(f)

def user_input_features():
    Present_Price = st.number_input("Present_Price", 5.5, 100.9, 9.85,step=1.0)
    Kms_Driven = st.number_input('Kms_Driven', 0, 200000, 6900)
    Owner = st.number_input('Owner', 0, 1)
    number_of_years = st.number_input('number of years', 0, 70, 7)
    Fuel_Type_CNG = st.number_input('Fuel_Type_CNG', 0, 1,0)
    Fuel_Type_Diesel = st.number_input('Fuel_Type_Diesel', 0, 1,0)
    Fuel_Type_Petrol = st.number_input('Fuel_Type_Petrol', 0, 1,0)
    Seller_Type_Dealer=st.number_input("Seller_Type_Dealer",0,1,0) 
    Seller_Type_Individual	=st.number_input("Seller_Type_Individual",0,1,0) 
    Transmission_Automatic = st.number_input('Transmission_Automatic', 0,1,0)
    Transmission_Manual = st.number_input('Transmission_Manual', 0,1,0)
    


    data = {
        "Present_Price":Present_Price,
        "Kms_Driven":Kms_Driven, 
        "Owner":Owner, 
        "number_of_years":number_of_years, 
        "Fuel_Type_CNG":Fuel_Type_CNG,
        "Fuel_Type_Diesel":Fuel_Type_Diesel,
        "Fuel_Type_Petrol":Fuel_Type_Petrol,
        " Seller_Type_Dealer": Seller_Type_Dealer,
        " Seller_Type_Individual": Seller_Type_Individual,
        "Transmission_Automatic":Transmission_Automatic,
        "Transmission_Manual ":Transmission_Manual 

    }

    features = pd.DataFrame(data, index=[0])
    features = features.rename(columns={'Kms_Driven ': 'Kms_Driven'})
    return features

def predict(model, features):
    prediction = model.predict(features)
    return prediction

def main():
    st.title("Car Prediction App")

    features = user_input_features()

    if st.button('Predict'):
        prediction = predict(model, features)
        st.write('Prediction:', prediction)

if __name__ == "__main__":
    main()