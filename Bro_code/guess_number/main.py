import random 

lowest_num = 1
highest_num = 100 
answer = random.randint(lowest_num, highest_num)
guesses = 0 
is_running = True 

#print(answer)
print ("Python number guesing games")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running :

    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That  number is out of range")
            print(f"Please select number between {lowest_num} - {highest_num}")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False
    else:
        print("Invalid guess")
        print(f"Please select number between {lowest_num} - {highest_num}")

        # WHY 
        # It can be useful to begin Practice in Programming as its a beginner friendly exercise.
        # But of course it also helps me to use pythons random module to generate numbers, encourrages logical thinking BUT most of all 
        #  it build a base for ai powered guessing games, probability analysis or more advanced applications.

        # How
        # I can use it for Learning, game dev and teaching probability
        # - It can be used to help practice loops,conditionals and users input.
        # - Can be expanded into advancegames with ai or UI.
        
        # WHAT 
        # It generates random number, asks a player to guess, provides hints (high or low) and ends when the correct number is guessed.

        