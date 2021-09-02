'''
경비원
'''

from sys import stdin

w, h = map(int, stdin.readline().split())
store = int(stdin.readline())
store_locate = [list(map(int, stdin.readline().split())) for _ in range(store)]
my_locate = list(map(int, stdin.readline().split()))

res = 0 

# 북쪽
if my_locate[0] == 1: 
    for direction, distance in store_locate:
        if direction == 1:
            res += abs(my_locate[1]-distance)
        elif direction == 2:
            left = my_locate[1] + h + distance
            right = (w-my_locate[1]) + h + (w-distance)
            res += min(left, right)
        elif direction == 3:
            res += my_locate[1] + distance
        elif direction == 4:
            res += (w - my_locate[1]) + distance
# 남쪽
elif my_locate[0] == 2: 
    for direction, distance in store_locate:
        if direction == 1:
            left = my_locate[1] + h + distance
            right = (w-my_locate[1]) + h + (w-distance)
            res += min(left, right)
        elif direction == 2:
            res += abs(my_locate[1]-distance)
        elif direction == 3:
            res += my_locate[1] + (h-distance)
        elif direction == 4:
            res += (w - my_locate[1]) + (h-distance)
# 서쪽
elif my_locate[0] == 3: 
    for direction, distance in store_locate:
        if direction == 1:
            res += my_locate[1] + distance
        elif direction == 2:
            res += (h-my_locate[1]) + distance
        elif direction == 3:
            res += abs(my_locate[1]-distance)
        elif direction == 4:
            left = my_locate[1] + w + distance
            right = (h - my_locate[1]) + w + (h-distance)
            res += min(left, right)
# 동쪽
elif my_locate[0] == 4:
    for direction, distance in store_locate:
        if direction == 1:
            res += my_locate[1] + (w-distance)
        elif direction == 2:
            res += (h-my_locate[1]) + (w-distance)
        elif direction == 3:
            left = (h-my_locate[1]) + w + (h-distance)
            right = my_locate[1] + w + distance
            res += min(left, right)
        elif direction == 4:
            res += abs(my_locate[1]-distance)
# 출력
print(res)