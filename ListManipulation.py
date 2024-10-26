### Part Three -- your code goes here. 

list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

list.sort()

while 1 in list:
    list.remove(1)

list += [7, 8]

print(list)
