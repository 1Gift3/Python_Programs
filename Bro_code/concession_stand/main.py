menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 3.50,
        "pretzel": 1.00,
        "soda": 3.00}

cart =[]
total = 0 

print("---------Menu --------")
for key,value in menu.items():
    print(f"{key:10}: R{value: .2f} ")
print("--------------------")

while True: 
    food = input("selects an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("---------- YOUR ORDER --------")
for food in cart:
    total += menu.get(food)
    print(food, end= " ")        

print()
print(f"Total is: R{total:.2f}")

# Seems like popcorn doesnt print out 

# Somehow the next day it works.
#   WHAT
# Question is Why would it be useful to assist with Small tasks to Small - vendors,small businesses, entreprenuers.
# It simplifies operations, boosts fundraising efforts, and provides valuable data that can inform better decisions.
#  How
# It can be useful too if a graph user interface comes in with payments ethods or a more detailed inventory management like adding Quantity.
# it would be useful to enhance efficiency, profitabilyty the overall experience for both vendors and customers. It simplifies operations, boosts fundraising efforts, and provides valuable data that can inform better decisions.
#    WHAT
#  It helps a Business to keep track of purchases, processing orders and callculate the total
