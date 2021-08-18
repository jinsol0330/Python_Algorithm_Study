'''
토마토

철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다.
창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 
보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 
하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다. 
대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 
철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.
토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 
며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.
'''

from sys import stdin
from collections import deque

def find():
    case = [[-1,0], [1,0], [0,-1], [0,1]]
    while q:
        x, y = q.popleft()
        for i in range(4):
            newx, newy = x + case[i][0], y + case[i][1]    
            # 범위 확인        
            if 0 <= newx < n and 0 <= newy < m and graph[newx][newy] == 0:
                # 일수 저장(1부터 시작)
                graph[newx][newy] = graph[x][y]+1
                q.append([newx, newy])

m, n = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]

q = deque()
for i in range(n):
    for j in range(m):
        # 익은 토마토가 있는 위치를 모두 큐에 먼저 넣음
        if graph[i][j] == 1:
            q.append([i,j])

# 익은 토마토 기준으로 탐색 시작
find()

res = 0
for i in range(n):
    for j in range(m):
        # 토마토가 모두 익지 못하는 상황일 때
        if graph[i][j] == 0:
            print(-1)
            exit()
        res = max(res, graph[i][j])
# 1부터 시작했으므로 -1
print(res-1)