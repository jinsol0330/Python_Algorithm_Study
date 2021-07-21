'''
톱니바퀴
'''

import sys

def find(target, direction):
    global wheel_info, rotate_target
    state = [0,0,0,0]
    state[target] = direction

    # 오른쪽(자신은 포함되지 않으므로 +1)
    for i in range(target+1,4):
        # 타켓 톱니바퀴와 그 오른쪽에 있는 톱니바퀴의 맞닿은 부분이 다르다면
        if wheel_info[i-1][2] != wheel_info[i][6]:
            # 방향이 1이면 그 다음은 -1, -1이면 그 다음은 1이 되어야 하므로 -1을 곱함
            state[i] = state[i-1] * -1
        else:
            break

    # 왼쪽(자신은 포함되지 않으므로 -1)
    for i in range(target-1, -1, -1):
        # 타켓 톱니바퀴와 그 왼쪽에 있는 톱니바퀴의 맞닿은 부분이 다르다면
        if wheel_info[i+1][6] != wheel_info[i][2]:
            state[i] = state[i+1] * -1
        else:
            break

    return state

def rotate(res):
    global wheel_info, rotate_target
    for i in range(4):
        # 톱니바퀴의 상태가 0이면 아무런 동작을 하지 않음
        if res[i] == 0:
            continue
        # 톱니바퀴의 상태가 1이면 시계방향으로 회전
        elif res[i] == 1:
            value = wheel_info[i].pop()
            # print(value)
            wheel_info[i].insert(0, value)
            # print(wheel_info[i])
        # 톱니바퀴의 상태가 -1이면 반시계방향으로 회전
        else:
            value = wheel_info[i][0]
            # print(value)
            del wheel_info[i][0]
            wheel_info[i].append(value)
            # print(wheel_info[i])

wheel_info = []
for i in range(4):
    wheel_info.append(list(map(int, sys.stdin.readline().strip())))
    # print(wheel_info)
n = int(input())

rotate_target = []
for i in range(n):
    rotate_target.append(list(map(int, input().split())))

for t, d in rotate_target:
    # 1번 바퀴는 실제 인덱스 0이므로
    res = find(t-1, d)
    rotate(res)

print(wheel_info[0][0] + wheel_info[1][0] * 2 + wheel_info[2][0] * 4 + wheel_info[3][0] * 8)
