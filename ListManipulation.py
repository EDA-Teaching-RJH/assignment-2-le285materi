### Part Three -- your code goes here. 
# Given list
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Sort the list, remove all  1s, add 7 and 8, then print final list
numbers.sort()

while 1 in numbers:
    numbers.remove(1)

numbers += [7, 8]

print(numbers)
