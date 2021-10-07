'''
과자 나눠주기
'''

from sys import stdin

M, N = map(int, stdin.readline().split())
snacks_length = list(map(int, stdin.readline().split()))

start, end = 1, max(snacks_length)
res = 0

while start <= end:
    mid = (start + end) // 2
    # 나누어 줄 수 있는 과자의 개수
    cnt = 0

    for snack in snacks_length:
        cnt += snack // mid

    # 만약 나누어 줄 수 있는 과자의 개수가 사람수 보다 크거나 같다면
    if cnt >= M:
        # 시작점 업데이트(기준 값을 높여야함)
        res = mid
        start = mid + 1
    # 과자의 수가 작다면 끝점 업데이트(기준 값을 낮춰야함)
    else:
        end = mid - 1

print(res)
