# Exercise 4.

word = input("Enter a word: ")

if len(word) > 0:
    modified = word[1:] + word[0]
    print("Modified word:", modified)
else:
    print("Please enter a valid word.")
