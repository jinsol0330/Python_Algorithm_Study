'''
부분수열의 합
'''

from sys import stdin
from itertools import combinations

N = int(stdin.readline())
S = list(map(int, stdin.readline().split()))

res = []
for i in range(1, N + 1):
    num_comb = combinations(S, i)

    '''
    print(*num_comb)

    ->  i = 1 일 때 (5,) (1,) (2,)
        i = 2 일 때 (5, 1) (5, 2) (1, 2)
        i = 3 일 때 (5, 1, 2)
    '''

    for num in num_comb:
        res.append(sum(num))
        
# 중복제거
res = set(res)

'''
N = 3 일 때 나올 수 있는 부분수열의 개수
->  2**3개
'''
for num in range(1, (2 ** N) + 1):
    if num not in res:
        print(num)
        break
