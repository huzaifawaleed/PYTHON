# FUNCTIONS.

# def add(a,b):
#  print("The Sum of two number is =", a + b)
# def sub(a,b):
#    print("The subtraction of two number is =", a - b)
# def mul(a,b):
#    print("The Multiplication of two number is =", a * b) 
# def div(a,b):
#    print("The Division of two number is =", a / b) 

# while True:
#      print("1: ADD")  
#      print("2: SUB")  
#      print("3: MUL")   
#      print("4: DIV")
#      print("5: EXIT")  
#      choose = int(input("Select The Calculation: "))
#      if choose == 5:
#          break
#      a = int(input("Enter Number 1: "))
#      b = int(input("Enter Number 2: "))
#      match choose:
#           case 1:
#            add(a,b)
               
#           case 2:
#             sub(a,b)
#           case 3:
#             mul(a,b)
#           case 4:
#            div(a,b)
#           case _:
#            print("Invalid Selection")  


# Create a function that checks if a number is even or odd.

# def check():
#     num = int(input("Enter a Number to Check EVEN or ODD: "))
#     if num % 2 == 0:
#         print("Even",num)
#     else:
#         print("Odd",num)

# check()

#Using RETURN METHOD.
# def check(num):
#     if num % 2 == 0:
#         return f"{num} is EVEN"
#     else:
#         return f"{num} is ODD"

# n = int(input("Enter a Number to Check EVEN or ODD: "))
# res = check(n)
# print(res)



# Input a list and make two even or odd and print.

# def lst(num):
#     e_lst = []
#     o_lst = []

#     for n in num:
#         if n % 2 == 0:
#             e_lst.append(n)
#         else:
#             o_lst.append(n)

#     print("Even List =", e_lst)
#     print("Odd List =", o_lst)


# num = list(map(int, input("Enter a LIST of Numbers: ").split()))
# lst(num)




# Make a function to find the square of a number.

# def sqr(num):
#    return num * num
# num = int(input("Enter a number to find square: "))
# sq = sqr(num)
# print("The of ",num," is = ",sq)


# Write a function that takes a name and prints a personal greeting.

# def greet(name):
#     print("Hello ",name,"! Welcome ")
# name = input("Enter Name: ")
# greet(name)
   



# Write two functions: one to return the square, and one to return the cube of a number.


# num = int(input("Enter a number to find square and cube: "))


# def sqr(num):
#    return num * num

# def cube(num):
#    return num * num * num

# sq = sqr(num)
# cb = cube(num)

# print("The square of ",num," is = ",sq)
# print("The cube of ",num," is = ",cb)


# Write a function that returns the factorial of a number.

# def fact(num):
#    res = 1
#    for i in range(1,num + 1):
#       res *= i
#    return res
# num = int(input("Enter a number to FACTORIAL: "))
# factorial = fact(num)
# print("The factorial of ",num," is = ", factorial)



# Write a function that takes a list and returns the total sum.

# def c_sum(lst):
#     total = 0
    
#     for l in lst:
#         total += l
#     return total
# lst = list(map(int, input("Enter a list of numbers to add: ").split()))
# res = c_sum(lst)
# print("The total sum of list is = ",res)



# Write a function that returns the largest number from a list.


# def c_sum(lst):
#     max_val = lst[0]
    
#     for l in lst:
#         if l > max_val:
#          max_val = l
#     return max_val
# lst = list(map(int, input("Enter a list of number to find larger: ").split()))
# res = c_sum(lst)
# print("The larger number is  = ",res)



# A function that checks if a given string or number reads the same backward.

# def p_checker(word):
#     word = str(word)
#     if word == word[::-1]:
#         print("The word is Palindrome")
#     else:
#         print("The word is not Palindrome")
# word = input("Enter a word/number to check it is palindrome or not: ")
# p_checker(word)


# A function that checks if a number is prime or not.

# def is_prime(num, i = 2):
#     if num <= 1:
#         print(num, "Not prime")
#     elif i == num:
#         print(num, "Prime")    
#     elif num % i == 0:
#         print("Not prime") 
#     else:
#         is_prime(num, (i+1))     
# num = int(input("Enter a number to check if it is prime: "))
# is_prime(num)        




# A function that prints the multiplication table of a number up to 10 or 20.

# def table():
#     for i in range(10, 20 +1):
#         print("5 x ",i," " ,5*i)
# table()


# A function that takes a word and returns the number of vowels.

# def v_count(word):
#     vowels ="aeiouAEIOU"
#     count = 0
#     for c in word:
#         if c in vowels:
#          count += 1
#     return count

# word = input("Enter a word to count how many vowels in it: ")
# vow = v_count(word)
# print("total voewls is",vow)





# Write a function to reverse a list or a string.

# def reverse_word():
#     word = input("Enter a word to reverse it: ")
#     r_word = word[::-1]
#     print(r_word)
# reverse_word()    


# def reverse_list():
#       lst = input("Enter a list to reverse it: ")
#       r_list = lst.split()
#       r_list = lst[::-1]
#       print(r_list)
# reverse_list() 






# Average of Numbers in a List

# def avg_list(lst):
#     total = 0
#     for n in lst:
#         total += n
#         avg = total / len(lst)
#     return avg   


# lst = list(map(int,input("Enter a list get its avg: ").split())) 
# print("The Average of the lsit is ",avg_list(lst))


# Find All Even or Odd Numbers in a List

def evenodd_list(lst):
    odd = []
    even = []
    for n in lst:
        if n % 2 == 0:
           even.append(n)
        else:
             odd.append(n) 
    return even , odd      


lst = list(map(int,input("Enter a list to get even or odd: ").split())) 
even , odd = evenodd_list(lst)
print("The Even List = ",even)
print("The Even List = ",odd)



# Separate Positive and Negative Numbers

# Check if a List is Sorted

# Return a List with Only Unique Elements

