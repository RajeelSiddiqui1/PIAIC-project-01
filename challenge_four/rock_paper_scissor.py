import random

print("Welcome to rock,paper,scissor game")

choice = ["rock","paper","scissor"]

comp_choice = random.choice(choice)

game = True

while game:
    user=input("Enter obj: ").lower()
  
    if comp_choice  == user:
        print("match draw!!!")

    elif user == "rock" and comp_choice == "scissor":
        print("you won!!!")     
    
    elif user == "scissor" and comp_choice == "paper":
        print("you won!!!")     

    elif user == "paper" and comp_choice == "rock":
        print("you won!!!")     


    elif comp_choice == "rock" and user == "scissor":
        print("you lose!!!")     
    
    elif comp_choice == "scissor" and user == "paper":
        print("you lose!!!")     

    elif comp_choice == "paper" and user == "rock":
        print("you lose!!!")  

    else:
        print("Enter right obj")       


    print("Do you want countineou(yes/no)")
    ans = input().lower()

    if ans == "no":
        game = False
        print("tanks for playing game")    
   
    
