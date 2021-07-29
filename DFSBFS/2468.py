'''
안전 영역
'''

from collections import deque

n = int(input())
rain_graph = []

def find(i,j,rain,visited):
    global n
    # 위, 아래, 오른쪽, 왼쪽 이동
    case = [[-1,0],[1,0],[0,1],[0,-1]]
    q = deque()
    q.append([i,j])
    visited[i][j] == 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            newx, newy = x+case[i][0], y+case[i][1]
            # 범위 확인
            if 0<= newx < n and 0<= newy < n:
                if rain_graph[newx][newy] > rain and visited[newx][newy] == 0:
                    visited[newx][newy] = 1
                    q.append([newx,newy])


# 그래프 내에서 가장 높은 지역 찾기
max_value = 0
for i in range(n):
    # rain_graph.append(list(map(int, stdin.readline().split())))
    val = list(map(int,input().split()))
    rain_graph.append(val)
    max_value = max(max(val),max_value)

res_list = [1]

# 비가 올 경우 모두 탐색(1~최대높이)
for rain in range(1, max_value):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    res = 0
    for i in range(n):
        for j in range(n):
            # 비의 양보다 건물 높이가 높고, 아직 방문하지 않았다면(안전구역 이라면)
            if rain_graph[i][j] > rain and visited[i][j] == 0:
                find(i,j,rain,visited)
                res += 1
    res_list.append(res)

print(max(res_list))


