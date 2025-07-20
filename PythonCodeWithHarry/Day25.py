# OPERATIONS ON TUPLES.


# This is how we manipulate tuple first made a tuple for adding values convert into list add values then convert back into tuple.

tup = ("Huzaifa", "Waleed", "Student")   #This is tuple.
new = list(tup)      # now converting tuple to list.
new.insert(2, "Full Time Student")    # adding values
new.pop()
new.append("Iqra University")
tup = tuple(new)             # Now again converting list to tuple
print(type(tup))
print(tup)

