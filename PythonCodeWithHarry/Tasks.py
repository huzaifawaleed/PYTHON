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
#               print("Enter Valis Number")
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
while True:
    print("1: Decimal To Binary")
    print("2: Binary To Decimal")
    print("3: Exit")
    option = int(input("Choose Option: "))

    match option:
      case 1:
          deci = int(input("Enter a Decimal Number to Convert into Binary: "))
          binary = ""
          num = deci
          while num > 0:
           rem = num % 2
           binary = str(rem) + binary
           num //= 2

          print(f"The Binary of {deci} is {binary}.")
      case 2:
          binary = input("Enter Binary Number to Convert into Decimal: ")
          dec = 0
          binary = binary[::-1]
          for b in range(len(binary)):
             bit = int(binary[b])
             dec += bit * (2 ** b)
          print(f"Decimal of {binary[::-1]} is {dec}.")      
    


















    
   
     