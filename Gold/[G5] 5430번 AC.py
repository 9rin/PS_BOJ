"""
16% 시간초과 해결하기
-> list 대신에 deque 이용

[1, 2, 3, 4, 5] 출력 X
[1,2,3,4,5] 출력 O
"""

import sys
from collections import deque
t = int(sys.stdin.readline())

for i in range(t):
    # 기본 입력 받기
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    arr = str(sys.stdin.readline().rstrip())
    if arr == "[]":
        arr = []
    else:
        arr = arr.strip('][')
        arr = deque(map(int,arr.split(",")))

    #RD 판단
    k,j = len(p),0
    reverse, res = 1,1
    while j != k:
        if p[j] == "R" and j+1<k and p[j+1] =="R":
            j += 2
            continue
        elif p[j] == "D" and len(arr) == 0:
            print("error")
            res = 0
            break
        elif p[j] == "D" and reverse == 1:
            arr.popleft()
        elif p[j] == "D" and reverse == -1:
            arr.pop()
        else:
            reverse = reverse * (-1)
        j += 1
    arr = list(arr)
    if res == 1:
        print("["+",".join(map(str, arr if reverse == 1 else arr[::-1])) + "]")
