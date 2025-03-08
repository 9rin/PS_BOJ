#시간 줄이기
import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr2 = sorted(list(set(arr)))

dict = {v:i for i, v in enumerate(arr2)}
print(" ".join(str(dict[i])for i in arr) + "\n")
