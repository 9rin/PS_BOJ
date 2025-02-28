"""
n과 k가 같은 경우 0 출력
"""
import sys
from collections import deque

queue = deque()
arr = [0]*100001
n, k = map(int, sys.stdin.readline().split())
queue.append(n)
tmp = [0]*3
a = 1

while(a == 1):
    if n == k:
        print(0)
        break
    q = queue.popleft()
    tmp[0], tmp[1], tmp[2] = q+1, q-1, 2*q
    for i in range(3):
        if tmp[i] == k:
            res = arr[q]+1
            print(res)
            a=0
        if tmp[i]>0 and tmp[i]<100001 and arr[tmp[i]] == 0:
            arr[tmp[i]] = arr[q]+1
            queue.append(tmp[i])
