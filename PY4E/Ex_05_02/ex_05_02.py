largest_no = None
lowest_no = None

while True:
    number = input("Enter Numba:")

    if number.lower() == "done":
        break

    try: 
        our_value = int(number)

        if largest_no is None or our_value > largest_no :
            largest_no = our_value

        if lowest_no is None or our_value < lowest_no :
            lowest_no = our_value

    except:

        print("Invalid input")     

print(f"Maximum is {largest_no}")
print(f"Minimum is {lowest_no}")