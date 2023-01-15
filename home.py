import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime 
import datetime
from PIL import Image
import requests



#Titre de l'application
st.title("Application de prévisions météorologiques")
st.text_input("Entrez votre ville", key="name")     #recuperation du nom de la ville
city_name = st.session_state.name       #on affecte la ville à lq variable city


# datetime object containing current date and time
if city_name:
    st.header("Météo Actuelle")
    now = datetime.now()
# dd/mm/YY H:M:S
    dt_string = now.strftime("%H:%M:%S")    # affichage de l'heure courante
    st.write('Heure :' +dt_string)


#Paramètre d'acces à l'API Openweathermap
api_key = "d850f7f52bf19300a9eb4b0aa6b80f0d"  # clé secrète d'access à l'API openWearhermap
base_url = "http://api.openweathermap.org/data/2.5/weather?" # lien d'accès au service de l'API

#city_name = city
complete_url = base_url + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name +"&lang=fr" # This is to complete the base_url, you can also do this manually to checkout other weather data available
response = requests.get(complete_url)   # Récupération de la réponse de l'API
x = response.json()   #reception de la réponse Json du serveur API  # Conversion de la réponse sous format jSON
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
   st.header("Température en degré celcius")
   try:
    st.write('' +str(current_temperature) + '°C')
   except Exception as e:
    print(e)
     


# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'selectionnez un mode',
    ('current_time', 'dayly_time')
)

if add_selectbox== 'dayly_time':

    url_forecast = "http://api.openweathermap.org/data/2.5/forecast?q="+city_name+"&lang=fr"+"&APPID=beb97c1ce62559bba4e81e28de8be095"
    r_forecast = requests.get(url_forecast)
    data = r_forecast.json()
    #print(data)
     
# recupère et affiche les informations météorologiques données par l'API
col1, col2, col3, col4 = st.columns(4, gap="small")

with col1:
   st.header("Vent")
   try:
    st.write('' +str(current_vent) )
    if add_selectbox =='dayly_time':
        for i in range (0,5):
            st.write(data['list'][i]['wind']['speed'])
   except Exception as e:
    print(e)
with col2:
   st.header("Humidté")
   try:
    st.write('' +str(current_humidity))
    if add_selectbox =='dayly_time':
        for i in range (0,4):
            data['list'][i]['main']['humidity']
   except Exception as e:
    print(e)

with col3:
   st.header("Description")
   try:
    st.write('' +str(weather_description))
    if add_selectbox =='dayly_time':
        for i in range (0,5):
            st.write(data['list'][i]['weather'][0]['description'])
   except Exception as e:
    print(e)

with col4:
   st.header("Pression")
   try:
    st.write('' +str(current_pression))
    if add_selectbox =='dayly_time':
        for i in range (0,5):
            st.write(data['list'][i]['main']['pressure'])
   except Exception as e:
    print(e)

   


