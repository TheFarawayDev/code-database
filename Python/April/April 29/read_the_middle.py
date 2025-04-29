def display_middle_to_end(filename="numbers.txt"):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return

    middle_index = len(lines) // 2
    for line in lines[middle_index:]:
        print(line.strip())

if __name__ == "__main__":
    display_middle_to_end()