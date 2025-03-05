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
