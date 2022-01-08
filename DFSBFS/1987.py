'''
알파벳
'''

from sys import stdin
from collections import deque


R, C = map(int, stdin.readline().split())
board = [list(map(str, stdin.readline())) for _ in range(R)]
case = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def find(board):
    res = 1
    # 현재 위치, 지금까지 지나온 알파벳 저장
    q = set([(0, 0, board[0][0])])

    while q:
        x, y, check = q.pop()

        for i in range(4):
            newx, newy = x + case[i][0], y + case[i][1]
            if 0 <= newx < R and 0 <= newy < C and board[newx][newy] not in check:
                q.add((newx, newy, check + board[newx][newy]))
                res = max(res, len(check)+1)
    print(res)


find(board)
