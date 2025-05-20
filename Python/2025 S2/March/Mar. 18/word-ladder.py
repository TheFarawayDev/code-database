def get_index(word):
    while True:
        try:
            index_str = input("Enter an index (-1 to quit): ")
            index = int(index_str)
            if index == -1:
                return -1
            elif 0 <= index < len(word):
                return index
            else:
                print("Invalid index")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_letter():
    while True:
        letter = input("Enter a letter: ")
        if len(letter) != 1:
            print("Must be exactly one character!")
        elif not 'a' <= letter <= 'z':
            print("Character must be a lowercase letter!")
        else:
            return letter

initial_word = input("Enter a word: ")
current_word_list = list(initial_word)

while True:
    index = get_index(initial_word)
    if index == -1:
        break

    letter = get_letter()
    current_word_list[index] = letter
    print("".join(current_word_list))

print("Thanks for playing!")