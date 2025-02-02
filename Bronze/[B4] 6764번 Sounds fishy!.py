"""
출력은 네 가지 가능성 중 하나입니다.
깊이 판독 값이 증가하는 경우 출력은 Fish Rising.
깊이 판독 값이 감소하는 경우 출력은 Fish Diving.
깊이 판독 값이 동일한 경우 출력은 Fish At Constant Depth.
그렇지 않은 경우 출력은 No Fish.
"""

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a<b and b<c and c<d:
    print("Fish Rising")
elif a>b and b>c and c>d:
    print("Fish Diving")
elif a==b and b==c and c==d:
    print("Fish At Constant Depth")
else:
    print("No Fish")