'''
치킨배달
'''

from sys import stdin
from itertools import combinations

n, m = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]

home = []
chicken = []

# 집과 치킨집 위치 저장
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home.append([i,j])
        elif graph[i][j] == 2:
            chicken.append([i,j])

# 치킨집 개수 고르기
c = list(combinations(chicken,m))
res_list = [0] * len(c)

for i in home:
    for j in range(len(c)):
    # j = [[0,1],[3,0]]
        res = 1e9
        for k in c[j]:
        # k = [0,1]
            tmp = abs(i[0]-k[0]) + abs(i[1]-k[1])
            res = min(res,tmp)
        res_list[j] += res
# print(res_list)
print(min(res_list))

# 집(i,j) 치킨집(n, m)
# |i-n| + |j-m|