import sys
n = int(sys.stdin.readline())
for i in range(n):
    w, k = map(int, sys.stdin.readline().split())
    print((w*k)//2)