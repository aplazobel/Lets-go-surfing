import json
import requests
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()

email = os.getenv("EMAIL")
token = os.getenv("TOKEN_SURFCHECK")

def getMoreBeaches(lat, longt):
    url = f"https://surfvideos.xyz/locations.json?latitude={lat}&longitude={longt}&distance=50"

    payload = {}
    headers = {
    'X-User-Email': email,
    'X-User-Token': token,
    'Accept': '{{Accept}}',
    'Content-Type': '{{Content}}'
    }

    response = requests.request("GET", url, headers=headers, data = payload)
    data = response.json()
    
    df = pd.DataFrame(
    [
        data[i]["data"]["attributes"]["name"], 
        data[i]["data"]["attributes"]["address"], 
        data[i]["data"]["attributes"]["direction"], 
        data[i]["data"]["attributes"]["experience"], 
        data[i]["data"]["attributes"]["wave_quality"], 
        data[i]["data"]["attributes"]["frequency"], 
        data[i]["data"]["attributes"]["bottom"], 
        data[i]["data"]["attributes"]["best_wind_direction"], 
        data[i]["data"]["attributes"]["best_swell_direction"],
        data[i]["data"]["attributes"]["latitude"],
        data[i]["data"]["attributes"]["longitude"]
] for i in range(len(data)))
    
    df = df.rename(columns={0: 'Name', 1: 'Address', 2: 'Direction', 3: 'Experience', 4: "Wave quality", 5: "Frequency", 6: 'Bottom', 7: 'Best wind', 8: 'Best swell', 9: "Latitude", 10:"Longitude"})
    df["latlong"] = None
  
    for i in range(df.shape[0]):
        df["latlong"][i] = f"{df['Latitude'][i]},{df['Longitude'][i]}"    
    
    return df





