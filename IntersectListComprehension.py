import random

rand_size_limit = 100
rand_num_limit = 5
a_size = random.randint(0, rand_size_limit)
b_size = random.randint(0, rand_size_limit)

a = []
b = []

for i in range(0, a_size):
    a.append(random.randint(0, rand_num_limit))

for j in range(0, b_size):
    b.append(random.randint(0, rand_num_limit))

if a_size > b_size:
    c = [int(k) for k in a if k in b]
else:
    c = [int(k) for k in b if k in a]
d = []
for l in c:
    if l not in d:
        d.append(l)
print("a: " + str(a))
print("b: " + str(b))
print("intersection: " + str(d))
