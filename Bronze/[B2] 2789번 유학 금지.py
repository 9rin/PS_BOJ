import sys
arr = ['C','A','M','B','R','I','D','G','E']
s = str(sys.stdin.readline().rstrip())

for i in s:
    if not i in arr:
        print(i, end="")
print()