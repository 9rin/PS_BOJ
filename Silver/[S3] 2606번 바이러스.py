from collections import deque
import sys
n = int(sys.stdin.readline())
t = int(sys.stdin.readline())
vi = []
res = set()
res.add(1)

for i in range(t):
    a = list(map(int, sys.stdin.readline().split()))
    vi.append(a)

for i in range(t):
    for j in range(t):
        if vi[j][0] in res:
            res.add(vi[j][1])
        elif vi[j][1] in res:
            res.add(vi[j][0])

print(len(res)-1)