import random as rnd

print("Welcome to Virtual Dice!")

# Infinite loop to keep the program running until the user decides to stop
while True:
    # Wait for user to press Enter key
    input("\nPress Enter key to roll the dice:").lower()
    # Chose random number from 1 to 6
    chosen = rnd.randint(1, 6)
    print("Your number :", chosen)

    # Ask if the user wants to continue
    choice = input("\nDo you want to continue? (y/n): ").lower()
    if choice != 'y':
        print("Your number :",chosen)
        break