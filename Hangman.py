import random as rnd

print("Welcome to Hangman!","\n")

print("* Guess a word by suggesting letters.")

# List of words to choose from systematically
word_list = ["python", "java", "kotlin", "javascript", "hangman", "programming", "developer", "algorithm"]

# Choose a random word from the list
chosen_word = rnd.choice(word_list)

# Hangman shapes for each incorrect guess
shapes = ["-----",
          "|   |",
          "|   O",
          "|  /|\\",
          "|  / \\",
          "|"]

# Create a hidden representation of the chosen word
hidden_word = ["-" for _ in chosen_word]

# Function to find the index of guessed letter in the true word
def find_letter_index(word_true,word_guessed):
    # Create a list of indices where the guessed letter appears in the true word
    list_index = [i for i, letter in enumerate(word_true) if letter == word_guessed]

    return list_index

# Initialize variables
i = 0
hangman = []

# Main game loop
while i<6:
    # Display the current state of the hidden word
    print("\nWord: ", " ".join(hidden_word))

    # Prompt the user to guess a letter
    user_choice = input(" Say the letters: ").lower()

    # Find the indices of the guessed letter in the chosen word
    index_letters = find_letter_index(chosen_word,user_choice)

    # If the guessed letter is in the word, reveal it in the hidden word
    if index_letters:
        # Update the hidden word with the guessed letter at the correct indices
        for idx in index_letters:
            hidden_word[idx] = user_choice
    else:
        # If the guessed letter is not in the word, add a part to the hangman
        hangman.append(shapes[i])
        # Display the current state of the hangman
        print("\n".join(hangman))
        # Increment the incorrect guess counter
        i += 1

    # check if user has guessed all letters
    if "-" not in hidden_word:
        print("\n You won! The word was:", chosen_word)
        break

else:
    print("\n Game Over! The word was:", chosen_word)