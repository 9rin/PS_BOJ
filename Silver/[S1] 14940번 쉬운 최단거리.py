import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
queue = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            arr[i][j] = 0
            queue.append((i,j))
            break

a = [1, -1, 0, 0]
b = [0, 0, -1, 1]
stack = []
while(len(queue)!=0):
    q = queue.popleft()
    for i in range(4):
        x = q[0] + a[i]
        y = q[1] + b[i]
        if 0<=x<n and 0<=y<m and arr[x][y] == 1 and (x,y) not in stack:
            arr[x][y] = arr[q[0]][q[1]] + 1
            if arr[x][y] == 1:
                stack.append((x,y))
            queue.append((x,y))

for i in range(n):
    for j in range(m):
        if (i,j) not in stack and arr[i][j] == 1:
            print(-1, end=" ")
        else:
            print(arr[i][j], end = " ")
    print("")