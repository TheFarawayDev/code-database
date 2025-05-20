coordinates = []

# Get 5 coordinate pairs from the user
for i in range(5):
    x = int(input(f"Enter x{i+1}: "))
    y = int(input(f"Enter y{i+1}: "))
    coordinates.append((x, y))

# Calculate and print slopes between adjacent pairs
for i in range(len(coordinates) - 1):
    (x1, y1) = coordinates[i]
    (x2, y2) = coordinates[i + 1]
    
    # Handle division by zero (vertical line)
    if x2 - x1 == 0:
        print(f"Slope between {coordinates[i]} and {coordinates[i+1]}: undefined (vertical line)")
    else:
        slope = (y2 - y1) / (x2 - x1)
        print(f"Slope between {coordinates[i]} and {coordinates[i+1]}: {slope}")
