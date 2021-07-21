'''
연산자 끼워넣기(2)
'''

n = int(input())
num_list = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_res, min_res = -1e9, 1e9

def cal(idx, res, add, sub, mul, div):
    global n, num_list, max_res, min_res
    # 연산자 개수 = n-1개
    # idx가 1부터 시작했으므로 연산자 n개에 대한 계산을 수행했을 때
    if idx == n:
        max_res = max(max_res, res)
        min_res = min(min_res, res)
        return
    if add:
        cal(idx+1, res + num_list[idx], add-1, sub, mul, div)
    if sub:
        cal(idx+1, res - num_list[idx], add, sub-1, mul, div)
    if mul:
        cal(idx+1, res * num_list[idx], add, sub, mul-1, div)
    if div:
        if res < 0:
            cal(idx+1, -((-res) // num_list[idx]), add, sub, mul, div-1)
        else:
            cal(idx+1, res // num_list[idx], add, sub, mul, div-1)

cal(1, num_list[0], add, sub, mul, div)
print(max_res)
print(min_res)





