import sys
a, b, c, d = map(int, sys.stdin.readline().split())
res = a+d-b-c
print(res if res > 0 else res *(-1))