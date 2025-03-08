import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
start, end = 1, max(arr)

while start <= end:
    mid = (start + end)//2
    sum = 0

    for i in range(n):
        if arr[i] > mid:
            sum += arr[i]-mid

    if sum >= m: start = mid+1
    else: end = mid-1
    #print(f"현재 start는 {start} end {end} mid {mid}")

print(end)