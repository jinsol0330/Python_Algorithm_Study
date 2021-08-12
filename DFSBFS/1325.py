'''
효율적인 해킹

해커 김지민은 잘 알려진 어느 회사를 해킹하려고 한다. 이 회사는 N개의 컴퓨터로 이루어져 있다. 
김지민은 귀찮기 때문에, 한 번의 해킹으로 여러 개의 컴퓨터를 해킹 할 수 있는 컴퓨터를 해킹하려고 한다.
이 회사의 컴퓨터는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있는데, 
A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다는 소리다.
이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때, 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 프로그램을 작성하시오.
'''

from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())

# 컴퓨터의 번호가 1~N 이므로
graph = [ [] for _ in range(N+1) ]

def find(x):   
    q = deque()
    q.append(x)
    visited = [0] * (N+1)
    visited[x] = 1
    cnt = 1
    while q:
        newx = q.popleft()
        for com in graph[newx]:
            if visited[com] == 0:
                visited[com] = 1
                q.append(com)
                cnt += 1
    return cnt

for _ in range(M):
    x, y = map(int, stdin.readline().split())
    # graph[x].append(y)
    graph[y].append(x)

res_list = []
max_tmp = -1e9
# 1번 컴퓨터부터 탐색 시작
for idx in range(1, N+1):
    res = find(idx)
    if res > max_tmp:
        # 컴퓨터 개수가 더 많다면, 그 컴퓨터 번호로 업데이트
        res_list = [idx]
        max_tmp = res
    elif res == max_tmp:
        # 컴퓨터 개수가 같다면, 뒤에 추가
        res_list.append(idx)
    else:
        continue

print(*res_list)
