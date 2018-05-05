import random

random_num = random.randint(1, 9)
guesses = 0
is_playing = True
while is_playing:
    guess = int(input("Guess a number!\n"))
    if guess == random_num:
        print("You guessed it correctly!")
        is_playing = False
    elif guess > random_num:
        print("Too high!")
    else:
        print("Too low!")
    guesses += 1
guess_str = "guesses"
if guesses == 1:
    guess_str = "guess"

print("It took you " + str(guesses) + " " + guess_str + " to get " + str(random_num) + "!")