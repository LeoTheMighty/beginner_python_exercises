# Use a dictionary to improve time cost


def get_fib_num(index):
    if index == 0:
        return 0
    if index == 1:
        return 1
    fib = {0: 0, 1: 1}
    i = 2
    for i in range(2, index + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[i]


print(get_fib_num(int(input("Which fibonacci do you want to see? "))))
