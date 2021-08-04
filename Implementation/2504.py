'''
괄호의 값

4개의 기호 ‘(’, ‘)’, ‘[’, ‘]’를 이용해서 만들어지는 괄호열 중에서 올바른 괄호열이란 다음과 같이 정의된다.
    1. 한 쌍의 괄호로만 이루어진 ‘()’와 ‘[]’는 올바른 괄호열이다. 
    2. 만일 X가 올바른 괄호열이면 ‘(X)’이나 ‘[X]’도 모두 올바른 괄호열이 된다. 
    3. X와 Y 모두 올바른 괄호열이라면 이들을 결합한 XY도 올바른 괄호열이 된다.
예를 들어 ‘(()[[]])’나 ‘(())[][]’ 는 올바른 괄호열이지만 ‘([)]’ 나 ‘(()()[]’ 은 모두 올바른 괄호열이 아니다. 
우리는 어떤 올바른 괄호열 X에 대하여 그 괄호열의 값(괄호값)을 아래와 같이 정의하고 값(X)로 표시한다. 
    1. ‘()’ 인 괄호열의 값은 2이다.
    2. ‘[]’ 인 괄호열의 값은 3이다.
    3. ‘(X)’ 의 괄호값은 2×값(X) 으로 계산된다.
    4. ‘[X]’ 의 괄호값은 3×값(X) 으로 계산된다.
    5. 올바른 괄호열 X와 Y가 결합된 XY의 괄호값은 값(XY)= 값(X)+값(Y) 로 계산된다.
예를 들어 ‘(()[[]])([])’ 의 괄호값을 구해보자. 
‘()[[]]’ 의 괄호값이 2 + 3×3=11 이므로 ‘(()[[]])’의 괄호값은 2×11=22 이다. 
그리고 ‘([])’의 값은 2×3=6 이므로 전체 괄호열의 값은 22 + 6 = 28 이다.
여러분이 풀어야 할 문제는 주어진 괄호열을 읽고 그 괄호값을 앞에서 정의한대로 계산하여 출력하는 것이다. 
'''

from sys import stdin
from collections import deque

def is_right(str):
    stack = []
    for s in str:
        # 왼쪽괄호를 만나면 스택에 넣어줌
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')' and stack:
            if stack[-1] == '(':
                stack = stack[:-1]
            else:
                stack.append(s)
        elif s == ']' and stack:
            if stack[-1] == '[':
                stack = stack[:-1]
            else:
                stack.append(s)
        else:
            stack.append(s)
    if stack:
        return False
    else:
        return True

def cal(str):
    stack = []
    for s in str:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if stack[-1] == '(':
                stack[-1] = 2
            else:
                tmp = 0
                for i in range(len(stack) - 1, -1, -1):
                    if stack[i] == '(':
                        stack[-1] = tmp * 2
                        break
                    else:
                        tmp += stack[i]
                        stack = stack[:-1]
        elif s == ']':
            if stack[-1] == '[':
                stack[-1] = 3
            else:
                tmp = 0
                for i in range(len(stack) - 1, -1, -1):
                    if stack[i] == '[':
                        stack[-1] = tmp * 3
                        break
                    else:
                        tmp += stack[i]
                        stack = stack[:-1]
    return sum(stack)

    

str = stdin.readline()

if is_right(str) == False:
    print(0)
else:
    print(cal(str))