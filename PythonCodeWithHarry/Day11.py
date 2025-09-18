# String.
name = "Huzaifa"
lastName = 'Waleed'
print (name + lastName)

# Using both.
random = "Hey its me, 'I want to play cricket'"
print(random)

# Multiline String can be in single or double quotes.

hmm = """Hey!
How are you?
My Name is Huzaifa.
What is Your Name?"""
print(hmm)

# Indexing Accessing the characters starting from 0...

print(name[0])  # H.....
print(name[0:2])  # Hu
print(name[0:3])  # Huz
print(name[1:4])  # uza. It starts from 1.
print(name[::2])  # When we slice like that it means it removes every 2 character.


# To Access large strings we run a loop.

for chars in random:
    print(chars)

for i in range(0, 5, 1):
    print(i)

