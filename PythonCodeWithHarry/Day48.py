# Loacl vs Global Variables.

b = 10 # this is a global variable

def myfunc():
       a = 20  # this is a local variable
       print(b) 

myfunc() 
# print(a)
