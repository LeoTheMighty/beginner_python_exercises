a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, -1000000]

num = int(input("What do you want to vent your list with?"))
newerList = [int(i) for i in a if i < num]

print(newerList)
