#Importing all the libraries and functions that are necessary

import streamlit as st
import pandas as pd
import numpy as np
from SRC.getUserCoordinates import getCoords
from SRC.getClosestBeach import getMoreBeaches 
from SRC.getBeachData import getSwellDir,getSwellHeight,getSwellPeriod,getWindSpeed,getWindDir,getWaterTemp,getWeatherDescription
from PIL import Image
from SRC.sendEmail import enviaMail
import pydeck as pdk
from SRC.pdf_generator import pdfMaker
from SRC.directionsAPI import getDirections

# Adding a title to the streamlit API
st.title("Let's go surfing")
my_slot1 = st.empty()

# Adding an image to the streamlit API
image = Image.open('INPUT/theboyz.JPG')
st.image(image, caption="Your developers surfing MAD waves! STAY RIDIN'",
              use_column_width=True)

# Getting inputs
user_input_st = st.text_input("Input your current location, if possible enter your exact address:")
experience_st = st.selectbox(
    "What's your experience? Choose from the dropdown menu",
    ('','Beginner', 'Experienced', 'Advanced/Pro')
)
email_st = st.text_input("Please input your email address:")

experience = experience_st
user_input = user_input_st

# The code below was used to check how everything worked on the terminal
#user_input = input("Input your current location, if possible enter your exact address:")
#experience = input("Input your experience: ")

# This if statement is to make sure that the functions don't start running before they're supposed to
if len(user_input) > 1:
    # Idem here, but also this function of the code won't be executed until there's an inputted location
    if len(experience) > 1:
        # This if statement is to make sure that the functions don't start running before they're supposed to
        if len(email_st) > 1:
            latlong = getCoords(user_input)
            longe = latlong[0]
            late = latlong[1]

            if longe == 0.0 and late == 0.0:
                raise ValueError("Your address wasn't specific enough, please reload the page and try again.") 
            
            #try:
            df = getMoreBeaches(late,longe, experience)
            #except:
            #    raise ValueError("Your address wasn't specific enough, please reload the page and try again.")
            df['Swell Height'] = df['latlong'].apply(getSwellHeight)
            df['Swell direction'] = df['latlong'].apply(getSwellDir)
            df['Swell period'] = df['latlong'].apply(getSwellPeriod)
            df['Wind speed'] = df['latlong'].apply(getWindSpeed)
            df['Wind direction'] = df['latlong'].apply(getWindDir)
            df['Water temperature'] = df['latlong'].apply(getWaterTemp) 
            df['Weather Description'] = df['latlong'].apply(getWeatherDescription)

            print(df)
            # Transforming to CSV. Then CSV is used to create a PDF that will be sent to user
            df.to_csv('OUTPUT/beaches.csv', index = False)
            pdfMaker()

            # Sending the email      
            enviaMail(email_st)

            st.subheader('Raw data')
            st.write(df)

            # Adding header before the map
            st.header("Best beaches near you:")
            my_slot2 = st.empty()
            #st.write(f"The beach is called **{df['Name']}**. The swell is expected to reach **{df['Swell height']} meters** ")

            # Getting a new dataframe to be able to plot the map
            df1 = df[['Latitude','Longitude']]

            #Plotting the map
            my_slot3 = st.empty()
            st.pydeck_chart(pdk.Deck(
            map_style='mapbox://styles/mapbox/light-v9',
            initial_view_state=pdk.ViewState(
                latitude = late,
                longitude = longe,
                zoom=11,
                pitch=50,
            ),
            layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=df1,
                get_position='[Longitude, Latitude]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,
                ),
            ],
            ))

            st.empty()
            st.subheader("Here are the indications to get to the beach:")
            st.empty()
            beach_name = df.iloc[0]["Name"]
            html = getDirections(user_input, beach_name)
            st.markdown(f'{html}', unsafe_allow_html=True)









