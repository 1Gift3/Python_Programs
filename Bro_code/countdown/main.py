import time 
my_time = int(input("Enter the time in seconds:"))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Times up")

# WHY
# Count down would be useful in so many ways from ecommerce to dealines on projects in radio public awareness etc it acts as a movitation to act creating a sense of urgency

#HOW
#  It can help you breakdowns tasks into manageable chuncks from time blocking small tasks e.g relax for 15 min, prioritizing and completing tasks 10 min countdown, increase focus with tracking progress on multiple small tasks, supporting small business operations admin tasks or customers service calls  
#  The user is asked to input a time in sec ( my_time -)
# The for loops starts at my_time and decrements by 1 each iteration until it reaches 0
# Inside the loop
# - The number of seconds is calculated using the modulo operator which returns the rremainder when the  total second are divided by 60
# - The numba of minutes is calculated by dividing the total secs by 60 then using the modulo operator to ensure the min stay withiin the 0-59 range
# - the number of hours is then calculated by divining the total secs by 3600
# The printf (f"{hours:02}) prints the time in the HH:MM forat where the :02 formatting ensures each value is displaysed as two digits
# time.splee(1) introduces a delay on 1 second between each iteration making the countdown happen in real time
# once the it reaches zero the message times up is printed.

# WHAT
#  It counts down the clock.
# Its a simple timer that takes input time in seconds from the user and counts down to zero, displaying the time in format HH:MM:SS when the timers reaches to zero it prints times up
# The program takes the input time in secs from user
# then counts down from that time and displays the remainning time in the format HH:MM:SS each sec
# after the countdown is finished it prints Times up

# 