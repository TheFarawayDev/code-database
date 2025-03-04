def remove_all_from_string(word, letters_to_remove):
  result = ""
  i = 0
  while i < len(word):
    if word[i:i + len(letters_to_remove)] == letters_to_remove:
      i += len(letters_to_remove)  # Skip the removed letters
    else:
      result += word[i]
      i += 1
  return result

# Get input from the user
word = input("Enter a word: ")
letters_to_remove = input("Enter the letters to remove: ")

# Call the function and print the result
new_word = remove_all_from_string(word, letters_to_remove)
print(new_word)