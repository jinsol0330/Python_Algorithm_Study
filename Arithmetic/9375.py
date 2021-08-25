'''
패션왕 신해빈

해빈이는 패션에 매우 민감해서 한번 입었던 옷들의 조합을 절대 다시 입지 않는다. 
예를 들어 오늘 해빈이가 안경, 코트, 상의, 신발을 입었다면, 다음날은 바지를 추가로 입거나 안경대신 렌즈를 착용하거나 해야한다. 
해빈이가 가진 의상들이 주어졌을때 과연 해빈이는 알몸이 아닌 상태로 며칠동안 밖에 돌아다닐 수 있을까?
'''

from sys import stdin

testcase = int(stdin.readline())

for t in range(testcase):
    N = int(stdin.readline())
    res_dict = {}
    # 옷의 종류를 key값으로 받고 딕셔너리에 key값이 없으면 value를 1로 준다. 존재하면 +1
    for i in range(N):
        value, kind = stdin.readline().split()
        if kind not in res_dict:
            res_dict[kind] = 1
        else:
            res_dict[kind] += 1

    res = 1
    # 같은 종류의 개수+1를해서 모두 곱하고 아무것도 선택하지 않은경우 1을 빼준다.
    for k, v in res_dict.items():
        res *= (v+1)

    print(res-1)