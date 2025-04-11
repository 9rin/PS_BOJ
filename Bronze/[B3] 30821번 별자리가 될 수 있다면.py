import sys, math
n = int(sys.stdin.readline())
res = math.factorial(n)/(120*math.factorial(n-5))
print(int(res))