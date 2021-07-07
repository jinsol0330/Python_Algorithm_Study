'''
빗물

2차원 세계에 블록이 쌓여있다. 비가 오면 블록 사이에 빗물이 고인다.
비는 충분히 많이 온다. 고이는 빗물의 총량은 얼마일까?
'''

h, w = map(int,input().split())
blocks = list(map(int, input().split()))
h_max = 0

# 가장 큰 높이를 가진 블럭을 구함
for i in range(len(blocks)):
    if h_max < blocks[i]:
        h_max = blocks[i]
        h_idx = i

# 오른쪽 구역
res = 0
val = 0
for i in range(h_idx+1):
    if val < blocks[i]:
        val = blocks[i]
    res += val

# 왼쪽 구역
val = 0
for i in range(w-1, h_idx, -1):
    if val < blocks[i]:
        val = blocks[i]
    res += val
    
print(res-sum(blocks))

