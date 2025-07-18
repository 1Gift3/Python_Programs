# WHAT
# This is a simple program for Job offers and salary negotiations.
# This too can be very neccessary for KasiLink
#
# Job offer functiooooooon makes the initial job offer with a specified base salary, it the returns the base salary to be used later in nego
# Salary nego func should the candidates expected salary be higher that the base salart, the employer makes a counteroffer thats halfwway between the base and the expected salary. The candidate is then asked whether they accept the counteroffer
# Lastly the main function runs the simulation, starting with the job offer and then proceeding to nego based on the users input for expected salary

# Improvements 
# Modify job title to reflact different job positions
# Changinging the base_salary to match the initial offer in dff scenarios
# Negotiation strategy as now the counter offer is simply 50% of the difference between the ase and expected salary. i can make the adjustment to make the nego more complex or realistic ( use ways offered on youtube to negotiate)

# WHAT
# When you run a python script, the interpreter assigns the value __main__ to the __name__ variable
# should python import the code as a module then it sets __name__ to the modules name instead.
# By encapsulating code within if __name__ == __main__, you can ensure it only runs in the intendd context.

# WHY
# Its usefuk for adding script specific logic, such as user input or test cases, without affecting module imports

# HOW
# When you want to create an additional entry point for a script, so that the file is accessible as a stand alone script as well as an importable module ( You might want that when your script needs to collect user input)
