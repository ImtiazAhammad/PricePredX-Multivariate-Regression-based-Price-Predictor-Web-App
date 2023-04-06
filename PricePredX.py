# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 01:47:46 2023

@author: imtia
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#loading the saved model

car_price_model = pickle.load(open('E:/Python/Machine Learning/Saved Models/car_price_model.sav','rb'))   
gold_model = pickle.load(open('E:/Python/Machine Learning/Saved Models/gold_price_model.sav','rb'))   
house_price_model = pickle.load(open('E:/Python/Machine Learning/Saved Models/house_price_model.sav','rb'))   





# sidebar for Nagigate

with st.sidebar:
    selected = option_menu('PricePredX', ['Car Price Prediction',
                                        'Gold Price Prediction',
                                        'House Price Predction'],default_index = 0)
    
    
    
    

# Car Price Predction page
if(selected == 'Car Price Prediction'):
    
    #page Title
    st.title('Car Price Prediction using Machine Learning')
    
    
    # getting the input data from user
    # Column for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Year = st.text_input('Year of buying the Car')
        
    with col2:
        Present_Price = st.text_input('Present Price of the Car')
        
    with col3:
        Kms_Driven = st.text_input('Kilometer Driven')
        
    with col1:
        Fuel_Type = st.text_input('Fuel Type')
        
    with col2:
        Seller_Type = st.text_input('Seller Type')
        
    with col3:
        Transmission = st.text_input('Transmission')
        
    with col1:
        Owner = st.text_input('Owner of the Car')
    

    
    # code for prediction
    car_price = ''
    
    # creating button for prediction
    
    if st.button('Predict Car Price'):
        car_price_prediction = car_price_model.predict([[Year,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission,Owner]])
        car_price = "The Estimited Car prise is:",car_price_prediction
        
    st.success(car_price)
    
    
    
    
#Gold Price Prediction page
if(selected == 'Gold Price Prediction'):
    
    #page Title
    st.title('Gold Price Prediction using Machine Learning')
    
    # getting the input data from user
    # Column for input fields
    col1, col2 = st.columns(2)
    
    with col1:
        SPX = st.text_input('SPX')
        
    with col2:
        USO = st.text_input('USO')
        
    with col1:
        SLV = st.text_input('SLV')
        
    with col2:
        EUR_USD = st.text_input('EUR/USD')
    
    

    
    # code for prediction
    gold_price = ''
    
    # creating button for prediction
    
    if st.button('Predict Gold Price'):
        gold_price_model = gold_model.predict([[SPX,USO,SLV,EUR_USD]])
        
    st.success(gold_price)
    
    
    
# House Price Prediction page
if(selected == 'House Price Predction'):
    
    #page Title
    st.title('House Price Predction using Machine Learning')
    
    
    
    # getting the input data from user
    # Column for input fields
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        CRIM = st.text_input('CRIM')
        
    with col2:
        ZN = st.text_input('ZN')
        
    with col3:
        INDUS = st.text_input('INDUS')
        
    with col4:
        CHAS = st.text_input('CHAS')
        
    with col5:
        NOX = st.text_input('NOX')
        
    with col1:
        RM = st.text_input('RM')
        
    with col2:
        AGE = st.text_input('AGE')
        
    with col3:
         DIS = st.text_input('DIS')
         
    with col4:
         RAD = st.text_input('RAD')
         
    with col5:
         TAX = st.text_input('TAX')
         
    with col1:
         PTRATIO = st.text_input('PTRATIO')
         
    with col2:
         B = st.text_input('B')
         
    with col3:
         LSTAT = st.text_input('LSTAT')
    

    
    # code for prediction
    house_price = ''
    
    # creating button for prediction
    
    if st.button('Predict House Price'):
        house_price = house_price_model.predict([[CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT]])
        
    st.success(house_price)
    
