names = [
    "Maya Angelou",
    "Chimamanda Ngozi Adichie",
    "Tobias Wolff",
    "Sherman Alexie",
    "Aziz Ansari"
]

last_names = [name.split()[-1] for name in names] # name.split() breaks the name into a list of words, and [-1] gets the last word

print(last_names)