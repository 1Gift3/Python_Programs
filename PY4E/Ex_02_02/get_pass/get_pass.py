import getpass

# Prompts the user for a secure password input
password = getpass.getpass("Enter your password:")

# Print the password length for demonstration purposes
print(f"Password has {len(password)} characters.")

