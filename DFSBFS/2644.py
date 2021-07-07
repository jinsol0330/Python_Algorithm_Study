'''
촌수계산

우리 나라는 가족 혹은 친척들 사이의 관계를 촌수라는 단위로 표현하는 독특한 문화를 가지고 있다. 
이러한 촌수는 다음과 같은 방식으로 계산된다. 
기본적으로 부모와 자식 사이를 1촌으로 정의하고 이로부터 사람들 간의 촌수를 계산한다. 
예를 들면 나와 아버지, 아버지와 할아버지는 각각 1촌으로 나와 할아버지는 2촌이 되고, 
아버지 형제들과 할아버지는 1촌, 나와 아버지 형제들과는 3촌이 된다.
여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오.
'''

from collections import deque

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
graph = [ [] for _ in range(n+1) ]
visited = [ False for _ in range(n+1) ]

def bfs(p1,p2): 
    q = deque()
    q.append([p1,0])
    # 큐가 빌 때 까지 반복
    while q:
        val,cnt = q.popleft()
        # 타겟값이면 리턴
        if val == p2:
            return cnt
        if not visited[val]:
            visited[val] = True
            # 촌수가 같아야 하므로, 인접 노드를 알아보기 전에 카운트를 세어야 함
            cnt += 1
            # 해당 노드의 인접 노드를 하나씩 살펴봄
            for i in graph[val]:
                if not visited[i]:
                    q.append([i,cnt])
    return -1


for i in range(m):
    x, y = map(int, input().split())
    '''
    예) 1 3 을 입력하면, 1 노드에 3을 넣어주고, 3 노드에도 1을 넣어줌
    '''
    graph[x].append(y)
    graph[y].append(x)

print(bfs(p1,p2))
