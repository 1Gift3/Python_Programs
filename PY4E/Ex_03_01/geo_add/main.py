# Now in here i was trying toadd geospatial concepts into my basic pay cal
# imagining a scenario where a company tracks the loc of its emplyess and their working hours

# Driver logs hei/hhis hours worked while travelling across diff areas
# Employee might also have dff pay rates depending on the region

# So we can build on eisting code by introducing geosetial component such as gps coordinates and applying based rules.
# - location based pay cal
# - geospatial filtering

# To modify the code lets assume
# We have a geospatial location with (long and latitude) for work 
# A higher pay rate applies to locations 
# gps coordinates are used to determince if employees was in a specific zone
# using libraries like
# - geopy
# - shapely : for grometric operations ( like checking if a point is within a certain area)
# - geopandas : to manipulate geo data and intergrate it with pandas


from geopy.distance import geodesic

hours = input("Enter hours worked: ")
usr_rate = input("Enter rate per hour: ")

# Convert inputs to correct data types
ih = int(hours)
fr = float(usr_rate)

# Example locations (lat, lon) — let's assume we have this info for both employee and city center.
employee_location = (40.7128, -74.0060)  # New York City (example)
city_center = (40.730610, -73.935242)   # Brooklyn, New York (example)

# Calculate the distance between employee location and city center
distance = geodesic(employee_location, city_center).kilometers

if distance <= 10:
    print("Employeee is in a higher demand area.")
    # Applying bonus rate for employees working near city
    fr = fr * 1.1 # Increasing rate by 10% fir high demand areas

# Pay cal
if ih > 40:
    reg_pay = 40 * fr # Regular pay for the first 40 hours
    otp = (ih - 40) * (fr * 1.5) # Overrtime for hours over 40
    total_pay = reg_pay = otp
else:
    total_pay = ih * fr # regular pay if no overtime
    print(f"Total pay: ${total_pay:.2f}")
    print(f"Employee location: {employee_location}")
    print(f"Distnce to the city center: {distance:.2f} km")

# WHAT
# The functionality of the code is to adjust the pay rate based on how far employee is from a predefined city centre
# It cal's an employees total pay based on hours worked (inputed), hour;y aso (input)
# and whether the employee is working near a specific geographic location
# It also calculates overtime pay
# Checking how far the employee is from a city center using gps coordinates
# applies a pay bonus 10% if the employee is whithin 10 km of that location.

# HOW
# Can be useful for delivery services or urban and rural
# - Differentiating Pay Based on Location: For companies with employees working in various locations, this code allows for a dynamic pay system that changes based on location
# calculating the distance between employee location and city center, businesses can make data-driven decisions
# Field technicians : Tech's who travel to clients locations, could be paid a higher rate if they’re located in remote areas or farther away from the central office.
# Payroll Automation: The code can be extended to track employee hours, work locations, and pay in real time. This can be integrated into payroll systems for automatic payment processing based on their work location and hours worked.

# WHY
# It brings fair compensation based on employee_location
# Introduces location aware payroll system
# Includes oertime logic





