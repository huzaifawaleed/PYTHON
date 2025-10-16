# Inheritance.

class Firstclass:
    def __init__(self, name, id, role):
        self.name = name
        self.id = id
        self.role = role


    def detail(self):
        print(f"Name is {self.name} | Id is {self.id} | Role is {self.role}")


class Secondclass(Firstclass):
    def __init__(self, name, id, role, salary):
        self.name = name
        self.id = id
        self.role = role
        self.salary = salary



    def showdetail(self):
        print(f"Name is {self.name} | Id is {self.id} | Role is {self.role} | salary is {self.salary}")        

e1 = Firstclass("Huzaifa", 111, "Student & Frontend Developer")
e2 = Secondclass("Hamza", 222, "Student",2000)
e3 = Secondclass("Afnan", 333, "Student", 10000)
e1.detail()
e3.showdetail()
e2.showdetail()
