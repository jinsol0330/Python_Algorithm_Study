from sys import stdin
from collections import deque

def pour(x,y):
    if visited[x][y] == False:
        visited[x][y] = True
        q.append([x,y])

def find():
    global res_list
    while q:
        x, y = q.popleft()

        res = c-x-y
        if x == 0:
            res_list.append(res)
        water = min(x, b-y)
        pour(x-water, y+water)

        water = min(x, c-res)
        pour(x-water, y)

        water = min(y, a-x)
        pour(x+water, y-water)

        water = min(y, c-res)
        pour(x, y-water)

        water = min(res, b-y)
        pour(x, y+water)

        water = min(res, a-x)
        pour(x+water, y)

a,b,c = map(int, stdin.readline().split())

visited = [[False for _ in range(b+1)] for _ in range(a+1)]
visited[0][0] = True
res_list = []

q = deque()
q.append([0,0])

find()
res_list.sort()
for i in res_list:
    print(i, end=' ')