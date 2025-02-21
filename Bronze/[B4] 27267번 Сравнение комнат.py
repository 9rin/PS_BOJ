import sys
a, b, c, d = map(int, sys.stdin.readline().split())
x = a*b
y = c*d
if x > y: print("M")
elif x < y: print("P")
else: print("E")