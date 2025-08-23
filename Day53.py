# map, filter and reduce.

# MAP.
def cube(x):
    return x*x*x
print(cube(2))

# THIS IS USING LOOP
lst = [2,4,6,8,5,3]
new = []
for i in lst:
    new.append(cube(i))
print("Using for Loop", new)

# THIS IS USING MAP()
new = list(map(cube,lst))
print("Using Map passing a cube function ", new)


# NOW SAME USING LAMBDA()

new = list(map(lambda x: x*x*x , lst))
print("Using lambda function ", new)



# FILTER.

num = [1,2,3,5,6,8,7,9,10]
def myfun(a):
    return a<3

num2 = list(filter(myfun,num))
print("using filter function ", num2)


num2 = list(filter(lambda a: a>3 , num))
print("using filter function with lambda function ", num2)


# REDUCE.
import functools

numbers = [1,2,3,4,5]
def func(x,y):
    return x + y

total = functools.reduce(func,numbers) 
print("Using reduce ", total)

total = functools.reduce(lambda x,y: x + y,numbers) 
print("Using reduce with lambda function ", total)



# 1. Map
# Write a program using map that takes a list of numbers:
# [1, 2, 3, 4, 5]
# and returns a list where each number is squared.

num = [1, 2, 3, 4, 5]
sqnums = list(map(lambda n: n*n , num))
print("Squared Nums ", sqnums)

# 🔹 2. Filter
# Given a list of numbers:
# [10, 15, 20, 25, 30, 35, 40]
# use filter to return only the numbers that are divisible by 5 but not by 10.

number = [10, 15, 20, 25, 30, 35, 40]
def divi(number):
        return number % 5 == 0 and number % 10 != 0
          
newlist = list(filter(divi , number))        
print("Numbers That are divisible by 5 ", newlist)


# 🔹 3. Reduce
# Use reduce to calculate the product (multiplication result) of all numbers in:
# [2, 3, 4, 5]
# (Expected answer: 120)

import functools

numbers = [2,3,4,5]

total = functools.reduce(lambda x,y: x * y,numbers) 
print("Using reduce with lambda function ", total)


# 🔹 4. Map + Filter
# Given a list of words:
# ["apple", "banana", "pear", "kiwi", "grapes"]
# First, use filter to select words with length > 4.
# Then, use map to convert them to uppercase.

lst = ["apple", "banana", "pear", "kiwi", "grapes"]
filtered = list(filter(lambda w: len(w) >4 , lst))
print("Length greater then 4 ", filtered)
up = list(map(lambda w: w.upper() , filtered))
print("UpperCase ", up)

# 🔹 5. Map + Reduce
# You have a list of prices in dollars:
# [20.5, 10.75, 5.99, 12.30]
# Use map to add a 10% tax to each price.
# Then use reduce to find the total bill amount.

prices = [20.5, 10.75, 5.99, 12.30]
tax = list(map(lambda price: round(price * 1.10 , 1),prices))
print("Prices with tax using MAP ", tax)

billAmount = functools.reduce(lambda a , b: round(a + b,1), tax)
print("Total Amount After Taxes " , billAmount)