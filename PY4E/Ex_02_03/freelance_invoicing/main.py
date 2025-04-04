from datetime import datetime

def calculate_gross_pay(hours, rate):
    """Function to calculate and return the gross pay."""
    return hours * rate
   

# Function to generate freelance invoice

def generate_invoice():
    """Function to take user input, calculate pay, and display the invoice."""

    try: 
        # User inputing for hours worked and rate
        hours = float(input("Enter Hours: "))
        rate = float(input("Enter rate: "))


        # Calling the function to calculate gross pay
        gross_pay = calculate_gross_pay(hours, rate)

        # Get the current dat and time
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

        # Printing te invoice with date and time and gross pay
        print(f"\nInvoice generated on: {formatted_time}")
        print(f"Gross pay: ${gross_pay:.2f}")

    except ValueError:
        print("Please enter valid numerical inputs for hours and rate.")

# Calling the function to generate the invoice
generate_invoice()        

# .strftime(format)
# Returns a string representing the date, controlled by an explicit format string.
# Formt codes referring to hours, minutes, or seconds will see 0 values.

# ValueError exception 
# Python valueErro is raised when a function receives an argument of the correct type but an inappropriate value
# We can use try-except block to handle ValueError exception
# It is alot raised in  mathematical operations.

# ValueError inherits from exception, you can decide to trap either only ValueError or exception.
# We generally use specific exceptions to trap only the ones that are likely to occur and leaves the rest untrapped.
# A specific exception.
