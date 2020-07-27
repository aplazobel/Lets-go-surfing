from getUserCoordinates import getCoords
from getClosestBeach import getMoreBeaches
from getBeachData import getSwellDir,getSwellHeight,getSwellPeriod,getWindSpeed,getWindDir,getWaterTemp,getWeatherDescription
import pandas as pd
#Might want to create a distance variable

address = input("Input your current location, if possible enter your exact address: ")

latlong = getCoords(address)
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

print(df.head())