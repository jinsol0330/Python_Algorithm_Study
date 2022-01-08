'''
A -> B
'''

from sys import stdin
from collections import deque


def find(A, B):
    q = deque()
    # A 값과 연산횟수(초기화 1)를 큐에 넣는다
    q.append([A, 1])
    while q:
        num, cnt = q.popleft()
        if num == B:
            return cnt
        # 2를 곱한다
        if num * 2 <= B:
            q.append([num * 2, cnt + 1])
        # 1을 수의 가장 오른쪽에 추가한다
        if int(str(num)+'1') <= B:
            q.append([int(str(num)+'1'), cnt + 1])
    
    return -1


A, B = map(int, stdin.readline().split())

print(find(A, B))