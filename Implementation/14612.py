'''
김식당
'''

from sys import stdin

N, M = map(int, stdin.readline().split())
order_info = []
for _ in range(N):
    word_info = input().split()

    if word_info[0] == "order":
        # [[time, table].....]
        order_info.append([int(word_info[2]), int(word_info[1])])

    elif word_info[0] == "sort":
        # 시간을 기준으로 오름차순 정렬
        order_info.sort()

    elif word_info[0] == "complete":
        for index, words in enumerate(order_info):
            # words[0] = 시간 정보, words[1] = 테이블 정보, word_info[1] = 입력받은 테이블 번호
            if words[1] == int(word_info[1]):
                order_info.pop(index)
                break

    if len(order_info) == 0:
        print("sleep")
    else:
        for time, table in order_info:
            print(table, end=' ')
        print()
