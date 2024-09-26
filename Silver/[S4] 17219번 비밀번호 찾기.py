import sys
n, m = map(int, sys.stdin.readline().split())
password = {}

for i in range(n):
    k, n = map(str, sys.stdin.readline().rstrip().split())
    password[k] = n

for i in range(m):
    a = str(sys.stdin.readline().rstrip())
    print(password[a])