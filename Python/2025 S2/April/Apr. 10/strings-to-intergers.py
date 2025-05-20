def safe_int(value):
    """
    Tries to convert a value to an integer. If it works, it returns the integer.
    If it doesn't work, it returns 0.
    """
    try:
        return int(value)  # Try to turn the value into an integer
    except ValueError:
        return 0  # If it fails, return 0

list_of_strings = ["a", "2", "7", "zebra"]  # Our list of strings

result = [safe_int(item) for item in list_of_strings]  # Create a new list using safe_int

print(result)  # Print the new list