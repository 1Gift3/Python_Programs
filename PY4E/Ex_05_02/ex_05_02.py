# WHAT
# A simple number tracker that finds the largest and smallest numba from user input
# It asks the user to enter numbers repeatedly and when the user types done it prints
# - the largest no entered
# - the smallest number entered
# Line 20 - Updates the largest no if this number is bigger than the current largest
# also updates lowest_no if its smaller than the current lowest
# It asks for number to be inputed repeatedly
# Tracks the highest and lowest numbers entered
# Ends when the user types done
# Handles invalid inputs gracefully 
# and then prints the max and min at the end


largest_no = None
lowest_no = None

while True:
    number = input("Enter Numba:")

    if number.lower() == "done":
        break

    try: 
        our_value = int(number)

        if largest_no is None or our_value > largest_no :
            largest_no = our_value

        if lowest_no is None or our_value < lowest_no :
            lowest_no = our_value

    except:

        print("Invalid input")     

print(f"Maximum is {largest_no}")
print(f"Minimum is {lowest_no}")

# WHY
# It helps understand loops, input, error handling and tracking values
# it acts as a base for more advanced programs : calculators, analytics and data filtering
# Also great intro to using none as a placeholder in logic

# HOW
# Grading system
# can be used as a sales tracker for small business inputing daily sales figures
# Expense or budget tracker
# perfomance monitoring
# and a data entry or logs to help analyze extremes without needing excel or fancy tools

# Expands 
# saving values to a file or database
# working with decimanl nummbers float instead of int
# Visualize with a graph (using matplotlib)

