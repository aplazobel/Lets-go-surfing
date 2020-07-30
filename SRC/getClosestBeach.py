import json
import requests
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()

email = os.getenv("EMAIL")
token = os.getenv("TOKEN_SURFCHECK")

def getMoreBeaches(lat, longt, experience_input):

    """
        Firstly, this function is in charge of the API request to get the closest beaches to the
        location inputted by the user. Secondly, this function ranks the beaches from best to worst, 
        based on some parameters such as the experience level inputted by the user, the frequency of the waves,
        and the quality of the waves.
    """
    # URL for the API request
    url = f"https://surfvideos.xyz/locations.json?latitude={lat}&longitude={longt}&distance=20"

    # Credentials needed for the API request
    payload = {}
    headers = {
    'X-User-Email': email,
    'X-User-Token': token,
    'Accept': '{{Accept}}',
    'Content-Type': '{{Content}}'
    }

    response = requests.request("GET", url, headers=headers, data = payload)
    data = response.json()
    
    # IMPORTANT STEP: Creating a dataframe with one row per beach. Each column is one param, check below
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
    
    # Replacing the names of the columns with real, recognizeable names
    df = df.rename(columns={0: 'Name', 1: 'Address', 2: 'Direction', 3: 'Experience', 4: "Wave quality", 5: "Frequency", 6: 'Bottom', 7: 'Best wind', 8: 'Best swell', 9: "Latitude", 10:"Longitude"})
    df["latlong"] = None
  
    # Creating another column with lat and long joined together. This will be needed for a second API we use
    for i in range(df.shape[0]):
        df["latlong"][i] = f"{df['Latitude'][i]},{df['Longitude'][i]}"  

    # Creating columns with ints instead of strings: The higher the int, the better the beach
    # This will help us in getting a score for each beach
    cleanup_cols = {"Wave quality_num":     {"Totally Epic": 4, "World Class": 3, "Regional Classic": 2, "Normal": 1, "Sloppy": 0},
                "Frequency_num": {"Very consistent (150 day/year)": 4, "Regular": 3, "Sometimes break": 2, "Rarely break (5day/year)": 1,
                                  "Don't know": 1 }}

    #df = df[df['Wave quality'].notna()]
    #df = df[df['Frequency'].notna()]

    df["Wave quality_num"] = df["Wave quality"]
    df["Frequency_num"] = df["Frequency"]

    df.replace(cleanup_cols, inplace=True)

    # Getting a score in column 'Score'
    df["Score"] = df["Wave quality_num"] + df["Frequency_num"]
    df = df.drop(['Wave quality_num', 'Frequency_num'], axis=1)

    # Sorting rows by Score. If they have the same score, they are sorted by how far away they are from the user
    df = df.sort_values(by=['Score'], ascending=False)

    # This series of conditions sort the dataframe based the experience of the user
    if experience_input == "Beginner":
        new_df = df[(df['Experience'] == "Beginners wave")|(df['Experience'] == "All surfers")]
    elif experience_input == "Experienced":
        new_df = df[(df['Experience'] == "All surfers")|(df['Experience'] == "Experienced surfers")]
    elif experience_input == "Advanced/Pro":
        new_df = df[(df['Experience'] == "All surfers")|(df['Experience'] == "Experienced surfers")|(df['Experience'] == "Pros or kamikaze only...")]

    return new_df.head()
 





