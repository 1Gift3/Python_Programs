principle = 0 
rate = 0 
time = 0 

while True:
    principle = float(input("Enter the principle amount:"))
    if principle < 0 :
        print ("Principle cant be less than zero")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        
        print("Interest rate cant be less than zero")
    else:
        break    

while True:
    time = float(input("Enter the time in years: "))
    if time < 0:
        
        print("Interest rate cant be less than zero")        
    else:
        break
total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} years/s: R{total:.2f}")

# This has two way of working it with While True and another first way

# While statements are used for repeated execution as long as expression it true
# - If its true it execute if flase the suit of the else clause if present is executed and the loop terminates

# Break statement is executed after executing else clause

# What it does allow me to do here is to if its supports the clause thats is the inputed by user is less than zero print statement else: break to the following loop state
