'''
양
'''

from collections import deque
from sys import stdin


def find(i, j):
    global sheep, wolf
    q = deque()
    visited[i][j] = 1
    q.append([i, j])

    while q:
        x, y = q.popleft()

        if board[x][y] == 'o':
            sheep += 1
        elif board[x][y] == 'v':
            wolf += 1
        board[x][y] = '.'

        for c in range(4):
            newx, newy = x + case[c][0], y + case[c][1]
            if 0 <= newx < R and 0 <= newy < C and board[newx][newy] != '#' and visited[newx][newy] == 0:
                q.append([newx, newy])
                visited[newx][newy] = 1


R, C = map(int, stdin.readline().split())
board = []
res = [0, 0]
visited = [[0] * C for _ in range(R)]
case = [[-1, 0], [1, 0], [0, -1], [0, 1]]

total_sheep = 0
total_wolf = 0

for _ in range(R):
    board.append(list(stdin.readline().rstrip()))

for i in range(R):
    for j in range(C):
        if board[i][j] == 'o' or board[i][j] == 'v':
            sheep = 0
            wolf = 0
            find(i, j)
            # 늑대의 수가 양의 수보다 크다면
            if wolf >= sheep:
                # 양은 다 잡아먹힘
                sheep = 0
            else:
                # 그렇지 않다면 양이 늑대를 이김
                wolf = 0

            total_sheep += sheep
            total_wolf += wolf
print(total_sheep, total_wolf)
