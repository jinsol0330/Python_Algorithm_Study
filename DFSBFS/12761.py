'''
돌다리

동규와 주미는 일직선 상의 돌 다리 위에있다. 
돌의 번호는 0 부터 100,000 까지 존재하고 동규는 번 돌 위에, 주미는 번 돌 위에 위치하고 있다. 
동규는 주미가 너무 보고싶기 때문에 최대한 빨리 주미에게 가기 위해 A,B만큼의 힘을 가진 스카이 콩콩을 가져왔다. 
동규가 정한 다리를 건너는 규칙은 턴 방식인데, 한 턴에 이동할 수 있는 거리는 이러하다. 
현 위치에서 +1칸, -1칸을 이동할 수 있고, 스카이 콩콩을 이용해 현 위치에서 A나 B만큼 좌우로 점프할 수 있으며, 
순간적으로 힘을 모아 현 위치의 A배나 B배의 위치로 이동을 할 수 있다. 
예를 들어 지금 동규가 7번 돌 위에 있고 스카이 콩콩의 힘이 8이면 그냥 점프를 해서 15번 돌에 갈 수도 있고, 순간적으로 힘을 모아 56번 돌에 갈 수도 있다는 것이다. 주어진 8가지의 방법 중 적절한 방법을 골라서 최대한 빨리 동규가 주미를 만날 수 있게 도와주자. 
'''

from collections import deque

def find(n):
    cnt = [-1] * 100001 
    q = deque()
    q.append(n)
    cnt[n] = 0
    while q:
        target = q.popleft()
        for i in [target-1, target+1, target+a, target-a, target+b, target-b, target*a, target*b]:
            if (0 <= i < 100001) and cnt[i] == -1:
                q.append(i)
                cnt[i] = cnt[target]+1
                if i==m:
                    return cnt[i]
a, b, n, m = map(int, input().split())

res = find(n)
print(res)