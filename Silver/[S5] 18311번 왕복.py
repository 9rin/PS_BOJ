import sys
n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
return_sum = sum(arr)
fsum = 0

if k > return_sum:
    k = k - return_sum
    for i in range(n-1,-1,-1):
        fsum += arr[i]
        if k <= fsum:
            print(i+1)
            break
elif k == return_sum:
    print(n)
else:
    for i in range(n):
        fsum += arr[i]
        if k < fsum:
            print(i+1)
            break

