'''
실패율 (Level1)
'''

def solution(N, stages):
    # 내림차순 정렬
    stages.sort()

    # 특정 스테이지와 실패율을 저장하는 튜플리스트
    answer = []

    for stage_cnt in range(1, N+1):
        if len(stages) == 0:
            answer.append((stage_cnt, 0))
        else:
            failure = (stages.count(stage_cnt) / len(stages))
            answer.append((stage_cnt, failure))
            # 해당 스테이지 제거
            while stage_cnt in stages:
                stages.remove(stage_cnt)
    
    result = []
    answer.sort(key = lambda x:x[1], reverse = True)

    for a in answer:
        result.append(a[0])
    
    return result




N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))