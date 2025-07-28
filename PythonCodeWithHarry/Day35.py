#  For loop with else.

name = ["Ali", "Usman", "Khan", "Huzaifa"]
for n in name:
    if n == "Huzaifa":
        print("Huzaifa is in the List")
        break
else:
    print("Huzaifa is not in the List")


for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print("Loop Finished") 

# Write a program that checks whether the word "Python" exists in the list below. If found, print "Found!", otherwise "Not Found" using for...else.



languages = ['Java', 'C++', 'Ruby', 'JavaScript']
for lang in languages:
    if lang == "C++":
        print("Found")
        break
else:
    print("Not Found & Now In the Else Block")       


    