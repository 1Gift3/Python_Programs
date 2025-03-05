email = input("Enter your email: ")

index = email.index("@")

username = email[:index]
domain = email[index + 1:]

print(f"Your username is {username} and domain is {domain}")

# i dont understant quiet well what index is -

# Indexing helps me to find the @ symbol positions while the sclicing extracts parts of it
# the []:index] gets everything before @ then the [+ 1:]after the @ 