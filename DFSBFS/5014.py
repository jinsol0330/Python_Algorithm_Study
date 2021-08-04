'''
스타트링크

강호는 코딩 교육을 하는 스타트업 스타트링크에 지원했다. 오늘은 강호의 면접날이다. 
하지만, 늦잠을 잔 강호는 스타트링크가 있는 건물에 늦게 도착하고 말았다.
스타트링크는 총 F층으로 이루어진 고층 건물에 사무실이 있고, 스타트링크가 있는 곳의 위치는 G층이다. 
강호가 지금 있는 곳은 S층이고, 이제 엘리베이터를 타고 G층으로 이동하려고 한다.
보통 엘리베이터에는 어떤 층으로 이동할 수 있는 버튼이 있지만, 강호가 탄 엘리베이터는 버튼이 2개밖에 없다. 
U버튼은 위로 U층을 가는 버튼, D버튼은 아래로 D층을 가는 버튼이다. 
(만약, U층 위, 또는 D층 아래에 해당하는 층이 없을 때는, 엘리베이터는 움직이지 않는다)
강호가 G층에 도착하려면, 버튼을 적어도 몇 번 눌러야 하는지 구하는 프로그램을 작성하시오. 
만약, 엘리베이터를 이용해서 G층에 갈 수 없다면, "use the stairs"를 출력한다.
'''

from sys import stdin
from collections import deque

def find(s,g):
    q = deque()
    q.append(s)
    # 현재 있는 위치에서는 버튼을 안 눌러도 되므로
    visited[s] = 0
    # 이동할 수 있는 경우
    case = [u, -d]
    while q:
        x = q.popleft()
        if x == g:
            return visited[x]
        for i in range(2):
            newx = x + case[i]
            if 0 < newx <= f and visited[newx] == -1:
                # 버튼을 한번 누름 (+1)
                visited[newx] = visited[x]+1
                q.append(newx)

    return 'use the stairs'

f, s, g, u, d = map(int, stdin.readline().split())
# 방문확인 겸 버튼 누른 횟수 알기 위한 용도
visited = [-1] * (f+1)

res = find(s,g)
print(res)