'''
치즈
'''

from sys import stdin
from collections import deque

def find():
    global n, m, graph, cheese_list
    case = [[-1,0],[1,0],[0,-1],[0,1]]
    visited = [[0]*m for _ in range(n)]
    q = deque()
    q.append([0,0])
    visited[0][0] = 1
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            newx,newy = x+case[i][0], y+case[i][1]
            # 범위확인
            if 0<=newx<n and 0<=newy<m and visited[newx][newy] == 0:
                visited[newx][newy] = 1
                if graph[newx][newy] == 0:
                    q.append([newx,newy])
                # 치즈가 있는 자리라면
                elif graph[newx][newy] ==1:
                    graph[newx][newy] = 0
                    # 치즈 개수 카운트
                    cnt += 1
    cheese_list.append(cnt)
    return cnt

n, m = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
# 시간
t = 0
# 치즈 개수 카운트
cheese_list = []

while True:
    t += 1
    res = find()
    if res == 0:
        break

print(t-1)
print(cheese_list[-2])






# n = 13
# m = 12
# graph =[[0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,1,1,0,0,0],
#         [0,1,1,1,0,0,0,1,1,0,0,0],
#         [0,1,1,1,1,1,1,0,0,0,0,0],
#         [0,1,1,1,1,1,0,1,1,0,0,0],
#         [0,1,1,1,1,0,0,1,1,0,0,0],
#         [0,0,1,1,0,0,0,1,1,0,0,0],
#         [0,0,1,1,1,1,1,1,1,0,0,0],
#         [0,0,1,1,1,1,1,1,1,0,0,0],
#         [0,0,1,1,1,1,1,1,1,0,0,0],
#         [0,0,1,1,1,1,1,1,1,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0]
#         ]

