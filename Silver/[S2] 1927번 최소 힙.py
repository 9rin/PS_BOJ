import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for i in range(n):
    a = int(sys.stdin.readline())
    if a == 0:
        print(0 if len(heap)==0 else heapq.heappop(heap))
    else:
        heapq.heappush(heap, a)