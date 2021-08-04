'''
컨베이어 벨트 위의 로봇
'''

from sys import stdin
from collections import deque

n,k = map(int, stdin.readline().split())
# 내구도
dur = deque(map(int, stdin.readline().split()))
# 로봇위치
robot = deque([0]*n)
# 단계
res = 1

def rotate_belt():
    dur.rotate(1)
    robot.rotate(1)

def move_robot():
    # (내리는 곳 바로 앞)뒤에서부터 차례로 이동
    for i in range(n-2, -1, -1):
        # 현재칸에 로봇이 있고, 다음칸엔 로봇에 없으며 내구성이 0보다 크면
        if robot[i] != 0 and robot[i+1] == 0 and dur[i+1] > 0:
            # 다음칸 내구성 -1
            dur[i+1] -= 1
            # 다음칸으로 로봇 이동
            robot[i+1] = 1
            # 현재칸에 있던 로봇은 사라짐
            robot[i] = 0
            
while True:
    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 회전한다
    rotate_belt()
    # 내리는 위치(N번째 칸)에서 로봇을 내림
    robot[-1] = 0

    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 
    move_robot()
    # 내리는 위치(N번째 칸)에서 로봇을 내림
    robot[-1] = 0
    
    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if dur[0] > 0 and robot[0] == 0: 
        # 내구성 -1
        dur[0] -= 1
        # 현재위치에 로봇 올리기
        robot[0] = 1

    # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
    if dur.count(0) >= k:
        print(res)
        break
    
    # 모든 과정이 끝나면 단계를 +1
    res += 1
