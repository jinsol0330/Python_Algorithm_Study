'''
사탕 게임
'''

from sys import stdin

N = int(stdin.readline())
candy = [list(stdin.readline().rstrip()) for _ in range(N)]
res = 0


def find():
    global res
    for row in range(N):
        tmp = 1
        # 가로 방향
        for col in range(N-1):
            # 사탕 색이 같다면 사탕을 먹을 수 있음
            if candy[row][col] == candy[row][col+1]:
                tmp += 1
                res = max(res, tmp)
            # tmp를 다시 1로 초기화 시켜서 다음 비교가 가능하게 해줌
            else:
                tmp = 1
    for row in range(N):
        tmp = 1
        # 세로 방향
        for col in range(N-1):
            if candy[col][row] == candy[col+1][row]:
                tmp += 1
                res = max(res, tmp)
            else:
                tmp = 1


# 가로 방향으로 교환
for row in range(N):
    for col in range(N-1):
        candy[row][col], candy[row][col+1] = candy[row][col+1], candy[row][col]
        find()
        # 다시 원래대로 바꾸기
        candy[row][col], candy[row][col+1] = candy[row][col+1], candy[row][col]

# 세로 방향으로 교환
for row in range(N):
    for col in range(N-1):
        candy[col][row], candy[col+1][row] = candy[col+1][row], candy[col][row]
        find()
        # 다시 원래대로 바꾸기
        candy[col][row], candy[col+1][row] = candy[col+1][row], candy[col][row]

print(res)
