# Reads numbers from a file, calculates their sum, and writes the result to another file by Marshall
def calculate_and_write_sum(input_filename="data.txt", output_filename="sum.txt"):
    try:
        with open(input_filename, "r") as infile:
            numbers = [int(line.strip()) for line in infile]  # Read numbers from each line
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
        return  # Exit if the input file doesn't exist
    except ValueError:
        print(f"Error: Invalid data in '{input_filename}'.  Ensure it contains only numbers, one per line.")
        return

    total_sum = sum(numbers)

    try:
        with open(output_filename, "w") as outfile:
            outfile.write(str(total_sum))
        print(f"Sum calculated and written to '{output_filename}'.")
    except Exception as e:
        print(f"An error occurred while writing to the file '{output_filename}': {e}")

if __name__ == "__main__":
    calculate_and_write_sum()

    # Example usage with different filenames
    # calculate_and_write_sum(input_filename="values.txt", output_filename="total.txt")