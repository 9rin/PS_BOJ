import sys
from collections import deque

n = int(sys.stdin.readline())
arr = deque()

for i in range(n):
    inp = list(sys.stdin.readline().split())

    if(len(inp)==2):
         arr.append(int(inp[1]))

    if(inp[0] == "2"):
        if(len(arr)==0):
            print("-1")
        else:
            print(arr[-1])
            arr.pop()
    if(inp[0] == "3"):
        print(len(arr))

    if(inp[0] == "4"):
        if(len(arr)==0):
            print(1)
        else:
            print(0)

    if(inp[0] == "5"):
        if(len(arr)==0):
            print(-1)
        else:
            print(arr[-1])
