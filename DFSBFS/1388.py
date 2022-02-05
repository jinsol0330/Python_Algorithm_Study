'''
바닥 장식
'''

from sys import stdin

N, M = map(int, stdin.readline().split())
board = [list(stdin.readline()) for _ in range(N)]

res = 0
cnt_row = 0
cnt_col = 0

# 행 체크
for i in range(N):
    for j in range(M):
        # 가로 방향으로 '-' 확인
        if board[i][j] == '-': 
            cnt_row +=1
        # 만약 '|' 를 만났다면 결과값 카운트
        elif board[i][j] == '|' and cnt_row != 0: 
            res += 1
            # 초기화
            cnt_row = 0
            
    # 가로 방향 끝까지 왔을 때 한번 더 체크
    if cnt_row > 0: 
        res += 1
        cnt_row = 0
        
# 열 체크
for i in range(M):
    for j in range(N):
        # 세로 방향으로 '|' 확인
        if board[j][i]=='|':
            cnt_col += 1
        # 만약 '-' 를 만났다면 결과값 카운트
        elif board[j][i] == '-' and cnt_col != 0:
            res += 1
            # 초기화
            cnt_col = 0
    
    # 세로 방향 끝까지 왔을 때 한번 더 체크
    if cnt_col > 0 :
        res += 1
        cnt_col = 0

print(res)