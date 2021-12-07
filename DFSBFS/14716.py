'''
현수막

ANT가 처음 알고리즘 대회를 개최하게 되면서 현수막을 내걸었다.
저번 학기 영상처리 수업을 듣고 배웠던 지식을 최대한 응용 해보고 싶은 혁진이는 이 현수막에서 글자가 몇 개인지 알아보는 프로그램을 만들려 한다.
혁진이는 우선 현수막에서 글자인 부분은 1, 글자가 아닌 부분은 0으로 바꾸는 필터를 적용하여 값을 만드는데 성공했다.
그런데 혁진이는 이 값을 바탕으로 글자인 부분 1이 상, 하, 좌, 우, 대각선으로 인접하여 서로 연결되어 있다면 한 개의 글자라고 생각만 하였다.
혁진이가 필터를 적용하여 만든 값이 입력으로 주어졌을 때, 혁진이의 생각대로 프로그램을 구현하면 글자의 개수가 몇 개인지 출력하여라.
'''

from sys import stdin
from collections import deque


def find(i, j, visited):
    case = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], \
        [-1, 1], [1, -1], [1, 1]]
    q = deque()
    q.append([i, j])
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for i in range(8):
            newx, newy = x + case[i][0], y + case[i][1]
            if 0 <= newx < M and 0 <= newy < N:
                if board[newx][newy] and not visited[newx][newy]:
                    visited[newx][newy] = 1
                    q.append([newx, newy])


M, N = list(map(int, stdin.readline().split()))
board = [list(map(int, stdin.readline().split())) for _ in range(M)]

res = 0
visited = [[0] * N for _ in range(M)]
for i in range(M):
    for j in range(N):
        if not visited[i][j] and board[i][j]:
            find(i, j, visited)
            res += 1

print(res)
