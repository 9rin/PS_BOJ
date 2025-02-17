"""
1 -> 1
2 -> 2
3 -> 3
4 -> 5
5 -> 8
"""

import sys
n = int(sys.stdin.readline())
memo = [0]*1000
memo[0], memo[1] = 1, 2
for i in range(2,n):
    memo[i] = memo[i-1] + memo[i-2]
print(memo[n-1]%10007)