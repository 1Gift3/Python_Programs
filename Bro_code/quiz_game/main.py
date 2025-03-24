questions = ("How many elements are in the periodic table?: ",
            "Which animal lays the largest eggs?: ", 
            "What is the most abundand gas in Earths atmosphere?: ", 
            "Which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon_dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C.208", "D.209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0 
question_num = 0

for question in questions: 
    print(" --------------")
    print(question)
    for option in options[question_num]:
        print(option)


    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print('correct')
    else:
        print("Incorrect!!!")
        print(f"{answers[question_num]} is the correct answer")    
    question_num += 1    


print(" --------------")
print("    RESULTS    ")
print(" --------------")


print("anwers: ", end="")
for answer in answers: 
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses: 
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your Test score is: {score}%")

# WHY
# It is useful for learning, skill dev and even practical applications 
# It reinforces knowledge in varioous subjects, engaging way to learn and memorize facts, and also it is made useful for teaching aid making mor e interactive.
# Can be a great way to practise fundamentals variable,conditionals, loops and functions
# Great way to also practise data structures lists dict or databases to store questions and answers
# It can also be used in real world applications - elearning platforms, gamification and entertainment : Trivia games
# Lastly  its knowledge can be expanded in web dev to build web-based versions of it using django and deploy online.
# Data base intergration to store questions ans answers and APIs to amke its data accessible via rest api

# HOW 
# Can used as a learning and self assessment to test your knowledge, skill dev and exam preparance
# can be used for reasearch and surveys to collect data and analytics
# Can use it to expand it to mobile app suing framework like React native or flutter.
#  Can be used as a technical interview preparations with coding questions


# WHAT
# Its an interactives program where a users answers questions to test their knowledge on a specific topic.
# It asks questions, collects the answers and provide feedback based ont he users response 
# It displays the question to the player
# Asks the user to input answer(input)
# It compares the players answer to the correct answer.
# Trackes the players score based on the correct or wrong answers
# Responds to the player if right or wrong 
# And it then displas the final score

