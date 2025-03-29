# Predefined a dict to store usernames and passwords

users_db = {
    "admin": "password1234",
    "user1": "mypassword1",
    "user2": "mypassword2,"
}

# Asking the user for credentials
username = input("Enter your name: ")
password = input("Enter your password: ")

# Verify credentials
if username in users_db and users_db[username] == password:
    print(f"Welcome, {username}! You have successfuly logged in. 🎉")
else: 
    print("Invalid username or password. Please try again. 👎")    


# WHAT
# The dict users_db stores the usernames as keys and their corresponding passwords as values
# The code then checks if the entered username exists as a key in the dict (users_db)
# - if the username is found, it then checks if the entered password matces the stored assword for that username
# Should both username and password match the stored values the user is loggen d in and a success message is displayed
# - should the username or the password be incorrect an error message will be shown

# WHY
# It provides a way to authenticate users in a program (simple), its the foundational concept of building login systems
# A dict based approach allows for easy management of user credentials espcially in small programs

# HOW
# I can use it if im building a command line tool that requres to log-in( to access or manage local databse).
# Can use it for practicing basic authentication concepts
# And can used if one is prototyping a new feature or testing a small app where complpex user authentication systems arent needed.

