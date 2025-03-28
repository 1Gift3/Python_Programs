name = input("enter your name:")
print(f"Hello, {name}! Nice to meet you.")

# Asking a follow up Q
mood = input ("What would you say How you feel like right now?")

# Respond based mood
if mood.lower() in ["good", "great", "happy", "awesome"]:
    print("Thats great that you feeling this way! Keep up being positive! 😊")
elif mood.lower() in ["sad", "tired", "not good", "bad"]:
    print("It happens sometimes, Its not the end...go through it can get what need it from it! 🌻")
else:
    print("Thats interesting! Hope you have a fantastic day ahead of you and be in every moment!")

# Asking another question
hobby = input("WHats yor favourite hobby?")
print(f"That sounds interesting, {name}! {hobby.capitalize()} is a great way to spend time.")

print("Thanks for chatting with me! Have a great one! 🚀")


# Line Two uses an f-string which is a formatted string in python
# What it does is that it allow me to format selected parts of a string
# And to specify a string as an f-string you simply put an f in front of the string
# Wanting control over formatting of your out put rhan simply printing space separed value to format out put we begin a string with f or F before openning qoutation mark or triple qoutation.

# Placeholders and modifiers
# Now to format values in a n f-string -y youd need  placeholders {}
# Which {name} is a container but also can contain operations,functions and modifiers to format the value.
# WHen i remove fstring the it prints the statement as it is "Hello, {name}!..." without input or formating the input string.

# WHY
# Reason why we use it is cause its cleaner and more readerble than using "+" for string concactenation

# #.Lower()
# is a string method that converts all characters in astring to lowercase.

# WHy
# It ensure a consistent input handling takes place

# Got reminded on how to use emojis again Windows, + and period .
