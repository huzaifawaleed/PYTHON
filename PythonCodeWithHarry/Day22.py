# LIST.


# lst1 = ["Huzaifa", "Waleed", "Karachi", "Iqra University"]
# lst2 = ["Web Dev", "Computer Science"]

# if "Huzaifa" in lst1:
#     print("Huzaifa is present")
# else:
#     print("Huzaifa is not present")

# lst1.append("Inaam")
# lst1.insert(0,900)  # This will change the index you want to change.
# lst1.extend(["inaam", 2000]) # This will add multiple values at once.
# print(lst1)
# print(lst1[-1])
# print(lst1[2])
# print(lst2)


# myDetails = ["Huzaifa Waleed", 20, "huzaifainaam@gmail.com", 5.4]
# print(type(myDetails[3]))









# Create a list of 5 numbers from the user and print the sum.


# lst = []
# lst = list(map(int,input("Enter list of 5 number: ").split()))

# if len(lst) == 5:
#     print(sum(lst))
# else:
#     print("Please enter only 5 numbers")





# Write a function that takes a list and prints all even numbers.

# def lsts(lst):
#     even = []
#     for n in lst:
#         if n % 2 == 0: 
#             even.append(n)
#     return even
       
# lst = list(map(int,input("Enter list of to find even numbers only: ").split()))
# print("All Even Numbers = ",lsts(lst))



# Count how many positive, negative, and zero values are in a list.

# def count_lst(nums):
#     count_zero = []
#     count_neg = []
#     count_pos = []
#     for n in nums:
#         if n > 0:
#             count_pos.append(n)
#         elif n < 0:
#              count_neg.append(n)
#         elif n == 0:
#             count_zero.append(n)  
#         else:
#             print("Enter a number")      
#     print("The Negative in a List = ",count_neg)
#     print("The Positive in a List = ",count_pos)
#     print("The Zeros in a List = ",count_zero)

# nums = list(map(int,input("Enter Numbers to count: ").split()))
# count_lst(nums)




# Find the maximum and minimum numbers in a list manually (without max() or min()).

# nums = list(map(int,input("Enter Numbers to Check Maximum & Minimum: ").split()))
# maximum = nums[0]
# minimum = nums[0]
# for i in nums:
#     if i > maximum:
#         maximum = i
#     if i < minimum:
#         minimum = i  
# print("The Maximum numbers ",maximum)  
# print("The Minimum numbers ",minimum)





# 🧠 Intermediate List Logic Questions
# Remove all duplicates from a list while keeping the order.

# unique = []
# nums = list(map(int,input("Enter Numbers to Check Unique: ").split()))
# for i in nums:
#     if i not in unique:
#         unique.append(i)
# print("These all are unique = ",unique)        



# 7️⃣ Write a function to sort a list without using sort() (hint: bubble sort or selection sort logic).

# Check if a list is sorted in ascending order.

# nums = list(map(int,input("Enter Numbers to Check List is sorted in Ascending order: ").split()))
# if nums == sorted(nums):
#     print("List is Sorted", nums)
# else:
#     print("List is not Sorted", nums)

# Enter a random number in a list and get sorted list.
# nums = list(map(int,input("Enter Numbers to Check List is sorted in Ascending order: ").split()))
# number = sorted(nums)
# print("Sorted List",number)



# Write a function to merge two user-given lists and remove duplicates.

# def merge_lists(lst1,lst2):
#     new_list = lst1 + lst2
#     unique = []
#     for i in new_list:
#         if i not in unique:
#             unique.append(i)

#     return unique

# lst1 = list(map(int,input("Enter list 1: ").split()))
# lst2 = list(map(int,input("Enter list 2: ").split()))
# new_list = merge_lists(lst1,lst2)
# print("Merged List Without Duplicates",new_list)







# Split a list into two lists — one with even numbers and one with odd numbers.

# lst = list(map(int,input("Enter a list to separate Even & Odd: ").split()))
# even = []
# odd = []
# for i in lst:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("Even List = ",even)
# print("Even List = ",odd)        



# 🔁 Loop-Based Challenges (For + While)
# Create a list and print the square of each element.

lst = list(map(int,input("Enter a list to get Square of every element: ").split()))
sqr = []
for i in lst:
    sqr.append (i * i)
print("The square of every element is",sqr)    



# 1️⃣2️⃣ Create a list of 10 numbers and print only those divisible by both 2 and 3.

# 1️⃣3️⃣ Find the second largest element in the list.

# 1️⃣4️⃣ Find the sum of elements at even indices (0, 2, 4...).

# 1️⃣5️⃣ Write a function to rotate a list to the left by 2 positions.

# 🎯 Challenge (Higher Order Thinking)
# 1️⃣6️⃣ Take a list of strings and return a list of only those with length > 3.

# 1️⃣7️⃣ Find the frequency of each element in a list (return a dictionary).

# 1️⃣8️⃣ Remove all elements that occur more than once (keep only unique ones).

# 1️⃣9️⃣ Write a function that finds the difference between max and min of a list.

# 2️⃣0️⃣ Accept a list and return another list where each element is the sum of itself and the next element.


