operator = input("Enter an operator ( + - * /): ")
num1 = float(input(" Enter the 1st number: "))
num2 = float(input("Enter the 2nd numbers: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator =="*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 /num2
    print(round(result, 3))
else:
    print(f"{operator} is not valid")    


# We used elif in these parts to avoid excessive indentation.
# - the elif is short of else if with the else statement optional
# - the if elif... elif like above sequence is a substitute for switch or case state's found in other languages.

# if statement is used to check if block of code is true
# In here the if statement is the first one checking if the operator is true, if it is not true the elif comes in to be checked too true or false if its true it runs result if not then the next statement.

# When we want to execute dff blcoks based on the evaluation of the condition.

# WHY
# It would be useful for time saving helping perform calculations quickly and accurately without tp manually work through
# Its useful for automation of calculations which you can automate repetitive cal
# Python helps me to design a cal that suits my specific needs
# It can also be intergrated with other larger projects where you can use it for scientefic simulations, financial app or any where arithmetic is needed
# Also helps to reiforce fundamentals concepts like variables, functions, conditionals, loops, and error handling.

# HOW
# I can also extend the cal to handle advance math operations like square roots, trigonometric functions,logarithms and even symbolic math(using sympy)
# Can be expanded with libraries like - Numpy for numeric cal, matplotlib for graphs or pandas for working with data tables

# WHAT
# It asks you to select an operation 1 to 4
# After you choose an operation it will prompt you to enter two numbers
# It will then display the results of the chose operation on the two numbers you provided.

# IMPROVE 
# Advance features like square roots, exponentials or trigonometrics functions using math module
# Loop: I could allow the user to perform multpile cal without restarting the program
# Error handling, i could handle cases like non-numeric input or division by zero more gracefully or unexpected cases

# FUTURE
# I could include graphical interface creating a graphical user (GUI) using tkinter or pyqt
# I could also store previous results or have a history of calculations

