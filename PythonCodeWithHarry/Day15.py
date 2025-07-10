# MATCH CASE STATEMENTS.

# Write a program that takes a number (1–7) and prints the day of the week using match-case.

# day = int(input("Enter 1-7 to Check Day of the Week: "))

# match day:
#     case 1:
#         print("MONDAY")
#     case 2:
#         print("TUESDAY")
#     case 3:
#         print("WEDNESDAY")        
#     case 4:
#         print("THURSDAY")
#     case 5:
#         print("FRIDAY")
#     case 6:
#         print("SATURDAY")   
#     case 7:
#         print("SUNDAY")
#     case _:
#         print("Not a DAY On This Number")             





# Take two numbers and an operation symbol (+, -, *, /) from the user.
# Use match-case to perform the correct operation.


# while True:
#     print("1: ADD")  
#     print("2: SUB")  
#     print("3: DIV")   
#     print("4: MUL")
#     print("5: EXIT")  

#     sel = int(input("Select The Operation: "))  
#     if sel == 5:
#         break

#     num1 = int(input("Enter Number 1: "))   
#     num2 = int(input("Enter Number 2: "))   

#     match sel:  # properly indented inside the loop
#         case 1:
#             print("Result:", num1 + num2)
#         case 2:
#             print("Result:", num1 - num2) 
#         case 3:
#             if num2 != 0:
#                 print("Result:", num1 / num2)
#             else:
#                 print("Error: Cannot divide by zero")
#         case 4:
#             print("Result:", num1 * num2)         
#         case _:
#             print("Invalid Selection")






# Ask the user to enter a grade (like A, B, C, D, F).
# Use match-case to print a message like:

# A → Excellent

# B → Good

# C → Fair

# D → Poor

# F → Fail


# grade = input("Enter a grade (like A, B, C, D, F) To Check Your Progress: ").lower()

# match grade:
#     case 'a':
#         print("Your Progress is Excellent")
#     case 'b':
#         print("Your Progress is Good")
#     case 'c':
#         print("Your Progress is Fair")
#     case 'd':
#         print("Your Progress is Poor")
#     case 'f':
#         print("Your Progress is Not Well You are FAIL")            






# Take input for a traffic light color (red, yellow, green) and use match-case to print the action:
# Red → Stop
# Yellow → Get Ready
# Green → Go


# signal = input("Enter a Traffic Signal Colour To Do a Action: ")

# match signal:
#     case 'red':
#         print("STOP!")
#     case 'yellow':
#         print("GET READY")
#     case 'green':
#         print("GO")        
#     case _:
#         print("NO ACTION")


# Take a month number (1–12) and use match-case to print the corresponding season:

# 12, 1, 2 → Winter
# 3, 4, 5 → Spring
# 6, 7, 8 → Summer
# 9, 10, 11 → Autumn

month = int(input("Enter Month To Find the Season: "))

match month:
    case 1| 2| 12:
        print("WINTER")
    case 3| 4| 5:
        print("SPRING")
    case 6| 7| 8:
        print("SUMMER")
    case 9| 10| 11:
        print("AUTUMN")            
    case 0| 13:
        print("No Season In This Month")    