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

def greet(name = "Guest"):
    print("Hello",name)
name = input("Enter Your Name (Press Enter to skip): ")  

if name:
    greet(name)
else:
    greet()
