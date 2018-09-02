import math

def mini(a, b, c, d):
    return(min(a, b, c, d)) 

arr = list(map(int, input().split()))


print(mini(arr[0], arr[1], arr[2], arr[3]))