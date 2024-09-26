import sys

n = int(sys.stdin.readline())
size = list(map(int, sys.stdin.readline().split()))
t, p = map(int, sys.stdin.readline().split())
tt = 0

for i in size:
    if(i<=t and i != 0):
        tt += 1
    elif(i==0):
        tt += 0
    else:
        if(i%t==0):
            tt += i//t
        else:
            tt += i//t + 1
print(tt)
print(n//p, n%p)