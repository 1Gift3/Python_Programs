# Functions to track time worked and calculated earnings
def track_part_time_hours():
    print("Welcome to the part-time job tracker!")

    # Ask for hourly rate
    hourly_rate = float(input("Enter your hourly rate (e.g, 15.50): $"))

    # Initializing total hours and total pay
    total_hours = 0
    total_pay = 0.0

    # Asking how many days you worked 
    days_worked = int(input("Enter the number of days you worked: "))

    # Looping through each day to eanter hours worked
    for day in range (1, days_worked + 1):
        hours = float(input(f"Enter hours worked on the day {day}: "))
        total_hours += hours # Adding hours worked to total
        total_pay += hours * hourly_rate # Calculating pay for the day and add to toal pay

        # Outputing the summary 

        print("\n --- Summary ---")
        print(f"Total hours worked: {total_hours:.2f} hours")
        print(f"Total earnings: ${total_pay:.2f}")

        # Calculating weekly earnings (assuming 7 days of a week)
        weekly_hours = total_hours # For simplicity, this can be used directly or adjusted for weekly report
        weekly_pay = total_pay

        print(f"Weekly hours worked: {weekly_hours:.2f} hours")
        print(f"Weekly earnings: ${weekly_pay:.2f}")

# Run the program
track_part_time_hours()        