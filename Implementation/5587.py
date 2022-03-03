'''
카드 캡터 상근이
- 놓여진 카드가 없다면 원하는 카드를 낼 수 있다.
- 놓여진 카드가 있다면 마지막에 나온 카드보다 큰 숫자가 적힌 카드를 낼 수 있다.
- 낼 카드가 없는 경우 상대의 차례가 된다. 이때, 자리에 나와있는 카드는 없어진다.
- 둘 중 한 명이라도 카드를 모두 사용하면 게임이 종료된다.
- 게임 종료시 상대방이 가지고 있는 카드의 수를 점수로 획득한다.
'''

from sys import stdin

N = int(stdin.readline())

sg_card = []
gs_card = []

for _ in range(N):
    sg_card.append(int(stdin.readline()))

sg_card.sort()

for i in range(1, (2 * N) + 1):
    if (i not in sg_card):
        gs_card.append(i)

cardmax = 0

# True = 상근차례, False = 근상차례
turn = True

while (len(sg_card) != 0 and len(gs_card) != 0):

    if (turn == True):
        current_card = sg_card
    else:
        current_card = gs_card

    flag = False
    
    for i in range(len(current_card)):
        if (current_card[i] > cardmax):
            flag = True
            cardmax = current_card[i]
            del(current_card[i])
            break

    if not flag:
        cardmax = 0
    
    turn = not turn

print(len(gs_card))
print(len(sg_card))