'''
차이를 최대로

N개의 정수로 이루어진 배열 A가 주어진다. 
이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.

|A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|
'''

from itertools import permutations

n = int(input())
num_list = list(map(int, input().split()))

res_list = list(set(permutations(num_list, n)))

res = -1e9

for i in res_list:
    tmp = 0
    tmp_list = list(i)
    for j in range(len(tmp_list)-1):
        tmp += abs(tmp_list[j]-tmp_list[j+1])
    res = max(res, tmp)
print(res)