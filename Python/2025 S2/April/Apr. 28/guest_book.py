def record_guest_entry():
    name = input("Enter your name: ")
    message = input("Enter your message: ")

    try:
        with open("guest_book.txt", "a") as file:
            file.write(f"Name: {name}, Message: {message}\n")
        print("Your entry has been recorded in the guest book.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

if __name__ == "__main__":
    record_guest_entry()