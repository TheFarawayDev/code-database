# fill in this function to return a list containing each character in the name
def spell_name(name):
    letters = []  # Create an empty list to store the letters
    for letter in name:  # Go through each letter in the name
        letters.append(letter)  # Add each letter to the list
    return letters # Return the list of letters

# Examples
print(spell_name('Jessica'))
# => ['J', 'e', 's', 's', 'i', 'c', 'a']

print(spell_name('Ariel'))
# => ['A', 'r', 'i', 'e', 'l']