unit = input("Is this temp in celcius or fahrenhait (C/F): ")
temp = float(input ("Enter the temp: "))

if unit == "C":
    temp = ((9 * temp) / 5 + 32, 1)
    print(f"The temp in Fahrenheit is : {temp}F")
elif unit == "F":
    temp =  round ((temp - 32) * 5/ 9, 1)
    print(f"The temp in celsius is: {temp}°")
else:
    print(f"{unit}  is an invalid unit of measurement")

# this too does not handle well error that is being inputed by user so that i need to check well
# the program states that both f and c are an invalid unit of measurement

# IMPROVEMENTS
# oOh it doesnt  specify use only uppercase when inputing hecnce that 
# need to input that in.
# Loop for Multiple Conversions – Let the user keep converting temperatures without rerunning the script.
# Better Error Handling – Check if the temperature input is a valid number (using try-except).


# WHY
# Its useful for practical application as many people need to convert temp
# It demostrates basic programmingg concepts user input (), type conversion float(), conditional logic if-elif-else(), mathematical operations and string formatting(f-strings)

# HOW
# i can run the scripts directly by saving code as .py file 
# Running it in a python envir
# and follows the prompts to enter c/f and the temp
# It keeps asking for conversions until you type Q
# handles invalid inputs(non - numbers, wrong units)
# No need to return the script each time.

# WHAT
# Its a simple temperature converter that allows user to input a temp in either celsius or fahrenheit and then converts it to the other unit.
# It prompts the user to specify the unit(C/F) and the temp making interctives.
# Checks if the input unit is valid (C or F) preventin incorrect conversions
# Precision control, the results are then rounded to 1 decimal place making the output clean and readable.
