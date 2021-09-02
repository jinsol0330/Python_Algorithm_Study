'''
트럭
'''

from sys import stdin
from collections import deque

N, W, L = map(int, stdin.readline().split())
trucks = list(map(int, stdin.readline().split()))

# 다리 위 트럭의 상태
bridge = [0] * W
# 현재 다리위 트럭의 무게
weight = 0
# 총 소요되는 시간
res = 0

while True:
    out = bridge.pop(0)    # 방금 다리를 건넌 트럭은 다리에서 제거해야한다.
    weight -= out    # 방금 다리 다리를 건넌 트럭의 무게를 weight에서 빼줘야 다음 트럭이 넘어 올 수 있다.
 
    if trucks:    # 넘어 올 트럭이 남아있을 때 
        if weight + trucks[0] <= L:    # 다리 하중을 견딜 수 있으면
            bridge.append(trucks[0])    # 다리를 건너려는 트럭
            weight += trucks[0]    # weight에 현재 다리를 건너려는 트럭 무게 추가
            trucks.pop(0)  
        else:    # 다리 하중을 견딜 수 없으면
            bridge.append(0)    # 0을 추가하여 다리위에 있는 트럭을 먼저 보낸다.
    res += 1    # 조건과 상관없이 시간은 흘러간다.
 
    if not bridge:    # 다리위에 트럭이 다 지나가면 반복문 종료
        break    
print(res)