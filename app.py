import streamlit as st
import pickle

import numpy as np
with open("Estate_Model.pkl", 'rb') as file:
    model = pickle.load(file)


def input():
    bedrooms = st.number_input("bed rooms ")
    bathrooms = st.number_input("bath rooms ")
    status = st.number_input("Status ")
    size = st.number_input("size")
    location = st.number_input("location")
    face = st.number_input("face")
    type = st.number_input("Type")
    arr = np.array([[bedrooms, bathrooms, status, size, location, face, type]])
    return arr
arr = input()   
check = st.button("Enter", type="primary")
if (check):
    st.write(model.predict(arr)) 
else:st.write("Please enter all the fields")
