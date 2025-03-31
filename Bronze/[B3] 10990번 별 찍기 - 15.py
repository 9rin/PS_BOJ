import sys
n = int(sys.stdin.readline())

if n == 1:
    print("*")
else:
    print(" "*(n-1), end="")
    print("*")
    for i in range(2,n+1):
        print(" "*(n-i), end = "")
        print("*", end = "")
        print(" "*(2*(i-1)-1), end = "")
        print("*")

