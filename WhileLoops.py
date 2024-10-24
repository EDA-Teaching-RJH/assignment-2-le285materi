### Part Two -- your code goes here. 
import random
correct_number = random.randint(1, 100)
guess=0

while guess != correct_number:
    guess = int(input("Guess a number between 1 and 100: "))
    
    if guess < correct_number:
        print("too low!")

    elif guess > correct_number:
        print("too high!")
    
    else:
        print("Congratulations! You guessed the correct number.")


