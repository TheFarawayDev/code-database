beatles = []
print("Step 1:", beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

members_to_add = ["Stu Sutcliffe", "Pete Best"]
for member in members_to_add:
    name = input(f"Please add {member}: ")
    beatles.append(name)
print("Step 3:", beatles)

del beatles[3]
del beatles[3]
print("Step 4:", beatles)

beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)

print("The Fab", len(beatles))