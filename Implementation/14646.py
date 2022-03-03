'''
욱제는 결정장애야!!
- 돌림판을 돌리고 돌림판에 걸린 칸을 확인한다.
- 걸린 칸에 스티커가 붙어있지 않다면, 스티커를 하나 붙인다.
- 걸린 칸에 스티커가 붙어있다면, 식단표에 해당하는 메뉴를 적어넣고 그 칸을 제거한다.(스티커도 떼어낸다) 
    욱제의 돌림판은 특별해서 어떤 칸이 제거되면 다음부터는 그 칸에 절대로 멈추지 않는 마법이 걸려있다. (!)
- 모든 칸이 제거될 때 까지 (0, 1, 2)을 반복한다.
-> pypy 성공
'''

from sys import stdin

N = int(stdin.readline())
menus = list(map(int, stdin.readline().split()))
res = 0
check = []

cnt = 0
for menu in menus:
    if menu not in check:  
        # 스티커를 붙임
        cnt += 1
        check.append(menu)
    else:
        # 스티커를 뗌
        cnt -= 1
        
    # 스티커 개수 비교 후 업데이트
    res = max(res, cnt)  

print(res)