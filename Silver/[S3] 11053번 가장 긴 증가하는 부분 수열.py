#다이나믹 프로그래밍
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

#가장 긴 증가 부분 수열의 길이 저장소
table = [1]*n

for i in range(n):

    leng = 0
    for j in range(i):
        if(arr[i]>arr[j] and leng < table[j]):
            leng = table[j]
    table[i] += leng
print(max(table))