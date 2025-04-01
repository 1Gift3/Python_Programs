import requests
from requests.auth import HTTPBasicAuth

#Define the url and user credentials
url = "https://examples.com/protected-endpoint"
username = "your_username"
password = "yor_password"

# sending a get request with basic authentication
response = requests.get(url, auth=HTTPBasicAuth(username, password))

# CHECK the response
if response.status_code == 200:
    print("successfully authenticated!")
    print(response.text) # printing the response from the server

else: 
    print(f"Failed to authenticate.Status code: {response.status_code}")

# WHAT
# It is an easy way to work with requests and handle authentication
# HTTPB is used to create the basic authentication headers
# the requests.get() method then sends the request with the appropriate authentication
# Then th e response.status.code checks to ensure the authentication was successsful (HTTP 200 is a success code)

# WHY
# the request library abstracts away much of the low-level handling of http requests and headers, making the code more readable and easier to maintain. and the httpbasicauth class automatically formats the authentication header for me
# Should your authentication flow involve multiple requests(such as maintaining a login session across different pages), requests has a built in support for handling cookies and sessions making it easty to work with subsuqeunt requests once authenticated
# The requets lib is one of the most popular for making http  requests in python,
# And the requests provided good error handling machanisms, such automatically retrying on failure, catching exceptions and making it easy to inspect the staus code and response.

# HOW
# When needing a quick and easy solution : if you're interacting with apis or making http requests with basic auth and dont need low level control over http operations requests is a perfect fit
# If your task invlolves interacting with forms uploading files handling redirects or working with sessions, requests provides high level tools tol handle these

