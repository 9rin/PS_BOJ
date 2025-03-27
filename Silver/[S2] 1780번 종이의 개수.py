res = [0, 0, 0]

def dcc(x1, x2, y1, y2, arr):
    global res
    first = arr[y1][x1]
    l = x2-x1
    #print(f"x1,x2: {x1, x2}, y1,y2: {y1,y2}, first = {first}, length = {l}, res = {res}")
    onel = l//3
    twol = 2*(l//3)

    if l == 1:
        res[arr[y1][x1]] += 1
        return
    else:
        for i in range(y1, y2):
            for j in range(x1, x2):
                if arr[i][j] != first:
                    #print(f"x1,x2: {x1, x2}, y1,y2: {y1, y2}, first = {first}, length = {l}, res = {res}")
                    dcc(x1, x1+onel, y1, y1+onel, arr)
                    dcc(x1 + onel, x1 + twol, y1, y1 + onel, arr)
                    dcc(x1+twol, x1+l, y1, y1+onel, arr)

                    dcc(x1, x1 + onel, y1+onel, y1+twol, arr)
                    dcc(x1 + onel, x1 + twol, y1+onel, y1+twol, arr)
                    dcc(x1 + twol, x1 + l, y1+onel, y1+twol, arr)

                    dcc(x1, x1+onel, y1+twol, y2, arr)
                    dcc(x1+onel, x1+twol, y1+twol, y2, arr)
                    dcc(x1+twol, x2, y1+twol, y2, arr)
                    return
        res[first] += 1
        return


import sys
n = int(sys.stdin.readline())
ar = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dcc(0,n,0,n,ar)
print(f"{res[2]}\n{res[0]}\n{res[1]}")
