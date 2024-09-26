import sys
n, m = map(int, sys.stdin.readline().split())
s = set(sys.stdin.readline().rstrip() for i in range(n))
res = 0

for _ in range(m):
    mm = sys.stdin.readline().rstrip()
    if mm in s:
        res += 1
print(res)