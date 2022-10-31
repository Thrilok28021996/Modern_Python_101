"""
Set:
-----

Set is all about being 'unique', it's very useful for certain operations.

Info:
-----
In a set all values are unique

"""

# ------------------------------------
# To show unique alphabets in magic
# -------------------------------------

magic_word = "abracadabra"
unique_alphabets: set[str] = set(magic_word)

print(f"Unique Alphaberts: {unique_alphabets}")


sentence = "the big blue sky and the big blue ocean"

unique_alphabets: set[str] = set(sentence)
print(f"Unique Alphaberts: {unique_alphabets}")

# ------------------------------------
# To see list of unique words
# -------------------------------------

word_list = sentence.split()
print(f"Word List: {word_list}")

# extract Unique words
unique_words = set(word_list)
print(f"Unique words: {unique_words}")

# ------------------------------------
# To add more words to the set
# -------------------------------------
unique_words.update(["big", "blue", "sky"])
print(f"Unique words: {unique_words}")

unique_words.update(["green", "grass"])
print(f"Unique words: {unique_words}")

# ------------------------------------
# remove a word from set
# -------------------------------------

unique_words.remove("grass")
print(f"Unique words: {unique_words}")
