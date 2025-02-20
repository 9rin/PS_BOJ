"""
정렬된 두 묶음의 숫자 카드 A, B 비교 A+B
N개의 숫자 카드 묶음의 각각의 크기가 주어질 때, 최소한 몇 번의 비교가 필요한지?

작은거부터 차례대로 비교할 때 가장 적게 비교 가능
-> 큐에 넣고 정렬 큐에 넣고 정렬
-> 큐는 정렬을 할 수 없음.
-> 우선순위큐를 통해 작은 숫자 먼저 OUT
"""

import sys
from queue import PriorityQueue
n = int(sys.stdin.readline())
q = PriorityQueue()

for i in range(n):
    a = int(sys.stdin.readline())
    q.put(a)
sum = 0
for i in range(n-1):
    x = q.get()
    y = q.get()
    sum += (x+y)
    q.put(x+y)

print(sum)