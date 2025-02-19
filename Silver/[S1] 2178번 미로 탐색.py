"""
BFS -> 길을 차례대로 가보기
1. BFS 너비 우선 탐색
2. 깊이가 하나씩 깊어질 때마다 1을 더해줘서 미로의 길이를 결정
3. 1이면 아직 방문 안함, 0은 길이 없음, 1보다 크면 방문함
"""

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
miro = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    a = list(input())
    for j in range(m):
        miro[i][j] = int(a[j])

queue = deque()
queue.append((0,0))
aa = [1,-1,0,0]
bb = [0,0,-1,1]

while(len(queue)!=0):
    q = queue.popleft()
    for i in range(4):
        a = q[0] + aa[i]
        b = q[1] + bb[i]
        if a>=0 and b>=0 and a<n and b<m:
            if miro[a][b] == 1:
                miro[a][b] = miro[q[0]][q[1]] + 1
                queue.append((a,b))

print(miro[n-1][m-1])
