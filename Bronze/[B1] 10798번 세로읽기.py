import sys
arr = [[0 for col in range(15)]for row in range(5)]
arr_len = [0]*5
for i in range(5):
    arr[i] = sys.stdin.readline().rstrip()
    arr_len[i] = len(arr[i])


for i in range(15): #열
    for j in range(5): #행
        if arr_len[j] > i:
            print(arr[j][i], end="")