import sys
n = int(sys.stdin.readline())
sum = 0
for i in range(n):
    s = str(sys.stdin.readline().rstrip())
    s = int(s[2::])
    if s <= 90: sum += 1
print(sum)
