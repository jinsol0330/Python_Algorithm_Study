'''
자원 캐기

로봇은 오른쪽(0,1)이나 아래쪽(1,0)으로만 이동할 수 있으므로,  
현재 있는 곳 기준 왼쪽(0,-1)과 위쪽(-1,0) 중 더 큰 값을 가져와서 현재 있는 곳의 값과 더한다.
'''

from sys import stdin

N, M = map(int, stdin.readline().split())
locate_info = [list(map(int, stdin.readline().split())) for _ in range(N)]

dp_table = [ [0] * M for _ in range(N) ]

dp_table[0][0] = locate_info[0][0]

for row in range(N):
    for col in range(M):
        if row == 0 and col == 0:
            continue
        if row == 0 and col - 1 > 0:
            dp_table[row][col] = dp_table[row][col-1] + locate_info[row][col]
        elif col == 0 and row - 1 > 0:
            dp_table[row][col] = dp_table[row-1][col] + locate_info[row][col]
        # 현재 있는 곳 기준 왼쪽(0,-1)과 위쪽(-1,0) 중 더 큰 값을 가져와서 현재 있는 곳의 값과 더한다.
        else:
            dp_table[row][col] = max(dp_table[row-1][col], dp_table[row][col-1]) + locate_info[row][col]

res = max(map(max, dp_table))
print(res)