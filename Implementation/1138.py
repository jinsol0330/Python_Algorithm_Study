'''
한 줄로 서기

N명의 사람들은 매일 아침 한 줄로 선다. 
이 사람들은 자리를 마음대로 서지 못하고 오민식의 지시대로 선다.

어느 날 사람들은 오민식이 사람들이 줄 서는 위치를 기록해 놓는다는 것을 알았다. 
그리고 아침에 자기가 기록해 놓은 것과 사람들이 줄을 선 위치가 맞는지 확인한다.

사람들은 자기보다 큰 사람이 왼쪽에 몇 명 있었는지만을 기억한다. 
N명의 사람이 있고, 사람들의 키는 1부터 N까지 모두 다르다.

각 사람들이 기억하는 정보가 주어질 때, 줄을 어떻게 서야 하는지 출력하는 프로그램을 작성하시오.
'''


# 키가 i 일 때
# 1. 왼쪽에 나보다 큰사람이 0인 경우 -> 리스트의 왼쪽부터 봤을때 가장 처음 0의 자리에 i를 넣는다.
# 2. 왼쪽에 나보다 큰사람이 j명인 경우 -> 리스트의 왼쪽부터 0 을 j만큼 지나친 이후의 0의 자리에 i를 넣는다.
n = int(input())
lines = list(map(int, input().split()))
res = [0] * n
cnt = 0

for i in range(n):
    # 왼쪽에 나보다 큰 사람이 없는 경우
    if lines[i] == 0:
        for j in range(n):
            if res[j] == 0:
                res[j] = i+1
                break
    # 왼쪽에 나보다 큰 사람이 있는 경우
    else:
        # 큰 사람이 cnt만큼 있음
        cnt = lines[i]
        for j in range(n):
            if res[j] == 0 and cnt != 0:
                cnt -= 1
            elif res[j] == 0 and cnt == 0:
                res[j] = i+1
                break
            else:
                continue
    # print(*res)
print(*res)
                

