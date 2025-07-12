# BREAK & CONTINUE.


#BREAK.
# for i in range(1,20 + 1):
#     print(i)
#     if i == 10:
#         break
# print("I am outside the loop now!")



# CONTINUE.

# for i in range(1, 10 + 1):
#       if i == 5:
#         continue
#       print(i)
     


#QUESTIONS.

# Write a loop where the user must guess a secret number between 1 and 10.
# Use break to exit the loop when the guess is correct.

# for n in range(1, 10 + 1):
#  n = int(input("Enter a Number until the secret appears: "))
#  if n == 3:
#     break
# print(n, "This is the secret number yay!")
  







# Print 1 to 10, But Stop at 5
# Use a loop to print numbers from 1 to 10.
# When the number reaches 5, use break to stop the loop.

# for i in range(1,11):
#     n = int(input("Enter the number to stop the bus(1 to 10)"))
#     print(i)
#     if n == 5:
#         break
# print("Bus Stops At 5 =",5)


# Skip Odd Numbers (Use continue)
# Print even numbers from 1 to 10.
# Use continue to skip odd numbers.

# for i in range(1,11):
#     if i % 2 != 0:
#         continue
#     print("Even",i)


# Print 1 to 10 but Skip 4 and 7
# Use continue to skip 4 and 7, print all others.

# for i in range(1,11):
#     if i == 4 or i == 7: # Here we use OR intead AND bcz it checks conditions one by one not both at the same time.
#         continue
#     print(i)


# ✅ Intermediate Level
# Ask for Input Until 'q' is Entered
# Keep asking the user to enter a number.
# Use break to exit when the user types 'q'.

# while True:
#    c = input("Enter (a to z) to check where is the break: ")
#    if c == 'q': 
#     break
# print("The loop breaks here at",c)


# Print Multiples of 3 from 1 to 30, Skip 15
# Use continue to skip 15, print all other multiples of 3.

# for i in range(1, 11):
#   product = 3 * i
#   if product == 15:
#    continue
#   print("3 x ",i,"", product)




# Loop from 1 to 1001, Break if Number is Divisible by 17 and 19
# Find the first number divisible by both 17 and 19, then break.

# i = 1
# while i <= 1001:
#     if i % 17 == 0 and i % 19 == 0:
#         break
#     i += 1
# print("The divisible of 17 and 19 is = ",i)    


# Password Validation
# Ask user to enter a password.
# Use a loop that gives 3 chances only.
# Use break when the correct password is entered.

# pas = 'huzaifa'
# for i in range(1,4):
#     pin = input("Enter your password (Attempts "+ str(i) +" of 3)"  )
#     if pin == pas:
#         print("Login")  
#         break
#     else:
#      print("incorrect pass")

# else: 
#    print("Too many attempts")








# ✅ Challenge Level
# Print All Numbers 1 to 50 But Skip Multiples of 3 and 5
# Use continue to skip those values.


# for i in range(1, 51):
     
#      if i % 3 == 0 or i % 5 == 0:
#          continue
#      print(i)




# Loop through a list of numbers, Stop at First Negative
# Use break when a negative number is found.


lst = [10, 12, -2, 19, 20]

for n in lst:
    if n < 0:
        print("Negative = ",n)
        break
    else:
        print("Positive = ",n)




