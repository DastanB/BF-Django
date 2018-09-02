import math

def min_div(n):
    for i in range(2, int(math.sqrt(int(n))) + 1):
        if (a % i == 0):
            return i
    return n
    


a = int(input())

print(min_div(a))