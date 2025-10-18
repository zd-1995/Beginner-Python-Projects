# Beginner Python Projects

This repository contains simple Python projects for practice and learning. It includes:

1 - **Calculator**

2 - **Text Analyzer**

3 - **Number Guessing Game**

4 - **Rock Paper Scissors**

5 - **Virtual Dice**

6 - **Password Generator**

7 - **Hangman Game**

---

## Files in this project

### 1. `Calculator.py`
This file is a **simple calculator** program.  
- Supports basic arithmetic operations: addition, subtraction, multiplication, division, modulus, and floor division.  
- Users can input two numbers and an operator to get the result.
- In the while loop section, you can execute a state of the calculator by commenting out one of two states. One section can be executed at a time.

### 2. `Text_analyzer.py`
This file is a **text analysis tool**.  
- Reads a text file and analyzes it.  
- Provides the following statistics:
  - Number of sentences  
  - Number of words  
  - Number of letters  
  - Average word length  
  - Most frequently used word  
- You can replace the sample file path with your own text file to analyze custom text.

### 3. `sample.txt`
This is a **sample text file** used for testing the `Text_analyzer.py` program.



### 4.  `Number Guessing Game`
This file is a **Number guessing game**. 
This is a simple Python project where the computer randomly selects a number between 1 and 100, and the player has to guess it.
- Features:
  - Random number generation  
  - User input for guesses  
  - Feedback ("Guess bigger" or "Guess smaller")  
  - Maximum 10 attempts  

### 5. `Rock Paper Scissors`
This file is a **Rock Paper Scissors game**.  
This is a simple Python project where the player competes against the computer in the classic **Rock, Paper, Scissors** game.
- Features:  
  - Random choice selection by the computer  
  - User input for selection (`rock`, `paper`, or `scissors`)  
  - Determines the winner based on game rules  
  - Handles invalid input with a warning message
  
### 6. `Virtual Dice`
This file is a **Virtual Dice game**.  
This is a simple Python project where the player can roll a virtual dice and get a random number between 1 and 6. The game continues until the player decides to stop.
- Features:  
  - Random number generation for the dice roll  
  - Infinite loop to keep the game running until the user quits  
  - User interaction with "Press Enter to roll"  
  - Option to continue or stop after each roll  

### 7. `Password Generator`
This file is a **Password Generator**.  
It is a simple Python project that creates secure 8-character passwords containing lowercase letters, uppercase letters, digits, and special symbols.  
- Features:
  - Random password generation  
  - Ensures inclusion of lowercase, uppercase, digit, and special character  
  - Uses Python’s `random` module  
  - Option to continue generating new passwords  

### 8. `Hangman Game`
This file is a **Hangman game** — a classic word-guessing game built using Python.  
The computer randomly selects a word, and the player must guess it one letter at a time before the hangman drawing is complete.
- Features:
  - Random word selection from a predefined list
  - Step-by-step display of the hangman figure for wrong guesses  
  - Dynamic word reveal as the user guesses letters correctly  
  - Win condition when all letters are guessed  
  - Lose condition after 6 incorrect guesses  

** All code files are executed only by running in the Python environment.

This project was developed and tested with the following versions:

- **Python**: 3.13.5    
- **re (Regular Expressions)**: 2.2.1