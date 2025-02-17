"""
1 -> 1
2 -> 3
3 -> 5
4 -> 11
memo[i] = memo[i-1] + 2*memo[i-2]
"""

import sys
n = int(sys.stdin.readline())
memo = [0]*1000
memo[0], memo[1] = 1, 3
for i in range(2,n):
    memo[i] = memo[i-1] + 2*memo[i-2]
print(memo[n-1]%10007)