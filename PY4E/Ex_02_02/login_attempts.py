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


# WHAT
# Max_attempts acts as a max attempt where the user is allowed to try to log in certatian number of time before being locked out temporarily
# Lock_time checks if the users exceeds the max number of login attempts(max_attempts), which will temorarily lockout for a specified period which is set to 10 ses and during this time you cant attempt to log in
# Then the program keeps track of number of incorrect attempts and enforeces the limit on failed logins.

# WHO
# Can be used to prevent brute force attacks 
# By limiting attempts after a certain number of failed login attempts, where the system temporarily locks the user out.
# Delaying between attempts enforcing delay (time.spleep()) between repeated login attempts forces attackers to  wait, slowing down brute force attempts significantly.

# WHY
# Can be used to protect user accounts fro Unauthorized access
# Redusing risk of account compromise
# Mitigating distributed attacks
# Preventing automated attacks
# Ensurinfg fair access and reducing system load
# encouraging strong passwords
# improving user trust




