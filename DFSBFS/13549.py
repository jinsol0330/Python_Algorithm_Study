'''
숨바꼭질(3)

수빈이는 동생과 숨바꼭질을 하고 있다. 
수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 
수빈이는 걷거나 순간이동을 할 수 있다. 
만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.
수빈이와 동생의 위치가 주어졌을 때, 
수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
'''

from collections import deque

def find(n, k):
    visited = [False] * 100001
    cnt = [-1] * 100001
    visited[n] = True
    cnt[n] = 0
    q = deque()
    q.append(n)
    while q:
        target = q.popleft()
        if target == k:
            return cnt[target]
        # 순간이동 하는 경우
        if 0 <= target*2 < 100001 and visited[target*2] == False:
            q.append(target*2)
            cnt[target*2] = cnt[target]
            visited[target*2] = True
        # 걷는경우(+1)
        if 0 <= target+1 < 100001 and visited[target+1] == False:
            q.append(target+1)
            cnt[target+1] = cnt[target]+1
            visited[target+1] = True
        # 걷는경우(-1)
        if 0 <= target-1 < 100001 and visited[target-1] == False:
            q.append(target-1)
            cnt[target-1] = cnt[target]+1
            visited[target-1] = True
        
n, k = map(int, input().split())
res = find(n, k)
print(res)