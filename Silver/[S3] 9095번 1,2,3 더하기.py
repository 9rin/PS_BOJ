import sys
memo = {}
def res(n):
    if n in memo:
        return memo[n]
    elif n==1: return 1
    elif n==2: return 2
    elif n==3: return 4
    else:
        memo[n] = res(n-1) + res(n-2) + res(n-3)
    return memo[n]

n = int(sys.stdin.readline())
for i in range(n):
    t = int(sys.stdin.readline())
    print(res(t))