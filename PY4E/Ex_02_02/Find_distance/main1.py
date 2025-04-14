from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Set up the geocoder
geolocator = Nominatim(user_agent="geo_backend_dev")

# Get coordinates for Sebokeng
sebokeng_location = geolocator.geocode("Sebokeng, South Africa")
vanderbijlpark_location = geolocator.geocode("Vanderbijlpark, South Africa")

if sebokeng_location and vanderbijlpark_location:
    sebokeng_coords = (sebokeng_location.latitude, sebokeng_location.longitude)
    vanderbijlpark_coords = (vanderbijlpark_location.latitude, vanderbijlpark_location.longitude)

    distance = geodesic(sebokeng_coords, vanderbijlpark_coords).kilometers

    print(f"The distance from Sebokeng to Vanderbijlpark is approximately {distance:.2f} km.")
else:
    print("Could not find one or both locations.")

# In this code i am cal distance to sbk to vander...but what next i want is to change name location to place.
