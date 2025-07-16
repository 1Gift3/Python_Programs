# Predefined a dict to store usernames and passwords

users_db = {
    "admin": "password1234",
    "user1": "mypassword1",
    "user2": "mypassword2",
}

# Asking the user for credentials
username = input("Enter your name: ")
password = input("Enter your password: ")

# Verify credentials
if username in users_db and users_db[username] == password:
    print(f"Welcome, {username}! You have successfuly logged in. 🎉")
else: 
    print("Invalid username or password. Please try again. 👎")    



