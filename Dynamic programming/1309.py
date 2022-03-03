'''
동물원
- 어떤 동물원에 가로로 두칸 세로로 N칸인 아래와 같은 우리가 있음
- 이 동물원에는 사자들이 살고 있는데 사자들을 우리에 가둘 때, 가로로도 세로로도 붙어 있게 배치할 수는 없음
- 2*N 배열에 사자를 배치하는 경우의 수가 몇 가지인지를 알아내는 프로그램을 작성

'''

from sys import stdin

N = int(stdin.readline())
dp_table = [1] * (N + 1)
dp_table[1] = 3

if N == 1:
    print(dp_table[1])
else:
    for idx in range(2, N + 1):
        '''
        N이 idx 일 때,
        1. N이 idx인 row에는 사자가 없고 idx-1인 row에만 있는 경우
            - N이 idx-1일 경우의 수와 같음 : dp_table[idx-1]
        2. N이 idx-1인 row에는 사자가 없고 idx인 row에만 있는 경우
            - N이 idx-2인 경우의 수의 두배 : dp_table[idx-2] * 2
        3. N이 idx인 row와 idx-1인 row에 한마리씩 있는 경우
            - N이 idx-1인 경우와 idx-2인 경우의 차이 : dp_table[idx-1] - dp_table[idx-2]
        '''
        dp_table[idx] = (dp_table[idx - 2] + (dp_table[idx - 1] * 2)) % 9901
    print(dp_table[N])