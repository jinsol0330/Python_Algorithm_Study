'''
N과 M(5)
'''

from sys import stdin


def find():
    if len(res) == M:
        print(' '.join(map(str, res)))
        return

    # 길이가 M이 아닌 경우
    for i in range(N):
        if not visited[i]:
            res.append(nums[i])
            visited[i] = True
            find()
            # 1 7 이면 7을 pop하고 그 자리를 다시 False 로
            res.pop()
            visited[i] = False


N, M = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))
nums.sort()
visited = [False] * N
res = []
find()
