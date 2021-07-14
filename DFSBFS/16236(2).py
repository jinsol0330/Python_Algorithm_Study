from collections import deque

n = int(input())
space = []
for i in range(n):
    space.append(list(map(int,input().split())))

case = [[-1, 0],[0, -1], [0, 1], [1, 0]]

shark_size = 2
fish_cnt = 0
eat_time = 0

def find_fish(x,y):
    res = []
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[x][y] = 1
    q = deque()
    q.append([x,y])
    while q:
        sx, sy = q.popleft()
        for i in range(4):
            newx = sx + case[i][0]
            newy = sy + case[i][1]
            # 범위내
            if 0<=newx<n and 0<=newy<n:
                # 이동가능
                if space[newx][newy] <= shark_size and visited[newx][newy] == 0:
                    # 먹기가능
                    if space[newx][newy] < shark_size and space[newx][newy] != 0:
                        res.append([newx, newy, visited[sx][sy]])
                    q.append([newx,newy])
                    visited[newx][newy] = visited[sx][sy] + 1
    if len(res) == 0:
        return -1, -1, -1
    else:
        res =  sorted(res, key = lambda x : (x[2],x[0],x[1]) )
        return res[0]


def eat_fish():
    global space, shark_size, fish_cnt, eat_time
    for i in range(n):
        for j in range(n):
            if space[i][j] == 9:
                sharkx, sharky, sec = find_fish(i,j)
                if sharkx == -1 and sharky == -1 and sec == -1:
                    return False
                else:
                    fish_cnt += 1
                    eat_time += sec
                    if shark_size == fish_cnt:
                        shark_size += 1
                        fish_cnt = 0
                    space[i][j] = 0
                    space[sharkx][sharky] = 9
                    return True

while True:
    if eat_fish():
        continue
    else:
        break

print(eat_time)