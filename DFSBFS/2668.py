'''
숫자고르기

방향이 있는 그래프(위->아래)로 보고 인접리스트로 입력을 받는다.
DFS로 탐색하면서 발생한 사이클을 다 더한다.

set()을 활용해 윗 칸 수들의 집합과 아래 칸 수들의 집합이 일치하는지 확인한다.
    -> 일치한다면 일치하는 집합(위든 아래든 아무거나)을 res 리스트에 추가한다.

마지막으로 res 리스트를 set으로 중복을 제거한 후 다시 리스트로 바꾸어 정렬한다. 
'''

from sys import stdin

N = int(stdin.readline())
graph = [[] for _ in range(N + 1)]

for idx in range(1, N + 1):
    graph[idx].append(int(stdin.readline()))
    

def find(num):
    if visited[num] == False:
        visited[num] = True
        for i in graph[num]:
            tmp_up.add(num)
            tmp_down.add(i)
            
            if tmp_up == tmp_down:
                res.extend(list(tmp_down))
                return
            
            find(i)
            
    visited[num] = False


res = [] 
for idx in range(1, N+1):
    visited = [False] * (N + 1)
    tmp_up = set()
    tmp_down = set()
    find(idx)
    
res = list(set(res))
res.sort()

print(len(res))
for i in res:
    print(i)