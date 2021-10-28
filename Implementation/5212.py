'''
지구 온난화
'''

from sys import stdin
import copy

R, C = map(int, stdin.readline().split())

sea = []
for i in range(R):
    sea.append(list(stdin.readline()))
new_sea = copy.deepcopy(sea)

case = [[-1, 0], [1, 0], [0, 1], [0, -1]]

for x in range(R):
    for y in range(C):
        # 땅이라면
        if sea[x][y] == 'X':
            sea_count = 0
            for i in range(4):
                newx, newy = x+case[i][0], y+case[i][1]
                # 지도에 없는 곳, 지도의 범위를 벗어나는 칸은 모두 바다
                # '.' 이 있는 칸도 바다
                if newx < 0 or newx >= R or newy < 0 or newy >= C or sea[newx][newy] == '.':
                    sea_count += 1

            # 만약 세 칸 이상이 바다라면 땅을 바다로 바꿈
            if sea_count >= 3:
                new_sea[x][y] = '.'

start_row = 0
end_row = 0
start_col = 0
end_col = 0

for idx in range(R):
    if 'X' in new_sea[idx]:
        start_row = idx
        break

for idx in range(R-1, -1, -1):
    if 'X' in new_sea[idx]:
        end_row = idx
        break

# 리스트 행 열 뒤집기
tmp_sea = copy.deepcopy(new_sea)
tmp_sea = list(map(list, zip(*tmp_sea)))

for idx in range(C):
    if 'X' in tmp_sea[idx]:
        start_col = idx
        break

for idx in range(C-1, -1, -1):
    if 'X' in tmp_sea[idx]:
        end_col = idx
        break

for row in range(start_row, end_row+1):
    for col in range(start_col, end_col+1):
        print(new_sea[row][col], end='')
    print()
