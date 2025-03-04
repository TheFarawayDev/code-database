def remove_all_from_string(word, letter):
  result = ""  # Start with an empty string
  i = 0
  while i < len(word):
    if word[i] != letter:
      result = result + word[i]
    i = i + 1
  return result

# Example 1
print(remove_all_from_string("python", "n"))  # Output: pytho

# Example 2
print(remove_all_from_string("pancakes", "a")) # Output: pnckes