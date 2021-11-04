'''
그림
'''

from sys import stdin
from collections import deque

N, M = list(map(int, stdin.readline().split()))
board = [list(map(int, stdin.readline().split())) for _ in range(N)]

case = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def find(i, j):
    tmp = 1
    q = deque()
    q.append([i, j])
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for c in range(4):
            newx, newy = x + case[c][0], y + case[c][1]
            if 0 <= newx < N and 0 <= newy < M and board[newx][newy] and visited[newx][newy] == 0:
                tmp += 1
                visited[newx][newy] = 1
                q.append([newx, newy])
    return tmp


picture_cnt = 0
picture_size = 0
tmp = 0
visited = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and board[i][j] == 1:
            tmp = find(i, j)
            picture_size = max(picture_size, tmp)
            picture_cnt += 1

print(picture_cnt)
print(picture_size)
