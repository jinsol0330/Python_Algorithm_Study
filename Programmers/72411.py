'''
메뉴 리뉴얼
'''

from itertools import combinations

def solution(orders, course):
    answer = []
    # course 배열의 크기만큼 딕셔너리 생성
    menus = [ {} for _ in range(11) ]
    for order in orders:
        # 가능한 코스요리만 탐색 
        # 예) course = [2,3,4] 라면 2가지 3가지 4가지 요리로 이루어지는 경우만 탐색
        for cnt in course:
            for comb in combinations(order, cnt):
                # (A,B)와 (B,A)를 같은 경우로 두기 위함 
                comb = sorted(comb)
                new_menu = ''.join(sorted(comb))
                # 메뉴가 이미 있다면 추천횟수 +1
                if new_menu in menus[cnt]:
                    menus[cnt][new_menu] += 1
                # 없다면 추천횟수를 1로
                else:
                    menus[cnt][new_menu] = 1

    for cnt in course:
        tmp = []
        max_res = 0
        for menu, menu_cnt in menus[cnt].items():
            # 추천 횟수가 2이상이고 그 추천횟수가 지금까지 나온 추천횟수보다 더 많다면 메뉴에 추가
            # 무조건 횟수가 2이상이면 추가하는 줄 알고 코드를 짰다가 시간을 많이 버렸음 ㅠ 문제를 잘 읽어야 겠다ㅠ
            if menu_cnt >= 2 and max_res < menu_cnt:
                max_res = menu_cnt
                tmp = [menu]
            # 추천 횟수가 같다면 함께 메뉴에 추가
            elif max_res == menu_cnt:
                tmp.append(menu)
        answer += tmp
        
    # 오름차순 정렬
    answer.sort()
    return answer