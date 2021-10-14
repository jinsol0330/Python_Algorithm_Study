'''
후보 추천하기
'''

from sys import stdin

# 사진틀 개수
n = int(stdin.readline())
# 총 추천 횟수
m = int(stdin.readline())
students = list(map(int, stdin.readline().split()))

# 사진틀 리스트
pic = []
# 추천횟수 리스트
pic_num = []

for s in students:
    if s in pic:
        # 인덱스 저장
        i = pic.index(s)
        # 그 인덱스를 가진 학생의 추천수 1 증가
        pic_num[i] += 1
    else:
        # 사진틀이 다 찼다면
        if len(pic) >= n:
            # 추천수가 가장 적은 학생
            tmp = min(pic_num)
            i = pic_num.index(tmp)
            del pic[i]
            del pic_num[i]

        # 새로추가
        pic.append(s)
        # 새로운 학생의 추천수(1부터)
        pic_num.append(1)

# 오름차순 정리
pic.sort()
for i in pic:
    print(i, end = ' ')
