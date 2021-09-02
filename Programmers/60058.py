'''
괄호 변환
'''
def separate(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
    if len(p) == 0:
        return ""
    # (
    cnt_left = 0  
    # )
    cnt_right = 0  
    
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
    for i in range(len(p)):
        if p[i] == '(':
            cnt_left += 1
        else:
            cnt_right += 1

        if cnt_left == cnt_right:
            '''
            3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
            (왼쪽, 오른쪽 괄호의 개수도 맞고 마지막이 ')'로 끝나면 올바른 문자열)
            '''
            if p[i] == ')':  
                # 문자열 v에 대해 1단계부터 다시 수행합니다. 
                return p[:i + 1] + separate(p[i + 1:])
            # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
            else:  
                return make_correct(p[:i + 1], p[i + 1:])

def make_correct(u, v):
    '''
    4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
    4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
    4-3. ')'를 다시 붙입니다. 
    '''
    tmp = '(' + separate(v) + ')'

    # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 
    u = u[1:-1]
    # 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
    for uu in u:
        if uu == '(':
            tmp += ')'
        else:
            tmp += '('
    return tmp
 
 
def solution(p):
    answer = separate(p)
    return answer
