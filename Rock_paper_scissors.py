import random as rnd

# Define the choices
choices = ["rock", "paper", "scissors"]

# Function to determine the winner
def determine_winner(user_choice, system_choice):
    if user_choice == system_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and system_choice == "scissors") or \
         (user_choice == "paper" and system_choice == "rock") or \
         (user_choice == "scissors" and system_choice == "paper"):
        return "You win!"
    else:
        return "System wins!"

# Randomly select the system's choice
chosen = choices[rnd.randint(0, 2)]

# Get user input
user_input = input("Enter rock, paper, or scissors: ").lower()

# Determine the winner
if user_input in choices:
    print(f"System chose: {chosen}")
    result = determine_winner(user_input, chosen)
    print(result)

else :
    print("Sorry, I didn't understand that.")

