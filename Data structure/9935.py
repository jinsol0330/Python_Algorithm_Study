'''
문자열 폭발
- 문자열이 폭발 문자열을 포함하고 있는 경우에, 모든 폭발 문자열이 폭발하게 된다.
- 남은 문자열을 순서대로 이어 붙여 새로운 문자열을 만든다.
- 새로 생긴 문자열에 폭발 문자열이 포함되어 있을 수도 있다.
- 폭발은 폭발 문자열이 문자열에 없을 때까지 계속된다.
'''

from sys import stdin
 
str = list(stdin.readline().rstrip())
bomb = list(stdin.readline().rstrip())
 
stack = []
 
for s in range(len(str)):
    # 입력 문자열을 앞에서부터 차례차례 한 글자씩 스택에 push
    stack.append(str[s])
    # 현재 글자가 폭발 문자열의 마지막 글자와 일치하면
    if stack[-1] == bomb[-1] and len(stack) >= len(bomb):
        # 스택의 top부터 폭발 문자열의 길이만큼 비교하면서 일치하는지 확인
        if stack[-len(bomb):] == bomb:
            # 폭발 문자열을 스택에서 pop
            for _ in range(len(bomb)):
                stack.pop()
 
if stack:
    print("".join(stack))
else:
    print("FRULA")

