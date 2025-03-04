import random

def select_random_word(word_list):
  """Returns a random word from the given list."""
  return random.choice(word_list)

def display_word(word, guessed_letters):
  """Displays the word with guessed letters revealed."""
  displayed_word = ""
  for letter in word:
    if letter in guessed_letters:
      displayed_word += letter
    else:
      displayed_word += "_"
  return displayed_word

def get_player_guess():
  """Gets and returns the player's letter guess."""
  while True:
    guess = input("Guess a letter: ").lower()
    if len(guess) == 1 and guess.isalpha():
      return guess
    else:
      print("Please enter a single letter.")

def check_letter(letter, secret_word):
  """Returns True if the letter is in the secret word, False otherwise."""
  return letter in secret_word

def check_win(secret_word, guessed_letters):
  """Returns True if all letters have been guessed, False otherwise."""
  for letter in secret_word:
    if letter not in guessed_letters:
      return False
  return True

def hangman():
  """Main Hangman game function."""
  word_list = ["apple", "banana", "cherry", "date", "elderberry"]
  secret_word = select_random_word(word_list)
  guessed_letters = []
  incorrect_guesses = 0
  max_incorrect_guesses = 6

  while incorrect_guesses < max_incorrect_guesses and not check_win(secret_word, guessed_letters):
    print("Word:", display_word(secret_word, guessed_letters))
    print("Incorrect guesses:", incorrect_guesses)
    print("Guessed letters:", guessed_letters)

    guess = get_player_guess()

    if guess not in guessed_letters:
      guessed_letters.append(guess)

      if check_letter(guess, secret_word):
        print("Correct guess!")
      else:
        print("Incorrect guess.")
        incorrect_guesses += 1
    else:
      print("You already guessed that letter.")

  if check_win(secret_word, guessed_letters):
    print("Congratulations! You guessed the word:", secret_word)
  else:
    print("You ran out of guesses. The word was:", secret_word)
    print("Game Over.")

# Start the game
hangman()