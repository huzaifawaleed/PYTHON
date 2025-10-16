# Opps Classes and Objects.

class details:
    name = "Huzaifa Waleed"
    status = "student BS/AC"
    age = 20
    def me(self):
        print(f"My name is {self.name}. My Status is {self.status}. My age is {self.age}")


a = details()
b = details()

b.name = "Daniyal"
b.status = "student BS/SE"
b.age = 19

a.me()
b.me()
# print(a.name )