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


