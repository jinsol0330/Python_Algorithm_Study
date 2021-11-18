'''
인구 이동
'''

from sys import stdin
from collections import deque

N, L, R = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]


def find(r, c):
    q = deque()
    q.append([r, c])
    visited[r][c] = True
    union = [board[r][c]]

    case = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    while q:
        x, y = q.popleft()

        for i in range(4):
            newx, newy = x+case[i][0], y+case[i][1]
            # 범위 확인 & 방문 확인
            if 0 <= newx < N and 0 <= newy < N and visited[newx][newy] == False:
                # 인구차이까지 만족하면, 국경선 열기
                if L <= abs(board[x][y] - board[newx][newy]) <= R:
                    union.append(board[newx][newy])
                    visited[newx][newy] = True
                    q.append([newx, newy])

    # 국경선을 열 수 없다면 인구이동 못함
    if len(union) == 1:
        return 0

    # 국경선을 다 열었으니 인구이동
    sum_num = 0
    for n in union:
        sum_num += n

    num = sum_num // len(union)

    for i in range(N):
        for j in range(N):
            board[i][j] = num

    return 1

# 인구이동이 며칠 동안 발생하는지
res = 0
while True:
    # 땅 크기만큼 생성
    visited = [[False] * N for _ in range(N)]
    # 인구이동이 가능한지 -> 가능하면1, 아니면0
    move_cnt = 0
    for row in range(N):
        for col in range(N):
            if not visited[row][col]:
                move_cnt += find(row, col)

    # 인구 이동을 할 수 없다면
    if move_cnt == 0:
        break

    res += 1

print(res)
