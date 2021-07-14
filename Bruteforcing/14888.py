'''
연산자 끼워넣기

N개의 수로 이루어진 수열 A1, A2, ..., AN이 주어진다. 
또, 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어진다. 
연산자는 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)으로만 이루어져 있다.
우리는 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있다. 
이때, 주어진 수의 순서를 바꾸면 안 된다.
예를 들어, 6개의 수로 이루어진 수열이 1, 2, 3, 4, 5, 6이고, 
주어진 연산자가 덧셈(+) 2개, 뺄셈(-) 1개, 곱셈(×) 1개, 나눗셈(÷) 1개인 경우에는 총 60가지의 식을 만들 수 있다
'''

from itertools import permutations

n = int(input())
num_list = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

op = []
op += ['+'] * add
op += ['-'] * sub
op += ['*'] * mul
op += ['%'] * div

# 연산자의 모든 경우의 수 구하기
operators = []
for i in list(permutations(op)):
    operators.append(i)
# 중복을 피하기 위해서(시간초과 위험)
operators = list(set(operators))

res_list = []
for i in operators:
    # 첫번째 값 
    res = num_list[0]
    # n : 숫자 개수, n-1 : 연산자 개수
    for j in range(n-1):
        # 현재 수와 그 다음 수의 연산 실행
        if i[j] == '+':
            res += num_list[j+1]
        elif i[j] == '-':
            res -= num_list[j+1]
        elif i[j] == '*':
            res *= num_list[j+1]
        else:
            # 음수 나누기 일 때
            if res < 0:
                res = -(-res // num_list[j+1])
            else:
                res //= num_list[j+1]
    res_list.append(res)
        
print(max(res_list))
print(min(res_list))
