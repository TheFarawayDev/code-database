# Reverses the order of characters in a file and saves the reversed content to a new file by Marshall
def reverse_file_content(input_filename="file.txt", output_filename="reversed.txt", char_variable_name="char"):
    try:
        with open(input_filename, "r") as infile, open(output_filename, "w") as outfile:
            infile.seek(0, 2)  # 0: from beginning; 2: to end
            file_position = infile.tell()  # Get the current position (end of file)

            reversed_text = ""

            # Loop through the file from the end to the beginning
            while file_position > 0:
                file_position -= 1  # Move the file pointer back by one character
                infile.seek(file_position, 0)  # Move to the new position
                char = infile.read(1)  # Read one character
                reversed_text += char # Append the character

            outfile.write(reversed_text)

        print(f"Reversed content of '{input_filename}' saved to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    reverse_file_content()

    # Example usage with different filenames and variable name:
    # reverse_file_content(input_filename="original.txt", output_filename="reversed_output.txt", char_variable_name="my_char")
