# Ask the user how many names they have
num_names = int(input("Number of names: "))

# Create an empty list to store the names
names = []

# Use a for loop to ask for each name and add it to the list
for i in range(num_names):
  name = input("Name: ")
  names.append(name)

# Get the first name (it's always at the beginning of the list)
first_name = names[0]

# Get the last name (it's always at the end of the list)
last_name = names[-1]

# Get the middle names (everything in between the first and last)
middle_names = names[1:-1]

# Print the results
print("First name:", first_name)
print("Middle names:", middle_names)
print("Last name:", last_name)