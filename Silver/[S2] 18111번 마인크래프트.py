import sys
r, c, b = map(int, sys.stdin.readline().split())
arr = [list(map(int, input().split())) for _ in range(r)]

n = min(min(arr))
ob = b
arr_max = max(max(arr))
time, res_time = 0, 9999999999

while(n<=arr_max):
    time = 0
    b = ob

    for i in range(r):
        for j in range(c):
            tmp = arr[i][j] - n
            if tmp < 0: # 블록을 써야함
                time += (-1)*tmp
                b -= (-1)*tmp
            elif tmp > 0: # 블록을 제거함
                time += 2*tmp
                b += tmp

    if(b>=0 and time <= res_time):
        res_n = n
        res_time = time
    n += 1

print(res_time, res_n)