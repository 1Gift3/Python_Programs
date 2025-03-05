unit = input("Is this temp in celcius or fahrenhait (C/F): ")
temp = float(input ("Enter the temp: "))

if unit == "C":
    temp = ((9 * temp) / 5 + 32, 1)
    print(f"The temp in Fahrenheit is : {temp}F")
elif unit == "F":
    temp =  round ((temp - 32) * 5/ 9, 1)
    print(f"The temp in celsius is: {temp}°")
else:
    print(f"{unit}  is an invalid unit of measurement")

# this too doesnot handle well error that is being inputed by user so that i need to check well
# the program states that both f and c are an invalid unit of measurement


# oOh it doesnt  specify use only uppercase when inputing hecnce that 

# might need to input that in.