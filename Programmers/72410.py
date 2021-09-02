'''
신규 아이디 추천
'''

def solution(new_id):
    answer = ''

    # 조건1
    new_id = new_id.lower()

    # 조건2
    for i in new_id:
    	if i.isalnum() or i == '-' or i == '_' or i == '.':
            answer += i

    # 조건3
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 조건4
    while answer[0] == '.' or answer[-1] == '.':
        answer = answer.strip('.')
        # .. 이 입력된 경우 고려해줘야 함(여기서 헤맸다ㅎ)
        if len(answer) == 0:
            answer += 'a'

    # 조건5
    if len(answer) == 0:
        answer += 'a'

    # 조건6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # 조건7
    if len(answer) < 3:
        while len(answer) < 3:
            answer += answer[-1]

    return answer