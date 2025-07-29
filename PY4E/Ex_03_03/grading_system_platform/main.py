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



score = float(input("Enter score (between 0.0 - 1.0): "))

if 0.0 <= score <= 1.0:
    if score >= 0.9:
        grade = "A"
    elif score >= 0.08:
        grade = "B"
    elif score >= 0.7:
        grade = "C"
    elif score >= 0.06:
        grade =  "D"

    else: grade "F"            

