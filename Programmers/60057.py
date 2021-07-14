'''
문자열 압축

1. 1부터 입력받은 문자열 길이의 절반까지 하나씩 for문을 돌면서 그 수 만큼 문자열을 자른 결과물을 before에 보관
2. 그 이후에 자를 문자열과 현재 문자열이 같은지 비교한다

'''

def solution(s):
    s_list=[]

    '''
    하아.. 엣지케이스의 중요성....*^^*
    여러분은 고려하셨나요? 전 안 해서 고생 꽤나 했답니다^^
    '''
    if len(s) == 1:
        return 1

    # 절반 이상 자르는 경우는 X
    for i in range(1, (len(s)//2)+1):
        res = ''
        # abab = 2ab가 되어야 하므로 0이 아닌 1로 초기화
        cnt = 1
        # 차례로 [0:1]-1개단위, [0:2]-2개단위, [0:3]-3개단위 ...
        before = s[:i]
        # i부터 i만큼 문자를 계속 자름
        # ex_ i=3이면, 위에서 [0:3]까지가 들어있는 before와 밑의 경우를 비교
        for j in range(i, len(s)+i, i):
            if s[j:j+i] == before:
                cnt += 1
            else:
                # 이전과 전혀 연관이 없는 경우에는 결과값에 before를 그대로 넣어줌
                if cnt == 1:
                    res += before
                # 이전까지 연관이 있는 경우가 있었다면, 그 전까지의 before를 cnt와 함께 넣어줌
                else:
                    res = res + str(cnt) + before
                    # cnt 초기화를 해주어야 다시 1부터 셀 수 있음
                    cnt = 1
                # 다음 비교대상 설정
                before = s[j:j+i]

        # 마지막에 남은 문자들 처리
        if cnt == 1:
            res += before
        s_list.append(len(res))
    return min(s_list)

while True:
    s = input()
    res = solution(s)
    print(res)