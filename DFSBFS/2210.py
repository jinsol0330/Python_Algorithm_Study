'''
숫자판 점프

5×5 크기의 숫자판이 있다. 
각각의 칸에는 숫자(digit, 0부터 9까지)가 적혀 있다. 
이 숫자판의 임의의 위치에서 시작해서, 인접해 있는 네 방향으로 다섯 번 이동하면서, 각 칸에 적혀있는 숫자를 차례로 붙이면 6자리의 수가 된다. 
이동을 할 때에는 한 번 거쳤던 칸을 다시 거쳐도 되며, 0으로 시작하는 000123과 같은 수로 만들 수 있다.
숫자판이 주어졌을 때, 만들 수 있는 서로 다른 여섯 자리의 수들의 개수를 구하는 프로그램을 작성하시오.
'''

'''
중복이 있어서는 안 됨, 000100도 숫자로 취급해야 하므로 문자로 변환해서 더해줌
길이가 6이 될 때 까지 그래프를 탐색하면서 문자열을 만들고, 
길이가 6이 되면 중복을 제거하고(set()사용) 결과값에 넣어준다.
'''
from sys import stdin

def make_num(x,y,s):
    s += str(num_board[x][y])
    case = [[-1,0],[1,0],[0,-1],[0,1]]
    # 문자열 길이가 6이면 즉시 리턴
    if len(s) == 6:
        res_list.append(s)
        return 
    for c in range(4):
        newx, newy = x+case[c][0], y+case[c][1]
        # 범위확인
        if 0 <= newx < 5 and 0 <= newy < 5:
            make_num(newx,newy,s)

res_list = []
num_board = []
for _ in range(5):
    b = list(map(int,stdin.readline().split()))
    num_board.append(b)

for row in range(5):
    for col in range(5):
        s = ''
        make_num(row,col,s)

# 중복 제거
res_list = set(res_list)
print(len(res_list))