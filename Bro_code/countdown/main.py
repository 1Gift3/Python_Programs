import time 
my_time = int(input("Enter the time in seconds:"))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Times up")

#  Count down would be useful in so many ways from ecommerce to dealines on projects in radio public awareness etc it acts as a movitation to act creating a sense of urgency

#  It can help you breakdowns tasks into manageable chuncks from time blocking small tasks e.g relax for 15 min, prioritizingand completing tasks 10 min countdown, increase focus with tracking progress on multiple small tasks, supporting small business operations admin tasks or customers service calls  

# 