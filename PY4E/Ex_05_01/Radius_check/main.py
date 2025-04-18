# WHAT
# Now Here this script gos with closest city finder just that now we checking if we are within a radiu(geofencing)
# You input your current loaction
# The program checks if your location is within the defined radius from a target city
# If you are within the radius, the program says youre inside otherwise it says your outside

from geopy.distance import geodesic

# Function to check if user is within a certainradius of a city
def is_within_radius(user_location, city_coords, radius_km):
    distance = geodesic(user_location, city_coords).kilometers
    if distance <= radius_km:
        return True, distance 
    else:
        return False, distance

# User input for location
lat = float(input("Enter your latitude: "))
lon = float(input("Enter your longitude: "))
user_location = (lat,lon) 

# City coord from cpt
cape_town_coords = (-33.9249, 18.4241)

# Checking if user is within 50 km of cpt
radius = 50 
is_inside, distance = is_within_radius(user_location, cape_town_coords, radius)

# Output the result
if is_inside:
    print(f"You are inside the {radius} km radius of CPT, {distance:.2f} km away.")

else:
    print(f"You are outside the {radius} km radius of CPT, {distance:.2f} km away. ")    


# Next Steps
# Web Version (API): You can take this code and turn it into a web service using Flask or FastAPI to return distances or proximity to multiple users.
# Real-time GPS: If you're working with hardware (Raspberry Pi, Arduino), you can plug in real GPS data instead of user input.

