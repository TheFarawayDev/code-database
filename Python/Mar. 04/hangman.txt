# Hangman Game Pseudocode

# 1. SET up the game
SET word_list = ["apple", "banana", "cherry", "date", "elderberry"]
SET secret_word = SELECT_RANDOM_WORD(word_list) # Pick a random word
SET guessed_letters = [] # Keep track of guessed letters
SET incorrect_guesses = 0 # Count wrong guesses
SET max_incorrect_guesses = 6 # Set the maximum number of wrong guesses

# 2. START the game loop
LOOP WHILE incorrect_guesses < max_incorrect_guesses AND player has not won:
    # 3. SHOW the current state
    DISPLAY "Word: " + DISPLAY_WORD(secret_word, guessed_letters)
    DISPLAY "Incorrect guesses: " + incorrect_guesses
    DISPLAY "Guessed letters: " + guessed_letters

    # 4. GET player's guess
    SET guess = GET_PLAYER_GUESS()

    # 5. CHECK if the guess is valid
    IF guess is not in guessed_letters:
        # 6. UPDATE guessed letters
        ADD guess to guessed_letters

        # 7. CHECK if the guess is correct
        IF CHECK_LETTER(guess, secret_word) is TRUE:
            DISPLAY "Correct guess!"
        ELSE:
            DISPLAY "Incorrect guess."
            INCREMENT incorrect_guesses by 1
    ELSE:
        DISPLAY "You already guessed that letter."

    # 8. CHECK for win
    IF CHECK_WIN(secret_word, guessed_letters) is TRUE:
        DISPLAY "Congratulations! You guessed the word: " + secret_word
        BREAK # Exit the loop

# 9. CHECK for loss
IF incorrect_guesses >= max_incorrect_guesses:
    DISPLAY "You ran out of guesses. The word was: " + secret_word
    DISPLAY "Game Over."