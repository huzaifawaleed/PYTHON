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

print("Welcome To Contact Book")
contacts = []
while True:
   print("1: Add New Contact")
   print("2: View All Contacts")
   print("3: Search Contact")
   print("4: Remove Contact")
   print("5: Exit")
   opt = int(input("Choose Option : ")) 
   if opt == 5:
         print("ThankYou For Using The Contact Book")
         break
   match opt:
       case 1:  
           u_name =input("Enter Full Name: ")
           u_num = input("Enter Contact Number: ")
           u_email = input("Enter Email: ")
           if u_name == "" or u_num == "" or u_email == "":
               print("Fill All the Fields To Add The contact")
           else:
            add_c = [u_name, u_num, u_email]
            contacts.append(add_c)
            print("Contact Added SuccessFully")
            print("Added Contact",add_c)
       case 2:
           print("Your Contacts")
           print(contacts)

       case 3:
           search = input("Enter the Name or Number To Search: ")
           find = False
           for con in contacts:
               if search in con:
                   print("Contact Found: Name: ",u_name," Number: ",u_num," Email: ",u_email," ")
                   find = True
                   break
               if not find:
                   print("Contact Not Found!")

       case 4:
           delete = input("Enter the Name or Number To Delete: ")
           for conn in contacts:
               if delete in conn:
                   contacts.remove(conn)
                   print("Contact Found: ",delete," Deleted Successfully")
                   break
               else:
                   print("Contact Not Found!")
           
       case _:
           print("Invalid Entry")
           

# ✅ Task 4: Movie Ticket Booking System
# Concepts: list, tuple, if-else, loops

# Simulate a simple ticket booking:

# Show list of available movies and times

# Let user select one and enter number of tickets

# Show total bill

# Bonus: Limit number of tickets per show using a list

# ✅ Task 5: Shopping Cart Console App
# Concepts: lists, loops, if-else, tuples

# Create a cart system:

# Add/remove items to/from cart

# View current cart

# Checkout (show total price)

# Store items as tuples: ("item", price)

