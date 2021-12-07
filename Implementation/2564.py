'''
경비원
'''

from sys import stdin

W, H = map(int, stdin.readline().split())
store = int(stdin.readline())
store_locate = [list(map(int, stdin.readline().split())) for _ in range(store)]
my_locate = list(map(int, stdin.readline().split()))

res = 0

# 북쪽
if my_locate[0] == 1:
    for direction, distance in store_locate:
        if direction == 1:
            res += abs(my_locate[1] - distance)
        # 남쪽
        elif direction == 2:
            left = my_locate[1] + H + distance
            right = (W - my_locate[1]) + H + (W - distance)
            res += min(left, right)
        elif direction == 3:
            res += my_locate[1] + distance
        elif direction == 4:
            res += (W - my_locate[1]) + distance
# 남쪽
elif my_locate[0] == 2:
    for direction, distance in store_locate:
        # 북쪽
        if direction == 1:
            left = my_locate[1] + H + distance
            right = (W - my_locate[1]) + H + (W - distance)
            res += min(left, right)
        elif direction == 2:
            res += abs(my_locate[1] - distance)
        elif direction == 3:
            res += my_locate[1] + (H - distance)
        elif direction == 4:
            res += (W - my_locate[1]) + (H - distance)
# 서쪽
elif my_locate[0] == 3:
    for direction, distance in store_locate:
        if direction == 1:
            res += my_locate[1] + distance
        elif direction == 2:
            res += (H-my_locate[1]) + distance
        elif direction == 3:
            res += abs(my_locate[1] - distance)
        # 동쪽
        elif direction == 4:
            left = my_locate[1] + W + distance
            right = (H - my_locate[1]) + W + (H - distance)
            res += min(left, right)
# 동쪽
elif my_locate[0] == 4:
    for direction, distance in store_locate:
        if direction == 1:
            res += my_locate[1] + (W - distance)
        elif direction == 2:
            res += (H-my_locate[1]) + (W - distance)
        # 서쪽
        elif direction == 3:
            left = (H-my_locate[1]) + W + (H - distance)
            right = my_locate[1] + W + distance
            res += min(left, right)
        elif direction == 4:
            res += abs(my_locate[1] - distance)
# 출력
print(res)
