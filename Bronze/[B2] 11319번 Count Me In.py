import sys
arr = ["A","E","I","O","U","a","e","i","o","u"]
n = int(sys.stdin.readline())

for i in range(n):
    s = list(str(sys.stdin.readline().rstrip()))
    mo = 0
    za = 0

    for i in s:
        if(i in arr):
            mo+=1
        elif(i == " "):
            mo += 0
        else:
            za += 1
    print(za, mo)