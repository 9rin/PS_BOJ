import sys
mbti = str(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline())
res = 0
for i in range(n):
    s = str(sys.stdin.readline().rstrip())
    if mbti == s: res += 1
print(res)