# Template for writing to a text file

def write_to_txt(filepath, content, append=False):
    mode = 'a' if append else 'w'
    try:
        with open(filepath, mode) as file:
            if isinstance(content, list):
                file.writelines(line + '\n' for line in content)
            else:
                file.write(content + '\n')
        print(f"Successfully wrote to '{filepath}'.")
    except Exception as e:
        print(f"An error occurred while writing to '{filepath}': {e}")

# Example usage for writing:
file_path_write = "my_output.txt"
text_to_write = "This is the first line of text."
more_text = ["This is the second line.", "And this is the third line."]

write_to_txt(file_path_write, text_to_write)
write_to_txt(file_path_write, more_text, append=True)