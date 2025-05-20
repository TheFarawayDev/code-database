def get_guess():
    while True:
        guess = input("Please enter your guess: ")
        if len(guess) != 1:
            print("Your guess must consist of exactly one character.")
        elif not guess.islower():
            print("Your guess must be a lowercase letter.")
        else:
            return guess

secret_word = "pythonisasnake"
word_length = len(secret_word)
guessed_letters = ["-"] * word_length
attempts_remaining = 10

while "-" in guessed_letters and attempts_remaining > 0:
    print("---")
    print(f"{attempts_remaining} incorrect attempts remaining.")
    print(" ".join(guessed_letters))
    current_guess = get_guess()

    if current_guess in secret_word:
        print("That letter is present in the secret word.")
        for index, letter in enumerate(secret_word):
            if letter == current_guess:
                guessed_letters[index] = current_guess
    else:
        attempts_remaining -= 1
        print("That letter is not present in the secret word.")

if "-" not in guessed_letters:
    print("---")
    print(" ".join(guessed_letters))
    print("You have correctly guessed the secret word:", secret_word)
else:
    print("---")
    print("You have used all attempts. The secret word was:", secret_word)
