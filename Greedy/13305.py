'''
주유소
'''

from sys import stdin

n = int(stdin.readline())
road = list(map(int, stdin.readline().split()))
price = list(map(int, stdin.readline().split()))
res = 0
tmp = price[0]
for i in range(len(road)):
    if price[i] < tmp:
        tmp = price[i]    
    res += tmp*road[i]
print(res)