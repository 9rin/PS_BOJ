import sys

n = int(sys.stdin.readline())
print("CY" if n%8 == 1 or n%8 == 3 else "SK")