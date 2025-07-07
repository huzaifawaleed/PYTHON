# User Input.
# Basic Syntax

# a = input("What is your Name: ")    # By default it is STRING.
# print("My Name is",a)


# Now here i am input a number but by default it is STRING so it concatenating the numbers.
# b = input("Enter first number: ")    
# c = input("Enter second number: ")
# print(b + c)

# Now i have define the data type.
# b = input("Enter first number: ")    
# c = input("Enter second number: ")
# print(int(b) + int(c))     # This is define the data type while printing.

# b = int(input("Enter first number: "))    # This is define the data type while taking input.
# c = int(input("Enter second number: "))
# print(b + c)

a = int(input("Enter a Number: "))
op = str(input("operator: "))
b = int(input("Enter a Number: "))
res = a, op, b
print("the sum is:",res)

