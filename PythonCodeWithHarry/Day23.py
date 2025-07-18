# LIST METHOD.

# append(x)	Adds an element x to the end of the list.
# insert(i, x)	Inserts element x at index i.
# extend(iterable)	Adds all elements from another iterable (like another list).
# remove(x)	Removes the first occurrence of value x.
# pop([i])	Removes and returns the element at index i. If i is not provided, removes last item.
# clear()	Removes all elements from the list.
# index(x)	Returns the index of the first occurrence of value x.
# count(x)	Counts how many times x appears in the list.
# sort()	Sorts the list in ascending order (modifies the original list).
# reverse()	Reverses the list in place.
# copy()	Returns a shallow copy of the list.


lst = ["zafi", 1,2,3,2,43]
# lst2 = ["Huzaifa", "Waleed"]
# lst.append("Huzaifa")
# lst.insert(0, 10)
# lst.extend(lst2)
# lst.remove(2)
# lst.pop(0)
# lst.clear()
lst2 = lst.copy()
lst2[0] = 20
print(lst)
print(lst2)