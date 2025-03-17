# Guess the Number Game

A simple command-line number guessing game where the player tries to guess a randomly chosen number between 0 and 100. The game provides feedback if the guess is too high or too low until the correct number is guessed.

## Features
- Random number generation
- User input handling
- Colored text output using `colorama`
- Continuous loop until the correct guess is made

## Prerequisites
Ensure you have Python installed on your system. You can check by running:
```sh
python --version
```

## Installation
1. Clone the repository or download the script.
```sh
git clone <repository_url>
```
2. Navigate to the project directory.
```sh
cd Guess-the-Number-Game
```
3. Install required dependencies.
```sh
pip install -r requirements.txt
```
(If `requirements.txt` does not exist, install `colorama` manually with `pip install colorama`.)

## How to Play
1. Run the script:
```sh
python guess_the_number.py
```
2. Enter a number when prompted.
3. The game will tell you if your guess is too high or too low.
4. Keep guessing until you find the correct number!

## Example Output
```
Welcome To Guess the Number Game :)
Enter Your Guess Number: 50
Your Number is More :(
Enter Your Guess Number: 25
Your Number is Less :(
Enter Your Guess Number: 37
You win ;)
```

## Dependencies
- `random` (Built-in Python module)
- `colorama` (For colored terminal output)

## License
This project is licensed under the MIT License.

## Author
Hesam Okati

