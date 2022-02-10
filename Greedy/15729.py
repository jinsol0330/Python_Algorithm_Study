'''
방탈출

그리디 알고리즘 특성상 앞에서부터 하나하나 보면
최소횟수를 찾을 수 있다
'''

from sys import stdin

N = int(stdin.readline())
target = list(map(int, stdin.readline().split()))

buttons = [0 for _ in range(N)]
res = 0
for idx in range(N):
    # 현재 위치와 타겟 위치의 값이 같다면 continue
    if buttons[idx] == target[idx]:
        continue
    
    # 값이 다른 경우
    #   -> 불이 꺼진 경우라면 켜고
    if buttons[idx] == 0:
        buttons[idx] = 1 
    #   -> 불이 켜진 경우라면 끄기
    else:
        buttons[idx] = 0
    #   -> 오른쪽 버튼 확인  
    if idx + 1 < N:
        if buttons[idx + 1] == 0:
            buttons[idx + 1] = 1
        else:
            buttons[idx + 1] = 0     
    if idx + 2 < N:
        if buttons[idx + 2] == 0:
            buttons[idx + 2] = 1 
        else:
            buttons[idx + 2] = 0       
    
    # 결과값 1 카운트
    res += 1

print(res)