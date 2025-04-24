# What changes from the previous code is that we are now using a dict to count how many times each email shows up
# .get(email,) safely gets the current count or returns 0 if its not there yet
# Then at the end we loop thruogh the dict and print each sender with how many time they appeared


fhandle = input("Enter file name: ")
document = open(fhandle)

email_counts = dict()

for line in document:
    if line.startswith("From "):
        words = line.split()
        email = words[1]

        # this counts the freq of each email
        email_counts[email] = email_counts.get(email, 0) + 1

# printing each eamil and its count
for email, count in email_counts.items():
    print(email, count)

print("There were", sum(email_counts.values()), "lines in the file with From as the first word")


