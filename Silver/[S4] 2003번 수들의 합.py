import sys
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
start, end, res = 0, 0, 0
sum = arr[0]

while start != n:
    if len(arr) == 1:
        if arr[0] == m: res = 1
        break

    if sum == m:
        #print(f"sum: {sum}, index: {start},{end}")
        res += 1
        if start == end:
            if end == n - 1: break
            else:
                sum -= arr[start]
                start += 1
                end += 1
                sum += arr[end]
        else:
            sum -= arr[start]
            start += 1
    elif sum < m:
        if end == n-1: break
        else:
            end += 1
            sum += arr[end]
    else:
        if start == end:
            if end == n - 1: break
            else:
                sum -= arr[start]
                start += 1
                end += 1
                sum += arr[end]
        else:
            sum -= arr[start]
            start += 1
print(res)