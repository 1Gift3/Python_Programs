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
# Well i believe k word would make me win guessing the word Orange so thats whtats wrong and also
# i am not guessing 5 times before the 6th to loose or win
# Line 79 iss a python construct used to control execution of a script - in
#simpler terms main will only run when script is executed directly and not run when its imported as a module.


# Seems like the problem was on main function line 38 on the hint as i before "Underscore" __ doubled that not single
# The issue also was on def main function on wrong_guesses when i initially put 6
# instead of zero which made the program to initially start @ 0 

# the variable wrong guesses keeps track of how many incorrect guesses player made
# now my dict stated that hangman has 7 states 0 - 6, not is wrong guess starts @ 6, the game will forever diplaying the final hangman


