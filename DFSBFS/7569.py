'''
토마토
'''

from sys import stdin
from collections import deque

def find():
    # 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 
    case = [[-1,0,0], [1,0,0], [0,0,-1], [0,0,1], [0,-1,0], [0,1,0]]
    while q:
        z, x, y = q.popleft()
        for c in range(6):
            newz, newx, newy = z + case[c][0], x + case[c][1], y + case[c][2]    
            # 범위 확인        
            if 0 <= newz < H and 0 <= newx < N and 0 <= newy < M and graph[newz][newx][newy] == 0:
                # 일수 저장(1부터 시작)
                graph[newz][newx][newy] = graph[z][x][y]+1
                q.append([newz, newx, newy])

M, N, H = map(int, stdin.readline().split())
graph = [[] for _ in range(H)]
# 3차원 배열 입력받기
for h in range(H):
    for n in range(N):
        graph[h].append((list(map(int, stdin.readline().split()))))

q = deque()
for h in range(H):
    for n in range(N):
        for m in range(M):
            # 익은 토마토가 있는 위치를 모두 큐에 먼저 넣음
            if graph[h][n][m] == 1:
                q.append([h,n,m])

# 익은 토마토 기준으로 탐색 시작
find()

res = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            # 토마토가 모두 익지 못하는 상황일 때
            if graph[h][n][m] == 0:
                print(-1)
                exit()
            res = max(res, graph[h][n][m])
# 1부터 시작했으므로 -1
print(res-1)