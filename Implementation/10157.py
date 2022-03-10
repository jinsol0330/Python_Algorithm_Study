'''
자리배정

-> 달팽이 모양으로 회전하는 알고리즘(?)
'''

from sys import stdin

C, R = map(int, stdin.readline().split())
K = int(stdin.readline())
seats = [[0 for _ in range(R + 1)] for _ in range(C + 1)]

case = [[1, 0], [0, 1], [-1, 0], [0,-1]]

if K > C * R:
    print(0)
else:
    r, c = 1, 1
    cnt = 1
    d = 0
    while cnt != K:
        seats[r][c] = cnt
        d = d % 4
        newr, newc = r + case[d][0], c + case[d][1]
        
        if 1 <= newr <= R and 1 <= newc <= C and not seats[newr][newc]:
            r, c = newr, newc
            cnt += 1
        else:
            d += 1
    
    print(c, r)