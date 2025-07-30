# Finally Keyword Exception Handling.



# Write a program that takes two numbers from the user and divides them. Handle the following exceptions:
# ValueError if the input is not a number
# ZeroDivisionError if the second number is zero
# Use finally to print "Process complete" every time


# try:
#     num1 = int(input("Enter Number 1: "))
#     num2 = int(input("Enter Number 2: "))
#     res = num1 / num2

# except ValueError:
#     print("Entered input is not a number")
# except ZeroDivisionError:
#    print("Zero is Not Allowed")
# else:
#     print("The Result is = ",res)
# finally:
#     print("This Block Always Run")
   

# Create a custom function to check if the user is 18+. If not, raise a ValueError with the message "Age must be 18 or above". Handle the exception with try-except.

def myfunc():
    try:
     age = int(input("Enter Your Age:"))
     if age < 18:
         raise ValueError("Age must be 18 or above")
     print("Age is 18+")
    except ValueError as e:
        print("Error:", e)

myfunc()       

# def myfunc():
#     try:
#         age = int(input("Enter Your Age: "))
#         if age < 18:
#             raise ValueError("Age must be 18 or above")
#         print("Age is 18+ ✅ Access Granted")
#     except ValueError as e:
#         print("Error:", e)

# myfunc()