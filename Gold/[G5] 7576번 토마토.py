"""
너비 우선 탐색 -> 상하좌우로 토마토가 익음. 익은 순서를 arr에 기록
결과 판단: 만약 arr에 0이 있다면 -1 출력
"""

import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
arr = [[0 for j in range(m)] for i in range(n)]
queue = deque()

for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        if a[j] == 1:
            queue.append((i,j))
        arr[i][j] = a[j]

aa = [1, -1, 0, 0]
bb = [0, 0, -1, 1]
res = 1

while len(queue) != 0:
    q = queue.popleft()
    for i in range(4):
        a = q[0] + aa[i]
        b = q[1] + bb[i]
        if a>=0 and b>=0 and a<n and b<m:
            if arr[a][b] == 0:
                arr[a][b] = arr[q[0]][q[1]] + 1
                queue.append((a,b))
                if res < arr[a][b]: res = arr[a][b]

for i in range(n):
    if 0 in arr[i]: res = 0
print(res-1 if res != 0 else -1)
