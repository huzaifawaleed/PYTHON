# lambda function.

#This is a simple function.
# def double(x):
#     return x + 10    
# print(double(10))


# This is a lambda function.

double = lambda x: x + 30
print(double(10))

avg = lambda x,y: (x + y) / 2
print(avg(10,30))

cube = lambda x: x*x*x
print(cube(10))

avger = lambda x,y,z: (x + y + z) / 3
print(avger(10,30, 40))


# Passing function as an argument.
def func(x , value):
    return 2 + x(value)
print(func(lambda x: x + 30, 2))

# Lambda function to calculate the product of two numbers,
# with additional print statement
mul = lambda x, y: print(f'{x} * {y} = {x * y}')
mul(6,5)



