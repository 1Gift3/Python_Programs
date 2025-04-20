num = 0 
tot = 0.0

while True :
    sval = input ('Enter a number: ') 
    if sval == 'done' :
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue    
    fval = float(sval)
    print(fval)
    num = num + 1
    tot = tot + fval

print('ALL DONE HERE')
print (tot, num, tot/num)    

# WHAT
# This is a python pattern used to collect numbers from the user in a loop and then cal their total count and average.
# We enter a while True loop which runs forever unless we break it manually
# the line asks the user to type a something (input)
# Should you input done, we break the loop and stop asking for input
# Then error handling try and except : Tries to convert the input to a float
# should the input fail to be converted like if they say hello, it prints Invalid and skips the rest of the loop using continue
# fval prints the valid number and updates the count(num) and the running total
# Then it shows the total sum the number of entries and the average

# WHY
# The script is flexibe can be used in tons of mini projects
# Its very safe avoiding crashes by handling invalid input
# Has a clean logic using patterns like break,continue and try/except which shows up everywhere in programming
# Lastly its easy expandable making it easy to turn into a bigger program later.

# HOW 
# We can use it to calculates grades, collecting tests scores from user a user then computing the average score, number of tests and assign a final letter grade
# Budget tracker
# Survey or Data entry
# Sensor data - e.g from Iot Devices (real time - scalability)
# Also a great tool to teach looops, conditionals, input handling, except handling, basic stats
