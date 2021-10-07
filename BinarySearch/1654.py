'''
랜선 자르기
'''

from sys import stdin

K, N = map(int, stdin.readline().split())
lans = [int(stdin.readline()) for _ in range(K)]

start, end = 1, max(lans)
res = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for l in lans:
        cnt += l // mid

    if cnt >= N:
        start = mid + 1
        res = mid
    else:
        end = mid - 1

print(res)