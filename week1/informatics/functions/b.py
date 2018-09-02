def power(a , n):
    x = 1
    for i in range(n):
        x = x * a
    
    return x

arr = list(map(float, input().split()))

print(power(arr[0], int(arr[1])))