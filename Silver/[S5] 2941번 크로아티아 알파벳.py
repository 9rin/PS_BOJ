import sys

cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
s = str(sys.stdin.readline().strip())
res = 0

for i in range(len(cro)):
    res += s.count(cro[i])

print(len(s)-res)