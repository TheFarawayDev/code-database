# A template for recording user input to a file with customizable prompts and format by Marshall.
def record_data(filename="output.txt", prompt1="Enter value 1:", prompt2="Enter value 2:", format_string="Value 1: [var1], Value 2: [var2]"):
    variable1 = input(f"{prompt1} ")
    variable2 = input(f"{prompt2} ")

    formatted_output = format_string.replace("[var1]", variable1).replace("[var2]", variable2)

    try:
        with open(filename, "a") as file:
            file.write(f"{formatted_output}\n")
        print(f"Your entry has been recorded in '{filename}'.")
    except Exception as e:
        print(f"An error occurred while writing to the file '{filename}': {e}")

if __name__ == "__main__":
    record_data()
    # Example of reuse:
    # record_data(filename="info.txt", prompt1="Enter your name:", prompt2="Enter your age:", format_string="Name: [var1], Age: [var2]")
    # record_data(filename="coords.txt", prompt1="Enter latitude:", prompt2="Enter longitude:", format_string="Latitude: [var1], Longitude: [var2]")