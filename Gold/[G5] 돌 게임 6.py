import sys
n = int(sys.stdin.readline())
print("CY" if n%7 == 0 or n%7 == 2 else "SK")