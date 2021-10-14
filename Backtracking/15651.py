'''
N과 M(3)
'''

from sys import stdin


def find():
    if len(res) == M:
        print(' '.join(map(str, res)))
        return

    # 길이가 M이 아닌 경우
    for i in range(1, N+1):
        res.append(i)
        find()
        res.pop()


N, M = map(int, stdin.readline().split())
res = []
find()
