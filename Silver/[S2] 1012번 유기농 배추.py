"""
너비우선탐색
-> queue로 상하좌우로 배추밭이 어떻게 연결되어 있는지 파악
-> queue에 원소가 없으면 배추밭 연결 끊김 지렁이 갯수 추가
"""

import sys
from collections import deque

aa = [1, -1, 0, 0]
bb = [0, 0, 1, -1]

T = int(sys.stdin.readline())
for i in range(T):

    # 배추밭 기본 정보
    m, n, k = map(int, sys.stdin.readline().split())
    lis = []
    for j in range(k):
        a, b = map(int,sys.stdin.readline().split())
        lis.append((b,a))

    # 너비 우선 탐색
    queue = deque()
    queue.append(lis[0])
    res = 1
    while len(lis) != 0:
        if len(queue) == 0:
            queue.append(lis[0])
            res += 1
        q = queue.popleft()
        lis.remove(q)

        for k in range(4):
            x = q[0] + aa[k]
            y = q[1] + bb[k]
            if x>=0 and y>=0 and x<n and y<m:
                if (x,y) in lis and (x,y) not in queue:
                    queue.append((x,y))
    print(res)