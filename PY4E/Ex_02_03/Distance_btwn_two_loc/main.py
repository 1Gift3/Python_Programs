from geopy.distance import geodesic

# Coordinates : 
location1 = ( -26.2041, 28.0473) # Joburg
location2 = ( -33.9249, 18.4241) # CPt

distance_km = geodesic(location1, location2).kilometers
print(f"Distance: {distance_km:.2f} km")


# WHY
# Can be useful for Business owners to calculate wages manually

# HOW
# Can help with calculating distance based pay,
# estimate dilivery costs
# Generating distance based bills
# Tracking driver earnings overtime
# and optimizing routes based on payouts

# geodesic or great_cirle - is for calculating distances
