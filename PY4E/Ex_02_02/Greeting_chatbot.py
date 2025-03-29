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
# WHAT
# What it does is that it allow me to format selected parts of a string
# WHY
# when you - Want control over formatting of out-put than simply printing space separated value.  
# HOW
# To format out-put, by begining a string with f or F before opening qoutation mark or triple qoutation.

# Placeholders and modifiers
# WHY
# To format values in an f-string -y you'd need  placeholders {}
# WHAT
# It enable {name} as a container (ie - but also can contain operations,functions and modifiers) to format the value.
# HOW
# WHen i remove fstring the it prints the statement as it is "Hello, {name}!..." without input or formating the input string.

# Alternative way!
# Since its cleaner and more readerble, if you want not that you cpuld use "+" for string concactenation

# .Lower()
# WHY
# is a string method that converts all characters in a string to lowercase.
# WHAT
# It ensure a consistent input handling takes place

# Learned
# Got reminded on how to use emojis again Windows, + and period .
