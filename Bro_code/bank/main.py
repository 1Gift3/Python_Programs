def show_balance(balance):
    print("***************")
    print(f"Your balance is ${balance:.2f}")
    print("***************")
   

def deposit():
    amount = float(input("Enter an amount to be deposited: "))
    print("***************")


    if amount < 0 :
        print("***************")
        print("That is not a valid amount ")
        print("***************")

        return 0
    else:
        return amount   

def withdraw(balance):
    print("***************")
    amount = float(input("Enter amount to be withdrawn: "))
    print("***************")


    if amount > balance:
        print("***************")
        print("Insufficient funds")
        print("***************")

        return 0
    elif amount < 0:
        print("***************")
        print("Amount must be greater than 0")
        print("***************")
        return 0    
    else:
        return amount
def main():
    balance = 0 
    is_running = True

    while is_running:
        print("***************")
        print("      Banking program     ")
        print("1. Show balance")
        print("2. Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("***************")


        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2': 
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False    
        else:
            print("***************")
            print("That is not a valid choice") 
            print("***************")
           
    print("***************")
    print("Thank you!")   
    print("***************")
   

if __name__ == '__main__':
    main()



# Something isnt right with my withdrawal

# What was wrong with my withdraw was that to my functions show_balance() line 1 i defined it without parameters but 
# to main() line 40 and 57 i called it with balance as an argument.

#    WHY (Docu)
#  Function. Parameter and Argument.
#  Functions a code that can be used over taking arg that are inputed by user then performing some computation
# - Parameter  a variable we use to define function
# - Arg a value that we push onto a functions as an input

# WHY
# It reinforces core programming conceopts like functions, control flow and loops
# It stimulates real world applications like managing balance, depositing and validating user.
# Helps to practice error handling


#  HOW
# On how i can use this is by use of global ( thats if i want to keep function without parameters)
# - But i must first ensure that balance is accessible in the global scopes(  where im calling the function)
# - balance = 100  # Global variable

#def show_balance():  # No parameters here
#    print(balance)  # This will work because `balance` is global

# Now call it without any argument
#show_balance()  # This will work correctly


#    WHAT
# In this case balance is a global var that doesnt need to be paased as an arg to show_balance. it will be accessible withing the Function.
# It keeps track of a users account starting @ zero
# allows the user to deposit money ensuring that the amount entered is valid
# Enables the user also to withdraw money but checks for sufficient balance and ensures the withdrawal amount is positive
# Displays the menu simple for user interaction with options show current balance, make deposit, withdraw money and exit program


# IMPROVEMENTS 
# File handling saving the balance to a file so it persists even after program ends
# User accounts allowing users with their unique balances 
# Improving interface adding colors or a cleaner menu display to make it more engaging
# And also adding interest cal over time on the balance

