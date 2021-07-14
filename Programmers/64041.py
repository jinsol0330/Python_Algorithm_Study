'''
크레인 인형뽑기

1. move의 원소들을 따라 차례로 보면서 그에 해당하는 board의 열을 확인
2. 그 board의 열에서 제일 위에 존재하는(맨 처음 존재하는) 0이 아닌 수를 꺼내서 바구니에 저장
3. board의 해당 위치를 다시 0으로 채움
4. 바구니에서(원소가 2개 이상일 때부터) 제일 위의 원소와 그 바로 아래의 원소를 비교해서,
같으면 결과값 1 증가하고 같은 원소 두개를 지움
'''

board = [[0,0,0,0,0],
         [0,0,1,0,3],
         [0,2,5,0,1],
         [4,2,4,4,2],
         [3,5,1,3,1]]

moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    answer = 0
    box = []
    for m in moves:
        # 해당 열을 기준으로 하나씩 탐색
        for i in range(len(board)):
            # moves안의 원소들이 실제 인덱스보다 1이 크므로 이에 맞게 1만큼 작게 처리
            # 해당 원소가 0이 아닌 수라면(=인형이 들어있다면)
            if board[i][m-1] != 0:
                # 바구니에 그 인형을 넣고
                box.append(board[i][m-1])
                # board의 해당 위치를 0으로 바꿔줌
                board[i][m-1] = 0
                break
            else:
                continue

        # 만약 바구니에 들어있는 인형의 개수가 2개 이상이라면
        if len(box) > 1:
            # 가장 위에 있는 원소와 그 바로 아래의 원소가 같다면 
            if box[-1] == box[-2]:
                box.pop(-1)
                box.pop(-1)
                answer += 2
    return answer