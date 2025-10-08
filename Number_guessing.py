import random as rnd

print("**Welcome to the Number Guessing Game!**")
# Random number selection between 1 and 100 by the system
chosen_number = rnd.randint(1, 100)

# Random number guess by the player
player_guess = int(input("Guess a number between 1 and 100 (* You only have 10 attempts) : "))

i = 1
# Loop until the player guesses the number or exhausts 10 attempts
while i<11:
    print(f"{i}. attempt")
    # Compare the player's guess with the chosen number
    if player_guess < chosen_number:
        print("Guess bigger")
        # Counter for attempts
        i +=1
        # Ask the player to guess again
        player_guess = int(input("Try again: "))

    elif player_guess > chosen_number:
        print("Guess smaller")
        i += 1
        player_guess = int(input("Try again: "))

    elif player_guess == chosen_number:
        print("Congratulations! You've guessed the number.")
        break

    else:
        print("Sorry, The number was not in the range.")
        i += 1
        player_guess = int(input("Try again: "))