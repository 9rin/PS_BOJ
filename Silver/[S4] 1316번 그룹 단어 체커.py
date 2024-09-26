import sys
n = int(sys.stdin.readline())
res = 0

for i in range(n):
    s = list(str(sys.stdin.readline().rstrip()))
    ss = []
    tmp, last = 0, 0

    for i in s:
        if(i not in ss or i == last):
            tmp += 1
        last = i
        ss.append(i)

    if(len(s)==tmp):
        res+=1

print(res)