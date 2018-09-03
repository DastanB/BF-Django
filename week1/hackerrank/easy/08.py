n = int(input())
l = []
for x in range(n):
    st = input().split(" ")
    com = st[0]
    if com == "print":
        print(l)
    if com == "append":
        l.append(int(st[1]))
    if com == "insert":
        l.insert(int(st[1]),int(st[2]))
    if com == "remove":
        l.remove(int(st[1]))
    if com == "pop" and len(l) != 0:
        l.pop()
    if com == "sort":
        l.sort()
    if com == "reverse":
        l.reverse()