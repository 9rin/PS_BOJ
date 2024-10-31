"""
재귀

Example: 3 7 7
2의 3승, (7,7) 입력 받음
2의 2승으로 나누면 (7,7) 4분면 존재
-> 사각형 3개 Z 더하기 (16 * 3 = 48)

그 다음 시작점 (3,3)
2의 1승으로 나누면 (3,3) 4분면 존재
-> 사각형 3개 Z 더하기 (4 * 3 = 12)

그 다음은 초기값 (1,1) 3 더하기
"""
import sys, math

def z(n, r, c):
    #print(f"n:{n}, r:{r}, c:{c}")
    if n == 1:
        if(r==1 and c==1):
            return 3
        elif(r==1 and c==0):
            return 2
        elif(r==0 and c==1):
            return 1
        else:
            return 0
    else:
        nemo = 2**(n-1)
        #print(f"nemo: {nemo}")
        if(r//nemo == 1 and c//nemo == 1):
            return (nemo**2) * 3 + z(n - 1, r % nemo, c % nemo)
        elif (r // nemo == 1 and c // nemo == 0):
            return (nemo**2) * 2 + z(n - 1, r % nemo, c % nemo)
        elif (r // nemo == 0 and c // nemo == 1):
            return (nemo**2) + z(n - 1, r % nemo, c % nemo)
        else:
            return z(n - 1, r % nemo, c % nemo)

n, r, c = map(int, sys.stdin.readline().split())
print(z(n,r,c))
