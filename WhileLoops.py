### Part Two -- your code goes here. 
import random
# generate a random number between 1 and 100
correct_number = random.randint(1, 100)

#give guess a starting number
guess=0

# While loop to keep asking for guesses until the correct number is guessed
while guess != correct_number:
    guess = int(input("Guess a number between 1 and 100: "))
    
    if guess < correct_number:
        print("too low!")

    elif guess > correct_number:
        print("too high!")
    
    else:
        print("Congratulations! You guessed the correct number.")


