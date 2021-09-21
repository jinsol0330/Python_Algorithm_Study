'''
로또의 최고 순위와 최저 순위 (Level1)
'''

def solution(lottos, win_nums):
    answer = [0, 0]
    rank = [6, 6, 5, 4, 3, 2, 1]
    cnt = 0
    cnt_zero = lottos.count(0)

    for lotto in lottos:
        if lotto in win_nums:
            cnt += 1
    answer[0], answer[1] = rank[cnt+cnt_zero], rank[cnt]

    return answer
