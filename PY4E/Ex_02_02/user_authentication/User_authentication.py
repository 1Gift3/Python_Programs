# Predefines username and password
stored_username = "admin"
stored_password = "password1234"

# Asks user for credentials
username = input ("Enter your username:")
password = input("Enter your password:")

# verifying credentials
if username == stored_username and password == stored_password:
    print(f"Welcome, {username}! You are successfuly logged in. 🎉")

else:
    print("Invalid username or password. Please try again. 👎")    



