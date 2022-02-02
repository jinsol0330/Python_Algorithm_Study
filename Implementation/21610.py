'''
마법사 상어와 비바라기
'''

from sys import stdin

N, M = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
move_info = [list(map(int, stdin.readline().split())) for _ in range(M)]

# 비바라기를 시전했을 때 구름의 처음 위치
# (N, 1), (N, 2), (N-1, 1), (N-1, 2)에서 인덱스를 고려
cloud_loc = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]

# 이동할 수 있는 방향(1~8번 순서대로)
directions = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]

for d, s in move_info:
    # step1 : 구름 이동 후 물의 양 1 증가
    for idx, cloud in enumerate(cloud_loc):
        x, y = cloud[0], cloud[1]
        cloud_loc[idx][0] = (x + directions[d-1][0] * s) % N
        cloud_loc[idx][1] = (y + directions[d-1][1] * s) % N
        
    # 뒤에 물의 양을 2 줄일 때 구름 위치를 제외하고 줄이기 위해 True로 변경
    visited = [[False] * N for _ in range(N)]
    for x, y in cloud_loc:
        # 구름이 있는 칸의 바구니에 저장된 물의 양 1 증가
        board[x][y] += 1
        visited[x][y] = True

    # step2 : 물복사버그 마법 시전
    # 현재 이동 후 구름의 위치가 저장되어있음
    for x, y in cloud_loc:
        cnt = 0
        # 대각선 방향으로 거리가 1칸
        case = [[-1, -1], [-1, 1], [1, 1], [1, -1]]
        for c in range(4):
            newx, newy = x + case[c][0], y + case[c][1]
            # 대각선 방향에 물이 있는 바구니의 수 만큼 물의 양 증가
            if 0 <= newx < N and 0<= newy < N and board[newx][newy] >= 1:
                cnt += 1
        board[x][y] += cnt
    print(board)
    new_cloud_loc = []
    # step3 : 물의 양이 2 이상인 칸에 구름이 생기고 물의 양 2만큼 줄이기
    for row in range(N):
        for col in range(N):
            if board[row][col] >= 2 and not visited[row][col]:
                new_cloud_loc.append([row, col])
                board[row][col] -= 2
                
    cloud_loc = new_cloud_loc


res = 0
for row in range(N):
    for col in range(N):
        res += board[row][col]
print(res)


