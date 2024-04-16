import random

# List of words for the game
word_list = ['apple', 'banana', 'orange', 'grape', 'strawberry', 'kiwi', 'pineapple']

# Select a random word from the list
word = random.choice(word_list)

# Initialize variables
guessed_letters = []
max_attempts = 6
attempts = 0

# Print welcome message
print("Welcome to Hangman!")
print("Try to guess the word.")

# Game loop
while True:
    # Display the current status of the word
    display_word = ''
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + ' '
        else:
            display_word += '_ '
    print(display_word)

    # Ask the player to guess a letter
    guess = input("Guess a letter: ").lower()

    # Check if the guessed letter is in the word
    if guess in word:
        print("Correct guess!")
        guessed_letters.append(guess)
    else:
        print("Incorrect guess!")
        attempts += 1

    # Check if the player has won or lost
    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You guessed the word:", word)
        break
    elif attempts >= max_attempts:
        print("Sorry, you ran out of attempts. The word was:", word)
        break
