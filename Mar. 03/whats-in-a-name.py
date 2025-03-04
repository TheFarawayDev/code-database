def name_contains(name, letter):
  if letter in name:
    return True
  else:
    return False

# Examples:
print(name_contains("michelangelo", "a"))  # Output: True
print(name_contains("gretchen", "s"))     # Output: False