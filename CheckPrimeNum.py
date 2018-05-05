# check to see if a number is prime or not
# 2,147,483,647 takes a long time to load


def check_prime(num):
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            return False
    return True


def get_integer(help_text="Give me a number: "):
    return int(input(help_text))


if check_prime(get_integer()):
    print("Is a prime number")
else:
    print("Is not a prime number")