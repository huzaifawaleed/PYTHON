# Dictionary.

# person = {
# 'name': "Huzaifa",
# 'age': 20,
# 'country': "Pakistan"
# }

# print(person['name'])
# print(person.keys())
# print(person.values())
# print(person.items())
# person.update({"email": "Huzaifa@gmail.com"})
# person.pop("name")
# print(person)


# cart = {
#     "apple": 3,
#     "banana": 5,
#     "mango": 2
# }

# print("Items in cart:")
# for item, qty in cart.items():
#     print(f"{item.title()} x {qty}")




# Beginner Level – Basics of Dictionary

# Create a dictionary of student data with keys: "name", "age", "class", and print each key and its value.
# stu_data = {
#     'name': "Huzaifa",
#     'age': 20,
#     'class': "Graduation"
# }
# print(stu_data['name'])
# print(stu_data['age'])
# print(stu_data['class'])


# Update the age of a student in a dictionary.

# stu_data = {
#     'name': "Huzaifa",
#     'age': 20,
#     'class': "Graduation"
# }
# stu_data.update({'age': 21})
# print(stu_data)



# Add a new key "email" to an existing dictionary.

# stu_data = {
#     'name': "Huzaifa",
#     'age': 20,
#     'class': "Graduation"
# }
# stu_data.update({'email': "Huzaifa@gmail.com"})
# print(stu_data)


# Delete the key "class" from a dictionary.

# stu_data = {
#     'name': "Huzaifa",
#     'age': 20,
#     'class': "Graduation"
# }
# del stu_data['class']
# print(stu_data)


# Check if the key "grade" exists in the dictionary.

# stu_data = {
#     'name': "Huzaifa",
#     'age': 20,
#     'class': "Graduation"
# }
# if 'grade' in stu_data:
#     print("Present")
# else:
#     print("Absent")


# 🔁 Looping & Accessing Dictionary Data
# Print all the keys from a dictionary using a loop.


# stu_data = {
#     'name': "Huzaifa",
#     'age': 20,
#     'class': "Graduation"
# }
# for key in stu_data.keys():
#     print(key)


# Print all the values using a loop.

# stu_data = {
#     'name': "Huzaifa",
#     'age': 20,
#     'class': "Graduation"
# }
# for value in stu_data.values():
#     print(value)


# Print all key-value pairs using .items() in a for loop.
# stu_data = {
#     'name': "Huzaifa",
#     'age': 20,
#     'class': "Graduation"
# }
# for key,value in stu_data.items():
#     print(key,value)



# Count how many times each letter appears in a word using a dictionary.
# Example input: "banana"
# Output: {'b':1, 'a':3, 'n':2}

# word = input("Enter a word: ")
# count = {}

# for c in word:
#     if c in count:
#         count[c] += 1 
#     else:
#         count[c] = 1

# print("Letters = ",count)        



# Take multiple employee records from the user and store them in a dictionary like this:
# {
#    1: {"name": "Ali", "salary": 50000},
#    2: {"name": "Sara", "salary": 60000}
# }

emp = {}
key = input("Enter key: ")
emp.update(key)
val = input("Enter Value ").isalnum()
emp.update(val)

print("Employee = ",emp)


# 🎯 Intermediate Challenges
# Write a Python program to merge two dictionaries.

# Write a program that sums all the values in a dictionary.

# Create a dictionary from two lists:

# python
# Copy
# Edit
# keys = ["name", "age", "department"]
# values = ["Noman", 28, "IT"]
# Find the key with the highest value in a dictionary:

# python
# Copy
# Edit
# sales = {"Ali": 250, "Nida": 400, "Zeeshan": 320}
# You are building an attendance system. Store student names as keys and "Present" or "Absent" as values.

# 🔒 Bonus: Real-World Logic Building
# Create a dictionary of product prices. Let the user input a product name, and show its price.

# Make a simple voting system where you count votes for candidates:

# python
# Copy
# Edit
# votes = {"Ali": 3, "Sara": 5, "Hamza": 2}
# Store marks of students in 3 subjects and calculate their average marks using dictionary.

# Build a dictionary that counts the number of words in a sentence.

# From a list of names, create a dictionary with names as keys and the length of each name as the value.

