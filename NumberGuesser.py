def find_yes_or_no(boolString):
    s = boolString.lower()
    if s == "no" or s == "nah" or s == "n":
        return False
    elif s == "yes" or s == "yeah" or s == "y":
        return True
    else:
        return -1


guessString = "lower"
bottom, top = 0, 1
ifFirstSection = True
ifSecondSection = False
ifPositive = True
ifGuessing = True

# find top with just positive
while ifFirstSection:
    if find_yes_or_no(input("Is your number " + guessString + " than " + str(top) + "?\n")):
        if top is 1:
            ifPositive = False
            bottom = -1
            top = 0
            ifSecondSection = True
            guessString = "higher"
        ifFirstSection = False
    else:
        bottom = top
        top *= 10

# top is set find negative side
while ifSecondSection:
    if find_yes_or_no(input("Is your number " + guessString + " than " + str(bottom) + "?\n")):
        ifSecondSection = False
    else:
        top = bottom
        bottom *= 10

# top and bottom are set
while ifGuessing:
    guess = int((top + bottom) / 2)
    answer = find_yes_or_no(input("Is your number " + guessString + " than " + str(guess) + "?\n"))
    interestNum = 0

    if answer != ifPositive:
        interestNum = bottom
        bottom = guess
    else:
        interestNum = top
        top = guess

    if guess == interestNum and not answer:
        ifGuessing = False
        print("Your number is " + str(guess) + "! I guessed it!")
