# use `in` to determine if `word` contains any vowels!
def contains_vowel(word):
    return any(vowel in word for vowel in "aeiou")

# Test cases
print(contains_vowel("hymn"))    # False
print(contains_vowel("hum"))     # True
print(contains_vowel("bubble"))  # True
