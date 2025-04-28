def extract_and_display_quotes(filename="quotes.txt"):
    try:
        # Attempt to open the file in read mode
        with open(filename, "r") as file:
            quotes = file.readlines()
    except FileNotFoundError:
        # Handle the case where the file doesn't exist
        print(f"File not found: {filename}. Creating it with default quotes.")
        # Create the file and write the default quotes
        with open(filename, "w") as file:
            default_quotes = [
                '"Think like a queen. A queen is not afraid to fail. Failure is another steppingstone to greatness." - Oprah Winfrey',
                '"The question isn\'t who\'s going to let me; it\'s who\'s going to stop me." - Ayn Rand',
                '"Life is not measured by the number of breaths we take, but by the moments that take our breath away." - Maya Angelou',
                '"Empowering women isn\'t just the right thing to do—it\'s the smart thing to do." - Barack Obama',
                '"Women belong in all places where decisions are being made." - Ruth Bader Ginsburg',
            ]
            file.write("\n".join(default_quotes))  # Write each quote on a new line

        # Now that the file exists, read the quotes
        with open(filename, "r") as file:
            quotes = file.readlines()

    # Process and print each quote
    for quote in quotes:
        # Remove leading/trailing whitespace
        quote = quote.strip()
        # Remove the quotation marks and author using string manipulation.
        if '"' in quote and '-' in quote:
            start_quote = quote.find('"') + 1
            end_quote = quote.find('"', start_quote)
            cleaned_quote = quote[start_quote:end_quote]
            print(cleaned_quote)
        else:
            print(quote) # print the whole line if it doesn't match expected format.

if __name__ == "__main__":
    # Call the function to extract and display the quotes
    extract_and_display_quotes()