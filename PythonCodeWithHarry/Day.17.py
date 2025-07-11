# FOR LOOPS.


# Write a for loop to print numbers from 1 to 10, each on a new line.

# numbers = "huzaifa"
# for n in numbers:
#     print(n)
#     if n == "z":
#         print("this is Z")



# for n in range(1,11): #This prints from 1 to 10
#     print(n)
     
# for i in range(10,0,-1):    #This will print 1 to 10 reverse because -1 is use for reversinsin here in RANGE function we have allowed 3 arguments START , END , STEP.
#     print(i)      


# for i in range(1,10,2):  #This will print ODD numbers like STARTS 1 END 10 ADD 2 every time
#     print(i) 


# for i in range(2, 10, 2):   #This will print EVEN numbers like STARTS 2 END 10 ADD 2 every time
#     print(i) 



# Take a number n from the user and use a for loop to calculate the sum from 1 to n.

# num = int(input("Enter a Number: "))
# sum = 0
# for n in range(1,num + 1):
#     sum = sum + n
#     print(sum)


# Ask the user for a number and print its multiplication table up to 10 using a for loop.
# Example: Input 5 → 5 x 1 = 5, ..., 5 x 10 = 50

# number = int(input("Enter a number to print table: "))

# for i in range(1, 11):
#    print(" ",number," x ",i," ",number * i)



# Use a for loop to print all even numbers between 1 and 50.


# for i in range(2,50,2):
#     print(i)





# Take a number from the user and print numbers in reverse from that number down to 1.
# Example: Input 5 → 5 4 3 2 1

# for i in range(5, 0, -1):
#     print(i)



# Take a word from the user and use a for loop to count how many vowels (a, e, i, o, u) are in it.



word = input("Enter a word to check Vowels in it: ")
vowels = "aeiouAEIOU"
count = 0
for c in word:
    if c in vowels:
        count += 1
        print("Vowels is",c)
          
print("You Entered",word)

# for c in word:
#     if c in vowels:
#         print("Vowel found:", c)
#         count += 1