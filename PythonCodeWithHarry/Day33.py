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

employees = {}
count = int(input("How many employees do you want to enter? "))

for i in range(1, count + 1):
    print(f"\nEnter details for employee #{i}")
    name = input("Name: ")
    salary = int(input("Salary: "))
    
    employees[i] = {"name": name, "salary": salary}

print("\nEmployee Records:")
for emp_id, info in employees.items():
    print(f"{emp_id}: Name = {info['name']}, Salary = Rs.{info['salary']}")



# 🎯 Intermediate Challenges
# Write a Python program to merge two dictionaries.

# ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
# ep2 = {222: 67, 566: 90}
# ep1.update(ep2)
# print(ep1)

# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
# merged_dict = dict1 | dict2
# print(merged_dict)



# Write a program that sums all the values in a dictionary.

dic = {'a': 20, 'b': 30}
add = 0
for value in dic.values():
    add += value
print(add)    



# Create a dictionary from two lists:


# keys = ["name", "age", "department"]
# values = ["Noman", 28, "IT"]
# dic = dict(zip(keys,values))
# print(dic)


# Find the key with the highest value in a dictionary:

sales = {"Ali": 250, "Nida": 400, "Zeeshan": 320}
high = 0
top_key = ""
for key,value in sales.items():
    if value > high:
        high = value
        top_key = key
print(f"The Highest is {high} by {top_key} ")        

sales = {"Ali": 250, "Nida": 400, "Zeeshan": 320}
less = 400
less_key = ""
for key,value in sales.items():
    if value < less:
        less = value
        less_key = key
print(f"The Lowest is {less} by {less_key} ")





# 🔒 Bonus: Real-World Logic Building
# Create a dictionary of product prices. Let the user input a product name, and show its price.

# products = {
#     'sugar': 180,
#     'tea': 190,
#     'oil': 550,
#     'bread': 90,
#     'milk': 220,
#     'yogurt': 100
# }

# name = input("Enter the product name to know its price: ").lower()

# if name in products:
#     print(f"The price of {name} is Rs.{products[name]}")
# else:
#     print("Product not found. Please enter a valid product name.")

       


# Make a simple voting system where you count votes for candidates:


# votes = {"Ali": 0, "Sara": 0, "Hamza": 0}


# while True:
#   user = input("Enter the name of the candidates to vote. Ali, Sara, Hamza: ").capitalize()
#   if user == "Ali":
#         votes["Ali"] += 1
#   elif user == "Sara":
#      votes["Sara"] += 1
#   elif user == "Hamza":
#      votes["Hamza"] += 1
#   elif user.lower() == "stop":
#       print("Voting Ends")
#       print("The Voting Results",votes)
#       break
#   else:
#       print("Invalid Candidate Name!")


# votes = {"Ali": 0, "Sara": 0, "Hamza": 0}

# while True:
#     print("Voting System.")
#     print("1. Cast Your Vote")
#     print("2. Stop")

#     opt = input("Enter Number to Choose: ")

#     if not opt.isdigit():
#         print("Enter a Valid Number")
#         continue
#     opt = int(opt)

#     match opt:
#         case 1:
#             while True:
#              user = input("Enter the name of the candidates to vote. Ali, Sara, Hamza or enter back to the menu: ").capitalize()
#              if user == "Ali":
#                  votes["Ali"] += 1
#              elif user == "Sara":
#                votes["Sara"] += 1
#              elif user == "Hamza":
#                votes["Hamza"] += 1
#              elif user.lower() == "back":
#                  break
#              else:
#                 print("Invalid Candidate Name!")  

#         case 2: 
#                 print("Voting Ends")
#                 print("The Voting Results",votes)
#                 break
#         case _:
#             print("Invalid Option")     



# Store marks of students in 3 subjects and calculate their average marks using dictionary.

marks = {'maths': 100, 'urdu': 90, 'english': 80}
add = 0
for val in marks.values():
    add += val
    avg = add/len(marks)
print(f"total marks {add} and average {avg}")    


# Build a dictionary that counts the number of words in a sentence.

# sen = input("Enter a Sentence: ")
# words = sen.split()

# dic = {}

# for w in words:
#     if w in dic:
#         dic[w] += 1
#     else:
#         dic[w] = 1
# print("The word In Sentence is ",dic)        


# This counts the length of words in a key.
# marks = {'maths': 100, 'urdu': 90, 'english': 80}
# count = 0
# for key in marks.keys():
#     count += len(key)
# print(count)


# From a list of names, create a dictionary with names as keys and the length of each name as the value.

name = ['huzaifa','usama','zubair','ali']
dic = {n: len(n) for n in name}
print(dic)