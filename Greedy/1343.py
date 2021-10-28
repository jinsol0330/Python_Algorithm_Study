'''
폴리오미노
'''

from sys import stdin

board = stdin.readline().rstrip()

idx = 0

while True:
    if idx >= len(board):
        break

    if board[idx:idx+4] == 'XXXX':
        # 인덱스 위치를 4칸 뒤로 변경
        idx += 4
        board = board.replace('X', 'A', 4)
    elif board[idx:idx+2] == 'XX':
        # 인덱스 위치를 2칸 뒤로 변경
        idx += 2
        board = board.replace('X', 'B', 2)
    elif board[idx] == '.':
        # 인덱스 위치를 1칸 뒤로 변경
        idx += 1
    else:
        board = -1
        break
print(board)
