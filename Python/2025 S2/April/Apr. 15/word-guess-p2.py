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

def update_dashes(secret_word, dashes, guess):
    """Updates the dashes string based on the guess."""
    result = ""
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            result += guess
        else:
            result += dashes[i]
    return result

secret_word = "example"  # Replace with your secret word!
dashes = "-" * len(secret_word) #creates the initial dashes string

for _ in range(10):  # Loop 10 times for 10 guesses
    print(dashes) #print dashes before asking for guess
    guess = get_guess()
    if guess in secret_word:
        print("That letter is in the word!")
        dashes = update_dashes(secret_word, dashes, guess) #update dashes
    else:
        print("That letter is not in the word.")