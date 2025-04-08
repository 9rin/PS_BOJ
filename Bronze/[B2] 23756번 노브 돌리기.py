import sys
n = int(sys.stdin.readline())
before = int(sys.stdin.readline())
sum = 0
for i in range(n):
    after = int(sys.stdin.readline())
    if before > after:
        sum += before - after if before-after < after + (360 - before) else after + (360 - before)
    else:
        sum += after-before if after-before<before+(360-after) else before+(360-after)
    before = after
print(sum)
