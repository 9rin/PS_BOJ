import sys
n = int(sys.stdin.readline())
for _ in range(n):
    g, c, e = map(int, sys.stdin.readline().split())
    km = 1
    if g == 2: km = 3
    elif g == 3: km = 5
    print(km*(e-c) if km*(e-c) > 0 else 0)
