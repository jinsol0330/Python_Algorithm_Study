'''
배열 돌리기 1
'''

from sys import stdin


def rotate(start):

    top = board[start][start]
    left = board[N-start-1][start]
    bottom = board[N-start-1][M-start-1]
    right = board[start][M-start-1]

    # 위쪽
    for idx in range(start+1, M-start):
        board[start][idx-1] = board[start][idx]
    # 왼쪽
    for idx in range(N-start-1, start, -1):
        board[idx][start] = board[idx-1][start]
    # 아래쪽
    for idx in range(M-start-1, start+1, -1):
        board[N-start-1][idx] = board[N-start-1][idx-1]
    # 오른쪽
    for idx in range(start+1, N-start):
        board[idx-1][M-start-1] = board[idx][M-start-1]

    # 값 업데이트
    board[start+1][start] = top
    board[N-start-1][start+1] = left
    board[N-start-2][M-start-1] = bottom
    board[start][M-start-2] = right


N, M, R = map(int, stdin.readline().split())
board = [list(map(int, input().split())) for _ in range(N)]

for _ in range(R):
    # 사각형을 기준으로
    for idx in range(min(N, M) // 2):
        rotate(idx)

for row in range(N):
    for col in range(M):
        print(board[row][col], end=' ')
    print()

