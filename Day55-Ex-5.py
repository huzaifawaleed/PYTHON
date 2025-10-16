# Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the snake beats the water. Write a python program to create a Snake Water Gun game in Python using if-else statements. Do not create any fancy GUI. Use proper functions to check for win.



import random
print("-----Welcome To Snake--Water--Gun Game-----")

   

while True:
   user = int(input("Enter 0 for Snake | 1 for Water | 2 for Gun: "))
   if user == 3:
      print("Game Exit")
      break

   comp = random.randint(0 , 2)
   def check(comp, user):
     
     if user == comp:
        return 0
     elif comp == 0 and user == 1:
        return -1
     elif comp == 1 and user == 2:
        return -1
     elif comp == 2 and user == 0:
        return -1
     else:
        return 1
    
   score = check(comp,user)  

   print("You Choose",user)
   print("Computer Choose",comp)

   if score == 0:
     print("The match is draw")
   elif score == -1:
    print("You Lose")
   else:
    print("You Won")



user_choice = input("Enter Your Weapon: ")

choices = ["snake", "water", "gun"]
comp_choice = random.choice(choices)
print(f"User Choice is {user_choice} and Computer Choice is {comp_choice}")
def result(user_choice, comp_choice):
    if user_choice == "snake" and comp_choice == "water":
        print("User Wins",user_choice)
    elif user_choice == "water" and comp_choice == "gun":
        print("User Wins",user_choice)
    elif user_choice == "gun" and comp_choice == "snake":
        print("User Wins",user_choice)
    elif user_choice == "snake" and comp_choice == "gun":
        print("Computer Wins",comp_choice)
    elif user_choice == "water" and comp_choice == "snake":
        print("Computer Wins",comp_choice)
    elif user_choice == "gun" and comp_choice == "water":
        print("Computer Wins",comp_choice)
    elif user_choice == comp_choice:
        print("Match Draw Both Choices are Same",comp_choice,user_choice)

result(user_choice, comp_choice)


