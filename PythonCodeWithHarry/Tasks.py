# Task 1: Student Grading System
# Concepts: variables, if-else, input(), string formatting

# Build a program that takes marks for 5 subjects and calculates the:

# Total marks

# Percentage

# Grade (use conditions: A, B, C, Fail)

# Print a neat report card

# ✅ Task 2: ATM Simulator
# Concepts: if-else, loops, variables
# Create a mini ATM interface:
# Login using a PIN
# Show balance, withdraw cash, deposit amount
# Use a while loop to keep the program running until user chooses exit

# print("\nWelcome To ATM")


# c_bal = 10000
# depo = 0
# his = []
# pin = 0000
# user_pin = int(input("Enter Your Pin Please: "))
# if pin == user_pin:
#     print("You Are Login Into Your Account")
    
#     while True:
#             print("1: Check Balance")
#             print("2: Deposit Money")
#             print("3: Withdraw Money")
#             print("4: Check History")
#             print("5: Exit")
#             opt = int(input("Choose Option To Do a Transaction: ")) 
#             if opt == 5:
#                  print("ThankYou For Using the ATM Have a Nice Day")
#                  break
#             match opt:
#                  case 1:  
#                       print("Your Current Balance is ",c_bal)
#                       his.append(f"Checked Balance: {c_bal}")
#                  case 2:
#                       d_amount = int(input("Enter the Amount You to Deposit: "))
#                       depo = d_amount
#                       c_bal += depo
#                       his.append(f"Deposit Amount: {d_amount}")
#                       print("Deposit Successfull! \nNow Your Balance After Deposit is ",c_bal)
#                  case 3:
#                       w_amount = int(input("Enter the Amount You Want to Withdraw: ")) 
#                       if w_amount <= c_bal:
#                            c_bal -= w_amount
#                            print("Withdraw Successfull! \nYour Balance After Withdraw is ",c_bal)
#                            his.append(f"Withdraw Amount: {w_amount}")
#                       else:
#                            print("Your Balance is Not Sufficient") 
#                  case 4:
#                       if his:
#                            for r in his:
#                                 print("Your History is",his)    
#                  case _:
#                        print("Invalid Selection")                         
# else:
#     print("Your Pin is Incorrect") 



# Design a Contact Book program in Python where users can:

# ➕ Add a new contact
# 📋 View all contacts
# 🔍 Search a contact by name
# ❌ Delete a contact
# 🚪 Exit the app

# print("Welcome To Contact Book")
# contacts = []
# while True:
#    print("1: Add New Contact")
#    print("2: View All Contacts")
#    print("3: Search Contact")
#    print("4: Remove Contact")
#    print("5: Exit")
#    opt = int(input("Choose Option : ")) 
#    if opt == 5:
#          print("ThankYou For Using The Contact Book")
#          break
#    match opt:
#        case 1:  
#            u_name =input("Enter Full Name: ")
#            u_num = input("Enter Contact Number: ")
#            u_email = input("Enter Email: ")
#            if u_name == "" or u_num == "" or u_email == "":
#                print("Fill All the Fields To Add The contact")
#            else:
#             add_c = [u_name, u_num, u_email]
#             contacts.append(add_c)
#             print("Contact Added SuccessFully")
#             print("Added Contact",add_c)
#        case 2:
#            if len(contacts) == 0:
#                print("No Contacts Available!")
#            else:
#                for idx, c in enumerate(contacts, start = 1):
#                    print(f"{idx}. Name: {c[0]} | Number: {c[1]} | Email: {c[2]}")

#        case 3:
#            search = input("Enter the Name/Number/Email To Search: ")
#            find = False
#            for con in contacts:
#                if search == con[0].lower() or search == con[1].lower() or search == con[2].lower():
#                 print(f"Contact Found:\n Name: {con[0]} | Number: {con[1]} | Email: {con[2]}")
#                 find = True
#                 break
#            if not find:
#              print("Contact Not Found!")

#        case 4:
#            delete = input("Enter the Name/Number/Email To Delete: ")
#            for conn in contacts:
#                if delete == conn[0] or delete == conn[1] or delete == conn[2]:
#                    contacts.remove(conn)
#                    print(f"Contact Found:\n Name:{conn[0]} | Number: {conn[1]} | Email: {conn[2]} \nDeleted Successfully!")
#                    break
#                else:
#                    print("Contact Not Found!")
           
#        case _:
#            print("Invalid Entry")
           

# ✅ Task 4: Movie Ticket Booking System
# Concepts: list, tuple, if-else, loops
# Simulate a simple ticket booking:
# Show list of available movies and times
# Let user select one and enter number of tickets
# Show total bill
# Bonus: Limit number of tickets per show using a list

# print("Welcome To Movie House")
# movie = [
#     ["Oppenheimer", "6:00 PM", 800, 20],
#     ["Dune 2", "9:00 PM", 1000, 15],
#     ["Kung Fu Panda 4", "3:00 PM", 600, 25]
# ]
# while True:
#  print("1: Available Movies & Booking")
#  print("2: Exit")


#  opt = input("Select Option: ")
#  if opt == "2":
#   print("ThankYou For Visting Movie House!")
#   break
#  elif opt == "1":
#    for idx, m in enumerate(movie , start=1):
#          print(f"{idx}. {m[0]} | Time: {m[1]} | Price: {m[2]} | Available Tickets: {m[3]}")

#    select = int(input("Enter the Movie Number You Want To Book: "))
#    if 1 <= select <= len(movie):
#     selected = movie[select -1]
#     print(f"You Selected {selected[0]} at {selected[1]}")
#     print(f"Price: {selected[2]} | Available Tickets: {selected[3]}")

#     booking = int(input("Enter the number of tickets you want to book: "))
#     if booking < 0:
#       print("Minimum Booking is 1 Ticket") 
#     elif booking > selected[3]:
#       print("This Amount is Not Available!")
#     else:
#       total = booking * selected[2]
#       selected[3]-= booking
#       print(f"Booking Confirmed! Total Price: {total}")
#       print(f"Enjoy Your Movie {selected[0]} at {selected[1]}")


# ✅ Task 5: Shopping Cart Console App
# Concepts: lists, loops, if-else, tuples
# Create a cart system:
# Add/remove items to/from cart
# View current cart
# Checkout (show total price)
# Store items as tuples: ("item", price)


# print("Welcome To Shopping Cart")

# cart = []
# while True:
#   print("1. Add Item")
#   print("2. View Item")
#   print("3. Remove Item")
#   print("4. Total Bill")
#   print("5. Exit")
  

#   choose = int(input("Select Option: "))
#   if choose == 5:
#      print("Thank You For Visit Shopping Cart")
#      break
#   match choose:
#        case 1:
#         item = input("Enter the Item Name You Want To Add: ")
#         price = int(input("Enter The Item Price: "))
#         cart.append((item,price))
#         print(f"Item Name: {item} | Price: {price} Added to Cart Successfully")
#        case 2:
#         if not cart:
#           print("Your Cart is Empty")
#         print("Items in a Cart.")
#         for i, (item,price) in enumerate(cart,start=1):
#           print(f"{i}. {item} & Rs.{price}")
#        case 3:
#            remove_item = int(input("Enter the Item Number To Remove From Cart: "))
#            if 1 <= remove_item <= len(cart):
#               removed_item = cart.pop(remove_item - 1)
#               print(f"{removed_item[0]} Successfully Removed From Cart")
#            else:
#               print("Enter Valid Number")
#        case 4:      
#          if not cart:
#           print("⚠️ Your cart is empty. Please add some items first.")
#          else:
#           for i, (item, price) in enumerate(cart, start=1):
#            print(f"{i}. {item} & Rs.{price}")

#          total = 0
#          buy_items = input("Enter the item numbers you want to buy (e.g. 1 2 3): ").split()

#          for n in buy_items:
#           if n.isdigit():
#             idx = int(n) - 1
#             if 0 <= idx < len(cart):
#                 item_name, item_price = cart[idx]
#                 total += item_price
#                 print(f"{item_name} & Rs.{item_price}")
#             else:
#                 print(f"⚠️ Invalid item number: {n}")

#          print(f"\n🧾 Total Bill is: Rs.{total}")
                  



# Decimal to binary
# while True:
#     print("1: Decimal To Binary")
#     print("2: Binary To Decimal")
#     print("3: Exit")
#     option = int(input("Choose Option: "))

#     match option:
#       case 1:
#           deci = int(input("Enter a Decimal Number to Convert into Binary: "))
#           binary = ""
#           num = deci
#           while num > 0:
#            rem = num % 2
#            binary = str(rem) + binary
#            num //= 2

#           print(f"The Binary of {deci} is {binary}.")
#       case 2:
#           binary = input("Enter Binary Number to Convert into Decimal: ")
#           dec = 0
#           binary = binary[::-1]
#           for b in range(len(binary)):
#              bit = int(binary[b])
#              dec += bit * (2 ** b)
#           print(f"Decimal of {binary[::-1]} is {dec}.")      
    


# Hangman Game.
# import random

# words = ["python", "java", "html", "javascript"]
# word = random.choice(words)
# dashes = ["_"] * len(word)
# chances = 5

# print("Welcome to the Game.")
# while chances > 0 and "_" in dashes:
#     print(" ".join(dashes))
#     guess = input("Guess a Letter: ").lower()
    
#     if guess in word:
#         for w in range(len(word)):
#             if word[w] == guess:
#                 dashes[w] = guess
#     else:
#         chances -= 1
#         print(f"Wrong Guess! Chances Left {chances}.")

# if "_" not in dashes:
#     print("You win! The word is", word)
# else:
#     print("Game over! The word was:", word)


# import random 
# import string
# length = int(input("Enter the Length of Password You Want to Set: "))
# chars = string.ascii_letters + string.digits + string.punctuation
# passs = "".join(random.choice(chars)for i in range(length))
# print("Your Password is", passs)



# import datetime
# def log():
#     note = input("Enter Your Note: ")
#     with open('log.txt', 'a') as f:
#         f.write(f"{datetime.datetime.now()} - {note}")
#     print("Note Saved!")

# def view():
#     with open("log.txt", 'r') as f:
#         print(f.read())  

# while True:
#     choice = input("What do you want to do? (log/view/exit): ").lower() 
#     if choice == "log":
#         log()
#     elif choice == "view":
#         view()
#     elif choice == "exit":
#         break         







# MENU = {
#     "espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 1.5},
#     "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2.5},
#     "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 3.0}
# }

# resources = {"water": 300, "milk": 200, "coffee": 100}

# def check_resources(order):
#     for item in order:
#         if item == "cost":   # skip cost key
#             continue
#         if order[item] > resources[item]:
#             print(f"Sorry not enough {item}.")
#             return False
#     return True


# def process_coins():
#     print("Please insert coins.")
#     total = int(input("Quarters: ")) * 0.25
#     total += int(input("Dimes: ")) * 0.10
#     total += int(input("Nickels: ")) * 0.05
#     total += int(input("Pennies: ")) * 0.01
#     return total

# while True:
#     choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
#     if choice == "off":
#         break
#     if choice in MENU:
#         drink = MENU[choice]
#         if check_resources(drink):
#             money = process_coins()
#             if money >= drink["cost"]:
#                 change = round(money - drink["cost"], 2)
#                 print(f"Here is your {choice}. Change: ${change}")
#                 for item in drink:
#                     if item != "cost":
#                         resources[item] -= drink[item]
#             else:
#                 print("Sorry not enough money.")
#     else:
#         print("Invalid choice.")



# user = set()
# names = []
# while True:
#     name = input("Enter the Names: ")
#     if name.lower() == "stop":
#         print("Voting Ends")
#         break  
#     else:
#         names.append(name)
#         user.add(name)

# print("The Names You Entered",names)
# print(f"\nTotal unique voters: {len(user)}")
# print(f"Voters: {user}")



# print("-----Voting System-----")
# candidates = ["Imran Khan", "Nawaz Sharif", "Zardari"]
# votes = [0, 0, 0]
# registration = []
# print("\n-----Register YourSelf-----")
# voters = int(input("Enter the number of voters wants to vote: "))
# for i in range(voters):
#     name = input("\nEnter Your Name: ").strip()
#     age = int(input("Enter Your Age: "))
#     if age >= 18:
#         if name not in registration:
#             registration.append(name)
#             print(f"{name} You have Registered Successfully")
#         else:
#             print(f"{name}You have already Registered")
#     else:
#         print("You Cannot Vote!")  

# print("\n-----Voting-----")  .,,,,,
# for registered in registration:
#     print(f"\n{registered} Your Turn to Vote.")  
#     print("--Candidates--")  
#     print("1. Imran Khan") 
#     print("2. Nawaz Sharif") 
#     print("3. Zaradri")  
#     choice = int(input("Choose Your Candidate (1-3): "))

#     if choice == 1:
#         votes[0] += 1
#         print("You Voted For Imran Khan")
#     elif choice == 2:
#         votes[1] += 1
#         print("You Voted For Nawaz Sharif")
#     elif choice == 3:
#         votes[2] += 1
#         print("You Voted For Zardari")
#     else:
#         print("Invalid Number!")

# print("-----Voting Results-----")  
# for i in range(len(candidates)):
#     print(f"{candidates[i]} With {votes[i]} Votes.")  

# highest = max(votes)
# winner = votes.index(highest)  
# print(f"The Winner is {candidates[winner]} With {highest} Votes")      




# Library Management System.

# Start with a Library class (attributes: books, no_of_books).
# Show menu (Add Book, Show Books, Count Books, Remove Book, Exit).
# If Add → take input and append to books list.
# If Show → loop through list and display.
# If Count → show number of books.
# If Remove → delete book from list.
# (Optional) Save and load book list from a file for persistence.


print("---Library Management System---")
class Library:
     def __init__(self):
         self.add_book = []
         self.no_books = 0
   
     def addbooks(self): 
            while True:
                bookname = input("Enter Books You want to add & type 'done' for exit: ")
                if bookname.lower() == 'done':
                    break
                else:
                    self.add_book.append(bookname)
                    self.no_books += 1 
                    print(f"{bookname} Added Sucessfully")
    
     def showbooks(self):
            if self.no_books == 0:
                print("Library is Empty!") 
            else:
                print("Books in Library")
                for i, books in enumerate(self.add_book,1):
                    print(f"{i}. {books}")
     
     def count_books(self):
            return self.no_books
     
     def removebooks(self):
          if self.no_books == 0:
               print("There are No Books to Remove!")
          else:
               self.showbooks()
               r_book = input("Enter the bookname you want to remove: ")
               if r_book in self.add_book:
                    self.add_book.remove(r_book)
                    self.no_books -= 1
                    print(f"{r_book} Remove Successfully")
               else:
                    print(f"{r_book} is Not in the library")

         
lib = Library()


while True:
    choice = input("Type what do you want to do? \nAdd/Show/Count/Remove/Exit: ")
    if choice.lower() == 'exit':
        break
    elif choice.lower() == 'add':
         lib.addbooks()
    elif choice.lower() == 'show':
         lib.showbooks()
    elif choice.lower() == 'count':
        print("Total Books in the Library:", lib.count_books())
    elif choice.lower() == 'remove':
         lib.removebooks()
    else:
         print("Enter Correct Choice!")    
                            




# Show menu (Add Student, View Students, Search Student, Exit).
# Add Student → input roll no, name, marks (store as dict).
# View Students → read all records and display.
# Search → enter roll number and display student info.
# Calculate total, percentage, grade dynamically.

students = {}
def calc_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    else:
        return "Fail"
while True:
    print("1. Add Students")
    print("2. View Students")
    print("3. Search Students")
    print("4. Exit")
    option = int(input('Enter Number To See: '))
    match option:
        case 1:
              roll_no = int(input("Enter the Roll no: "))
              name = input("Enter the Name: ")
              marks = list(map(int,input("Enter marks of different subjects by space:").split()))
              total = sum(marks)
              percentage = (total / (len(marks)* 100)) * 100
              grade = calc_grade(percentage)

              students[roll_no] = {"Name": name, "Marks": marks, "Total": total, "Percentage": percentage, "Grades": grade }
              print(f"{name} Added Successfully")

            
        case 2:
          if not students:
                print("No students found!")
          else:
                for roll_no, det in students.items():
                 print(f"Roll No: {roll_no} | Name: {det['Name']} | Marks: {det['Marks']} | "
                        f"Total: {det['Total']} | Percentage: {det['Percentage']:.2f}% | Grades: {det['Grades']}")
 

        case 3:
            search_stu = int(input("Enter Roll No To Search Student: "))
            if search_stu in students:
                det = students[roll_no]
                print(f"Found Student - Roll No: {roll_no} | Name: {det['Name']} | Marks: {det['Marks']} | "
                      f"Total: {det['Total']} | Percentage: {det['Percentage']:.2f}% | Grades: {det['Grades']}")
            else:
                print("Student not found.")

        case 4:
            print("Closing Student Management System")
            break        

                  


# Show menu (Add, Subtract, Multiply, Divide, Exponent, View History, Exit).
# User chooses an option.
# Take two numbers as input.
# Perform operation using a function.
# Handle errors (like divide by zero) with try-except.
# Save result in a history list.
# User can view history anytime. 


print("---Simple Calculator---")
history = []
def add(a,b):
    result = a + b
    history.append(f"{a} + {b} = {result}")
    return result
def sub(a,b):
    result = a - b
    history.append(f"{a} - {b} = {result}")
    return result
def mul(a,b):
    result = a * b
    history.append(f"{a} * {b} = {result}")
    return result
def div(a,b):
    try:
     result = a / b
     history.append(f"{a} / {b} = {result}")
     return result
    except ZeroDivisionError:
        print("Value Must be greater then Zero.")
def exp(a,b):
    result = a ** b
    history.append(f"{a} ** {b} = {result}")
    return result


while True:
    choice = input("Add / Subtract / Multiply / Divide / Exponent / History / Exit: ").lower()
    if choice == 'exit':
        print("Closing the Calculator!")
        break

    elif choice == 'history':
       if not history:
           print("History is Empty!")
       else:
           print("---Calculation History---")
           for i , h in enumerate(history,1):
               print(f"{i}. {h}")
    
    elif choice in ["add", "subtract", "multiply", "divide", "exponent"]:
     a = int(input("Enter Number 1: "))
     b = int(input("Enter Number 2: "))

    if choice == 'add':
        print("Result = ", add(a,b))
    elif choice == 'subtract':
        print("Result = ",sub(a,b))
    elif choice == 'multiply':
        print("Result = ",mul(a,b))
    elif choice == 'divide':
        print("Result = ",div(a,b))
    elif choice == 'exponent':
        print("Result = ",exp(a,b))
    
    









# Show menu (Add Expense, View All, View Summary by Category, Exit).
# Add Expense → input category, amount → store in dictionary ({category: [amounts]}).
# View All → print every expense.
# View Summary → calculate total spent per category.
# Save all expenses to file (CSV or JSON).
# Load saved expenses at program start.