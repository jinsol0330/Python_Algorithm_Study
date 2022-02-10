'''
겉넓이 구하기

위 아래는 N * M
둘레는 바로 옆 블록과의 높이 차이 계산
마주보는 경우 면적이 같기 때문에 하나만 구해서 X 2
'''

from sys import stdin

N, M = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]

res_by_row = 0
for row in range(N):
    for col in range(M):
        # 각 행의 가장 첫 블록인 경우 그대로 저장
        if col == 0:
            res_by_row += board[row][col]
        # 그 이후부터는 차이 계산
        else:
            if board[row][col] > board[row][col - 1]:
                res_by_row += board[row][col] - board[row][col - 1]

res_by_col = 0
for col in range(M):
    for row in range(N):
        if row == 0:
            res_by_col += board[row][col]
        else:
            if board[row][col] > board[row - 1][col]:
                res_by_col += board[row][col] - board[row - 1][col]
                

res = ((N * M) + res_by_row + res_by_col) * 2
print(res)

