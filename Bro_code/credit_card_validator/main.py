# Pythons credit card

# Removes any '-' or ' '
# add all digits in the places from the right to left 
# double every second digit from right to left
    # IF RESULT IS A TWO DIGIT NUMBER
    # ADD THE TWO digit number together to the single digit
# sum the totals of steps 2 & 3
# if sum is divisible by 10, the credit cards # is valid

#  First of all why im using Luhn Algo is because its commonly used to vslidate credit card numbas
# Why it works is becaause this Modulus 10 it was crerated or being used to identify credit cards IMEI no. and canandian social insurance numbers
# - its simple method to distinguish valid numbers from mistyped or incorrect, designed to protect against accidental errors not malicious attacks

# How it is used is that first step
# - it starts from your numba from the rightmost with a double on the value of every second digit
# - if the doubling result in two digits, you add those digits toget a single numba
# - if you still get double youll have to add again
# - once done take the sum of all digits
# - if the total ends in zero the card numba is valid
# Now my code here still does the same but now removes - or ' ' the proceeds with the steps of Mod 10
#  We can incorporate other card types by prefix and length
# Visa: Starts with 4, 13 or 16 digits.
# MasterCard: Starts with 51–55 or 2221–2720, 16 digits.
# American Express: Starts with 34 or 37, 15 digits.
# Discover: Starts with 6011, 622126–622925, 644–649, or 65, 16 digits.

# This reads a card numba to validate whether is works or not
# - cleaning the card numba
# - You can add reverse for easy right to left
# - doubles every second digit
# - calculates the toal sum then checks for validity.

sum_odd_digits = 0 
sum_even_digits = 0 
total = 0 

card_number = input("Enter a credit card #: ")
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")
card_number = card_number[::-1]

for x in card_number[::2]:
    sum_odd_digits += int(x)


for x in card_number[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += (1 + (x % 10))
    else:
        sum_even_digits += x

total = sum_odd_digits + sum_even_digits


if total % 10 == 0:
    print("VALID")
else:
    print("INVALID")
    
        