print ("\t\t\t\t\t\tQuiz test\n")
name = input("Enter your name :")
age = int(input("Enter your age : "))
country = input("Enter your country :")
print("\n")
score = 0
q1 = input("1. Number of letters in Tamil : ")
if q1 == "247":
    score += 1
else: 
    print("wrong answer\nCorrect answer : 247\n")
q2 = input("2. Value of pi in 5 significant figures :")
if q2 == "3.1415":
    score += 1
else: 
    print("wrong answer\nCorrect answer : 3.1415\n")
q3 = input("3. number of squaress in a chess board :")
if q3 == "64":
    score += 1
else: 
    print("wrong answer\nCorrect answer : 64\n")
q4 = input("4. Father of python :").lower
if q4 == "guido van rossum":
    score += 1
else: 
    print("wrong answer\nCorrect answer : guido van rossum\n")
q5 = input("5. When was twitter released :")
if q5== "2006":
    score += 1
else: 
    print("Wrong answer \nCorrect answer : 2006\n")
q6 = input("6. 3*3 Rubiks cube world record timing : ")
if q6 == "3.14":
    score += 1
else: 
    print("Wrong answer\nCorrect answer : 3.14\n ")  
q7 = input("7. Total number of elements in a periodic table  :")      
if q7 == "118":
    score += 1
else: 
    print("Wrong answer \nCorrect answer : 118\n ")
q8 = input("8. Total number of thirukkurals  :")      
if q8 == "1330":
    score += 1
else: 
    print("Wrong answer \nCorrect answer : 1330\n ")
q9 = input("9. First ever language spoken by humans  :") .upper     
if q9 == "TAMIL":
    score += 1
else: 
    print("Wrong answer \nCorrect answer : TAMIL ")
q10 = input("10. National language of india  :").lower()      
if q10 != "hindi" or q10 != "english":
    score += 1
else: 
    print("Wrong answer \nCorrect answer : There is no national language for india ")

percentage = score/10 * 100
print(" \nYour score: ", score)
print("\nPercentage :" + str(percentage) + "%")
if score == 10:
    print("Excellent", name, "you scored CENTUM!!!")
elif score <= 3:
    print("Dont worry", name, "maybe this is not the place to show your talent")
elif score >= 7:
    print("Excellent work", name, "you are almost done")
elif score >= 4:
    print("Good work", name , "try again later" ) 
else:
    print(" Someone just hacked  into!!!!")           