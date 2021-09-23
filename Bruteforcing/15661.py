'''
링크와 스타트

1. 팀을 나눌 수 있는 모든 경우의 수를 조합을 이용해 구한다

2. 조합 하나하나를 보면서 나올 수 있는 모든 값을 구하고 최솟값을 갱신한다

'''

from sys import stdin
from itertools import combinations

N = int(stdin.readline())
S = [list(map(int, stdin.readline().split())) for _ in range(N)]

res = 1e9

# 팀 조합을 구하기 위한 리스트 생성
teams=[]
for team in range(N):
    teams.append(team)

# 나올 수 있는 팀 조합 구하기
for div_num in range(1, int(N / 2) + 1):
    min_value = 1e9
    comb_team = combinations(teams, div_num)

    for t in comb_team:
        team_start = list(t)
        '''
        리스트끼리 빼기 -> set 사용
        [0,1,2,3] 이라면
        [0], [1,2,3] 로 나누기
        '''
        team_link = list(set(teams) - set(team_start))

        team_start_power_sum = 0
        team_link_power_sum = 0

        for i in range(N - 1):
            for j in range(N - 1):
                try :
                    team_start_power = S[team_start[i]][team_start[j]]
                except :
                    team_start_power = 0
                try :
                    team_link_power = S[team_link[i]][team_link[j]]
                except:
                    team_link_power = 0

                team_start_power_sum += team_start_power
                team_link_power_sum += team_link_power
            
        difference = abs(team_start_power_sum - team_link_power_sum)
        min_value = min(difference, min_value)
    
    res = min(min_value, res)

print(res)