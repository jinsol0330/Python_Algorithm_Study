'''
로봇 청소기
'''

from sys import stdin

N, M = map(int, stdin.readline().split())
r, c, d = map(int, stdin.readline().split())
board = [list(stdin.readline().split()) for _ in range(N)]

# 0:북   1:동   2:남   3:서
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def find(r, c, d):
    # 현재 자리는 청소한 상태이므로
    res = 1
    while True:
        '''
        2번 
        -> 현재 위치에서 현재 방향을 기준으로 왼쪽부터 차례대로 탐색
        '''
        flag = False
        for i in range(4):
            # 왼쪽으로 회전
            d = (d + 3) % 4
            newr, newc = r + directions[i][0], c + directions[i][1]
            
            # 청소가 되어있지 않다면 1번으로 감
            if 0 <= newr < N and 0 <= newc < M and board[newr][newc] == 0:
                '''
                1번 
                -> 청소를 하고 결과값 +1
                '''
                board[newr][newc] = 2
                res += 1
                r, c = newr, newc
                flag = True
                break
                
        # 네 방향 모두 청소가 이미 되어있거나 벽인 경우
        if not flag:
            backr, backc = r - directions[d][0], c - directions[d][1]
            if 0 <= backr < N and 0 <= backc < M:
                # 후진했을 때에도 벽인 경우는 작동을 멈춤
                if board[backr][backc] == 1:
                    return res
                # 한칸 후진후 2번으로 돌아감
                else:
                    r, c = backr, backc


# 현재 위치는 청소할 필요가 없으므로
board[r][c] = 2
res = find(r, c, d)

print(res)