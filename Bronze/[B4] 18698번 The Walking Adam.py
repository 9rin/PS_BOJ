import sys
n = int(sys.stdin.readline())
for i in range(n):
    s = str(input())
    res = 0
    for i in s:
        if i == "D": break
        res += 1
    print(res)
