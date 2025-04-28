# Template for reading from a text file

def read_from_txt(filepath):
    try:
        with open(filepath, 'r') as file:
            lines = [line.strip() for line in file.readlines()]
        return lines
    except FileNotFoundError:
        print(f"Error: File not found at '{filepath}'.")
        return None
    except Exception as e:
        print(f"An error occurred while reading from '{filepath}': {e}")
        return None

def read_from_txt_line_by_line(filepath):
    try:
        with open(filepath, 'r') as file:
            for line in file:
                processed_line = line.strip()  # Remove leading/trailing whitespace
                print(f"Processing line: {processed_line}")
                # Add your specific line processing logic here
    except FileNotFoundError:
        print(f"Error: File not found at '{filepath}'.")
    except Exception as e:
        print(f"An error occurred while reading from '{filepath}': {e}")

# Example usage for reading:
file_path_read = "my_output.txt"
content_read = read_from_txt(file_path_read)
if content_read:
    print("\nContents of the file:")
    for line in content_read:
        print(line)

print("\nReading line by line:")
read_from_txt_line_by_line(file_path_read)