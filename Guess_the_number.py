"""
Guess the Number Game

A simple number guessing game where the user attempts to guess a randomly 
selected number between 0 and 100. The game provides hints if the guess is 
too high or too low until the correct number is guessed.

Modules Used:
- random: For generating a random number.
- colorama: For adding colored text in the command line interface.
"""

import random
import colorama 

# Initialize colorama to automatically reset colors after each print
colorama.init(autoreset=True)
color = colorama.Fore

# Print welcome message in green
print(color.GREEN + "Welcome To Guess the Number Game :)")

# Generate a random number between 0 and 100 for the computer's guess
computer_guess = random.randint(0, 100)

# Get user's first guess input in yellow
user_guess = int(input(color.YELLOW + "Enter Your Guess Number:  "))

# Loop until the user guesses correctly
while user_guess != computer_guess:
    
    # Check if the user's guess is lower than the computer's number
    if user_guess < computer_guess:
        print(color.RED + "Your Number is Less :(")
    
    # Check if the user's guess is higher than the computer's number
    if user_guess > computer_guess:
        print(color.RED + "Your Number is More :(")
    
    # Ask the user to guess again
    user_guess = int(input(color.YELLOW + "Enter Your Guess Number:  "))
    
# If the loop exits, the user has guessed correctly
print(color.GREEN + "You win ;)")
