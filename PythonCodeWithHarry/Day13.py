# STRING METHODS


# lower()
# it change all into lowercase.

# upper()
# it change all into uppercase.

# title()
# it change the first letter of every word into uppercase. it also returns true if the first letter of all words are capital.

# capitalize()
# it change the first letter of every word into uppercase.

# strip()
# it removes spaces from a string from start and end.

# lstrip()
# it removes spaces and any trailing characters from left side.

# rstrip()
# it removes spaces and any trailing characters from left side.

# replace()
# it repalce the characters you want to replace with.

# find()
# it finds the character and gives the index where it locate.

# index()
# same as find() it finds the character and gives the index where it locate.

# count()
# it counts how many times the character appears.

# startswith()
# it rteurns True if the words is start with like "Huzaifa" startswith("Hu").

# endswith()
# it rteurns True if the words is start with like "Huzaifa" endswith("fa").

# isalpha()
# Returns True if all characters are alphabet letters. a to z.

# isdigit()
# Returns True if all digits like numbers. 0 to 9.

# isalnum()
# it returns True if the string contains both alphabets and digits or just alphabets or numbers it returns True. abc123.

# isspace()
# it returns True if a string is only have space.

# split()
# converts all the strings into list by giving a , like split(",").

# center()
# centers the string.

# join()
# swapcase()
# zfill()
# casefold()
# rfind()
# rindex()
# partition()
# rpartition()
# expandtabs()
# encode()
# isidentifier()

a = "Huzaifa"
b = "waleed"
c = "hello !!!!"
d = "123"
z = "ac1211"
x = " "
li = "Huzaifa, Waleed, Hello"
print(a.lower())
print(a.upper())
print(a.title())
print(b.capitalize())
# print(c.strip())
print(c.rstrip("!"))
print(c.replace("l","o"))
print(a.find("a"))
print(a.index("i"))
print(b.count("e"))
print(a.startswith("Hu"))
print(a.endswith("fa"))
print(a.isalpha())
print(d.isdigit())
print(z.isalnum())
print(z.isspace())
print(li.split(","))