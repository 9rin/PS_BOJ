import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    a = int(sys.stdin.readline())
    arr.append(a)
arr.sort()

sum, res = 0, 0
for i in range(n):
    sum = arr[i]*(n-i)
    if res < sum:
        res = sum
print(res)
