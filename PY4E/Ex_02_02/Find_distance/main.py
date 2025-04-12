# typical way of retrieving a geocoder class 
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Setting up geocoder
geolocator = Nominatim(user_agent="geo_backend_dev")

# Input name and city
name = input("Enter your name:")
city = input("Hi there" + name + "! Enter a city name:")

#Geocode the city to get coodinates
location = geolocator.geocode(city)

if location: 
    user_coords = (location.latitude, location.longitude)
    # Reference points : Lets say your HQ is in New York
    hq_coords = (40.7128, - 74.0060)

    distance = geodesic(user_coords, hq_coords).kilometers

    print(f"{city} is about {distance:.2f} km from our HQ in NYC.")
else:
    print("Couldn't find that Location. Try Again.")

# I first installed geopy as i havent used it before but was applying a print hello script into geospatial

# Now in geopy 
# - Nominatim - is for geocoding(Like getting coodinates from place names)
# geodesic or great_cirle - is for calculating distances

# Basic Usage flow
# Now geocode a location : converts a city/place name to latitude and longitude
# Reverse geocode: It converts coordinates back into a place name
# Measure distances: Calculates how far two locations are in kilometers or miles

# Important notes 
# - Always pass a user_agent string when initializing Nominatim, or it will give an error
# - geopy uses online services(Like OpenstreetMap), so it requires internet access
# - Also you must be aware of rate limits if you're doing many requests

# WHAT
# The script accepts a place name 
# converts it to coordinates(geocoding)
# Calculates distance from a fixed point
# And uses geospatial libraries like geopy

# It asks the user to enter their name and city
# The input is then passed to the geopy geocoder to get its geographical coordinates (lat or longi)
# the code then calculates the distance from the city you input to a fixed reference point
# It then prints the result(distance)back to the user


# WHY
# geopy - It provides me with foundational understanding of geo data handling
# Using geocoding helps to know coordinates of a place, lets us do eveyrthing from building location-aware app to integrating maps
# Can help also in being a starting point for any geospatial analysis e.g distance between two places, mapping,route planning
# geodesic method helps calculate between two sets of coordinates

# HOW
# It can be useful for travel and navigational services - like trip planning app etc
# Can be used for Logistics and shippings
# Real estate webistes too for properties to cal between a property and schools,hospitals, shopping centres etc
# Geospatail analytics - for data science or analytics.
# Tourism or event based app - like finding current location and recommedations or for an event based applications calculating how far someone is from n event or venue

#  Expanding it
# API version
# It can be made into a web service, so users can send city names through an http request and get distance back as json responses

# Adding more data
# - Adding more features, like population data,weather, or tourist info when user enter a city, all based on the location
# Intergrate into other projects
# - Using distance cal in applications that need location based decisions
# - Mobile app where users check distances from their current location to nearby places etc
 
# GEOPY Documentation
# https://geopy.readthedocs.io/en/stable/