# typical way of retrieving a geocoder class 
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Setting up geocoder
geolocator = Nominatim(user_agent="geo_backend_dev")

# Input name and city
name = input("Enter your name:")
city = input("Hi there "  + name +  "! Enter a city name:")

#Geocode the city to get coodinates
location = geolocator.geocode(city)

if location: 
    user_coords = (location.latitude, location.longitude)
    # Reference points : Lets say your HQ is in Zweni
    hq_coords = (-26.563404, 27.844164)

    distance = geodesic(user_coords, hq_coords).kilometers

    print(f"{city} is about {distance:.2f} km from our HQ in Zweni.")
else:
    print("Couldn't find that Location. Try Again.")

# I had an interest in fixing this space in print ( Line 10)
# So what was missing was that a little space was needed in my String concactenation
# This is important using concactenation in python - especially with input() prompts or any facing messages, as the spacing becomes super important for making the text readable
# Another way i could use string format - which i tried at first, but needed do delve in why its not working.
# But heres a way 
# - city = input(f"Hi there {name}! Enter a city name:")

# Maybe calculate real distance Like joburg or vanderbijilpark
# For this geocode needs to be looked at, as in the moment it says couldnt find location, try again.
# So What needed to be done was to change hq ordinates, then on the code it will ask you to input city then you can play around
# But seems like my calculations are not correct.
# - How this was fixed was on line 18 when i first included a minus there which altered my calculations.

