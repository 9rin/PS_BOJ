import sys
n, a = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
res = 0
for i in range(n):
    res += arr[i]//a
print(res)