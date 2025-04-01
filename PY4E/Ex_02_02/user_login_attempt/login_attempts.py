import time

users_db = {
    "admin": "password1234",
    "user1": "mypassword1",
    "user2": "mypassword2,"
}
# maximum number of attempts allowed
MAX_ATTEMPTS = 3
LOCK_TIME = 10  # Time in seconds that the user will be locked out after exceeding MAX_ATTEMPTS

def register_user():
    username = input("Enter your new username: ")
    password = input("Enter your new password: ")

    if username in users_db:
        print("Username already taken.try another one.")
    else: 
        users_db[username] = password
        print(f"User {username} successfuly registered!")

# Function to log in a user 
def login_user():
    # asking for credentials
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # track the numb of failed login attempts
    attempts = 0 

    # Attempt login until the max number of attempts is reached
    while attempts < MAX_ATTEMPTS:
        if username in users_db and users_db[username] == password:
            print(f"Welcome, {username}! You have successfuly logged in. -🎉")
            break
        else:

            attempts += 1
            print(f"Invalid username or password.Attempt {attempts} of {MAX_ATTEMPTS}. Please try again. 👎 ")
        
            if attempts == MAX_ATTEMPTS:
                print(f"Too many failed attempts. Please try again after {LOCK_TIME} seconds.")
                time.sleep(LOCK_TIME) # Lock the user for the defined time in secs
                print("You can now try again.")
                break
# Main menu
while True:
     print("1. Register")
     print("2. Login")
     print("3. Exit")
     choice = input("Enter your choice:")

     if choice == "1":
          register_user()
     elif choice == "2":
        login_user()
     elif choice == "3":
         break
     else:
         print("Invalid choice. Try again.")    





