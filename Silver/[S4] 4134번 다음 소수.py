import sys, math

def gcd(a, b):
    while b>0:
        a, b = b, a%b
        return a

def sosu(n):
    if(n<2):
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            return False
    return True

n = int(sys.stdin.readline())
for i in range(n):
    t = int(sys.stdin.readline())
    a = 0
    while a==0:
        if(sosu(t)):
            print(t)
            a = 1
        elif t==2:
            print(2)
            a = 1
        t += 1