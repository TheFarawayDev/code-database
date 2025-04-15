def get_guess():
    """Retrieves a valid guess from the user."""
    while True:
        guess = input("Guess: ")
        if len(guess) != 1:
            print("Your guess must have exactly one character!")
        elif not guess.islower():
            print("Your guess must be a lowercase letter!")
        else:
            return guess

secret_word = "example"  # Replace with your secret word!

for _ in range(10):  # Loop 10 times for 10 guesses
    guess = get_guess()
    if guess in secret_word:
        print("That letter is in the secret word!")
    else:
        print("That letter is not in the secret word!")