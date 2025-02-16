import sys
arr = ["ABCD", "EFGH", "IJKL", "MNO."]
key = {"A":"00", "B":"01", "C":"02", "D":"03",
       "E":"10", "F":"11", "G":"12", "H":"13",
       "I":"20", "J":"21", "K":"22", "L":"23",
       "M":"30", "N":"31", "O":"32"}
res = 0

for i in range(4):
    s = str(sys.stdin.readline().rstrip())
    for j in range(4):
        if s[j] != arr[i][j] and s[j] != ".":
            a = key[s[j]]
            res += abs(int(a[0])-i) + abs(int(a[1])-j)
print(res)