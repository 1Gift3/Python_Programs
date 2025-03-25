foods = []
prices = []
total = 0 

while True: 
    food = input("Enter to Buy(q to quit):")
    if food.lower() == "q":
        break
    else: 
        price = float(input("Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print ("----- YOUR CART -------")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price 

print()
print(f"Your total is: ${total}")        

# WHY
# It helps learn programming basics like data structures demonstrating the use of lists (food and prices) to store multiple values
# Control flow and loops using a while loop and if-else for input
# String formatting using f-strings to format and display info
# and type conversions showing th e usse of float() for converting input to numeric data.
# We can also use it for real world app - point of sales systems : like the logic mirror basic POS systems where items and price are entered, displayed and totaled.
# Budget tracking and inventory management.

# HOW
# Can use it for grocery planning.
# Can expand it to build a GUI: using a library like tkinter or pyqt to make it graphical desktop app
# Database intergration to store items and prices 
# Web App turning it into a web app using django and react
# And also mobile app using kivy(python) or react native.

# WHAT
# The user can enter food items along with their prices view their cart and sees the total cost before exiting.
# Takes the user input
# stores data item names are saved in the foods list and prices list
# and displays the cart, by listing all the items you addded and calculates and shows the total cost of all the items.

# IMprovements
# Error handling inputs for prices
# displays enhancements, displaying item names with their respective prices
# And Advaced feautures, allowing users to remove items from the cart, add ing tax calculations and tracking quantities of each item.

