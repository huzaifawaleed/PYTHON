# Raising Custom Error.

# a = int(input("Enter a Number b/w 5 and 9: "))
# if a<5 or a>9:
#     raise ValueError("Value should be between 5 and 9")
# print(a)

# try:
#  sal = int(input("Enter salary: "))
#  if not 2000 < sal < 5000:
#     raise ValueError("Invalid salary amount")
#  print(sal)
# except ValueError as err:
#  print(err)


# Quick Quiz.
try:
 val = input("Enter Number b/w 5 and 10: ")
 if val == "quit":
    print("Program Quit")
 else:
   a = int(val) 
   if a < 5 or a > 10:    
     raise ValueError("Number Must be b/w 5 and 10")
   print(a)
except ValueError as e:
  print(e)


