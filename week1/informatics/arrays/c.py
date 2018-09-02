n = int(input())

arr = list(map(int, input().split()))
s = 0

for element in arr:
    if element > 0:
        s += 1

print(s)