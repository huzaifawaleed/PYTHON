# Set Joining Methods.

# Union() & Update()
# In union() it returns the values of two sets in a new third set like set3 = set1.union(set2).
# In update() it returns the values of both sets in first set there is no need to create third variable like car1.update(car2)


# car1 = {"Honda", "Toyota", "Suzuki","Hyundai"}
# car2 = {"Honda", "Changan", "Peugeot","Hyundai"}
# car3 = car1.union(car2)
# print(car3)

# car1 = {"Honda", "Toyota", "Suzuki","Hyundai"}
# car2 = {"Honda", "Changan", "Peugeot","Hyundai"}
# car1.update(car2)
# print(car1)


# intersection() & intersection_update().
# In intersection() it returns the common values of both sets in a new set like set3 = set1.intersection(set2).
# In intersection_update() it returns the values of both sets in first set there is no need to create third variable like car1.intersection_update(car2).


# car1 = {"Honda", "Toyota", "Suzuki","Hyundai"}
# car2 = {"Honda", "Changan", "Peugeot","Hyundai"}
# car3 = car1.intersection(car2)
# print(car3)

# car1 = {"Honda", "Toyota", "Suzuki","Hyundai"}
# car2 = {"Honda", "Changan", "Peugeot","Hyundai"}
# car1.intersection_update(car2)
# print(car1)


# symmetric_difference() & symmetric_difference_update().
# In symmetric_difference() it returns the values which are not common in both sets in a new set like set3 = set1.symmetric_difference(set2).
# In intersection_update() it returns the values which are not common in both sets in first set there is no need to create third variable like car1.symmetric_difference_update(car2).


# car1 = {"Honda", "Toyota", "Suzuki","Hyundai"}
# car2 = {"Honda", "Changan", "Peugeot","Hyundai"}
# car3 = car1.symmetric_difference(car2)
# print(car3)

# car1 = {"Honda", "Toyota", "Suzuki","Hyundai"}
# car2 = {"Honda", "Changan", "Peugeot","Hyundai"}
# car1.symmetric_difference_update(car2)
# print(car1)


# Difference() & Difference_Update().
# In difference() it returns the values which are only present in orignal set means set1 in a new variable like set3 = set1.difference(set2).
#In difference_update() it returns the values which are only present in orignal set means set1 there is no need of new variable it updates existing variable like set1.difference_update(set2).

# car1 = {"Honda", "Toyota", "Suzuki","Cultus"}
# car2 = {"Honda", "Changan", "Peugeot","Hyundai"}
# car3 = car1.difference(car2)
# print(car3)

# car1 = {"Honda", "Toyota", "Suzuki","Cultus"}
# car2 = {"Honda", "Changan", "Peugeot","Hyundai"}
# car1.difference_update(car2)
# print(car1)


# SETS METHODS.

# isdisjoint()
# it is use to check that the values of set is present in another set if present it return FALSE else TRUE.

# car1 = {"Honda", "Toyota", "Suzuki","Cultus"}
# car2 = {"Honda", "Changan", "Peugeot","Hyundai"}
# print(car1.isdisjoint(car2))   #False


# issuperset()
# it checks if ALL the values of particular/second set is present in original set if present it returns TRUE else FALSE.

# car1 = {"Honda", "Toyota", "Suzuki","Cultus"}
# car2 = {"Honda", "Changan", "Peugeot","Hyundai"}
# print(car1.issuperset(car2))   #False
# car3 = {"Honda", "Toyota", "Suzuki","Cultus"}
# print(car1.issuperset(car3))  #True

# issubset()
# it is the opposite of issuperset() checks if ALL the values of original set is present in particular/second set if present it returns TRUE else FALSE.


# car1 = {"Honda", "Changan", "Suzuki","Cultus"}
# car2 = {"Honda", "Changan"}
# print(car2.issubset(car1))   #True
# car3 = {"Honda", "Toyota", "Suzuki","Cultus"}
# print(car3.issubset(car2))  #False


# add().
# it is used to add a single value in a set.

# car1 = {"Honda", "Changan", "Suzuki","Cultus"}
# car1.add("Mehran")
# print(car1)


#update().
# if you want to add one or item in a set simply create a new set or use update method to up the existing set.

# car1 = {"Honda", "Changan", "Suzuki","Cultus"}
# car2 = {"Mehran"}
# car1.update(car2)
# print(car1)


#remove()/discard().
# it remove or discard the item from set.

# car1 = {"Honda", "Changan", "Suzuki","Cultus"}
# car1.remove("Honda")
# print(car1)

# car1 = {"Honda", "Changan", "Suzuki","Cultus"}
# car1.discard("Cultus")
# print(car1)


# pop()
# this method use to remove the last item from set but sets are unorder we don't which item will be remove to know this assign pop() to a variable.

# car1 = {"Honda", "Changan", "Suzuki","Cultus"}
# item = car1.pop()
# print(car1)
# print(item)


# del
# it deletes the entire set it is not a method it is a keyword.

# car1 = {"Honda", "Changan", "Suzuki","Cultus"}
# del car1
# print(car1)


# clear().
# This method clears the entire set and returns a empty set.

# car1 = {"Honda", "Changan", "Suzuki","Cultus"}
# car1.clear()
# print(car1)




#  Beginner Level (Basics of Sets)
# Create a set containing 5 fruits and print it.

# fruit = {"Banana", "Apple", "Gauva", "Grapes", "Mango"}
# print(fruit)

# Add "banana" to a set. If it's already there, should it show twice? Explain.

# fruit = {"Banana", "Apple", "Gauva", "Grapes", "Apple"}
# print(fruit)
# sets don't accept duplicate values.

# Remove "apple" from the set using:

# fruit = {"Banana", "Apple", "Gauva", "Grapes", "Apple"}
# fruit.remove("Apple")
# print(fruit)
# # discard()
# fruit = {"Banana", "Apple", "Gauva", "Grapes", "Apple"}
# fruit.discard("Grapes")
# print(fruit)


# Create a set from this list:
# ["a", "b", "a", "c", "d", "b"]
# How many unique values are in the set?

# lst = ["a", "b", "a", "c", "d", "b"]
# unique = set(lst)
# print("The unique is",unique)
# print("Total Unique Values",len(unique))


# ⚡️ Intermediate Level (Set Operations)
# Given two sets:

# Union of A and B

# one = {1, 2, 3, 4, 5}
# two = {4, 5, 6, 7}
# three = one.union(two)
# print(three)

# Intersection of A and B

# one = {1, 2, 3, 4, 5}
# two = {4, 5, 6, 7}
# print(one.intersection_update(two))
# print(one)

# Difference (A - B)

# one = {1, 2, 3, 4, 5}
# two = {4, 5, 6, 7}
# three = one.difference(two)
# print(three)

# Symmetric Difference

# one = {1, 2, 3, 4, 5}
# two = {4, 5, 6, 7}
# three = one.symmetric_difference(two)
# print(three)

# Check if set A is a subset of B.

# one = {1, 2, 3, 4, 5}
# two = {4, 5, 6, 7}
# three = one.issubset(two)
# print(three)  #False

# Check if two sets have no common elements using isdisjoint().

# one = {1, 2, 3, 4, 5}
# two = {6, 7}
# three = one.isdisjoint(two)
# print(three) #True

# 🧠 Logic Building (Problem Solving)

# Take 5 unique numbers from the user and store them in a set.
# Then let the user enter another number.
# Tell if it was already in the set or not.

my_set = set()
print("Enter 5 Unique Numbers: ")
while len(my_set) < 5:
    num = int(input(f"\nEnter Number {len(my_set) + 1}: "))
    my_set.add(num)
print("Numbers = ",my_set, end=" ")
new = int(input("\nEnter another number: "))
if new in my_set:
        
 print("The Number is Already in set")
else:
  print("This is Not Present in set")


# Find out which languages are common in both.
# programming = {"Python", "Java", "C++"}
# web = {"HTML", "CSS", "JavaScript", "Python"}
# find = programming.intersection(web)
# print(find)

# You are building a voting system. Store names of people who voted in a set to avoid duplicates. Let the user input names in a loop, and stop when they enter "stop". Finally, print how many unique people voted.

# user = set()
# names = []
# while True:
#     name = input("Enter the Names: ")
#     if name.lower() == "stop":
#         print("Voting Ends")
#         break  
#     else:
#         names.append(name)
#         user.add(name)

# print("The Names You Entered",names)
# print(f"\nTotal unique voters: {len(user)}")
# print(f"Voters: {user}")

           
              




# 🧪 Bonus (Real-world Practice)
# Remove all duplicate values from a list using set.
# lst = [1,2,3,4,5,5,4,6,2,1]
# new_list = list(set(lst))
# print(new_list)


# Find all the vowels used in a given sentence.
# word = input("Enter a String: ")
# vowels = "aeiouAEIOU"
# find = set()
# for c in word:
#     if c in vowels:
#        find.add(c)
# if find:
#     print("The Vowels Found In Word",find,end=" ") 
# else:
#     print("The Word Dosen't Contain Any Vowels")      


# Check whether a string contains all unique characters using a set.

# user = input("Enter a String: ")
# char = set(user) 
# if len(char) == len(user):
#     print("All Characters Are Unique")
# else:
#     print("Some Characters are Duplicate")

