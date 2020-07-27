import json
import requests
from datetime import datetime
import pprint
import pandas as pd

def getSwellHeight(latlong):
    key = "4bf49534c534477aa8a80201202707"
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
    key = "4bf49534c534477aa8a80201202707"
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
    key = "4bf49534c534477aa8a80201202707"
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
    key = "4bf49534c534477aa8a80201202707"
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


def getSwellPeriod(latlong):
    key = "4bf49534c534477aa8a80201202707"
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
    key = "4bf49534c534477aa8a80201202707"
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
    key = "4bf49534c534477aa8a80201202707"
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
        
