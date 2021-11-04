'''
제곱수의 합
'''

from sys import stdin

N = int(stdin.readline())
dp_table = [i for i in range(N+1)]

for i in range(1, N+1):
    j = 1
    while j*j <= i:
        if dp_table[i] > dp_table[i-j*j] + 1:
            dp_table[i] = dp_table[i-j*j] + 1
        j += 1
print(dp_table[N])
