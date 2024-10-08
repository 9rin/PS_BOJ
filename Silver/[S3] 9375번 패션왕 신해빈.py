import sys
from itertools import combinations

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    cloth = {}
    for i in range(n):
        a, b = map(str, sys.stdin.readline().rstrip().split())
        if b in cloth:
            cloth[b] += 1
        else:
            cloth[b] = 1

    if len(cloth) == 1: print(cloth[b])
    else:
        sum = 1
        arr = list(cloth.values())

        for i in arr:
            sum *= (i+1)
        print(sum-1)

