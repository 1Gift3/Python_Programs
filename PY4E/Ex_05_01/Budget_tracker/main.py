# WHAT
# A Basic terminal based budget tracker - CLI version
# It tracks my expenses
# Lets me add categories
# Then shows summary at the end

# The script initializes total amount spent, number of entries and an empty list to store all expenses
# Displays welcome message and tells the user how to enter data
# Loop collects expense entries promoting the user for input until the type done
# if user types done(case insensitive the loops ends
# Line 28 the code here deals with breaking down what the user enters,extracting relevant info like the amount and category and making everything is corrected.
# - entry.split : input function allows the user to type in a string and split method is sued to split that string into parts based on spaces
# - amount = float : takes the first part of the split string which would represent the expense amount and converts it to float point
# - Then category : after splitting the input, the line checks if there is more than one part..or category to assign it to.
# Summarised line 28
# - Splits input by spaces, first part is the amount, secondly in optional e.g food, transporrt, if no category is given, it uses uncategorised by default
#  Adds the expense to a list, adding amount to total and increments the count of entries
# gives back feedback - what was added
# Error handling
# prints the total and number of entries
# Calculates average per entry
# Loops through stored expenses to sum up total per category
# Then prints per category total


total_expense = 0.0 
num_entries = 0
expenses = []

print(" Welcome to the Bugdet Tracker")
print("Enter expenses one by one. Type 'done' to finish.\n ")

while True:
    entry = input("Enter expense amount (optionally: amount category): ")

    if entry.lower() == 'done':
        break 

    try:
        parts = entry.split()
        amount = float(parts[0])
        category = parts[1] if len(parts) > 1 else "uncategorized"

        # My storing - which is a list of tuples
        expenses.append((amount, category))
        total_expense += amount
        num_entries += 1

        print(f" Added: R{amount:.2f} for {category}")

    except ValueError:
        print(" Invalid input. Please enter a number, optionally followed by a category. ")


print("\n Budget Summary:")
print(f"Total Expenses: R{total_expense:.2f}")
print(f"NUmber of entries: {num_entries}")

if num_entries > 0:
    print(f"Average Expense: R{total_expense / num_entries:.2f}")

# Showing category breakdown
print("\n Breakdown by category: ")
category_totals = {}
for amount, category in expenses:
    category_totals[category] = category_totals.get(category, 0) + amount

for category, total in category_totals.items():
    print(f" - {category.capitalize()}: R{total:.2f}")


# Expand 
# 💾 Save expenses to a CSV or JSON file
# 📱 Turn it into a web app or API 
# Integrate with SQLite or Postgres
# Authentication
# geotagged expenses


# HOW
# can be used to track down personal spending 
# Expense analysis showing total expenses, average expense per entry and spending per category
# Can be used to prototype a real app backend finance chatbot or dash board or a backend service
# Can be extended to log into a file (like csv or json) making it useful for recording business expenses or testing financial models 
# 🧾 Freelancers tracking project costs
# 🏠 Roommates splitting shared expenses
# 👨‍💻 Developers building proof-of-concept finance tools
# 🧪 Test input for a full budgeting API backend

# WHY
# A good teaching tool, working on core concepts like user input, data parsing, error handling, list/dict usage and loops+ conditionals
# Since it needs no internet or UI by running in any terminal is great for quick data entry or testing ideas on the go


# Adde on saving to a JSON File

import json

# Converting expenses to list of dictionaries
expense_data = [{"amount": amount, "category": category} for amount, category in expenses]

with open("expenses.json", "w") as jsonfile:
    json.dump(expense_data, jsonfile,indent=4)

print("\n Expenses saved to expenses.json") 

# WHY
# Its great for a structured data
# making it easy to read and parse in web or backend apps
# And can easily extent it with timestamps later

# WHAT
# JSON - a common and lightweight way to store structured data in a text file
# it converts my python lists of tuples into a list of dictionaries
# Saves the data to a .json file in a human readable format
# Making it easy to be opened later to see saved data or load it back into app for continued tracking
