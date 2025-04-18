# WHAT
# A Basic terminal based budget tracker - CLI version
# It tracks my expenses
# Lets me add categories
# Then shows summary at the end


total_expense = 0.0 
num_entries = 0
expenses = []

print(" Welcome to the Bugdet Tracker")
print("Enter expenses one by on. Type 'done' to finish.\n ")

while True:
    entry = input("Enter expense amount (optionally: amount category): ")

    if entry.lower() == 'done':
        break 

    try:
        parts = entry.split()
        amount = float(parts[0])
        category = parts[1] if len(parts) > 1 else "uncategorized"


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
    print(f" - {category.capitalizr()}: R{total:.2f}")


# Expand 
# 💾 Save expenses to a CSV or JSON file
# 📱 Turn it into a web app or API

        