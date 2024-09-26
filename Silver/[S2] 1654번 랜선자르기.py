import sys
k,n = map(int, sys.stdin.readline().split())
arr = []
for i in range(k):
    a = int(sys.stdin.readline())
    arr.append(a)
arr.sort()

start, end = 1, arr[-1]
res = []


while start <= end:
    arrsum = 0
    mid = (start+end)//2
    for i in arr:
        arrsum += i//mid
    #print("start:",start,"end:",end,"arrsum:",arrsum,"  mid:",mid)
    if arrsum >= n:
        res.append(mid)
        start = mid + 1
    elif arrsum < n:
        end = mid - 1
    else:
        start = mid + 1

res.reverse()
print(res[0])