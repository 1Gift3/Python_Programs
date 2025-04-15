from fastapi import FastAPI, Query
from geopy.geocoders import Nominatim
from geopy.distance import geodesic 
from fastapi.responses import JSONResponse

app = FastAPI()
geolocator = Nominatim(user_agent="geo_backend_dev")

HQ_COORDS= (-26.563404, 27.844164)

@app.get("/distance_to_zweni")
def distance_to_zweni(city: str = Query(..., description="City to calculate distance from Zweni HQ")):
   location = geolocator.geocode(city)

   if not location:
      return JSONResponse(status_code=404, content={"error": "Location not found."})
    
   user_coords = (location.latitude, location.longitude)
   distance_km = geodesic(user_coords, HQ_COORDS).km


   return {
      "city": city,
      "coodinates": {
         "latitude": location.latitude,
         "longitude": location.longitude
      },
      "distance_to_zweni_km": round(distance_km, 2)
   }

# This is a basic API with one endpoint getting -
# GET /distance_to_zweni?city=Johannesburg
# Now this code uses Geocode the city using geopy
# Calculates the distance to Zweni my HQ
# And returns result as JSON

# But i firstly had to install fastapi
# - I was turning my script into a small web api which Fastapi and uvincorn are there to assist
# pip install fastapi
# Uvicorn is ASGI server that run my fastapi app handling incoming web requests.
# And also had to install uvicorn

# So basically i use Fastapi to define API Logic and use Uvicorn to serve it on localhost ( or deploy it later)

# To run code i Run * python -m uvicorn main:app --reload *
# Then test it in browser http://127.0.0.1:8000/docs

# Questions
# Fastapi query
# JSON

# WHAT
# The script receives a city name
# Geocodes it turning it into GPS coordinates using geopy
# Calculates distance from that point to my HQ Zweni
# Returns the distance in KM

# HOW
# This API can be used by a mobile app to show users hor far they from my base or office
# Can offer location based features
# And allows us to compare locations.
# Can used for a web Portal for logistics company or NGO
# - Entering any city to instantly know proximity to HQ
# - Plan routes or assign workers based on distance
# - Use it in dashboards for regional planning
# Can add this as a backend component
# - into a larger system, to check distance from driver to HQ
# Using it as a notification system.

# WHY
# It makes it accessible from any device not just PC
# Allows other developers to use it
# Makes it scalable - connecting it to 100+ devices at once

# SO now for me i want to intergrate e.g Saloons in Zweni that specialize of specialities around my area



