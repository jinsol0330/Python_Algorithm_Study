'''
용돈 관리
'''

from sys import stdin

N, M = map(int, stdin.readline().split())
money_list = [int(stdin.readline()) for _ in range(N)]

start = max(money_list)
end = sum(money_list)

while start <= end:
    mid = (start + end) // 2
    my_money = 0
    cnt = 1

    for money in money_list:
        my_money += money

        # 돈이 부족하다면 새롭게 인출
        if my_money > mid:
            cnt += 1
            my_money = money

    if cnt > M:
        start = mid + 1
    else:
        end = mid - 1
        res = mid

print(res)
