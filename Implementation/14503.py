'''
로봇 청소기
'''

from sys import stdin


def find(r, c, d):
    global res
    
    # 현재 좌표를 통해 청소할 수 있는 지 확인
    if board[r][c] == 0:
        board[r][c] = 2
        res += 1
        
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    for _ in range(4):
        # 왼쪽 방향으로 회전
        newd = (d + 3) % 4
        newr, newc = r + directions[newd][0], c + directions[newd][1] 
        
        # 왼쪽 방향으로 회전한 결과가 0이면 다음 좌표와 방향을 탐색
        if board[newr][newc] == 0:
            find(newr, newc, newd)
            return
        d = newd
        
    # 뒤로 이동
    newd = (d + 2) % 4
    newr, newc = r + directions[newd][0], c + directions[newd][1]
    
    # 뒤가 벽이면 바로 종료
    if board[newr][newc] == 1:
        return
    # 그렇지 않으면 방향을 유지한채로 다음 좌표와 방향 탐색
    find(newr, newc, d)


N, M = map(int, stdin.readline().split())
r, c, d = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]

res = 0
find(r, c, d)
print(res)