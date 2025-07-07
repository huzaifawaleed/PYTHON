# Solving Questions.


# Take a name as input from the user and print a greeting message like:
# Hello, [name]!

name = input("Enter your name: ")
print("Hello!",name)



# Input two numbers from the user and print their sum, difference, product, and quotient.

num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))

print("The sum of ",num1," and ",num2," is:",num1 + num2)
print("The difference of ",num1," and ",num2," is:",num1 - num2)
print("The product of ",num1," and ",num2," is:",num1 * num2)
print("The quotient of ",num1," and ",num2," is:",num1 / num2)



# Ask the user to enter their age and print whether they are eligible to vote (age ≥ 18).

age = int(input("Enter Your To Check Vote Eligibilty: "))

if age >= 18:
    print("You are eligible to vote")
elif age < 18:
    print("You are not eligible to vote")
else:
    print("Invalid")


# Take a user's birth year and calculate their current age.

birthYear = int(input("Enter your birth year to calculate your age: "))
currentYear = 2025
age = currentYear - birthYear
print("Your Age is",age)


# Ask the user to input a word and print its length using len().

word = input("Enter a word to count it's character: ")
print(len(word))


# Ask the user for a sentence and print it in reverse order.

word = input("Enter a word to Reverse it: ")
reversed_word = word [::-1]     #Slice method
print(reversed_word)


# Take a single character input and print its ASCII value using ord().

word = input("Enter a character to find ASCII value: ")
print(ord(word))

# Input three numbers from the user and print the largest one.

n1 = int(input("Enter Number 1: "))
n2 = int(input("Enter Number 2: "))
n3 = int(input("Enter Number 3: "))

if n1 > n2 and n1 > n3:
    print(" ",n1,"is greater then ",n2," and ",n3," = ",n1)
elif n2 > n1 and n2 > n3:
    print(" ",n2,"is greater then ",n1," and ",n3," = ",n2)
elif n3 > n1 and n3 > n2:
    print(" ",n3,"is greater then ",n1," and ",n2," = ",n3)
else:
    print("Please Enter a Number")



# Write a program that asks the user for a password and checks if it matches a pre-defined password.

pas = "huzaifa123"
passs = input("Enter a Existing Password: ")
if pas == passs:
    print("Your Password Matched")
else: 
    print("Your Password is Not Matched")




# Take a string input and check whether it is a palindrome (same forwards and backwards).

st = input("Enter a word to check it is Palindrome: ")
if st == st[::-1]:
    print("The word is Palindrome") 
else:
    print("The word is not Palindrome")



# Ask the user for their full name, then display it in title case (e.g., john doe → John Doe).

name = input("Enter Your Full Name: ")

print("The Name With Title Case is ", name.title())


# Take a sentence and count how many vowels it contains.

word = input("Enter words to check vowels in it: ")

vowels = "aeiouAEIOU"

count = 0

for c in word:
    if c in vowels:
        count += 1
        print("The vowels in word are =",count)
