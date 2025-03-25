import random 

options = ("rock", "paper", "scissors")

running = True

while running:
    
    player = None 
    computer = random.choice(options)
    


    while player not in options:
        player = input("Enter a choice (rock, papper, scissors): ")

    print (f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("its a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else: 
        print("You loose! :( ")                

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")        


#WHY
# It is useful for various reasons like decision making tool.
# Its a great way also for beginners to practice programming coding , logic and conditional statements
# Gives fundamentals of game theory concepts like probability and startegy and also it is useful for teaching probability and statistic.
# Gives also insights that people often try to predict patterns making it interesting for psychology used in experiments on decision making and randomness.
# It helps develop quick thinking pattern recognition and strategic decision making.


#HOW
# It can be used to build an AI that learns patterns and tries to predicts the users next move
# And also analyze players strategies to see if there's a bias in their choices.

#WHAT
# The random module is imported to use random.choice() function which randomly selects an option for the pc
# A tuple options is created with the 3 possible choices
# The running variable controls the main game loop and it continues until the player decideds to stop
# Player is initialized to none to start and the computer randomly selects an option using random.choice((options)
# The program keeps asking the player for a valid choice until they enter the options
# Display choices of both the player and th e pc are displayed using formatted strings
# If both choices are the same its a tie, the players wins if their choice beats the pc choice arccording to the games rules otherwise the player loses.
# Players again option - the player is prompted to play again, if they enter anything others than "y" the game ends.
# When the player decides to quit, a farewell message is displayed.

# Improvements 
# Handling invalid inputs like spellling mistakes more gracefully
# keep track of players score across multple rounds 
# add a best of 3 or best of 5 features

