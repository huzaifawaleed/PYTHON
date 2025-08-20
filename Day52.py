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






# def appl(fx, value):
#   return 6 + fx(value)
# print(appl(lambda x: x * x , 2))