#guessing game using random.randInt()
import random

def guess_number(num):
    random_number = random.randint(1,num)
    guess = 0
        
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {num}: "))
        if guess > random_number:
            print("Oops! Try again. That is too high")
        elif guess < random_number:
            print(f"Oh no! That is too low, try again")
    print(f"Congrats! You guessed it right! The correct number is {random_number}")    
    
guess_number(30)
     
