import sys
n = int(sys.stdin.readline())
print("CY" if n%5 == 0 or n%5 == 2 else "SK")