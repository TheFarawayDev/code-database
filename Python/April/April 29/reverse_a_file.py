def reverse_file_content(input_filename="story.txt", output_filename="reversed.txt"):
    try:
        with open(input_filename, "r") as infile, open(output_filename, "w") as outfile:
            # Move to the end of the input file
            infile.seek(0, 2)
            file_position = infile.tell()

            reversed_text = ""

            # Loop through the file from the end to the beginning
            while file_position > 0:
                file_position -= 1
                infile.seek(file_position, 0)
                char = infile.read(1)
                reversed_text += char

            outfile.write(reversed_text)

        print(f"Reversed content of '{input_filename}' saved to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    reverse_file_content()
