import sys

#2436번
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

n = int(sys.stdin.readline())
for i in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    sum = 0
    for j in range(1,len(arr)-1):
        for k in range(j+1,len(arr)):
            sum += gcd(arr[j],arr[k])
    print(sum)