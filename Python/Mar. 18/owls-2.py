def check_for_owl(text):
    words = text.lower().split()
    owl_indices = []
    for index, word in enumerate(words):
        if "owl" in word:
            owl_indices.append(index)

    owl_count = len(owl_indices)
    print(f"There were {owl_count} words that contained 'owl'.")
    if owl_indices:
        print(f"They occurred at indices: {owl_indices}")
    else:
        print("No words containing 'owl' were found.")

# Let's ask the user for some text
user_text = input("Enter some text: ")

# And then we'll check it for owls and their locations!
check_for_owl(user_text)