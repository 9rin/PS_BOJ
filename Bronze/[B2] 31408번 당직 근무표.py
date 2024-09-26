import sys

n = int(sys.stdin.readline())
arr = [0]*100001
num = list(map(int, sys.stdin.readline().split()))
ans = n//2+1 if n%2==1 else n//2

for i in num:
    arr[i] += 1

print("NO" if max(arr)>ans else "YES")