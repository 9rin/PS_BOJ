import sys

n = int(sys.stdin.readline())
res, i = 0, 666

while res != n:
    if "666" in str(i):
        res += 1
    i += 1

print(i-1)