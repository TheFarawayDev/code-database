# fill in this function to greet the user!
def greeting(user_info):
    info_list = user_info.split()  # Split the string into a list of words
    name = info_list[0]  # Get the name (first word)
    hobby = info_list[2] # Get the hobby (third word)
    return f"Hello, {name}! I also enjoy {hobby}!" # Use f-strings for easy formatting

# Examples
print(greeting('Jose 17 hockey'))
# => 'Hello, Jose! I also enjoy hockey!'

print(greeting('Cindy 14 robotics'))
# => 'Hello, Cindy! I also enjoy robotics!'