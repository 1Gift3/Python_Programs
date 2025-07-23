# WHAT
# This is a simple program for Job offers and salary negotiations process between you a job candidate and the employer.
# This too can be very neccessary for KasiLink

# The program is made up of three main functions
# Job_offer() - Which annouces a job offer (Announcement)
# negotiate_salary() - Handles negotiations if you the candidate expects a higher salary
# Then main() - Being an entry point that runs the above functions

**Function i**
# Job_offer function simulates a job offer for you the candidate with inputs of base_salary from the employer (offer) and job_title for the position printing a congradulatory message with title and salary
# Then return te base salary to be furtherly processed.

**Function ii**
# Now we start the negotiations with base_salary from employer and your expected salary.
# Should you the cadidates expected salary be higher than then base salary, the employer will then propose a counter-offer halfway the two or anything they desire
# You the user will then be asked whether you accept the counter-offer (yes or No)
# if yes, it will print an acceptance message
# if no, it will say negotiation failed
# If then youn th candidate expectation is met or lower than the base salary - it will just print that the bas offer was accepted.

**Function iii**
# What happens here is the program sets job title and base salary 
# Prompts you the user for your expected salary then after wards converts it to Float.
# Calls jobs_offer() function to show the initial offer.
# Calls again function negotiate_salary() function to handle any potential negotiations
# and then it displays the final agreed upon salary
# Special Block 
# if __name__ == "__main__";
# What this does is that it ensures that the script runs the main() function only when its run directly  - not when its imported as a module in another script.


# Job offers functiooooooon makes the initial job offer with a specified base salary, it the returns the base salary to be used later in nego
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
