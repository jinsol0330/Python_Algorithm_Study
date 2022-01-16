'''
도서관
'''

from sys import stdin

N, M = map(int, stdin.readline().split())

books_loc = list(map(int, stdin.readline().split()))

plus_loc = []
minus_loc = []

max_loc = 0

for loc in books_loc:
    if loc > 0:
        plus_loc.append(loc)
    else:
        minus_loc.append(loc)
    # 마지막으로 가져올 책
    if abs(loc) > abs(max_loc):
        max_loc = loc

# 양수는 내림차순, 음수는 오름차순 정렬
plus_loc.sort(reverse= True)
minus_loc.sort()

# 걸음 수
res = 0

# 양수 탐색
for loc in range(0, len(plus_loc), M):
    if plus_loc[loc] != max_loc:
        res += plus_loc[loc]

# 음수 탐색
for loc in range(0, len(minus_loc), M):
    if minus_loc[loc] != max_loc:
        res += abs(minus_loc[loc])
        
# 왕복 걸음 수 고려
res *= 2
# 제일 멀리 있는 책
res += abs(max_loc)

print(res)
