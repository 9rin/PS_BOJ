def facto(n):
    return n * facto(n-1) if n>1 else 1

import sys
n = int(sys.stdin.readline())
nn = str(facto(n))
res = 0
print(nn)

for i in range(1,len(nn)+1):
    if(nn[-i]=="0"):
        res += 1
    else:
        break
print(res)