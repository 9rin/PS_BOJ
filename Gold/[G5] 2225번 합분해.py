"""
2225번 합분해 풀이과정

2차원 배열 dp 선언
dp[i][j] <- i번째 수로 합이 j가 되는 경우의 수
하나하나 다 구해보면 규칙이 보인다.
"""

import sys
n, k = map(int, sys.stdin.readline().split())
dp = [[1 for _ in range(n+1)] for _ in range(k+1)]

for i in range(n+1):
    dp[0][i] = 0

for i in range(1,k+1):
    for j in range(1,n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[k][n]%1000000000)