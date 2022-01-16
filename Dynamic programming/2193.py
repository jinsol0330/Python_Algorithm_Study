'''
이친수

0과 1로만 이루어진 수를 이진수라 한다. 
이러한 이진수 중 특별한 성질을 갖는 것들이 있는데, 이들을 이친수(pinary number)라 한다. 이친수는 다음의 성질을 만족한다.
    -> 이친수는 0으로 시작하지 않는다.
    -> 이친수에서는 1이 두 번 연속으로 나타나지 않는다. 
    즉, 11을 부분 문자열로 갖지 않는다.
    
[1, 1, 2, 3, 5, 8, 13 .....]
-> 앞에 두 수를 더한 값이 다음 수가 됨
'''

from sys import stdin

N = int(stdin.readline())

dp_table = [1, 1]

# N(1 ≤ N ≤ 90)
for idx in range(2, 90):
    dp_table.append(dp_table[idx-1] + dp_table[idx-2])
    
print(dp_table[N-1])