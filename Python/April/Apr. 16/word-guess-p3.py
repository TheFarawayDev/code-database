def get_guess():
    """Requests a letter guess from the user and ensures it is a valid single, lowercase letter."""
    while True:
        guess = input("Please enter your guess: ")
        # Check if the guess is exactly one character long.
        if len(guess) != 1:
            print("Your guess must consist of exactly one character.")
        # Check if the guess is a lowercase letter.
        elif not guess.islower():
            print("Your guess must be a lowercase letter.")
        # If both checks pass, the guess is valid, so we return it.
        else:
            return guess

secret_word = "pythonisasnake"
word_length = len(secret_word)
# Create a list to represent the letters the user has guessed so far.
# It starts with dashes for each letter in the secret word.
guessed_letters = ["-"] * word_length
# Set the number of incorrect attempts the user has.
attempts_remaining = 10

# This loop continues as long as there are unguessed letters (dashes)
# in 'guessed_letters' AND the user has attempts remaining.
while "-" in guessed_letters and attempts_remaining > 0:
    print("---")
    print(f"{attempts_remaining} incorrect attempts remaining.")
    # Display the current state of the guessed word, with spaces between letters/dashes.
    print(" ".join(guessed_letters))
    # Get the user's next guess.
    current_guess = get_guess()

    # Check if the user's guess is in the secret word.
    if current_guess in secret_word:
        print("That letter is present in the secret word.")
        # Go through each letter in the secret word and its position (index).
        for index, letter in enumerate(secret_word):
            # If the guessed letter matches a letter in the secret word at the current position,
            # update the 'guessed_letters' list at that position.
            if letter == current_guess:
                guessed_letters[index] = current_guess
    # If the guess is not in the secret word.
    else:
        # Reduce the number of remaining attempts.
        attempts_remaining -= 1
        print("That letter is not present in the secret word.")

# After the loop finishes, check if the user guessed all the letters.
if "-" not in guessed_letters:
    print("---")
    print(" ".join(guessed_letters))
    print("You have correctly guessed the secret word:", secret_word)
# If there are still dashes in 'guessed_letters', it means the user ran out of attempts.
else:
    print("---")
    print("You have used all attempts. The secret word was:", secret_word)