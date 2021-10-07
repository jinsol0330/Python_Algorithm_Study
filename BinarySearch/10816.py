'''
숫자 카드 2
'''

from sys import stdin

N = int(stdin.readline())
target_cards = list(map(int, stdin.readline().split()))
M = int(stdin.readline())
my_cards = list(map(int, stdin.readline().split()))

target_cards.sort()
card_info = {}

for card in target_cards:
    if card in card_info:
        card_info[card] += 1
    else:
        card_info[card] = 1

for card in my_cards:
    if not card in card_info.keys():
        print(0, end=" ")
    else:
        print(card_info[card], end=" ")

