import sys
n = int(sys.stdin.readline())
ptime = list(map(int, sys.stdin.readline().split()))
ptime.sort()
res = 0

for i in range(n):
    res += sum(ptime)
    ptime.remove(ptime[-1])
print(res)