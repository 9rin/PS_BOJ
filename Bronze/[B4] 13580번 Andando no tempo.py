#S or N

arr = list(map(int, input().split()))
arr.sort()
arr2 = set(arr)

if arr[0]+arr[1]==arr[2] or len(arr2)<3:
    print("S")
else: print("N")