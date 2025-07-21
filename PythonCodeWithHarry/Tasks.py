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

print("\nWelcome To ATM")


c_bal = 10000
depo = 0
his = []
pin = 0000
user_pin = int(input("Enter Your Pin Please: "))
if pin == user_pin:
    print("You Are Login Into Your Account")
    
    while True:
            print("1: Check Balance")
            print("2: Deposit Money")
            print("3: Withdraw Money")
            print("4: Check History")
            print("5: Exit")
            opt = int(input("Choose Option To Do a Transaction: ")) 
            if opt == 5:
                 print("ThankYou For Using the ATM Have a Nice Day")
                 break
            match opt:
                 case 1:  
                      print("Your Current Balance is ",c_bal)
                      his.append(f"Checked Balance: {c_bal}")
                 case 2:
                      d_amount = int(input("Enter the Amount You to Deposit: "))
                      depo = d_amount
                      c_bal += depo
                      his.append(f"Deposit Amount: {d_amount}")
                      print("Deposit Successfull! \nNow Your Balance After Deposit is ",c_bal)
                 case 3:
                      w_amount = int(input("Enter the Amount You Want to Withdraw: ")) 
                      if w_amount <= c_bal:
                           c_bal -= w_amount
                           print("Withdraw Successfull! \nYour Balance After Withdraw is ",c_bal)
                           his.append(f"Withdraw Amount: {w_amount}")
                      else:
                           print("Your Balance is Not Sufficient") 
                 case 4:
                      if his:
                           for r in his:
                                print("Your History is",his)    
                 case _:
                       print("Invalid Selection")                         
else:
    print("Your Pin is Incorrect") 



# ✅ Task 3: Mini Quiz App (Like KBC)
# Concepts: lists, if-else, loops, input, tuple (optional)

# Rebuild or improve your KBC quiz:

# Store questions/options/answers in lists

# Reward user with amount after each correct answer

# Break the loop on wrong answer

# You’ve almost nailed this already, just refine it more. ✅

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

