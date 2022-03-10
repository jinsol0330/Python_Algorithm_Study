'''
침투

-> 맨 윗줄 상태만 일단 저장한 후 탐색
'''

from sys import stdin
from collections import deque

def find():
    while q:
        x, y = q.popleft()
        
        # pop한 행이 맨 마지막 행이라면, 침투될 수 있음
        if x == N - 1:
            print("YES")
            return 

        case = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for c in range(4):
            newx, newy = x + case[c][0], y + case[c][1]
            if 0 <= newx < N and 0 <= newy < M and board[newx][newy] == 0:
                q.append([newx, newy])
                board[newx][newy] = 2
            
    print("NO")

N, M = map(int, stdin.readline().split())
board =  [list(map(int, stdin.readline().rstrip())) for _ in range(N)]

q = deque()
for idx in range(M):
    if board[0][idx] == 0:
        q.append([0, idx])
        board[0][idx] = 2

find()
        