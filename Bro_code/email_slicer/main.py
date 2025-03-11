email = input("Enter your email: ")

index = email.index("@")

username = email[:index]
domain = email[index + 1:]

print(f"Your username is {username} and domain is {domain}")

# i dont understant quiet well what index is -

# Indexing helps me to find the @ symbol positions while the sclicing extracts parts of it
# the []:index] gets everything before @ then the [+ 1:]after the @ 

# Its because it lets use easily access specific elements in a list []
#  # list_name [start:end: step]
# - This step is useful because it specifys the interval between elemnts dafault to 1 if ommited
# List slice allows outof bound indexing without errors - we simply specify indicies beyond length then it will return the available


# It can be used by [::]
#  - in simple is get every [::2] second element from the list
# - the []:index] gets everything before @ then the [+ 1:]after the @ 
# Another way that it can be used is using negative indexing accessing elments from the end of list -1, -2.
# We can also reverse the entire list by using [::-1] - indicates that Python should traverse the list in reverse order, starting from the end. The slice a[::-1] starts from the end of the list and moves to the beginning which result in reversing list


# It lets us easily access specific elements in a List[]
