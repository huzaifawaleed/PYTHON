# Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the snake beats the water. Write a python program to create a Snake Water Gun game in Python using if-else statements. Do not create any fancy GUI. Use proper functions to check for win.



import random
print("-----Welcome To Snake--Water--Gun Game-----")
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


