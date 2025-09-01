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



class BankAccount:
    def __init__(self, acc_no, balance=0):
          self.acc_no = acc_no
          self.balance = balance
       

    def depo(self,amount):
        self.balance += amount
        print(f"You Deposit {amount}. New Balance is {self.balance}")

    def widthraw(self,amount):
       if amount <= self.balance:
        self.balance -= amount
        print(f"You Widthraw {amount}. Remaining Balance is {self.balance}")
       else:
           print("Insufficient Balance")
            

acc1 = BankAccount(100321, 5000)
acc2 = BankAccount(321890, 10000)
# print(acc2.balance)
acc1.depo(1000)
acc1.widthraw(2000)




class Calculator:
    def add(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b
    
    def mul(self, a, b):
        return a * b
    
    def div(self, a, b):
        return a / b
    

cal = Calculator()
print("Addition", cal.add(8 , 9))    
print("Subtraction", cal.sub(10 , 5))    
print("Multiplication", cal.mul(15 , 5))    
print("Division", cal.div(10 , 2))   


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def is_long_book(self):
        return self.pages > 300

# Example usage
book1 = Book("Python Basics", "John Doe", 250)
book2 = Book("Advanced Programming", "Jane Smith", 450)

print(book1.title, "is long?", book1.is_long_book())
print(book2.title, "is long?", book2.is_long_book())
