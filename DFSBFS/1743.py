'''
음식물 피하기
'''

from sys import stdin
from collections import deque

def find(i,j):
    global n, m, graph
    case = [[-1,0],[1,0],[0,1],[0,-1]]
    q = deque()
    q.append([i,j])
    # 겹치게 하지 않기 위함
    graph[i][j] = 0
    # 쓰레기 크기
    res = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            newx, newy = x+case[i][0], y+case[i][1]
            if 0<= newx < n and 0<= newy < m:
                if graph[newx][newy] == 1:
                    q.append([newx,newy])
                    # 방문했으므로 다시 방문 하지 않게 하려고
                    graph[newx][newy] = 0
                    res += 1
    return res

n, m, k = map(int, stdin.readline().split())

graph = [[0 for _ in range(m)] for _ in range(n)]
for i in range(k):
    r, c = map(int, stdin.readline().split())
    # 입력받는 동시에 쓰레기 위치를 1로 바꿈
    graph[r-1][c-1] = 1

res_list = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            res_list.append(find(i,j))

print(max(res_list))