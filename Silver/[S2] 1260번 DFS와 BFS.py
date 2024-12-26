import sys
from collections import deque

visited = []
#깊이 우선 탐색
def dfs(start, node, n, visited):
    visited.append(start)
    for i in range(n):
        if node[start][i] == 1:
            if i not in visited:
                #print(start, visited)
                dfs(i, node, n, visited)
    return visited


queue = deque()
visit = []
# 너비 우선 탐색
def bfs(node, n, queue):
    while len(queue) != 0:
        start = queue.popleft()
        print(start+1, end = " ")
        for i in range(n):
            if(node[start][i] == 1):
                if i not in visit:
                    visit.append(i)
                    queue.append(i)
        bfs(node, n, queue)

# 노드, 간선, 시작 정점
n, m, v = map(int, sys.stdin.readline().split())
node = [[0 for j in range(n)] for i in range(n)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    node[a-1][b-1] = 1
    node[b-1][a-1] = 1

dfs(v-1, node, n, visited)
for i in visited:
    print(i+1, end=" ")
print()

queue.append(v-1)
visit = [v-1]
bfs(node, n, queue)

