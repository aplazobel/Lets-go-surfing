import requests

def geocode(location):
    res = requests.get(f"https://geocode.xyz/{location}", params={"json":1})
    data = res.json()
    return {
        "type":"Point",
        "coordinates":[float(data["longt"]),float(data["latt"])]
    }

def getCoords(location):
    my_coordinates = geocode(location)
    return my_coordinates["coordinates"]