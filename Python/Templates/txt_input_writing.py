# This is a template for a function that writes variable information to a text file by Marshall

def print_variable_info(var1, var2, var3, var4, filename="output.txt"):
    try:
        with open(filename, "w") as file:
            file.write(f"var1: {var1}, Var1: {var1}\n")
            file.write(f"var2: {var2}, Var2: {var2}\n")
            file.write(f"var3: {var3}, Var3: {var3}\n")
            file.write(f"var4: {var4}, Var4: {var4}\n")
        print(f"Variable information written to {filename}")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def main():
    v1 = input("Enter the value for variable 1: ")
    v2 = input("Enter the value for variable 2: ")
    v3 = "Hello"
    v4 = 123

    print_variable_info(v1, v2, v3, v4)

if __name__ == "__main__":
    main()
