import sys
n = int(sys.stdin.readline())
t=0
res = 0
for i in range(1,n+1):
    nsum = int((i*(i+1))/2)
    if nsum == n:
        res = i+1
        if res % 2 == 0:
            print("1/",res-1,sep="")
        else:
            print(res-1,"/1",sep="")
        break

    elif nsum > n:
        res = i+1
        t = n - int(((i-1)*i)/2)

        if res % 2 == 0:
            print(res - t, "/", t,sep="")
        else:
            print(t, "/", res - t,sep="")
        break




