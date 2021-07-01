'''
근이는 카약 대회를 개최했다. 그런데, 갑자기 엄청난 강풍이 경기장에 불었고, 일부 카약이 부서졌다. 
다행히 일부 팀은 혹시 모를 사태에 대비해서 카약을 하나 더 경기장에 들고 왔다. 
카약은 매우 무겁고 운반하기 어렵다. 따라서, 자신의 바로 다음이나 전에 경기하는 팀에게만 카약을 빌려주려고 한다. 
즉, 팀 4는 여분의 카약을 3이나 5에게만 빌려줄 수 있다. 
또, 카약을 하나 더 가져온 팀의 카약이 손상되었다면, 여분의 카약으로 경기에 출전하게되고, 이 카약은 다른 팀에게 빌려줄 수 없다.
카약이 부서진 팀과 하나 더 가져온 팀이 주어진다. 카약을 적절히 빌렸을 때 출발하지 못하는 팀의 최솟값은 몇 팀인지 구하는 프로그램을 작성하시오.
'''

# 팀의 수 N, 카약이 손상된 팀의 수 S, 카약을 하나 더 가져온 팀의 수 R
n, s, r = map(int, input().split())

demaged = list(map(int,input().split()))
extra = list(map(int,input().split()))

# 카약 정보를 가지는 리스트 생성 후 1으로 초기화
list1 = [1] * n

# 손상된 카약을 가진 팀 = 0 
for i in demaged:
    list1[i-1] -= 1

# 여분의 카약을 가진 팀 = 2
for j in extra:
    list1[j-1] += 1

for k in range(len(list1)):
    # 손상된 카약을 가진 팀이라면
    if list1[k] == 0:
        # 첫번째 원소일때
        if k == 0:
            if list1[k+1] == 2:
                list1[k+1] = 1
                list1[k] = 1
        # 마지막 원소일때
        elif k == len(list1)-1:
            if list1[k-1] == 2:
                list1[k-1] = 1
                list1[k] = 1
        # 중간 원소일때
        else:
            if list1[k-1] == 2:
                list1[k-1] = 1
                list1[k] = 1
                continue              
            if list1[k+1] == 2:
                list1[k+1] = 1
                list1[k] = 1
                continue
    else:
        continue
print(list1.count(0))