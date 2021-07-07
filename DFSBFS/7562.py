'''
나이트의 이동

체스판 위에 한 나이트가 놓여져 있다. 
나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 
나이트가 이동하려고 하는 칸이 주어진다. 
나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?
'''

from collections import deque

def bfs(start_x, start_y, end_x, end_y):
    q = deque()
    # 시작 위치는 이미 밟고 있으므로 1으로 설정
    graph[start_x][start_y] = 1
    q.append([start_x, start_y])

    # 큐가 빌 때 까지 실행
    while q:
        x, y = q.popleft()
        if x == end_x and y == end_y:
            return (graph[x][y]-1)

        for i in range(len(case)):
            newx = x+case[i][0]
            newy = y+case[i][1]
            # 체스판을 벗어나는지 아닌지 확인
            if (0 <= newx < chess_size) and (0 <= newy < chess_size):
                if graph[newx][newy] == 0:
                    # 그 전의 값에서 한번만 더 가면 되기 때문
                    q.append([newx, newy])
                    graph[newx][newy] = graph[x][y] + 1

test_case = int(input())
case = [[2,1],[1,2],[-1,2],[-2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]]

for i in range(test_case):
    chess_size = int(input())
    start_x, start_y = map(int,input().split())
    end_x, end_y = map(int,input().split())
    
    # 지나간 횟수를 체크하기 위함
    graph = [[0] * chess_size for _ in range(chess_size)]

    if start_x == end_x and start_y == end_y:
        print(0)
    else:
        print(bfs(start_x, start_y, end_x, end_y))