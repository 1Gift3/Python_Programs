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


# WHAT
# It takes Stored username and password as exsisting user credentials
# User is then prompted to enter username and password
# should the entered username and password match the stroed ones, then the user is logged in.
# Otherwise an error message is displyed

# WHY
# In real world applications, but passwords should be hashed and stored securely instead of plain text

# HOW
# Can be useed to getpass for secure input
# Used for a dict for multiple users to store their names and passwords
# limit login attempts by preventing brute force attacks by adding a limit on incorrect atttempts.


