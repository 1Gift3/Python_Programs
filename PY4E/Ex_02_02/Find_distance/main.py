# typical way of retrieving a geocoder class 
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Setting up geocoder
geolocator = Nominatim(user_agent="geo_backend_dev")

# Input name and city
name = input("Enter your name:")
city = input("Hi there"  + name +  "! Enter a city name:")

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

# Have an interest in fixing this space in print ( Line 10)
# Maybe calculate real distance Like joburg or vrega