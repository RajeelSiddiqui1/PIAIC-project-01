print("Welcome to the 'Guess the Number' game!")
print("Think of a number between 1 and 100, and I will try to guess it.")
print("Respond with 'too high', 'too low', or 'correct'.")

low = 1
high = 100
attempts = 0

game = True

while game:
     
     guess = (low + high) //2
     attempts +=1

     feedback = input(f"My guess is: {guess}. Is it too high, too low, or correct? ").lower()

     if feedback == "too high":
          high = -1 

     elif feedback == "too low":
          low = +1

     elif feedback == 'correct':
        print(f"I guessed your number {guess} in {attempts} attempts!")
        break
     else:
        print("Please respond with 'too high', 'too low', or 'correct'.")

     print("Do you want countineou(yes/no)")
     ans = input().lower()

     if ans == "no":
        game = False
        print("tanks for playing game")    
   
          