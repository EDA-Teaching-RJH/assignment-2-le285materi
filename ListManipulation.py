### Part Three -- your code goes here. 

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

numbers.sort()

while 1 in numbers:
    numbers.remove(1)

numbers += [7, 8]

print(numbers)
