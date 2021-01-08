import random
choice = input("rock , papper or scissor ? : ")
choices = ["rock","papper","scissor"]
computer = random.choice(choices) 

def choice_checking():
    global choice
    if choice not in choices:
        choice = input("Enter the correct choice : ")

def play_game():
    choice_checking()
    print("You selected",choice,"and computer selected",computer)
    if choice == computer:
        print("Draw , try again")
    elif choice == "rock" and computer == "scissor":
        print("You Won the match") 
    elif choice == "scissor" and computer == "papper":
        print("You Won the match")
    elif choice == "papper" and computer == "rock":
        print("You Won the match")
    else:
        print("You Lose and computer won the match , Try again") 
play_game()
         