import streamlit as st
import pandas as pd
import numpy as np
from controllers.getUserCoordinates import getCoords
from controllers.getClosestBeach import getMoreBeaches
from controllers.getBeachData import getSwellDir,getSwellHeight,getSwellPeriod,getWindSpeed,getWindDir,getWaterTemp,getWeatherDescription

st.title("Let's go surfing")
my_slot1 = st.empty()

user_input = st.text_input("Input your current location, if possible enter your exact address:")
experience = st.selectbox(
    "What's your experience? Choose from the dropdown menu",
    ('Beginner', 'Experienced', 'Advanced/Pro')
)

latlong = getCoords(user_input)
longitude = latlong[0]
latitude = latlong[1]

df = getMoreBeaches(latitude,longitude)
df['Swell Height'] = df['latlong'].apply(getSwellHeight)
df['Swell direction'] = df['latlong'].apply(getSwellDir)
df['Swell period'] = df['latlong'].apply(getSwellPeriod)
df['Wind speed'] = df['latlong'].apply(getWindSpeed)
df['Wind direction'] = df['latlong'].apply(getWindDir)
df['Water temperature'] = df['latlong'].apply(getWaterTemp) 
df['Weather Description'] = df['latlong'].apply(getWeatherDescription)

df.to_csv('../OUTPUT/beaches.csv')
print(df.head())

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)
