# Create an empty list to hold the numbers
numbers = []

# Use a for loop to ask for five numbers
for i in range(5):
  # Ask the user for a number
  num_str = input("Number: ")
  # Convert the number from text to a real number (integer)
  number = int(num_str)
  # Add the number to our list
  numbers.append(number)
  # Print the list so far
  print(numbers)

# Now let's find the sum of all the numbers in the list
total = 0
for num in numbers:
  total = total + num

# Print the final sum
print("Sum:", total)