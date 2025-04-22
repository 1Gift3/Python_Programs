# WHAT
# the script asks for a numeric input 
# Validates the input 
# Stored the data
# Shows a summary of total,count and average
# Option to save to a .csv 

print(" Data collector")
print("Enter numeric values. Type 'done' to finish. \n")

data = []
while True:
    val = input("Enter a number: ")
    if val.lower() == 'done':
        break

    try:
        fval = float(val)
        data.append(fval)

    except ValueError:
        print(" Invalid input. Please enter a valid number.")    

# Showing Summary
if data:
    total = sum(data)
    count = len(data)
    average = total / count
    print("\n Data collection completed!")
    print(f"Total entries: {count}")
    print(f"Sum: {total}")
    print(f"Average: {average:.2f}")
else:
    print("\n No data was entered.") 

# The script is a foundation of apps like surveys,analytics tools, admin dashboards and Iot data processors

# WHY
# When we want to collect user input in a structured manner or form
# When we want to summarise statistics by cal total,count and aver useful in Business KPI, customers feedback, perfomance tracking and budgeting
# In data validation it also can be useful.

# HOW - For real world cases
# - Mini survey tools 
# - Inventory or stock counting
# - delivery distance tracker
# - Lab/ experiment Data entry

# Improvements 
# Track maximum and minimum distances
# Add unit hnadling in miles or km