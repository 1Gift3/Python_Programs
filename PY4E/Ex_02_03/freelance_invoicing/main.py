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
