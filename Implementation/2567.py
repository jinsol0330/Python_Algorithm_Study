'''
색종이

가로, 세로 길이를 거리 정보를 통해 하나하나 구하는 방법으로 접근했는데,
그럴 필요 없이 색종이가 위치하는 곳을 표시하고 그 면적의 크기를 구하면 되는 문제였다.
'''

from sys import stdin

N = int(stdin.readline())
papers = [list(map(int, stdin.readline().split())) for _ in range(N)]
board = [ [0 for _ in range(101)] for _ in range(101) ]

# 색종이가 있는 곳 1로 표시
for paper in papers:
    w, h = paper[0], paper[1]
    for i in range(w, w + 10):
        for j in range(h, h + 10):
            board[i][j] = 1 

case = [[-1, 0], [1, 0], [0, -1], [0, 1]]
res = 0
for row in range(1, 101):
    for col in range(1, 101):
        
        if board[row][col] == 0:
            continue
        
        # 색종이와 인접한 변(?)의 개수를 세기 위함
        cnt = 0
        for c in range(4):
            newx, newy = row + case[c][0], col + case[c][1]
            if board[newx][newy] == 1:
                cnt += 1
        
        # if cnt == 1:
        #     res += 3
        # elif cnt == 2:
        #     res += 2
        # else:
        #     res += 1
        
        
        if cnt == 2:
            res += 2
        # 여기서 else로 하면, 사방이 다 막혀있는 경우에도 +1을 하기 때문에 elif로 명확히 조건을 제시해야 한다.
        elif cnt == 3:
            res += 1
            
print(res)