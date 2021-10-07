'''
입국심사
'''

from sys import stdin

M, N = map(int, stdin.readline().split())
times = [int(stdin.readline()) for t in range(M)]

# 최대 값 = 가장 오래 걸리는 시간 * 사람 수
start, end = 1, max(times) * N
res = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for time in times:
        cnt += mid // time

    # 만약 사람 수보다 크거나 같다면 시간을 줄여야 함
    if cnt >= N:
        end = mid - 1
        res = mid
    # 사람수보다 작다면 시간을 늘려야 함
    else:
        start = mid + 1


print(res)
