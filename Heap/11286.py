'''
절댓값 힙
절댓값 힙은 다음과 같은 연산을 지원하는 자료구조이다.
    배열에 정수 x (x ≠ 0)를 넣는다.
    배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 
    절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
    프로그램은 처음에 비어있는 배열에서 시작하게 된다.
'''
import heapq
from sys import stdin

n = int(stdin.readline())
heap = []

for i in range(n):
    data = int(stdin.readline())
    # 입력받은 데이터가 0이면
    if data == 0:
        if heap:
            # heappop() 함수를 통해 원소 삭제
            # 기본적으로 heapq 모듈은 최소힙 기능으로 동작
            # [0] = 절대값, [1] = 실제 데이터
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    # 0이 아니면 heap에 데이터 추가
    else:
        '''
        heappush() 함수를 사용할 때 첫 번째 인자로는 삽입할 리스트, 
        두 번째 인자로는 튜플을 사용할 경우 
        튜플의 첫 번째 항목을 기준으로 우선순위를 가지게 됨
        '''
        res = (abs(data), data)
        heapq.heappush(heap, res)

