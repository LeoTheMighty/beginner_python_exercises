# Divisor takes in a number and returns all the divisors of that number

# ie div(13) == [1, 13]
#    div(4) == [1, 2, 4]

def div(num):
    divList = []
    for i in range(1, int(num / 2) + 1):
        if num % i == 0:
            divList.append(i)

    divList.append(num)
    return divList


num = int(input("Choose a number to get divisors of "))

print(div(num))
