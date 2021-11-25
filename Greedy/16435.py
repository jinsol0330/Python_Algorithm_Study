'''
스네이크버드
'''

from sys import stdin

N, L = map(int, stdin.readline().split())
fruits = list(map(int, stdin.readline().split()))
fruits.sort()

for i in fruits:
    if i > L:
        break
    else:
        L += 1
print(L)
