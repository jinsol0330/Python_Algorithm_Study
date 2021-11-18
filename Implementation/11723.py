'''
집합
'''


from sys import stdin

M = int(stdin.readline())
S = set()

for _ in range(M):
    my_input = stdin.readline().strip().split()

    if len(my_input) == 1:  # all, empty 인 경우
        if my_input[0] == "all":  # all : S를 {1, 2, ..., 20} 으로 바꾼다.
            S = set([i for i in range(1, 21)])
        else:  # empty : S를 공집합으로 바꾼다.
            S = set()

    else:
        op, num = my_input[0], my_input[1]
        num = int(num)
        if op == "add":  # add x: S에 x를 추가한다. S에 x가 이미 있는 경우에는 연산을 무시한다.
            S.add(num)
        elif op == "remove":  # remove x: S에서 x를 제거한다. S에 x가 없는 경우에는 연산을 무시한다.
            if num in S:
                S.remove(num)
            else:
                continue
        elif op == "check":  # check x: S에 x가 있으면 1을, 없으면 0을 출력한다.
            if num in S:
                print(1)
            else:
                print(0)
        elif op == "toggle":  # toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다.
            if num in S:
                S.remove(num)
            else:
                S.add(num)
