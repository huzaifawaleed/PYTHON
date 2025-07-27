# Dictionary Methods.

student = {
     "Ali": {"age": 21, "course": "Python"},
    "Sara": {"age": 22, "course": "Java"},
    "Usman": {}
}

# Try to set "age" if it doesn't exist
student.setdefault("age", 21)

# Try to set "course" again (won't overwrite it)
student.setdefault("course", "Java")

print(student)


# Keys().
# is used to vew all keys in dictionary.

# Values().
# is used to vew all values in dictionary.

# Clear().
# is used to clear the dictionary. | students.clear()  


# update().
# is used to add the value to the dictionary. | new_student = {"Zoya": {"age": 23, "course": "JavaScript"}}
# students.update(new_student)

# pop(key).
# is used to remove the value from dictionary. | students.pop("Usman")

# del is a keyword.
# is used to del the value from the dictionary.

# setdefault().
# is used set the default value | students.setdefault("Hassan", {"age": 0, "course": "Not Assigned"})
