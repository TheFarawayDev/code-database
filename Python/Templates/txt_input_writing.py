# This is a template for a function that writes variable information to a text file using kwargs by Marshall

def print_variable_info(**kwargs):
    filename = "output.txt"
    try:
        with open(filename, "w") as file:
            for name, value in kwargs.items():
                file.write(f"{name}: {value}\n")
        print(f"Variable information written to {filename}")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def main():
    v1 = input("Enter the value for variable 1: ")
    v1_name = input("Enter the name you want for variable 1 in the output: ")
    v2 = input("Enter the value for variable 2: ")
    v2_name = input("Enter the name you want for variable 2 in the output: ")

    print_variable_info(**{v1_name: v1, v2_name: v2})

if __name__ == "__main__":
    main()