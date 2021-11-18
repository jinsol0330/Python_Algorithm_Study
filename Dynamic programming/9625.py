'''
BABBA
'''

from sys import stdin

k = int(stdin.readline())
dp_table = [0]*(k+1)
dp_table[1] = 1

for i in range(2, k+1):
    dp_table[i] = dp_table[i-1] + dp_table[i-2]
print(dp_table[k-1], dp_table[k])
