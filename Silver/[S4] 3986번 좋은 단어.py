import sys
n = int(sys.stdin.readline())

def goodword(word):
    stack = []
    for i in word:
        if len(stack)>0 and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    if len(stack)==0:return 1
    else: return 0

res = 0
for i in range(n):
    word = list(str(sys.stdin.readline().rstrip()))
    if len(word) % 2 == 0:
        res += goodword(word)
print(res)