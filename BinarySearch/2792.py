'''
보석 상자
'''

from sys import stdin

N, M = map(int, stdin.readline().split())
jewels = [int(stdin.readline()) for _ in range(M)]
start, end = 1, max(jewels)
res = 0

while start <= end:
    # 한 학생이 가져갈 수 있는 보석의 개수
    mid = (start + end) // 2
    # 학생 수
    cnt = 0

    for jewel in jewels:
        if jewel % mid == 0:
            cnt += jewel // mid
        else:
            cnt += jewel // mid + 1

    # N명보다 많은 사람이 보석 가져감
    # -> 한 명이 가져가는 보석 수 늘림
    if cnt > N:
        start = mid + 1
    else:
        end = mid - 1
        res = mid

print(res)
