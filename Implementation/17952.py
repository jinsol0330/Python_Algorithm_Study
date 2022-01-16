'''
과제는 끝나지 않아!
'''

from sys import stdin

N = int(stdin.readline())
assignments = []
res = 0

for _ in range (N):
    info = list(map(int, stdin.readline().split()))
    # 과제가 있다면 스택에 삽입
    if info[0] == 1:
        assignments.append([info[1], info[2]])
    
    # 과제 해결
    if assignments:
        # 시간 -1
        assignments[-1][1] -= 1 
        # 과제를 다 했을 경우
        if assignments[-1][1] == 0:
            res += assignments[-1][0]
            assignments.pop()

print(res)

