import sys

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())

up = a*d + c*b
down = b*d
t = gcd(up, down)

print(up//t, down//t)