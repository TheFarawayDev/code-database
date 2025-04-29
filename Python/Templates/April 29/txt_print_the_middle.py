# Displays the data from the middle of a file to the end. by Marshall
def display_middle_to_end(filename="file.txt", display_format="{data}"):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return

    middle_index = len(lines) // 2  # Integer division to find the middle index
    for line in lines[middle_index:]:
        # Remove leading/trailing whitespace and newline characters before displaying
        data = line.strip()
        print(display_format.replace("{data}", data))

if __name__ == "__main__":
    display_middle_to_end()

    # Example usage with a different filename and format:
    # display_middle_to_end(filename="my_data.txt", display_format="Value: {data}")
