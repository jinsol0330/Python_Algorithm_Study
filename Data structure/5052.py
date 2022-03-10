'''
전화번호 목록

- 현재 전화번호의 문자열과 다음 전화번호의 현재 전화번호 길이만큼의 문자열을 비교한다.
- 같으면 일관성이 없는 것이고 다르면 일관성이 있는 것이다.

-> 단순히 포함되었는지만 확인하면 X
-> 이중 포문으로 작성 시 시간초과
'''

from sys import stdin

testcase = int(stdin.readline())

for _ in range(testcase):
    N = int(stdin.readline())
    numbers = [stdin.readline().strip() for _ in range(N)] 
    
    # 오름차순으로 정렬하여 사전순으로 정렬
    numbers.sort() 
    res = True

    for idx in range(len(numbers) - 1):
        # 현재 전화번호[idx]와 다음 전화번호[idx+1] 비교
        # 현재 전화번호 길이만큼 슬라이싱[0:len(numbers[idx])]해서 같은지 비교
        if numbers[idx] == numbers[idx + 1][0:len(numbers[idx])]:
            res = False

    if res == True:
        print("YES")
    else:
        print("NO")