import sys
t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    memo = [1]*n
    if n < 4:
        print(1)
    else:
        i = 3
        while i != n:
            memo[i] = memo[i-2] + memo[i-3]
            i+=1
        print(memo[n-1])