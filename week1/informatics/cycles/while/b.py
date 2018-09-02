n = int(input())

i = 2
min_del = 1

while(i <= n):
    if(n % i == 0):
        min_del = i
        print(i)
        break
    i = i + 1