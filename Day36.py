# Exception Handling.

try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
    
except IndexError:
  print("Index Error")


# try:
#     num = int(input("Enter an integer: "))
# except ValueError:
#     print("Number entered is not an integer.")


# try:
#     num = int(input("Enter a Number: "))
#     res = 10 / num
# except ZeroDivisionError:
#     print("Do not Divide by Zero")
# except ValueError:
#     print("Invalid Error")
# else:
#     print("The Result is = ",res)
# finally:
#         print("Execution complete.")
