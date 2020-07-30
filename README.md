<img src="INPUT/thereadmeboyz.png"> 

            
            An API to find the perfect wave

        By Umberto Sajonia Coburgo and Alfredo Pla

## How it works
We have created an API that requires three inputs to function:
- The user's location.
- The user's email.
- The user's surf skills.

Knowing the users location, our program returns the a list of the beaches that are within a 50 mile radius of the user's provided location. Not only that we suggest what we believe is the best beach for the user's surfing level within the 50 km radius. To do so we created a rating system that takes into account the quality of the waves and their consistency by giving points for each characteristic. In addition to giving the nearest beaches we provide the user with additional information about all the beaches. We provide characteristics about the beach as well as real time information on the relevant weather points. The information includes:
​
- Address: The specific address of the beach
- The wave direction: This can be a left, right or both
- Experience: This provides the recommended surfer level
- Bottom: What the seabed is made of and how the wave forms
- Best Wind: The ideal wind direction
- Best Swell: The ideal swell direction
- latlong: The exact coordinates of the beach
- Swell Height: Size of the swell
- Swell Direction: Actual direction of the swell
- Swell Period: The period of the swell
- Wind Speed: Actual wind speed in that moment.
- Wind Direction: Actual wind direction
- Water Temperature: Actual water temperature
- Weather Description: A brief description on the actual weather.
​
Finally, the email account (second input) is used to send a PDF with the most important real-time information to the user.
​
## Where do we get out information?
​
We transform the users location to coordinates using the gocode.xyz API that can be found here:
- https://geocode.xyz
​
We extract the closest beaches and their ideal conditions from the SurfCheck API that can be found here:
- https://documenter.getpostman.com/view/6379421/SVfH1CeA?version=latest
​
We exctract real time weather information from an API that can be found at: 
- https://www.worldweatheronline.com/developer/api/marine-weather-api.aspx
