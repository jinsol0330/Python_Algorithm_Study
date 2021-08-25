'''
부등호
'''

from sys import stdin

# 숫자를 추가할 때마다 비교해주는 함수
def compare_num(n1, n2, op):
    print(n1, n2)
    if op == '<':
        if n1 < n2:
            return True
        return False
    else:
        if n1 > n2:
            return True
        return False

def solve(idx, s):
    global max_res, min_res
    # 종료 조건 : 숫자 개수가 K+1개 일 때(부등호 개수가 K이므로)
    if idx == K + 1:
        # 0부터 탐색하기 때문에 뒤에 나오는 조합(?)이 무조건 더 크게 되어있음
        # min_res에 값이 없다면 s를 최소값으로
        if(len(min_res) == 0):
            min_res = s
        # min_res에 값이 있다면 s를 최대값으로 설정
        else:
            max_res = s
        return

    for i in range(10):
        # 해당 숫자를 아직 사용하지 않았다면
        if check[i] == False:
            # idx == 0 조건은 처음 시작할 때(숫자가 0일때를 고려해준 것)
            if idx == 0 or compare_num(s[-1], str(i), operators[idx - 1]) == True:
                check[i] = True
                solve(idx + 1, s + str(i))
                # 조건에 맞지 않았던 수는 다시 False로 바꿔줌
                check[i] = False

K = int(stdin.readline())
operators = list(stdin.readline().split())

# 0~9까지의 수를 사용했는지 체크
check = [False] * 10
max_res = ""
min_res = ""

solve(0, "")

print(max_res)
print(min_res)