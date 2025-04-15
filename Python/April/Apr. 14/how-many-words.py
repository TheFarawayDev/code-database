def count_words():
  """
  Asks the user for text, splits it into words, and counts each word.
  """
  user_text = input("Please enter some text: ")  # Ask the user for text
  words = user_text.lower().split()  # Split the text into words and make them lowercase

  word_counts = {}  # Create an empty dictionary to store word counts

  for word in words:  # Go through each word in the list of words
    if word in word_counts:  # If the word is already in the dictionary
      word_counts[word] += 1  # Increase its count by 1
    else:  # If the word is not in the dictionary
      word_counts[word] = 1  # Add it to the dictionary with a count of 1

  print(word_counts)  # Print the dictionary of word counts

count_words() #call the function.