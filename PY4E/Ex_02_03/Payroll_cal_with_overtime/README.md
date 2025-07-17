# WHAT
# At its core, this is a simple payroll calculation, calculating gross pay based on the number of hours worked and hourly pay rate.
# Also taking overrtime into account
# The program uses 40 hours as regular working hours
# If the hours worked are 40 or less, gross pay is calculated by multiplying hours by the rate (ie - No overtime is paid in this case)
# Should it  happen that you have worked more than 40 hours
# - It first computes regular pay for 40 hours
# - Secondly Calculates how many extra hours were worked
# - Thirdly overrtime pay is calculated at 1.5 times the regular rate
# - Then it adds boths regular pay and the overrtime to get the total gross pay
# Then the program prints the total pay, formatted to 2 decimals.


Example:
Hours Worked: 40 hours

Hourly Rate: $15.75/hour

Gross Pay: 40 * 15.75 = $630.00

# HOW
For real-world payroll purposes, we often need to account for other factors, such as:

Overtime Pay (if hours exceed 40 hours per week)

Tax Deductions (if you're including tax withholdings)

Bonuses or Deductions (like bonuses, health insurance, etc.)

