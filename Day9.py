# TYPE CASTING

# Explicit Type Cating
# By this 'a' and 'b' is considered as as a string the output will be 14. 
a = "1"
b = "4"
print(a + b)

# But to convert the same into number we can add their DATA TYPE in the print line then the output will be 5.
a = "1"
b = "4"
print(int(a)+int(b))

# Similarly number to string
a = 1
b = 4
a = str(a)
b = str(b) 
# print(type(a))
print(a + b)

a = "10"
print(type(a))

c = "15"
d = 7
c = int(c) #throws an error if the string is not a valid integer
sum= c + d
print("The Sum of both the numbers is: ", sum)

# Implicit Type Cating
# Data types in python have not same level some is higher some is lower in implicit if the one variable of different data type then python automatically converts into higher level

a = 7.6
b = 10
b += 2
print(a+b)