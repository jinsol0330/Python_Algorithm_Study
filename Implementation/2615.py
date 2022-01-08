'''
오목
'''

from sys import stdin

board = [list(map(int, stdin.readline().split())) for _ in range(19)]
 
# 8가지 경우를 모두 볼 필요 없음    
# 아래, 오른쪽아래, 오른쪽, 오른쪽 위
case = [[1, 0], [1, 1], [0, 1], [-1, 1]]

def find():
    for x in range(19):
        for y in range(19):
            if board[x][y]:
                for c in range(4):
                    newx, newy = x + case[c][0], y + case[c][1]
                    cnt = 1
 
                    while 0 <= newx < 19 and 0 <= newy < 19 and board[x][y] == board[newx][newy]:
                        # 바둑알 개수 카운트
                        cnt += 1
 
                        if cnt == 5:
                            # 여섯개가 나란히 있는 지 판단 1. 마지막 바둑알 기준
                            if 0 <= newx + case[c][0] < 19 and 0 <= newy + case[c][1] < 19 and board[newx][newy] == board[newx + case[c][0]][newy + case[c][1]]:    
                                break
                            # 여섯개가 나란히 있는 지 판단 2. 처음 바둑알 기준
                            if 0 <= x - case[c][0] < 19 and 0 <= y - case[c][1] < 19 and board[x][y] == board[x - case[c][0]][y - case[c][1]]:   
                                break
                            # 오목이라면 색과 좌표를 반환
                            return board[x][y], x + 1, y + 1    
                        # 다음 탐색을 위한 좌표값 업데이트
                        newx += case[c][0]
                        newy += case[c][1]
    # 승부가 결정되지 않을 경우
    return 0, -1, -1    
 
res, x, y = find()

if res == 0:
    print(res)
else:
    print(res)
    print(x, y)