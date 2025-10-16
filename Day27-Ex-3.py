# Exercise 3

question = ["What is the capital of Pakistan?",
    "Which language is used to style web pages?",
    "Who is known as the founder of Pakistan?",
    "Which planet is known as the Red Planet?",
    "Which data structure uses FIFO order?",
    "What does CPU stand for?",
    "In which year did Pakistan become independent?",
    "Which animal is known as the Ship of the Desert?",
    "HTML is used for?",
    "Which gas do plants absorb from the atmosphere?"]

option = [
    ["A. Karachi", "B. Islamabad", "C. Multan", "D. Lahore"],
    ["A. Css", "B. Html", "C. JS", "D. PHP"],
    ["A. Quaid e azam", "B. bilawal bhutto", "C. allama iqbal", "D. sir syed ahmed khan"],
    ["A. Venus", "B. Mars", "C. Jupiter", "D. Mercury"],
    ["A. Stack", "B. Queue", "C. Tree", "D. Graph"],
    ["A. central panel unit", "B. control panel unit", "C. motherboard", "D. Central processin unit"],
    ["A. 1948", "B. 1940", "C. 1947", "D. 1945"],
    ["A. Horse", "B. Elephant", "C. Camel", "D. Donkey"],
    ["A. Styling pages", "B. Storing data", "C. Structuring content", "D. Running programs"],
    ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"]
]

ans = ["B", "A", "A", "B", "B", "D", "C", "B", "C", "C"]

amounts = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

home_amount = 0
all = True
for i in range(len(question)):
    print("Q:",i+1," ",question[i])
    for o in option[i]:
        print(o)




    u_input = input("Select the Correct Option (A/B/C/D): ").upper()

    if u_input == ans[i]:
     print("Correct Answer! You Won",amounts[i])
     home_amount = amounts[i]              
    else:
     print("Wrong Answer Game Over!")
     all = False
     break

if all:
   print("Game Finished")
   print("Your All Answers Were True Congratulations")
print("The Total Amount You Won",home_amount)
