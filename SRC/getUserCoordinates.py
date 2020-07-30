import requests

def geocode(location):
    """
        A function where you enter a string and it returns the latitude and longitude
    """

    res = requests.get(f"https://geocode.xyz/{location}", params={"json":1})
    data = res.json()
    return {
        "type":"Point",
        "coordinates":[float(data["longt"]),float(data["latt"])]
    }

def getCoords(location):
    """
        A function that returns the lat and long 
    """

    try:
        my_coordinates = geocode(location)
        return my_coordinates["coordinates"]
    except:
        return -4.29151, 43.3856