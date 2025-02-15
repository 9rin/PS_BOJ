n = int(input())
for _ in range(n):
    be = 0
    s = str(input())
    for i in s:
        if i != be:
            print(i, end="")
        be = i
    print("")