
import random

def rps(user_input):
    # Define the game rules
    rules = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }

    # Define the game options
    options = list(rules.keys())

    # Validate user input
    if user_input not in options:
        return "Invalid choice"

    # Get computer input
    computer_input = random.choice(options)

    # Determine the game result
    if user_input == computer_input:
        return "It's a tie!"
    elif rules[user_input] == computer_input:
        return "You win!"
    else:
        return "You lose!"
