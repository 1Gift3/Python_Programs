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


# HOW
# Stored username and password act as exsisting user credentials
# The user is then prompted to enter username and password
# should the entered username and password match the stroed ones, then the user is logged in.
# Otherwise an error message is displyed

# In real world applications, passwords should be hashed and stored securely instead of plain text
# Can use getpass for secure input
# Use a dict for multiple users to store their names and passwords
# limit login attempts by preventing brute force attacks by adding a limit on incorrect atttempts.

