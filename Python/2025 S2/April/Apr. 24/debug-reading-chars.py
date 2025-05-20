try:
    file = open("example.txt", "r")
    num_chars = 11
    data = file.read(num_chars)
    print("Read characters:", data)
except FileNotFoundError:
    print("Error: The file 'example.txt' was not found.")
except ValueError as e:
    print(f"Error: {e}")
finally:
    if 'file' in locals() and not file.closed:
        file.close()