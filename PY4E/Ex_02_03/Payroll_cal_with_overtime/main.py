hrs = input("Enter Hours:")
usr_rate = input("Enter rate:")

# Convert input to numbas
hrs = float(hrs)
usr_rate = float(usr_rate)

# Calculate regular pay
if hrs <= 40:
    gross_pay = hrs * usr_rate
else:
    regular_pay = 40 * usr_rate 
    overtime_hours = hrs - 40 
    overtime_pay = overtime_hours * (usr_rate * 1.5)  # Overtime is 1.5 times the regular rate    
    gross_pay = regular_pay + overtime_pay
    
print(f"Total Gross Pay: ${gross_pay:.2f}")

