# WHAT
# Here we are finding th e closest city from your location
# The code takes Lat/long from the user ( can also get this from a GPS sensor in real applications)
# We have a dict of cities with their coordinates which ( we can use to expand this to inlcude more cities)
# The program then uses geodesic to cal the distance between the users locations and each city
# Then it loops through the cities and compares the distance to each city, the closest one geet stored and returned.


from geopy.distance import geodesic
def find_closest_city(user_location, city_list):
    closest_city = None
    closest_distance = float('inf')

    for city, coords in city_list.items():
        distance = geodesic(user_location, coords).kilometers
        print(f"Distance to {city}: {distance:.2f}km")


        if distance < closest_distance:
            closest_distance = distance
            closest_city = city

    return closest_city, closest_distance 

lat = float(input("Enter your Latitude: "))
lon = float(input("Enter your longitude: "))

user_location = (lat, lon)

# List of cities with their coordinates
cities = {
    "Johannesburg": (-26.2041, 28.0473),
    "Cape Town": (-33.9249, 18.4241),
    "Durban": (-29.8587, 31.0218),
    "Pretoria": (-25.7461, 28.1881)
}

# Find closest city
city, distance = find_closest_city(user_location, cities)

# Output the result
print(f"\nThe closest city to you is {city}, which is {distance:.2f} km away")


