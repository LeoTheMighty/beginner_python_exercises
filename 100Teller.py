__author__ = "leo"

import math

print("hello world")

person = input("What is your name?\n")
age = int(input("What is your age?\n"))
copies = int(input("How many copies do you want printed?\n"))

for i in range(0, copies):
    print("{}, you will turn 100 in {}.".format(person, 2018 + (100 - age)))

#print("{}, you will turn 100 in {}.".format(person, 2018 + (100 - age)))
print("The value of PI is {}".format(math.pi))

print("a", "b", "c", sep=' ')
