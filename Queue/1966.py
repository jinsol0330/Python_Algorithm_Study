'''
상근이는 새로운 프린터기 내부 소프트웨어를 개발하였는데, 이 프린터기는 다음과 같은 조건에 따라 인쇄를 하게 된다.

현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 
이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
예를 들어 Queue에 4개의 문서(A B C D)가 있고, 중요도가 2 1 4 3 라면 C를 인쇄하고, 
다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.

현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내라
'''

testcase = int(input())

for i in range(testcase):
    n, m = map(int, input().split())
    p = list(map(int,input().split()))
    # 문서위치 확인용 리스트 생성
    target = [0] * n
    target[m] = 1
    
    res = 0
    
    while True:
        # 첫번째 원소가 가장 큰 우선순위를 가진다면
        if p[0] == max(p):
            res += 1
            # 해당 원소가 타켓 원소라면
            if target[0] == 1:
                print(res)
                break
            else:
                # 인쇄
                del p[0]
                del target[0]
        # 우선순위가 가장 크지 않다면
        else:
            # 그 값을 리스트 가장 뒤로 재배치
            p.append(p[0])
            target.append(target[0])
            # 맨 앞에 있는 값은 즉시 삭제
            del p[0]
            del target[0]
