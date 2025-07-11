# WHILE LOOP.


# Write a while loop to print numbers from 1 to 10.

# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1


# Take a number from the user and use a while loop to calculate the sum from 1 to that number.
# n = int(input("Enter a number: "))
# sum = 0
# i = 1
# while i <= n:
#     sum = sum + i
#     print(sum)
#     i = i + 1
   

# Ask the user for a number and print its multiplication table from 1 to 10 using a while loop.

# n = int(input("Enter a number print table: "))
# i = 1
# while i <= 10:
#     print(" ",n," x ",i," ", i * n)
#     i = i + 1




# Take a number from the user and use a while loop to count down to 1.
# Example: input 5 → output: 5 4 3 2 1


# n = int(input("Enter a number: "))
# i = n
# while n > 0:
#     print(n)
#     n = n - 1



# Take an integer from the user and use a while loop to count how many digits it has.
# Example: input 1234 → output: 4 digits


# n = int(input("Enter a number: "))
# count = 0
# while n > 0:
#     n = n // 10
#     count = count + 1

# print(count)



# Create a game where the user must guess a secret number between 1 and 10.
# Use a while loop to keep asking until they guess correctly.

# number = int(input("Enter a number 1 to 10 guess the secret number: "))

# sec_num = 7
# i = 1
# if number == sec_num:
#     print("This is the Secret Number Yes!",sec_num)
# else:
#    while i <= 10:
#        number = int(input("Enter a number 1 to 10 guess the secret number: "))
#        print(number)
#        i = i + 1 






# 7. Print All Even Numbers From 1 to 50
# Use a while loop to print all even numbers between 1 and 50.

i = 1

while i <= 50:
    if i % 2 == 0:
        print("Even Numbers",i)
    i = i + 1    