import random 

words = ("apple", "orange", "banana", "coconut", "pineapple")

# Dict of key:() and a  tuple
hangman_art = {0: (" ",
                   " ",
                   " "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: ("   o ",
                   "  /| ",
                   "     "),
               4: ("   o  ",
                   "  /|\\ ",
                   "      "),
               5: ("   o  ",
                   "  /|\\",
                   "  /   "),
               6: ("   o  ",
                   "  /|\\",
                   "  / \\")}

def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guesssed")   


        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

        else:
            wrong_guesses += 1   

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False

        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses) 
            display_answer(answer) 
            print("YOU LOSE!") 
            is_running = False 


if __name__ == '__main__':
    main()

# Something is not right here so you need to check  
# what ever i seem to type it gives me results - somehow i think i know not how it works
# Well i believe k word wouldn't make me win guessing the word Orange so thats whats wrong and also
# i am not guessing 5 times before the 6th to loose or win
# I seem to Guess 9 times

# Learned
# Line 79 is a python construct used to control execution of a script - in
# simpler terms main will only run when script is executed directly and not run when its imported as a module.
# Its a boilerplate code that protects users from accidentally invoking the script when they ddnt intent to.
# HOW it WORKS - check code sample


# Seems like the problem was on main function line 38 on the hint as i before "Underscore" __ doubled that not single
# The issue also was on def main function on wrong_guesses when i initially put 6
# instead of zero which made the program to initially start @ 6

# the variable wrong guesses keeps track of how many incorrect guesses player made
# now my dict stated that hangman has 7 states 0 - 6, not is wrong guess starts @ 6, the game will forever diplaying the final hangman

# Oooh just checked it again and it seems it only gives me 6 tried wrong answers then it hangs but when i keep guessing the correct one that doesn t include it.

# WHY
# It delves more or abit into DSictionaries and also taught me about using line 79 - running only when script is executed directly and when its imported.
# besides the obvious of helping think of word, phrase, or sentence even other try guesses that might match.
# It helps alot on problem solving as its an advance code program
# Helps me understand control flow ( While, for, break and continue)
# Its relies alot on string manipulation, checking for substrings and formatting output essential skills in text processing
# Using data structures like lists to store guessed letters and sets to avoid duplicates
# as an advance program it breaks the game into functions for better code Org and teaches modular desing
# Error invalid inputs helps in understanding (try and except mechanisms)

# Besides all this you can also extend the game to GUI version. intergratee it with a database or even create a multiplayer version.
# Web version using Django/Flask.
# Database integration to track scores and Networking for multiplayer capability.

# How
# It can be used training data for ai - can be used for a simple machine learning model to predicts words, enhancing understanding of ai concepts.


# WHAT 
# It is a guess wording game where a player tries to guess or think a hidden word one letter at a time.
# It accepts user input for guessing
# Checks if the guessed letter is in the hidden word
# Keeps track of the correct guesses and remainnning attempts 
# Displays the partially revealed word after each guess
# And ends the game with a win or losse message after 6 wrong tries.

