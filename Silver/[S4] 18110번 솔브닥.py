def ban(num):
    if(num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

import sys
n = int(sys.stdin.readline())
arr = [0]*n

if n == 0:
    print(0)
else:
    for i in range(n):
        arr[i] = int(sys.stdin.readline())
    a = ban((n*15)/100)
    arr.sort()
    if a != 0:
        arr = arr[a:-a]
    print(ban(sum(arr)/len(arr)))