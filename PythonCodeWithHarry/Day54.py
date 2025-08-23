# is and == in python.

# Lists are mutable the value can be change. 
a = [1,2,3]
b = [1,2,3]
print(a is b)  # FALSE
print(a == b)  # TRUE

# strings and integers are immutable the value cannot be change.
c = 12
d = 12
print(c is d) # TRUE
print(c == d) # TRUE

e = "Huzaifa"
f = "Huzaifa"
print(e is f) # TRUE
print(e == f) # TRUE