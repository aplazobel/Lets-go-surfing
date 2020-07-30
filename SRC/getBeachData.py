import json
import requests
from datetime import datetime
import pprint
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()

key = os.getenv("KEY")
# getTime(current_time)
def getSwellHeight(latlong):
    """
        Each of these functions does the same thing. We add data to the dataframe
    
    """
    key = os.getenv("KEY")
    url = f"http://api.worldweatheronline.com/premium/v1/marine.ashx?key={key}&format=json&q={latlong}"

    res = requests.get(url)
    data = res.json()

    now = datetime.now()
    current_time = now.strftime("%H" + "00")
    current_time = int(current_time)

    def getTime(current_time):
        for i in (data["data"]["weather"][0]["hourly"]):
            if current_time <= int(i["time"]):
                return(i["time"])

    for i in data["data"]["weather"][0]["hourly"]:
        if i["time"] == getTime(current_time):
            return i["swellHeight_m"]


def getWindDir(latlong):
    key = os.getenv("KEY")
    url = f"http://api.worldweatheronline.com/premium/v1/marine.ashx?key={key}&format=json&q={latlong}"

    res = requests.get(url)
    data = res.json()

    now = datetime.now()
    current_time = now.strftime("%H" + "00")
    current_time = int(current_time)

    def getTime(current_time):
        for i in (data["data"]["weather"][0]["hourly"]):
            if current_time <= int(i["time"]):
                return(i["time"])

    for i in data["data"]["weather"][0]["hourly"]:
        if i["time"] == getTime(current_time):
            return i["winddir16Point"]


def getSwellDir(latlong):
    key = os.getenv("KEY")
    url = f"http://api.worldweatheronline.com/premium/v1/marine.ashx?key={key}&format=json&q={latlong}"

    res = requests.get(url)
    data = res.json()

    now = datetime.now()
    current_time = now.strftime("%H" + "00")
    current_time = int(current_time)

    def getTime(current_time):
        for i in (data["data"]["weather"][0]["hourly"]):
            if current_time <= int(i["time"]):
                return(i["time"])

    for i in data["data"]["weather"][0]["hourly"]:
        if i["time"] == getTime(current_time):
            return i["swellDir16Point"]


def getWindSpeed(latlong):
    key = os.getenv("KEY")
    url = f"http://api.worldweatheronline.com/premium/v1/marine.ashx?key={key}&format=json&q={latlong}"

    res = requests.get(url)
    data = res.json()

    now = datetime.now()
    current_time = now.strftime("%H" + "00")
    current_time = int(current_time)

    def getTime(current_time):
        for i in (data["data"]["weather"][0]["hourly"]):
            if current_time <= int(i["time"]):
                return(i["time"])

    for i in data["data"]["weather"][0]["hourly"]:
        if i["time"] == getTime(current_time):
            return i["windspeedKmph"]

#getTime(current_time)
def getSwellPeriod(latlong):
    key = os.getenv("KEY")
    url = f"http://api.worldweatheronline.com/premium/v1/marine.ashx?key={key}&format=json&q={latlong}"

    res = requests.get(url)
    data = res.json()

    now = datetime.now()
    current_time = now.strftime("%H" + "00")
    current_time = int(current_time)

    def getTime(current_time):
        for i in (data["data"]["weather"][0]["hourly"]):
            if current_time <= int(i["time"]):
                return(i["time"])

    for i in data["data"]["weather"][0]["hourly"]:
        if i["time"] == getTime(current_time):
            return i["swellPeriod_secs"]


def getWaterTemp(latlong):
    key = os.getenv("KEY")
    url = f"http://api.worldweatheronline.com/premium/v1/marine.ashx?key={key}&format=json&q={latlong}"

    res = requests.get(url)
    data = res.json()

    now = datetime.now()
    current_time = now.strftime("%H" + "00")
    current_time = int(current_time)

    def getTime(current_time):
        for i in (data["data"]["weather"][0]["hourly"]):
            if current_time <= int(i["time"]):
                return(i["time"])

    for i in data["data"]["weather"][0]["hourly"]:
        if i["time"] == getTime(current_time):
            return i["waterTemp_C"]


def getWeatherDescription(latlong):
    key = os.getenv("KEY")
    url = f"http://api.worldweatheronline.com/premium/v1/marine.ashx?key={key}&format=json&q={latlong}"

    res = requests.get(url)
    data = res.json()

    now = datetime.now()
    current_time = now.strftime("%H" + "00")
    current_time = int(current_time)

    def getTime(current_time):
        for i in (data["data"]["weather"][0]["hourly"]):
            if current_time <= int(i["time"]):
                return(i["time"])

    for i in data["data"]["weather"][0]["hourly"]:
        if i["time"] == getTime(current_time):
            return i["weatherDesc"][0]["value"]
        
