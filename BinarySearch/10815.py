'''
숫자 카드
'''

from sys import stdin

N = int(stdin.readline())
target_cards = list(map(int, stdin.readline().split()))
M = int(stdin.readline())
my_cards = list(map(int, stdin.readline().split()))

target_cards.sort()
res = []

for card in my_cards:
    flag = False
    start = 0
    end = len(target_cards) - 1

    while start <= end:
        mid = (start + end) // 2
        # 비교하려는 카드 값이 중간값보다 크다면
        if card > target_cards[mid]:
            # 시작점 업데이트
            start = mid + 1
        # 비교하려는 카드 값이 중간값보다 작다면
        elif card < target_cards[mid]:
            # 끝 점 업데이트
            end = mid - 1
        # 상근이가 카드를 가지고 있다면 1 출력
        else:
            res.append(1)
            flag = True
            break
    # 상근이가 카드를 가지고 있지 않으면 0 출력
    if not flag:
        res.append(0)

print(*res)
