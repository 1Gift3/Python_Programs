import http.client 
import base64


# defines connection and credentials
conn = http.client.HTTPSConnection("example.com")
username = "your_username"
password = "your_password"

# Preparing the authrization header
auth_value = base64.b64encode(f"{username}:{password}".encode('utf-8')).decode('utf-8')
headers = {
    'Authorization': f'Basic {auth_value}'
}


# Sendinf Get request with basic authentication
conn.request("GET", "/protected-endpoint", headers=headers)

# Get the response
response = conn.getresponse()

# Printing the response
if response.status == 200:
    print("Successfully authenticated!")
    print(response.read().decode()) # Print the response body

else:
    print(f"Failed to authenticate. Status code: {response.status}")
    
# Closing the connection
conn.close()

# WHAT
# We manually encode the username and password in Base64 using base64.b64...
# the authorization header is set manually to include the base64 encoded username and password
# And we send the GET request using conn.request() and process the response

# WHY
# is a low level lib for http communication, giving a more granular control over requests and response
# its part of the python standard lib, so theres no need to install externall dependenciesl. This is important if youre working in envir where adding third party lib like requests is not feasible
# If you need to manually manipulate headers, cookies or other components of the http request, http.clioent provides a more hands on way to do so. you can encode the credentials yourself which is useful for understanting the inner workings of http basic auth
# It gives you more insight into inner workings of https,including headers,status codes and connectiion info. useful for debugging or building custom behaviou on specific responses.

# HOW
# When you need more control, to customise the way requests and response are handles such as connection pooling,headers or managing specific htttp statuses it offers control
# When you dont want external dependencies like working in an envir wheere i cant install third part lib.
# Whne im implimenting comlex http workflows like building http clients, handling low level inteactions with apis, or dealing with a non standard api, http.client allows for fine tuned control over your requests.

