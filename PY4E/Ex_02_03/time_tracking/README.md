# WHAT
# The program is a simple time tracker invoicing and pay earned for freelancer or Part- time Jobs(Can be useful for KasiLink)

# Firstly on the program you defined a function 
# The program firstly starts by prompting the user for hourly rate, converting String to a floating point
# Continues to prompt you the user for number of days worked, converting that string to Integer
# The For loop starts from day to days_worked, meaning what it does is to repeat the process for every day you the user worked.
# It asks you the user to enter how many hours you have worked on the current day. Float converts the input(string) into a decimal number.
# += Adds current days hours to a running total of all hours worked.
# Calculates the pay for the current day by multiplying the hours worked by hourly rate 
# Adding that to the running total pay.
# Then It proceeds to print Summary from Total hours worked converting or Formatted to 2 decimals to total earnings.
# Weekly_hours = total_hours - what it does is just to copy total values to weekly_hours and Weekly_pay, not doing anything significant unless you the user change the logic to reset after 7 days.
# Prints weekly hours and earning same as the total hours and earnings.
# Then Track_part_time_hours() calls the functtion track_part_time...that was defined. 



# The program continues to track total hours worked and calculates total earnings based on your hourly rate 
# Then it willl display a summary showing:
# - total hours worked 
# - Total pay earned for the days worked
# - Weekly summary
