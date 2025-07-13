# FUNCTIONS.

def add(a,b):
 print("The Sum of two number is =", a + b)
def sub(a,b):
   print("The subtraction of two number is =", a - b)
def mul(a,b):
   print("The Multiplication of two number is =", a * b) 
def div(a,b):
   print("The Division of two number is =", a / b) 

while True:
     print("1: ADD")  
     print("2: SUB")  
     print("3: MUL")   
     print("4: DIV")
     print("5: EXIT")  
     choose = int(input("Select The Calculation: "))
     if choose == 5:
         break
     a = int(input("Enter Number 1: "))
     b = int(input("Enter Number 2: "))
     match choose:
          case 1:
           add(a,b)
               
          case 2:
            sub(a,b)
          case 3:
            mul(a,b)
          case 4:
           div(a,b)
          case _:
           print("Invalid Selection")  





