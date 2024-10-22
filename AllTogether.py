### Part Four -- your code goes here. 

import random

# create a list of 10 random numbers between 1 and 100
numbers = [random.randint(1, 100) for _ in range(10)]
print("list with even numbers:")

# use a for loop to go through the list
for number in numbers:
    print(str("Checking") + ": " + str(number))

# use a while loop to remove all even numbers
i = 0
while i < len(numbers):
        # If the number is even
    if numbers[i] % 2 == 0:  
        # Remove the number at the current i
        numbers.pop(i)  
        
    else:
        # only go through if the element was not removed
        i += 1  

# print the remaining odd numbers
print("Remaining odd numbers:", numbers)