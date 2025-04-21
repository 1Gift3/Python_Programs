# Simple educational platform grading system

# WHAT
# The grading tool accepts a students test score between 0.0 and 1.0
# Converts that score into a letter grade A and F
# Stores and displays the result like a mini dashboard
# It takes a score input when the user enters a score like 0.85 or anything. its then converted into a float
# it then converts the score into a grade, if the score is not inthe vaalid range like 1.1 or -0.2 it prints an error message
# results are then stored putting the score and grade in a dictionary
# Then lastly it displays a dash board



# Getting input from user
score = float(input("enter score (between 0.0 and 1.0): "))

# determining grade based on score
if 0.0 <= score <= 1.0:
    if score >= 0.9:
        grade = "A"
    elif score >= 0.8:
        grade = "B"
    elif score >= 0.7:
        grade = "C"
    elif score >= 0.6:
        grade = "D"
    else:
        grade = "F"

# Storing results ( and could also be saved to a data base in a real app) 
    student_result = {
        "Score" : score,
        "Grade" : grade
    }           

# Display results simulating a dash board
    print("\n--- Student Dashboard ---")
    print(f"Score: {student_result['score']}")
    print(f"Grade: {student_result['Grade']}")

else:
    print("Error: Please enter a score between 0.0 and 1.0")



# HOW 
# can be used in a class room or a E-learning platform
# Its logic can be put into a mobile app or django for students to check their scores
# Can be useful for practice projects or portfolio build
# to build an automatic grading tool for teachers.

# WHY
# It saves time and reduces Human error
# Automates repetitive work
# Helps track student perfomances
# easy to scale and upgrade
# And Great tool for devs to learn
