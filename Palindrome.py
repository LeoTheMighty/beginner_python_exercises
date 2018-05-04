input1 = input("Give a word\n")
input2 = input("Give another word\n")

length = len(input1)
if length != len(input2):
    print("Not a palindrome")
else:
    ifPal = True
    end = length - 1
    for i in range(0, length):
        if input1[i] != input2[end - i]:
            ifPal = False
    if ifPal:
        print("Is a palindrome!")
    else:
        print("Is not a palindrome")

# Whoops I accidentally don't know what a palindrome is lol