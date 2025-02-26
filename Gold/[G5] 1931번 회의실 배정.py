"""
그리디, 정렬
85% 해결 -> 첫 번째 원소 정렬 후 두 번째 원소 정렬
"""

import sys

# 기본 정보 입력
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    arr.append((a,b))

# 정렬
arr = sorted(arr, key = lambda x:x[0])
arr = sorted(arr, key = lambda x:x[1])

# 그리디
res = 1
x = arr[0][1]

for i in range(1,n):
    if x <= arr[i][0]:
        x = arr[i][1]
        res += 1
print(res)