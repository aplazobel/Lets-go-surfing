import urllib.request, json
from dotenv import load_dotenv
load_dotenv()
import os


def getDirections(orig, dest):
    #Google MapsDdirections API endpoint
    endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
    api_key = os.getenv("GOOGS")
    #Asks the user to input Where they are and where they want to go.
    origin = orig.replace(' ','+')
    destination = dest.replace(' ','+')
    #Building the URL for the request
    nav_request = 'origin={}&destination={}&key={}'.format(origin,destination,api_key)
    request = endpoint + nav_request
    #Sends the request and reads the response.
    response = urllib.request.urlopen(request).read()
    #Loads response as JSON
    directions = json.loads(response)

    html_string = ''

    for num in directions["routes"][0]["legs"][0]["steps"]:
        html_string += num['html_instructions']+"\n"
        
    return html_string

    