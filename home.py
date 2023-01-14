import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime 
import datetime
from PIL import Image
import requests




st.title("Application de prévision météorologique")
st.text_input("Entrez votre ville", key="name")
# You can access the value at any point with:
city_name = st.session_state.name
from datetime import datetime

# datetime object containing current date and time
if city_name:
    st.header("Météo Actuelle")
    now = datetime.now()
# dd/mm/YY H:M:S
    dt_string = now.strftime("%H:%M:%S")
    st.write('Heure :' +dt_string)


#Paramètre d'acces à l'API Openweathermap
api_key = "d850f7f52bf19300a9eb4b0aa6b80f0d"  # Enter the API key you got from the OpenWeatherMap website
base_url = "http://api.openweathermap.org/data/2.5/weather?"

#city_name = city
complete_url = base_url + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name +"&lang=fr" # This is to complete the base_url, you can also do this manually to checkout other weather data available
response = requests.get(complete_url)
x = response.json()   #reception de la réponse Json du serveur API
try:
        if x["cod"] != "404":
                y = x["main"]
                
                current_temperature = y["temp"] - 273.15
                current_humidity = y["humidity"] 
                current_pression = y["pressure"]
                z = x["weather"]

                weather_description = z[0]["description"]
                a = x["wind"]
                current_vent= a["speed"]
                

                
                #st.write('' +str(current_pression))
                #st.write('' +str(current_temperature))
                #st.write('' +str(weather_description))
                #st.write('' +str(current_humidity))
                #st.write('' +str(current_vent) )

        else:
                st.write(" City Not Found ")
    
except Exception as e : 
        print(e)



col1, col2, = st.columns(2, gap="small")
with col1:
   image = Image.open('icon.jpg')

   st.image(image, caption='')
with col2:
   st.header("Température")
   st.write('' +str(current_temperature) + '°C')
 

import streamlit as st

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)



# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    d = st.sidebar.date_input('current_time', 'Dayly_time')
)


# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('current_time', 'dayly_time')
)



 

col1, col2, col3, col4 = st.columns(4, gap="small")

with col1:
   st.header("Vent")
   st.write('' +str(current_vent) )
with col2:
   st.header("Humidté")
   st.write('' +str(current_humidity))

with col3:
   st.header("Description")
   st.write('' +str(weather_description))

with col4:
   st.header("Pression")
   st.write('' +str(current_pression))

   


