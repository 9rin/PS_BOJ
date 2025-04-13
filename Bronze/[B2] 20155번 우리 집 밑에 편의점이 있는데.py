import sys
n, m = map(int, sys.stdin.readline().split())
x = list(map(int, sys.stdin.readline().split()))
arr = []
for i in range(1,m+1):
    arr.append(x.count(i))
print(max(arr))