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