# Ask the user for their first and last name
first_name = input("First name: ")
last_name = input("Last name: ")

# Print full name
print("Full name:", first_name, last_name)

# Swap the order for citation format
first_name, last_name = last_name, first_name

# Print citation
print("Citation:", f"{first_name}, {last_name}")
