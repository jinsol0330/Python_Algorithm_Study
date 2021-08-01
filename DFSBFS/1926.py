'''
그림

어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 
단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 
가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 
그림의 넓이란 그림에 포함된 1의 개수이다.
'''

from sys import stdin
from collections import deque

n, m = list(map(int, stdin.readline().split()))
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]

case = [[-1,0], [1,0], [0,-1], [0,1]]

def find(i, j, visited):
    area = 1
    q = deque()
    q.append([i,j])
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            newx, newy = x + case[i][0], y + case[i][1]            
            if 0 <= newx < n and 0 <= newy < m:
                if graph[newx][newy] and not visited[newx][newy]:
                    area += 1
                    visited[newx][newy] = 1
                    q.append([newx, newy])
    return area

res = 0
res_list = [0]
visited = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j]:
            res_list.append(find(i, j, visited))
            res += 1

print(res)
print(max(res_list))