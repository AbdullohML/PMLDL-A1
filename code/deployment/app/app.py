import os

import requests
import streamlit as st


API_URL = os.getenv("API_URL", "http://api:8000")


st.title("California House Price Prediction")

st.write("Enter housing information to estimate the median house value.")

med_inc = st.number_input("Median income", value=3.5)
house_age = st.number_input("House age", value=30.0)
ave_rooms = st.number_input("Average rooms", value=5.0)
ave_bedrms = st.number_input("Average bedrooms", value=1.0)
population = st.number_input("Population", value=1000.0)
ave_occup = st.number_input("Average occupancy", value=3.0)
latitude = st.number_input("Latitude", value=34.0)
longitude = st.number_input("Longitude", value=-118.0)

if st.button("Predict"):
    payload = {
        "MedInc": med_inc,
        "HouseAge": house_age,
        "AveRooms": ave_rooms,
        "AveBedrms": ave_bedrms,
        "Population": population,
        "AveOccup": ave_occup,
        "Latitude": latitude,
        "Longitude": longitude,
    }

    try:
        response = requests.post(
            f"{API_URL}/predict",
            json=payload,
            timeout=10,
        )
        response.raise_for_status()

        result = response.json()

        st.success(
            f"Predicted median house value: ${result['prediction_usd']:,.2f}"
        )

    except requests.RequestException as error:
        st.error(f"Could not connect to the prediction API: {error}")
