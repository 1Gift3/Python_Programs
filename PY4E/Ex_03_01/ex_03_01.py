hours = input("Enter hours:")
usr_rate = input("Enter rate:")

#print(hours, usr_rate)

ih = int(hours)
fr = float(usr_rate)

#print ("ih, fr")

if ih > 40 :
    #print("That's overtime")
    reg_pay = ih * fr
    otp = (ih - 40.0) * (fr * 0.5)
    #print(reg_pay, otp)
    Xy = reg_pay + otp
    print (Xy)    

else:
  #Print ("Reg_pay")
  Xy = ih * fr



# WHAT
# A simple pay cal helping compute weekly earnings of an employee
# Based on number of hours worked and houly rate
# It takes the user input for hours and rate
# Converts input into appropriate data types
# Checks if hours exceeds 40 - which is the standard time for work week
# if yes meaning overritme
# - It then cal's regular pay
# - Calculates overrtime pay 
# - and adds both to get total pay
# if not then it just adds regular pay
# - Multiplies hours by rate
# LAstly it prints total pay

# WHY
# Can be used for a basic payroll cal
# Also is a good excercise for understanding input, if-else, castin and basic arithmetic

# HOW
# Can use it to track one's pay or for small business payroll tool
# Good for learning more on data types and conversion int() and float
# - conditional logic (if, else)

# IMprovements
# Multpiple employees entries
# Saving data to a file or database
# a web interface
# Exporting reports(pdf,excel)

