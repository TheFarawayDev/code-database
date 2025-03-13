def citation(author_name):
    first_name = author_name[0]
    middle_name = author_name[1]
    last_name = author_name[2]
    return last_name + ", " + first_name + " " + middle_name

print(citation(("Martin", "Luther", "King, Jr.")))
print(citation(("J.", "D.", "Salinger")))
print(citation(("Ursula", "K.", "Le Guin")))
print(citation(("J.", "K.", "Rowling")))