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

print("Welcome To Movie House")
movie = [
    ["Oppenheimer", "6:00 PM", 800, 20],
    ["Dune 2", "9:00 PM", 1000, 15],
    ["Kung Fu Panda 4", "3:00 PM", 600, 25]
]
while True:
 print("1: Available Movies")
 print("2: Book Tickects")
 print("3: Exit")


 opt = input("Select Option: ")

 if opt == "1":
   for idx, m in enumerate(movie , start=1):
         print(f"{idx}. {m[0]} | Time: {m[1]} Price: {m[2]} Available Tickets: {m[3]}")

   select = int(input("Enter the Movie Number You Want To Book: "))
   if 1 <= select <= len(movie):
    select = movie[select -1]
    print("Please Select the Valid Number")
   else:
    print(f"You Seleted {select[0]} at {select[1]}")
    print(f"Price: {select[2]} | Available Tickets: {select[3]}")











# print("🎬 Welcome to the Movie Ticket Booking System 🎟️")

# # List of movies [Title, Show Time, Price, Tickets Available]
# movies = [
#     ["Oppenheimer", "6:00 PM", 800, 20],
#     ["Dune 2", "9:00 PM", 1000, 15],
#     ["Kung Fu Panda 4", "3:00 PM", 600, 25]
# ]

# while True:
#     print("\n📋 Available Movies:")
#     for idx, m in enumerate(movies, start=1):
#         print(f"{idx}. {m[0]} | Time: {m[1]} | Price: Rs.{m[2]} | Tickets Left: {m[3]}")
    
#     print("\n1. Book Tickets")
#     print("2. Exit")
#     choice = input("Choose an option (1/2): ")

#     if choice == "2":
#         print("👋 Thank you for using the Movie Ticket Booking System.")
#         break

#     elif choice == "1":
#         try:
#             movie_choice = int(input("Enter the movie number you want to book: "))
#             if 1 <= movie_choice <= len(movies):
#                 selected_movie = movies[movie_choice - 1]
#                 print(f"You selected: {selected_movie[0]} at {selected_movie[1]}")
#                 print(f"Ticket Price: Rs.{selected_movie[2]} | Tickets Available: {selected_movie[3]}")
                
#                 num_tickets = int(input("Enter number of tickets to book: "))

#                 if num_tickets <= 0:
#                     print("❌ Number of tickets must be greater than 0.")
#                 elif num_tickets > selected_movie[3]:
#                     print("❌ Not enough tickets available!")
#                 else:
#                     total_price = num_tickets * selected_movie[2]
#                     selected_movie[3] -= num_tickets  # reduce available tickets
#                     print(f"✅ Booking Confirmed! Total Price: Rs.{total_price}")
#                     print(f"🎟️ Enjoy your movie: {selected_movie[0]} at {selected_movie[1]}")
#             else:
#                 print("❌ Invalid movie selection.")
#         except ValueError:
#             print("❌ Please enter valid numbers only.")
#     else:
#         print("❌ Invalid option. Please choose 1 or 2.")






# ✅ Task 5: Shopping Cart Console App
# Concepts: lists, loops, if-else, tuples

# Create a cart system:

# Add/remove items to/from cart

# View current cart

# Checkout (show total price)

# Store items as tuples: ("item", price)

