# Constructor in OOPS.

class student:
    def __init__(self, name, roll_no, marks):
          self.name = name
          self.roll_no = roll_no
          self.marks = marks

    def stu_info(self):
     print(f"Student Name is {self.name} | Roll No is {self.roll_no} | Marks is {self.marks}")

s1 = student("Huzaifa", 125, 100)
s2 = student("Ali", 127, 90)

s1.stu_info()    
s2.stu_info()    