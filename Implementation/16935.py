'''
배열 돌리기 3
'''

from sys import stdin


# 1. 상하 반전 연산(행만 고려)
def rotate_1(N, M, board):
    res = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        res[i] = board[N-1-i]
    return res


# 2. 좌우 반전 연산(행 열 모두 고려)
def rotate_2(N, M, board):
    res = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            res[i][j] = board[i][M-1-j]
    return res


# 3. 오른쪽으로 90도 회전시키는 연산
def rotate_3(N, M, board):
    res = [[0 for _ in range(N)] for _ in range(M)]
    for i in range(M):
        for j in range(N):
            res[i][j] = board[N-1-j][i]
    return res


# 4. 왼쪽으로 90도 회전시키는 연산
def rotate_4(N, M, board):
    res = [[0 for _ in range(N)] for _ in range(M)]
    for i in range(M):
        for j in range(N):
            res[i][j] = board[j][M-1-i]
    return res


# 5. 4개의 그룹으로 나눈 뒤 시계방향으로 회전
def rotate_5(N, M, board):
    res = [[0 for _ in range(M)] for _ in range(N)]
    r = int(N / 2)
    c = int(M / 2)
    for i in range(N):
        for j in range(M):
            if (0 <= i < r and 0 <= j < c):
                res[i][j] = board[i + r][j]
            elif (0 <= i < r and j >= c):
                res[i][j] = board[i][j - c]
            elif (i >= r and j >= c):
                res[i][j] = board[i-r][j]
            elif (i >= r and 0 <= j < c):
                res[i][j] = board[i][j+c]
    return res


# 6. 4개의 그룹으로 나눈 뒤 반시계방향으로 회전
def rotate_6(N, M, board):
    res = [[0 for _ in range(M)] for _ in range(N)]
    r = int(N / 2)
    c = int(M / 2)
    for i in range(N):
        for j in range(M):
            if (0 <= i < r and 0 <= j < c):
                res[i][j] = board[i][j+c]
            elif (0 <= i < r and j >= c):
                res[i][j] = board[i+r][j]
            elif (i >= r and j >= c):
                res[i][j] = board[i][j-c]
            elif (i >= r and 0 <= j < c):
                res[i][j] = board[i-r][j]
    return res


N, M, R = map(int, stdin.readline().split())
board = [list(map(int, input().split())) for _ in range(N)]
rotate_info = list(map(int, stdin.readline().split()))

# 연산
for idx in rotate_info:
    if idx == 1:
        board = rotate_1(N, M, board)
    elif idx == 2:
        board = rotate_2(N, M, board)
    elif idx == 3:
        board = rotate_3(N, M, board)
        tmp = N  # 연산 후 바뀐 행과 열 값을 다시 원래대로 바꾸기
        N = M
        M = tmp
    elif idx == 4:
        board = rotate_4(N, M, board)
        tmp = N  # 연산 후 바뀐 행과 열 값을 다시 원래대로 바꾸기
        N = M
        M = tmp
    elif idx == 5:
        board = rotate_5(N, M, board)
    else:
        board = rotate_6(N, M, board)

for row in range(N):
    for col in range(M):
        print(board[row][col], end=' ')
    print()
