n = int(input())

i = 0
x = 1

while(n >= 1):
    i = i + n % 2
    n = n / 2

if ( i == 1 ): print("YES")
else: print("NO")