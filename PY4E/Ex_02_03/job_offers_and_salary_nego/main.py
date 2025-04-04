def job_offer(base_salary, job_title):
    """"
    Simulates a job offer process, providing an offer to the candidate.
    """

    print(f"Congradulations! Yove've received a job offer for the position of {job_title}.")
    print(f"The base salary offered is: ${base_salary:,.2f}")
    return base_salary


def negotiate_salary(base_salary, expected_salary):
    """
    Simulates salary negotiations between the employer and the candidate.
    """

    print("\nSalary Negotiation Begins:")
    if expected_salary > base_salary:
        print(f"Candidate is asking for ${expected_salary:,2.f} which is higher than the base salary.")

        # Employer response
        counter_offer = base_salary + (expected_salary - base_salary) * 0.5 # Employer offers
        print(f"The employer offers ${counter_offer:,.2} instead of the expected salary.")

        # Candidate responds
        decision = input("Do you accept the counter offer? (yes/no): ").strip().lower()
        if decision == "yes":
            print(f"Congradulations! You've accepted the counter offer of ${counter_offer:,.2f}.")   
        else:
            print("The negotiation did not result in a mutually agreed salary.")
    else:
        print("Candidate accepts the base salary offer.")
        return base_salary
    
def main():
    # Example job offer
    job_title = "Geospatial Developer" 
    base_salary = 75000 # Employer initial offer
    expected_salary = float(input("Enter your expected salary: $"))   

    # Starting with the job offer
    current_salary = job_offer(base_salary, job_title)

    # Negotiating salary if expected salary is higher
    current_salary = negotiate_salary(current_salary, expected_salary)

    print(f"\nFinal salary offer: ${current_salary:,.2f}")

if __name__ == "__main__":
    main()
# This ABOVE
#  __name__ is a special python variable that holds the name of the module currently being excecuted, except when the module is strted from the command line, in which it becomes __main__   
# It helps control code executions in scripts.
# WHAT
# When you run a python script, the interpreter assigns the value __main__ to the __name__ variable
# should python import the code as a module then it sets __name__ to the modules name instead.
# By encapsulating code within if __name__ == __main__, you can ensure it only runs in the intendd context.

# WHY
# Its usefuk for adding script specific logic, such as user input or test cases, without affecting module imports

# HOW
# When you want to create an additional entry point for a script, so that the file is accessible as a stand alone script as well as an importable module ( You might want that when your script needs to collect user input)
