import pickle
import streamlit as st
import numpy as np


st.title("House Price Prediction Model")


data = []
under_construction = st.selectbox('Is Your house is in Under Construction',('Yes','No'))
if under_construction == 'Yes':
    data.append(int(1))
else:
    data.append(int(0))

rera = st.selectbox('Is Your house is Nominated for RERA',('Yes','No'))
if rera == 'Yes':
    data.append(int(1))
else:
    data.append(int(0))
    

bhk = st.number_input('Enter the BHK ',min_value=0,max_value=10)
data.append(bhk)

squarefeet = st.number_input('Enter the  Squarefeet Area',min_value=0)
data.append(squarefeet)

readytomove = st.selectbox('Is Your house is in Living Condition',('Yes','No'))
if rera == 'Yes':
    data.append(int(1))
else:
    data.append(int(0))

resale = st.selectbox('Is your house is Resale property ?',('Yes','No'))
if rera == 'Yes':
    data.append(int(1))
else:
    data.append(int(0))
    
city = [st.text_input(label="Enter the city of your house",placeholder = 'city name')]

# import the trained model for encode the city
file = open(r"C:\Users\Asus\Documents\house_price_encode.pkl","rb")
encode = pickle.load(file)


# loading the model
file = open(r"C:\Users\Asus\Documents\house_price_model.pkl","rb")
model = pickle.load(file)

print(data)
btn = st.button(label = 'Predict Price')
if btn == True:
    flag = False
    try:
        encode_value=encode.transform(city)[0]
        data.append(encode_value)
        data = np.array(data)
        data = data.reshape(1,-1)
        predicted_value = model.predict(data)
        st.success("Estimated  Price of House is  {} LPA ".format(predicted_value[0]))
    except ValueError:
        st.warning('Please Enter correct City name !!')


    

