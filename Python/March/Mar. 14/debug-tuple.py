my_tuple = (0, 1, 2, "hi", 4, 5)

# Slice the tuple before the "hi"
first_part = my_tuple[:3]  # This gets (0, 1, 2)

# Slice the tuple after the "hi"
second_part = my_tuple[4:] # This gets (4, 5)

# Create the new tuple by combining the slices and the new element
my_tuple = first_part + (3,) + second_part

print(my_tuple)