n = int(input())
arr = list(map(int, input().split()))

for element in arr:
    if element % 2 == 0:
        print(element)