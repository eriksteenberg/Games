# TODO: Develop a console-based Rock Paper Scissors Lizard Spock game in Python
# Game should be modular, allowing for easy updates or rule changes
# Implement game rules:
# - Scissors decapitate lizard
# - Scissors cuts paper
# - Paper covers rock 
# - Rock crushes lizard 
# - Lizard poisons Spock 
# - Spock smashes scissors 
# - Lizard eats paper 
# - Paper disproves Spock 
# - Spock vaporizes rock 
# - Rock crushes scissors
# Include user input for selecting options and display game results

import random

def rpsls():

    # Define the game rules
    rules = {
        "rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard": ["spock", "paper"],
        "spock": ["scissors", "rock"]
    }

    # Define the game options
    options = list(rules.keys())

    # Initialize counters
    user_wins = 0
    computer_wins = 0

    # Repeat the game for 3 runs
    for _ in range(3):
        # Get user input
        user_input = input("Enter your choice: ").lower()

        # Validate user input
        if user_input not in options:
            print("Invalid choice")
            return

        # Get computer input
        computer_input = random.choice(options)

        # Display the game options
        print(f"User: {user_input}")
        print(f"Computer: {computer_input}")

        # Determine the game result
        if user_input == computer_input:
            print("It's a tie!")
        elif computer_input in rules[user_input]:
            print("User wins!")
            user_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1

    # Check who won the most
    if user_wins > computer_wins:
        print("User won the most!")
    elif computer_wins > user_wins:
        print("Computer won the most!")
    else:
        print("It's a tie! Adding another round.")
        rpsls()

# Run the game
rpsls()
