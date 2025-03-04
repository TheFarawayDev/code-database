def replace_at_index(string, index, letter):
    # Construct the new string with the letter replacing the character at the given index
    return string[:index] + letter + string[index+1:]

# Example usage:
print(replace_at_index("house", 0, "m"))  # => "mouse"
print(replace_at_index("door", 3, "t"))   # => "doot"
