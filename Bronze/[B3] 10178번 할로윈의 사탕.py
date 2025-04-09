import sys
n = int(sys.stdin.readline())
for i in range(n):
    c, v = map(int, sys.stdin.readline().split())
    print(f"You get {c//v} piece(s) and your dad gets {c%v} piece(s).")