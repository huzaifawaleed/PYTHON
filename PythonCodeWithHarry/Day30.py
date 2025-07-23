# Recursion.

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return (n * factorial(n - 1))
# n = int(input("Enter a Number To Get a Factorial: ")) 
# print("Number = ",n)
# print("Factorial = ",factorial(n))   


def fibonacci(num):
    if num == 0: 
          return 0
    elif num == 1:
        return 1
    else:
         return fibonacci(num -1) + fibonacci(num - 2)
num = int(input("Enter a Number: "))  
for n in range(num):    
 print(fibonacci(n), end=" ")

# num = int(input("Enter a Number: "))
# first = 0
# second = 1
# for i in range(num):
#    print(first , end=" ")

#    next = first + second
#    first = second 
#    second = next
