'''
경쟁적 전염
'''

from sys import stdin
from collections import deque


def find(virus_board):
    q = deque(virus_board)

    while q:
        virus, x, y, time = q.popleft()

        if time == S:
            break

        case = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for i in range(4):
            newx, newy = x + case[i][0], y + case[i][1]

            if 0 <= newx < N and 0 <= newy < N and board[newx][newy] == 0:
                board[newx][newy] = virus
                q.append([virus, newx, newy, time+1])


N, K = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
S, X, Y = map(int, stdin.readline().split())
virus_board = []

for row in range(N):
    for col in range(N):
        if board[row][col] != 0:  # 바이러스가 존재하는 모든 칸의 정보를 virus_board 에 추가
            virus_board.append([board[row][col], row, col, 0])

virus_board.sort()  # 번호가 낮은 바이러스부터 탐색 시작
find(virus_board)

print(board[X-1][Y-1])
