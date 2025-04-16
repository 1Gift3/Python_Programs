score = float(input ("Enter score:"))

#print(score)

if score >= 0.9 and score <= 1.0 :
    print("A")   

elif score >= 0.8:
        print("B")

elif score >=0.7:
        print("C")

elif score >=0.6:
        print("D")

elif score < 0.6 and score >= 0.0:
        print("F")

else:
    
    if score >= 1.0 :
        print("Error, Enter between 0.0 and 1.0")

# WHAT
# A simple grading script that takes in a score and prints out a corresponding letter grade based on a scale.
# It prompts the user to input a score between 0.0 and 1.0
# Converts t from string to float
# It then checks which range the score falls into and assigns a grade

# WHY
# It would be useful as it introduces condistional statements
# Teaching range checking
# Demostrating basic input validation
# And great for turning into a function later.

# HOW
# Can be very useful for education platforms taking in stdents test scores
# - Converting them into letter grades
# - storing or displaying results on a dashboard
# As an API grading as a service - where clients use it online to grade sending their scores and getting back a gradde.
# For practice when creating terminal based apps or building small projects with conditions and user input

