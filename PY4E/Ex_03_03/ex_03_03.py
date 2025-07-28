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


