"""
후위 표기식
우선 순위: 괄호 > 곱셉과나눗셈 > 더하기와 빼기

알고리즘
1. 스택 선언
2. 숫자면 바로 출력, 연산자면 조건에 맞게 행동
    ㄱ. 괄호 ( 면 스택에 넣기
    ㄴ. 괄호 ) 면 (이거 만날 때까지 차례 대로 출력 하기
    ㄷ. +,- 면 자기 앞에 있는 얘가 우선 순위가 크면 걔를 출력 하고 자기는 스택에 넣기
    ㄹ. *,/ 도 자기 앞에 있는 얘가 우선 순위가 크면 걔를 ""
        아니면 자기가 우선 순위가 크면 자기가 출력 되기
"""

import sys
shic = list(str(sys.stdin.readline().rstrip()))
stack = []

def lank(i):
    if i == "(":
        return 0
    elif i == "*" or i == "/":
        return 2
    elif i == "+" or i == "-":
        return 1

yeon = ["/","(",")","*","+","-"]
for i in shic:
    if i in yeon:
        if len(stack) == 0:
            stack.append(i)
        elif i == ")":
            while stack[-1] != "(":
                print(stack[-1], end="")
                stack.pop()
            stack.pop()
        elif i == "(":
            stack.append(i)
        else:
            while(len(stack) != 0 and lank(i) <= lank(stack[-1])):
                print(stack[-1], end="")
                stack.pop()
            stack.append(i)
            #print(f": 현재 스택은 {stack}입니다")
    else:
        print(i, end="")
        #print(f": 현재 스택은 {stack}입니다")

while(len(stack)!=0):
    print(stack[-1],end="")
    stack.pop()




