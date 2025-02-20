"""
python3 - PriorityQueue
pypy3 - heapq
백준에서 pypy3로 PriorityQueue를 사용하려고 하면 런타임 에러 발생
"""
import heapq
n = int(input())
heap = []

for i in range(n):
    a = int(input())
    heapq.heappush(heap, a)

sum = 0
for i in range(n-1):
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
    tmp = x+y
    sum += tmp
    heapq.heappush(heap, tmp)
print(sum)