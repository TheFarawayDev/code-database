# update this function so it replaces all lowercase 'i's in `text` with '!'
def exclamation(text):
    text_list = list(text)
    for i in range(len(text_list)):
        if text_list[i] == 'i':
            text_list[i] = '!'
    return "".join(text_list)

# Example 1
print(exclamation("I like music."))
# This will print: I l!ke mus!c.

# Example 2
print(exclamation("Mississippi"))
# This will print: M!ss!ss!pp!