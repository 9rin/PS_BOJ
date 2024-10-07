import sys
memo = {}

def fi(n):
    if n in memo:
        return memo[n]

    if n==0 or n==1:
        return n

    else:
        memo[n] = fi(n-1) + fi(n-2)
    return memo[n]

n = int(sys.stdin.readline())
for i in range(n):
    a, b = 0, 0
    t = int(sys.stdin.readline())

    if t == 0:
        print(1, 0)
    elif t == 1:
        print(0, 1)
    else:
        print(fi(t-1), fi(t))
"""피보나치 함수에서 fi(t)의 값은 1이 호출된 횟수, 
fi(t-1)의 값은 0이 호출된 횟수이다.

이유는 모르겠지만, 노가다를 하니까 그렇게 나왔다. 
피보나치 함수에서 나온 1을 모두 다 더하면 피보나치의 함수 결과값이
나오니까 fi(t)의 값이 1이 호출된 횟수인 것 같다.

fi(t-1)의 값이 0이 호출된 횟수인 이유는 뭘까...
흠.......................

"""

