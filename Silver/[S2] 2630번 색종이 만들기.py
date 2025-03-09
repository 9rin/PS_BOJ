"""
list comprehension 대신 좌표 값을 return 주면서 시간 줄이기
"""
# divide - conquer - combine
white, blue = 0, 0

def dcc(arr,x1,x2,y1,y2):
    global white, blue
    a = arr[x1][y1]
    same = True

    for i in range(x1,x2):
        for j in range(y1,y2):
            if arr[i][j] != a:
                same = False
                break
            if not same: break
    if same:
        if a == 1: blue += 1
        else: white += 1
        return
    mx = (x1+x2)//2
    my = (y1+y2)//2

    dcc(arr, mx, x2, y1, my) #1사분면
    dcc(arr, x1, mx, y1, my) #2사분면
    dcc(arr, x1, mx, my, y2) #3사분면
    dcc(arr, mx, x2, my, y2) #4사분면

import sys
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dcc(arr, 0, n, 0, n)
print(f"{white}\n{blue}")