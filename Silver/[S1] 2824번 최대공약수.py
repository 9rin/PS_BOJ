import sys
n = int(sys.stdin.readline())
nn = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
mm = list(map(int, sys.stdin.readline().split()))

a, b = 1, 1
for i in nn: a *= i
for i in mm: b *= i

def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

res = list(str(gcd(a,b)))

if(len(res)>9):
    print(''.join(res[len(res)-9::]))
else:
    print(''.join(res))