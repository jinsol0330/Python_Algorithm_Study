'''
간식 파티
'''

from sys import stdin

N  = int(stdin.readline())
dp_table = [0] * N

snacks = []
for _ in range(N):
    snacks.append(int(stdin.readline()))

for i in range(N):
    dp_table[i] = snacks[i] 
    for j in range(i):
        # 현재 먹으려는 간식이 이전에 먹었던 간식보다 평점이 높다면
        if snacks[i] > snacks[j]:
            # 현재 인덱스의 dp_table의 값과 새롭게 업데이트 될 값을 비교해 큰 값을 저장
            dp_table[i] = max(dp_table[i], dp_table[j] + snacks[i])
print(max(dp_table))