### Part Four -- your code goes here. 

import random
numbers = [random.randint(1, 100) for _ in range(10)]
print("List with even numbers:")

for number in numbers:
    print(str("Checking") + " : " + str(number))

i = 0
while i < len(numbers):
       
    if numbers[i] % 2 == 0:  
     numbers.pop(i)  
        
    else:
         i += 1  

print("Remaining odd numbers:", numbers)