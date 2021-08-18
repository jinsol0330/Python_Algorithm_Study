'''
데스 나이트

게임을 좋아하는 큐브러버는 체스에서 사용할 새로운 말 "데스 나이트"를 만들었다. 
데스 나이트가 있는 곳이 (r, c)라면, 
(r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1)로 이동할 수 있다.
크기가 N×N인 체스판과 두 칸 (r1, c1), (r2, c2)가 주어진다. 
데스 나이트가 (r1, c1)에서 (r2, c2)로 이동하는 최소 이동 횟수를 구해보자. 
체스판의 행과 열은 0번부터 시작한다.
데스 나이트는 체스판 밖으로 벗어날 수 없다.
'''

from sys import stdin
from collections import deque

def find(r1, c1, r2, c2):
    q = deque()
    q.append([r1, c1])
    graph[r1][c1] = 1
    case = [[-2,-1], [-2,1], [0,-2], [0,2], [2,-1], [2,1]]
    while q:
        r, c = q.popleft()
        if r == r2 and c == c2:
            # 처음을 1로 시작했기 때문에 -1
            return graph[r][c] - 1
        for idx in range(6):
            newr, newc = r + case[idx][0],  c + case[idx][1]
            # 범위확인
            if 0 <= newr < N and 0 <= newc < N and graph[newr][newc] == 0:
                q.append([newr, newc])
                graph[newr][newc] = graph[r][c] + 1
    return -1

N = int(stdin.readline())
r1, c1, r2, c2 = list(map(int, stdin.readline().split()))
graph = [[0] * N for _ in range(N)]
res = find(r1, c1, r2, c2)
print(res)