def return_books():
  """Asks for the last names of five authors and prints them in sorted order."""

  author_last_names = []
  for i in range(5):
    while True:
      name = input(f"Please enter the last name of author {i+1}: ")
      if name:  # Make sure the user enters something
        author_last_names.append(name)
        print(f"Name: {name}")
        break
      else:
        print("Please enter a name.")

  author_last_names.sort()
  print(author_last_names)

# Let's run the function!
return_books()