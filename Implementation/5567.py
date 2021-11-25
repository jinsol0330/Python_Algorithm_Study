'''
결혼식

상근이는 자신의 결혼식에 학교 동기 중 자신의 친구와 친구의 친구를 초대하기로 했다.
상근이의 동기는 모두 N명이고, 이 학생들의 학번은 모두 1부터 N까지이다.
상근이의 학번은 1이다.
상근이는 동기들의 친구 관계를 모두 조사한 리스트를 가지고 있다.
이 리스트를 바탕으로 결혼식에 초대할 사람의 수를 구하는 프로그램을 작성하시오.
'''

from sys import stdin
from collections import deque


def find(x):
    global cnt
    visited = [0] * (N+1)
    visited[x] = 1
    q = deque()
    # 위치와 카운트 변수 추가(친구와, 친구의 친구까지 총 2번만 실행하기 위함)
    q.append([x, 0])
    res = 0
    while q:
        value, cnt = q.popleft()
        for i in board[value]:
            # 2번까지(0,1)만 실행
            if visited[i] == 0 and cnt < 2:
                visited[i] = 1
                q.append([i, cnt+1])
                res += 1
    return res


# 동기 수
N = int(stdin.readline())
# 리스트 수
M = int(stdin.readline())
board = [[] for _ in range(N+1)]
cnt = 0
for i in range(M):
    a, b = map(int, stdin.readline().split())
    # 관계를 나타내는 리스트에 알맞게 추가
    board[a].append(b)
    board[b].append(a)

# 상근이(1)부터 실행
res = find(1)
print(res)
