'''
퇴사

상담원으로 일하고 있는 백준이는 퇴사를 하려고 한다.
오늘부터 N+1일째 되는 날 퇴사를 하기 위해서, 남은 N일 동안 최대한 많은 상담을 하려고 한다.
상담을 하는데 필요한 기간은 1일보다 클 수 있기 때문에, 모든 상담을 할 수는 없다
상담을 적절히 했을 때, 백준이가 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하시오.
'''

n = int(input())

list_t = []
list_p = []
price = 0

# 값을 저장해 놓을 테이블 리스트 생성 
dp_table = [0] * n+1

for i in range(n):
    t, p = map(int, input().split())
    list_t.append(t)
    list_p.append(p)

for j in range(n-1,-1,-1):
    # 상담 가능 시간
    time = j + list_t[j]
    # 상담 가능 시간이 퇴사일보다 길다면, 상담 불가능
    if time > n:
        dp_table[j] = price
    else:
        dp_table[j] = max(list_p[j] + dp_table[j+list_t[j]], price)
        price = dp_table[j]

print(price)

