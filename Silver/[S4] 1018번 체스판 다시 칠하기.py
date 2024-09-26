import sys
n, m = map(int, sys.stdin.readline().split())
arr = [0 for j in range(n)for i in range(m)]
ans1 = ["WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW"]
ans2 = ["BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB"]

for i in range(0, n):
    arr[i] = list(input().rstrip())

res1, res2 = 0, 0
res = []

for i in range(n-7):
    for j in range(m-7):
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (arr[k][l] != ans1[k - i][l - j]):
                    res1 += 1
                if (arr[k][l] != ans2[k - i][l - j]):
                    res2 += 1

        res.append(res1)
        res.append(res2)
        res1, res2 = 0, 0

print(min(res))