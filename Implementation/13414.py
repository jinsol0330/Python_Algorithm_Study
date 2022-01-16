'''
수강신청
'''

from sys import stdin

K, L = map(int, stdin.readline().split())

students_info = {}

for idx in range(L):
    student = stdin.readline().rstrip()
    # 학번을 키로, 들어온 순서를 값으로 가지는 딕셔너리
    # 중복확인을 하지 않아도 나중에 들어온 값으로 대체됨
    students_info[student] = idx

cnt = 0

# 값(수강신청을 한 순서)을 기준으로 정렬
students_info = sorted(students_info.items(), key = lambda x : x[1])

for student in students_info:
    cnt += 1
    if cnt > K:
        break
    # 학번 출력
    print(student[0])