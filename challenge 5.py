import random

a = []
b = []

for i in range (0,12):
    f = random.randint(1,20)
    a.append(f)

for i in range (0,15):
    f = random.randint(1,20)
    b.append(f)


c = []  

[c.append(i) for i in a if i == b or a]

c = list(set(c))

print(c)

