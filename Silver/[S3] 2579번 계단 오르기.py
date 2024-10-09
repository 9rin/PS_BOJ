"""
[2579번] 계단 오르기
-> DP로 해결

- 3계단 오르기 X (최대 1개 건너뛰기 가능)
- 2계단 연속 밟기 가능 (3개 연속 X)
    - 밟는 경우 (1번, 2번)
    - 밟지 않는 경우

dp[i][j] i번 계단을 j번 연속 밟을 때 최대 점수

"""

import sys
n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]
dp = [[0 for _ in range(3)] for _ in range(n+1)]

dp[1][1] = arr[0]
dp[1][2] = arr[0]

for i in range(2, n+1):
    dp[i][0] = max(dp[i-1][2], dp[i-1][1])
    dp[i][1] = dp[i-1][0] + arr[i-1]
    dp[i][2] = dp[i-1][1] + arr[i-1]

print(max(dp[n][1],dp[n][2]))


