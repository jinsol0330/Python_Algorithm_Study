'''
회의실 배정

한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 
각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 
단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 
회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.
'''

from sys import stdin

N = int(stdin.readline())

meetings = [list(map(int, stdin.readline().split())) for _ in range(N)]
# 1번째 인덱스를 기준으로 오름차순 정렬
# 회의가 빨리 끝나야, 그 뒤에 올 수 있는 회의 개수가 많아질 것이기 때문
meetings.sort(key=lambda x:(x[1], x[0]))

res = 0
now = 0

for start, end in meetings:
    # 시작 시간과 종료 시간이 같을 수 있으므로 >=
    # 앞으로 시작될 회의 시간이 현재 시간보다 같거나 커야함
    if start >= now:
        res += 1
        # 회의가 끝난 시간을 현재 시간으로 업데이트
        now = end
print(res)

