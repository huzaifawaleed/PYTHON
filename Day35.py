#  For loop with else.

name = ["Ali", "Usman", "Khan", "Huzaifa"]
for n in name:
    if n == "Huzaifa":
        print("Huzaifa is in the List")
        break
else:
    print("Huzaifa is not in the List")


for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print("Loop Finished") 

# Write a program that checks whether the word "Python" exists in the list below. If found, print "Found!", otherwise "Not Found" using for...else.



languages = ['Java', 'C++', 'Ruby', 'JavaScript']
for lang in languages:
    if lang == "C++":
        print("Found")
        break
else:
    print("Not Found & Now In the Else Block")       


#Take a number input from the user and check if it is prime or not prime using for...else.

# num = int(input("Enter a Number: "))
# for n in range(2,num):
#     if num % n == 0:
#         print(f"{num} not a prime number")
#         break
# else:
#     print(f"{num} prime number")    


# Given a list of numbers, use for...else to find if there’s any even number in it. If found, print it and stop. If not, print "No even numbers found".

numbers = [11, 13, 14, 15, 17]

for i in numbers:
    if i % 2 == 0:
        print("Even Number Found",i)
        break
else:
   print("There are not a even number in list")


# You have 3 chances to guess a correct password. If the user guesses "admin123" correctly, print "Access Granted" and stop. If not guessed in 3 tries, use else to print "Account Locked".   


password = "admin123"
p = 1
while p<4:
    user = input("Enter a Password  (Attempts "+ str(p) +" of 3): ")
    if user == password:
        print("Access")
        break
    else:
        print("Wrong Password")
        p += 1
else:
    print("Account Locked")