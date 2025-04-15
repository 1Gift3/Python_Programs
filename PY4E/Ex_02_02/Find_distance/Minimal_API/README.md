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


