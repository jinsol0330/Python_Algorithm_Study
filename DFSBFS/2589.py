'''
보물섬
'''

from sys import stdin
from collections import deque


def find(x, y, time):
    q = deque()
    q.append([x, y, time])
    visited[x][y] = 1
    while q:
        x, y, time = q.popleft()
        for c in range(4):
            newx, newy = x + case[c][0], y + case[c][1]
            if 0 <= newx < N and 0 <= newy < M and visited[newx][newy] == 0 and board[newx][newy] == 'L':
                visited[newx][newy] = 1
                q.append([newx, newy, time+1])
    return time


N, M = map(int, stdin.readline().split())
board = [list(stdin.readline()) for _ in range(N)]


case = [[1, 0], [-1, 0], [0, 1], [0, -1]]
res = 0

for row in range(N):
    for col in range(M):
        if board[row][col] == 'L':
            visited = [[0] * M for _ in range(N)]
            res = max(res, find(row, col, 0))

print(res)
