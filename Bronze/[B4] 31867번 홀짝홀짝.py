import sys
n = int(sys.stdin.readline())
k = str(sys.stdin.readline().rstrip())
sum = 0

for i in k:
    if int(i)%2==0: sum += 1
    else: sum -= 1
if sum == 0:
    print(-1)
else:
    print(0 if sum > 0 else 1)