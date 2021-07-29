'''
물통

각각 부피가 A, B, C(1≤A, B, C≤200) 리터인 세 개의 물통이 있다. 
처음에는 앞의 두 물통은 비어 있고, 세 번째 물통은 가득(C 리터) 차 있다. 
이제 어떤 물통에 들어있는 물을 다른 물통으로 쏟아 부을 수 있는데, 
이때에는 한 물통이 비거나, 다른 한 물통이 가득 찰 때까지 물을 부을 수 있다. 
이 과정에서 손실되는 물은 없다고 가정한다.
이와 같은 과정을 거치다보면 세 번째 물통(용량이 C인)에 담겨있는 물의 양이 변할 수도 있다. 
첫 번째 물통(용량이 A인)이 비어 있을 때, 세 번째 물통(용량이 C인)에 담겨있을 수 있는 물의 양을 모두 구해내는 프로그램을 작성하시오.
'''

from sys import stdin
from collections import deque

def pour(x,y):
    if visited[x][y] == False:
        visited[x][y] = True
        q.append([x,y])

def find():
    while q:
        x,y = q.popleft()
        # 물통 c에 남아있는 물의 양
        res = c-x-y

        # a물통이 비어있을 때 c물통에 남아있는 물의 양을 리스트에 저장
        if x == 0:
            res_list.append(res)

        '''
        ex) a->b물통으로 물을 옮기는 경우
            1. a가 가지고 있는 물을 모두 옮김
            2. b가 앞으로 가질 수 있는 물의 양 만큼만 받음
        이 두 경우 중, 더 작은 값을 옮길 양으로 정함
            : a가 가지고 있는 물의 양이 b가 받을 수 있는 양보다 크면 안되므로 
        '''
        # a물통에서 b물통
        water = min(x, b-y)
        pour(x-water, y+water)
        # a물통에서 c물통
        water = min(x, c-res)
        pour(x - water, y)
        # b물통에서 a물통
        water = min(y, a-x)
        pour(x + water, y-water)
        # b물통에서 c물통
        water = min(y, c-res)
        pour(x, y-water)
        # c물통에서 a물통
        water = min(res, a-x)
        pour(x+water, y)
        # c물통에서 b물통
        water = min(res, b-y)
        pour(x, y+water)

a,b,c = map(int, stdin.readline().split())

visited = [[False for _ in range(b+1)] for _ in range(a+1)]
visited[0][0] = True

q = deque()
# 물통 a,b에 들어있는 물의 양(물통 a,b는 비어있는 상태로 시작)
q.append([0,0])

res_list = []
# 탐색시작
find()

# 오름차순 정렬
res_list.sort()
for i in res_list:
    print(i, end=' ')