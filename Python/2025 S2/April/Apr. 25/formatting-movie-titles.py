def title_case_movies(filename="movies.txt"):
    try:
        # Attempt to open the file in read mode
        with open(filename, "r") as file:
            movie_titles = file.readlines()  # Read all lines from the file
    except FileNotFoundError:
        # Handle the case where the file doesn't exist
        print(f"File not found: {filename}. Creating it with default movies.")
        # Create the file and write some default movie titles
        with open(filename, "w") as file:
            default_movies = [
                "snow white and the seven dwarfs",
                "cinderella",
                "sleeping beauty",
                "beauty and the beast",
                "aladdin",
                "the lion king",
                "pocahontas",
                "mulan",
                "the little mermaid",
                "the princess and the frog",
                "tangled",
                "frozen",
                "moana",
                "coco",
                "zootopia",
                "toy story",
                "finding nemo",
                "the incredibles",
                "up",
            ]
            file.write("\n".join(default_movies))  # Write each movie on a new line

        # Now that the file exists, read the movie titles
        with open(filename, "r") as file:
            movie_titles = file.readlines()

    # Iterate through the movie titles, title-case them, and print
    for movie_title in movie_titles:
        # Remove leading/trailing whitespace and title-case the movie title
        title_cased_title = movie_title.strip().title()
        print(f"Movie: {title_cased_title}")

if __name__ == "__main__":
    # Call the function to process the movie titles
    title_case_movies()