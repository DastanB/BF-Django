import math

a = int(input())
b = int(input())

for i in range(a, b + 1):
    j = int(math.sqrt(i))

    if (j * j == i):
        print(i)