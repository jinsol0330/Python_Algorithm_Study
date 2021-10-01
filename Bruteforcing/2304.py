'''
창고 다각형
'''

from sys import stdin

N = int(stdin.readline())
blocks = []

max_length = 0
max_height = 0

# 입력받는 동시에 가장 큰 높이를 가진 블럭을 구함
for i in range(N):
    L, H = map(int, stdin.readline().split())
    blocks.append([L, H])
    # 예제에서는 16
    if max_length < L:
        max_length = L
    if max_height < H:
        max_height = H
        max_idx = L

container = [0] * (max_length + 1)
for L, H in blocks:
    container[L] = H

res = 0
tmp = 0

for idx in range(max_idx + 1):
    if container[idx] > tmp:
        tmp = container[idx]
    res += tmp

tmp = 0
for idx in range(max_length, max_idx, -1):
    if container[idx] > tmp:
        tmp = container[idx]
    res += tmp

print(res)