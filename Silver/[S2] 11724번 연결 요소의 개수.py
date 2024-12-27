import sys

visited = []
def dfs(start, node, n, visited):
    visited.append(start)
    for i in range(n):
        if node[start][i] == 1:
            if i not in visited:
                #print(start, visited)
                dfs(i, node, n, visited)
    return visited


n, m = map(int, sys.stdin.readline().split())
node = [[0 for j in range(n)] for i in range(n)]
nn = set()

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    node[a - 1][b - 1] = 1
    node[b - 1][a - 1] = 1
    nn.add(a)
    nn.add(b)

connected = 0
if len(nn) != n: connected += n-len(nn)

for i in nn:
    if (i-1) not in visited:
        dfs(i-1, node, n, visited)
        connected += 1
print(connected)
