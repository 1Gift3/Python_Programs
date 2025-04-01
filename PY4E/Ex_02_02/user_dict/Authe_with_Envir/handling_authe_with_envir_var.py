# To avoid hardcoding your username and password, it's a good practice to use environment variables. This approach is more secure and flexible.

import os 
import requests
from requests.auth import HTTPBasicAuth

# Loading credentials from envir variables
username = os.getenv('API_USERNAME')
password = os.getenv('API_PASSWORD')

# url for the protectedd resource
url = "https://example.com/protected-endpoint"

#Sending the get request with basic auth
response = requests.get(url, auth=HTTPBasicAuth(username, password))

# Check the response
if response.status_code == 200:
    print("successfully authenticated!")
    print(response.text)
else:
    print(f"Failed to authenticate. Status code: {response.status_code}")


# Before running this, make sure you set the environment variables API_USERNAME and API_PASSWORD on your system.    
# On Windows, you can set environment variables in the system settings or via command prompt:

#set API_USERNAME=your_username
#set API_PASSWORD=your_password

#Storing sensitive data (like usernames and passwords) directly in your code is not a good practice, especially in production environments. Using environment variables can help protect these credentials and make your code more secure.


# WHY
# Security resonses , as stroring credentials int he code can expose sensitive data.
# Portability, using envir var makes sure your code is more portable.
# And flexibility which envir variables can easily be managed through deployments tools, CI/CD pipelines or configuration management systems, providing flexibility when working in cloud or enterprise envir 

# HOW
# In porduction environments keeping always credentials secure
# When working with multiple envir.