import sys
n, k = map(int, sys.stdin.readline().split())
arr = []
for i in range(n):
    s = str(sys.stdin.readline().rstrip())
    arr.append(s)
arr2 = sorted(arr)
print(arr2[k-1])