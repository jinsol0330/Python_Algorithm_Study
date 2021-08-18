'''
숫자 정사각형

N*M크기의 직사각형이 있다. 각 칸은 한 자리 숫자가 적혀 있다. 
이 직사각형에서 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형을 찾는 프로그램을 작성하시오. 
이때, 정사각형은 행 또는 열에 평행해야 한다.
'''

from sys import stdin

N, M = map(int, stdin.readline().split())
board = []    
for _ in range(N):
    b = list(map(int, stdin.readline().rstrip()))
    board.append(b)

# 가장 작은 정사각형 값은 1이므로 1로 초기화
res = 1
for row in range(N-1):
    for col in range(M-1):
        # 정사각형 크기를 조절
        num = 1
        while True: 
            # 범위를 벗어날 때 
            if (row+num) == N or (col+num) == M:
                break
            # 각 꼭짓점 숫자 확인
            if board[row][col] == board[row+num][col] and board[row][col] == board[row][col+num] and board[row][col] == board[row+num][col+num]:
                res = max(res, (num+1)*(num+1))
                # print(res)
            num += 1
print(res)

        
