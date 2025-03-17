# this function should return the number of words that contain "owl"!
def owl_count(text):
    # First, let's make everything lowercase so we don't miss any "Owl" or "OWLS"
    lower_text = text.lower()

    # Now, let's break the text into individual words
    words = lower_text.split()

    # Let's keep track of how many "owl" words we find
    count = 0

    # Now, we'll go through each word in the list
    for word in words:
        # If the word has "owl" in it, we'll add to our count!
        if "owl" in word:
            count = count + 1

    # Finally, we'll tell you the total number of "owl" words we found!
    return count

# Let's try it out with the example text!
text = "I really like owls. Did you know that an owl's eyes are more than twice as big as the eyes of other birds of comparable weight? And that when an owl partially closes its eyes during the day, it is just blocking out light? Sometimes I wish I could be an owl."
number_of_owl_words = owl_count(text)
print(number_of_owl_words)
# => 4

another_text = "Howling owls are so neat! I saw a little owlette in the forest."
another_count = owl_count(another_text)
print(another_count)
# => 3