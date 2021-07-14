'''
아기상어

N×N 크기의 공간에 물고기 M마리와 아기 상어 1마리가 있다. 
공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 한 칸에는 물고기가 최대 1마리 존재한다.
아기 상어와 물고기는 모두 크기를 가지고 있고, 이 크기는 자연수이다. 
가장 처음에 아기 상어의 크기는 2이고, 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동한다.
아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다. 
아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다. 따라서, 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.
아기 상어가 어디로 이동할지 결정하는 방법은 아래와 같다.
- 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
- 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
- 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
    -> 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
    -> 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다고 가정한다. 
즉, 아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동했다면, 이동과 동시에 물고기를 먹는다. 
물고기를 먹으면, 그 칸은 빈 칸이 된다.
아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다. 
예를 들어, 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다.

공간의 상태가 주어졌을 때, 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하는 프로그램을 작성하시오.
'''
from collections import deque

n = int(input())
space = []
for i in range(n):
    space.append(list(map(int, input().split())))

# 상하좌우로 이동한다고 가정
case = [[-1, 0],[0, -1], [0, 1], [1, 0]]

# 상어 크기
shark_size = 2

def find(x,y):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[x][y] = 1
    q = deque()
    q.append([x, y])
    res = []
    while q:
        x, y = q.popleft()
        # 상하좌우 탐색
        for i in range(4):
            newx = x + case[i][0]
            newy = y + case[i][1]
            if 0 <= newx < n and 0 <= newy < n:
                # 이동 가능한지 확인(물고기 크기, 이전에 방문했는지에 대한 여부)
                if space[newx][newy] <= shark_size and visited[newx][newy] == 0:
                    # 먹을 수 있는지 확인
                    if space[newx][newy] < shark_size and space[newx][newy] != 0:
                        res.append([newx, newy, visited[x][y]])
                    else:
                        # 이동한 위치를 넣어줘야 그 다음부턴 그 위치를 기준으로 계산할 수 있음
                        # ex_거리가 1일때, 2일때, 3일때 ...
                        q.append([newx,newy])
                        # 탐색하는 데 걸린 시간을 업데이트
                        visited[newx][newy] = visited[x][y] + 1
    # 상어가 물고기를 하나도 먹지 못한 경우
    if len(res) == 0:
        return -1, -1, -1
    else:
        # x[0] = x좌표(상하), x[1] = y좌표(좌우), x[2] = 물고기를 먹기까지 걸리는 시간
        res = sorted(res, key=lambda x: (x[2], x[0], x[1]))
        return res[0]

# 상어가 물고기를 먹는데 걸리는 총 시간
time = 0
# 상어가 물고기를 먹은 횟수
shark_cnt = 0

def eat_fish():
    global space, shark_cnt, shark_size, time
    for i in range(n):
        for j in range(n):
            if space[i][j] == 9:
                sharkx, sharky, sec = find(i,j)
                if sharkx == -1 and sharky == -1 and sec == -1:
                    return False
                else:
                    shark_cnt += 1
                    time += sec
                    # 상어 크기과 먹은 물고기 수가 같으면
                    if shark_size == shark_cnt:
                        shark_size += 1
                        shark_cnt = 0
                    # 현재 상어의 위치를 0으로 만들기
                    space[i][j] = 0
                    # 상어가 이동할 위치를 9로 만들기
                    space[sharkx][sharky] = 9
                    return True

while True:
    if eat_fish():
        continue
    else:
        break

print(time)