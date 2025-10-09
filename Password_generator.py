import random as rnd

# Function to generate a password
def password_generator():

    # Random selection of lowercase
    lowercase_character = rnd.choices("abcdefghijklmnopqrstuvwxyz", k=4)

    # Random selection of uppercase
    uppercase_character = rnd.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ",k=4)

    # Random selection of digits
    digits_character = rnd.choices("0123456789", k=4)

    # Random selection of special characters
    special_character = rnd.choices("!@#$%^&*",k=4)

    # Create a list of characters to choose
    characters_list = lowercase_character + uppercase_character + digits_character + special_character

    return characters_list, lowercase_character, uppercase_character, digits_character, special_character

# Wait for user to press Enter key
input("\nPress Enter to create a password:")

# Infinite loop to keep the program running until the user decides to stop
while True:
    # Generate password
    password_creating = password_generator()

    # Create a password of length 8
    password_created = rnd.choices(password_creating[0], k=8)
    # Gluing characters together
    password_created = ''.join(password_created)

    # Check if the password contains at least one lowercase, one uppercase, one digit, and one special character
    has_lower = any(c in password_creating[1] for c in password_created)
    has_upper = any(c in password_creating[2] for c in password_created)
    has_digit = any(c in password_creating[3] for c in password_created)
    has_symbol = any(c in password_creating[4] for c in password_created)

    # If the password meets the criteria, print it
    if has_lower and has_upper and has_digit and has_symbol:
        print(f"Your password is: {password_created}")

        # Ask if the user wants to continue
        choice = input("\nDo you want to continue? (y/n): ").lower()
        if choice != 'y':
            break
    else :
        # Keep building the password until it meets the criteria
        continue



