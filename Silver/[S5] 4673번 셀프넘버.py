from sys import stdin, stdout
print = stdout.write
ans = set(i for i in range(1,10001))

for i in range(1, 10001):
    n = i
    for j in str(i):
        n += int(j)
    ans.discard(n)

for i in ans:
    print(str(i) + '\n')