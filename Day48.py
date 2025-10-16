# Loacl vs Global Variables.

# b = 10 # this is a global variable

# def myfunc():
#        a = 20  # this is a local variable
#        print(b) 

# myfunc() 
# print(a)


b = 10 # this is a global variable

def myfunc():
       global b
       b = 30
       a = 20  # this is a local variable
       print(a) 

myfunc() 
print(b)
