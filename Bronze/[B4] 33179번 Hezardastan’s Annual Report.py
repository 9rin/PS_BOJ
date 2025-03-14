n = int(input())
arr = list(map(int, input().split()))
sum = 0
for i in arr:
    if i % 2 == 0:
        sum += i//2
    else:
        sum += i//2 + 1
print(sum)