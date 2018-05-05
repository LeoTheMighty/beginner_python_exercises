import random


def list_ends(list1):
    return [list1[0], list1[-1]]


def random_list(size_l, num_l):
    size = random.randint(0, size_l)
    list2 = []
    for i in range(0, size - 1):
        list2.append(random.randint(0, num_l))
    return list2


print(list_ends(random_list(100, 1000)))
