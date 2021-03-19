import streamlit as st
import datetime
import numpy as np
import pandas as pd
import requests


st.set_page_config(
            page_title="Quick reference", # => Quick reference - Streamlit
            page_icon="🍎",
            layout="centered", # wide
            initial_sidebar_state="auto") # collapsed

''' # NYC Taxi Fare
'''

CSS = """
h1 {
    color: red;
}
body {
    background-image: url(https://avatars1.githubusercontent.com/u/9978111?v=4);
    background-size: cover;
}
"""
st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)


st.markdown('<style>body{background-color: Blue;}</style>',unsafe_allow_html=True)


#time
today = datetime.date.today()
date = st.date_input('Pick-Up Time', today)


#pickup_longitude
pickup_longitude = st.text_input('pickup longitude', -73.950655)

#pickup_latitude
pickup_latitude = st.text_input('pickup latitude', 40.783282)

# dropoff longitude
dropoff_longitude = st.text_input('dropoff longitude', -73.984365)

# dropoff latitude
dropoff_latitude = st.text_input('dropoff latitude', 40.769802)

# passenger
@st.cache
def get_select_box_data():
    return pd.DataFrame({
          'first column': list(range(1, 9)),
        })

df = get_select_box_data()
passenger_count = st.selectbox('Passenger count', df['first column'])



url = 'https://testtesttest-ozjcvkosra-ew.a.run.app/predict_fare/'

if url == 'http://taxifare.lewagon.ai/predict_fare/':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')


dictionary=dict(
        key='iaugds',
        pickup_datetime=f'{date} 12:12:12 UTC',
        pickup_longitude=float(pickup_longitude),
        pickup_latitude=float(pickup_latitude),
        dropoff_longitude=float(dropoff_longitude),
        dropoff_latitude=float(dropoff_latitude),
        passenger_count=int(passenger_count))


if st.button('Prediction'):
    response= requests.get(url,params=dictionary).json()
    st.markdown('Predicted Fare $'+str(round(float(response['prediction']),2)))


