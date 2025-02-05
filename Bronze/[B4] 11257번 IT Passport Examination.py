import sys
n = int(sys.stdin.readline())
for i in range(n):
    a, b, c, d = map(int, sys.stdin.readline().split())
    if b>=11 and c>=8 and d>=12 and b+c+d>=55:
        res = "PASS"
    else: res = "FAIL"
    print(f"{a} {b+c+d} {res}")