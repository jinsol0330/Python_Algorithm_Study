'''
아기상어(2)

N×M 크기의 공간에 아기 상어 여러 마리가 있다. 
공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 
한 칸에는 아기 상어가 최대 1마리 존재한다.
어떤 칸의 안전 거리는 그 칸과 가장 거리가 가까운 아기 상어와의 거리이다. 
두 칸의 거리는 하나의 칸에서 다른 칸으로 가기 위해서 지나야 하는 칸의 수이고, 
이동은 인접한 8방향(대각선 포함)이 가능하다.
안전 거리가 가장 큰 칸을 구해보자. 
'''

from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]

case = [[-1,0], [1,0], [0,-1], [0,1], [-1,-1], [-1,1], [1,-1], [1,1]]

INF = 1e9
visited = [[INF for _ in range(M)]for _ in range(N)]

for row in range(N):
    for col in range(M):
        if board[row][col] == 1:
            q = deque()
            # 큐에 x,y좌표 이동한 위치의 정보를 넣음
            q.append([row, col, 1])
            # 상어의 현재 위치는 안전거리를 굳이 구하지 않아도 되므로 0으로 표시
            # 이 좌표가 곧 거리가 됨 (d값이 들어가므로)
            visited[row][col] = 0
            while q:
                x, y, d = q.popleft() 
                for c in range(8):
                    newx = x + case[c][0]
                    newy = y + case[c][1]
                    # 범위 확인
                    if 0 <= newx < N and 0 <= newy < M:
                        if board[newx][newy] == 0 and visited[newx][newy] > d:
                            # 앞으로 탐색할 x,y좌표와 거리정보(이전보다 한 칸 +)를 큐에 저장
                            q.append([newx, newy, d + 1])
                            # 거리정보 d 저장
                            visited[newx][newy] = d
            # print(visited)
            
max_distance = 0
for row in range(N):
    for col in range(M):
        if visited[row][col] >= max_distance:
            max_distance = visited[row][col]
print(max_distance)

