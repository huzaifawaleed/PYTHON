# FUNCTION ARGUMENTS.

# Write a function add(x, y) that takes two numbers from the user and prints their sum.

# def add(x,y):
#     return(x+y)
# num1 = int(input("Enter number 1: "))  
# num2 = int(input("Enter number 2: ")) 
# total = add(num1,num2)
# print("Total is = ",total)



# Create a function bio(name, city) and call it using keyword arguments with input values.

# def bio(name,city):
#     print("Your Name is ",name," and City is ",city,"")
# n = input("Enter your Name: ")
# c = input("Enter your City: ")  
# bio(n,c)      


# def add(a,b=10):
#     print(a + b)

# add(90)  



# Define a function greet(name="Guest") that prints a greeting.
# Ask the user to enter a name or leave it blank — use default if blank.

# def greet(name = "Guest"):
#     print("Hello",name)
# name = input("Enter Your Name (Press Enter to skip): ")  

# if name:
#     greet(name)
# else:
#     greet()




# Write a function profile(name="Unknown", age=0, city="N/A").
# Let the user update any of these via input.


# def profile(name="Unknown", age=0, city="N/A"):
#     print("User Profile")
#     print("Your Name is ",name)
#     print("Your Age is ",age)
#     print("Your City is ",city)

# n = input("Enter Your Name: ")
# a = input("Enter Your Age: ")
# c = input("Enter Your City: ")

# if n != "":
#      name = n
# else:
#   name = "Unknown"

# if a != "":
#     age = int(a)
# else:
#   age = 0 

# if c != "":
#     city = c
# else:
#     city = "N/A" 

# profile(name,age,city)  




# Take multiple numbers from the user and pass them to a function calculate_total(*args) to get the sum.



# def numbers(*nums):
#     print("You Entered = ",nums)
#     print("Total = ", sum(nums))

# lst = list(map(int,input("Enter a list of Numbers: ").split()))
# numbers(*lst)      



# Build a function find_max(*numbers) that takes user input (multiple numbers) and finds the largest value.

def find_max(*lst):
     max_val = lst[0]
    
     for l in lst:
         if l > max_val:
          max_val = l
     return max_val
nums = list(map(int, input("Enter a list of number to find larger: ").split()))
res = find_max(*nums)
print("The larger number is  = ",res)


