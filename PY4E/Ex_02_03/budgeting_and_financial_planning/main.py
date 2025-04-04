# Getting user input
hrs_per_week = float(input("Enter hours worked per week: "))
hourly_rate = float(input("Enter your hourly rate: $"))
weeks_per_month = 4 # Assuming 4 weeks in a months 
tax_rate = 0.14 # Flat 14% tax
saving_goal_percentage = float(input("Enter the percentage of income you want to save (e.g, 20 for 20%): ")) / 100

# Calculate gross pay (before tax)
gross_weekly_pay = hrs_per_week * hourly_rate
gross_monthly_pay = gross_weekly_pay * weeks_per_month 

# Calculating tax reductions
tax_deductions = gross_monthly_pay * tax_rate 

# Calculating net pay(after tax)
net_monthly_pay = gross_monthly_pay - tax_deductions

# Calculate savings
monthly_savings = net_monthly_pay * saving_goal_percentage

# Display results
print(f"\nYour gross monthly pay (before tax): ${gross_monthly_pay:.2f}")
print(f"Your tax deductions (14%): ${tax_deductions:.2f}")
print(f"Your net monthly pay (after tax): ${net_monthly_pay:.2f}")
print(f"Your monthly savings goal({saving_goal_percentage*100}%): ${monthly_savings:.2f}")


# %f - is a formatter specifically used for formatting float values, to specify the number of the decimal numbers to be returned when a floating point is rounded up.
# %.2f means to round up by two decimal places.

# HOW
# We can use another formatter %d in python - which returns the whole number in a floating point.
