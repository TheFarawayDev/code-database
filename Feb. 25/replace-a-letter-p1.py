def replace_at_index(string, index):
    # Return the new string with the character at the given index replaced by a dash
    return string[:index] + '-' + string[index+1:]

# Example usage:
print(replace_at_index("eggplant", 3))  # => "egg-lant"
print(replace_at_index("strange", 0))   # => "-trange"
