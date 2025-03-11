import random

print("Gusses number game")

number = random.randint(1,100)

print("Welcome to the Guess the Number game!")
print("I have selected a number between 1 and 100.")
print("Your task is to guess the number.")

attempt = 0
game = True

while game:
    guess = int(input("Enter the number"))
    
    attempt +=1

    if guess < number:
        print("It's too low")
    
    elif guess > number:
        print("It's too hight")

    else:
        print(f"Congratulations! You've guessed the number {number} with in {attempt} attempts ")    

    print("Do you want countineou(yes/no)")
    ans = input().lower()

    if ans == "no":
        game = False
        print("tanks for playing game")    
