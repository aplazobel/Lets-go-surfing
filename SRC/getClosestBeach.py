import json
import requests
import pandas as pd
#import os get ...

def getMoreBeaches(lat, longt):
    url = f"https://surfvideos.xyz/locations.json?latitude={lat}&longitude={longt}&distance=50"

    payload = {}
    headers = {
    'X-User-Email': 'ap1468@georgetown.edu',
    'X-User-Token': 'edJsbzQC2YbM2bYFPWYm',
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
        data[i]["data"]["attributes"]["bottom"], 
        data[i]["data"]["attributes"]["best_wind_direction"], 
        data[i]["data"]["attributes"]["best_swell_direction"],
        data[i]["data"]["attributes"]["latitude"],
        data[i]["data"]["attributes"]["longitude"]
] for i in range(len(data)))
    
    df = df.rename(columns={0: 'Name', 1: 'Address', 2: 'Direction', 3: 'Experience',4: 'Bottom', 5: 'Best wind', 6: 'Best swell', 7: "Latitude", 8:"Longitude"})
    df["latlong"] = None
  
    for i in range(df.shape[0]):
        df["latlong"][i] = f"{df['Latitude'][i]},{df['Longitude'][i]}"    
        
    df = df.drop(columns=['Latitude', 'Longitude'])
        
    return df

    

df = getMoreBeaches("43.479472","-3.80868")


