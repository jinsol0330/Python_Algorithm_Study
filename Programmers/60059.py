'''
자물쇠와 열쇠
'''

def rotate(key):
    return list(zip(*key[::-1]))

def check(board, key, row, col, K, L):
    # board에 키 값 넣기
    for i in range(K):
        for j in range(K):
            board[row+i][col+j] = key[i][j]
    '''
    정ㄴ말 저는 바보입니다..
    모르겠슴니다....T-T
    저는 멍청이입니다..........

    '''
    

def solution(key, lock):
    K = len(key)
    L = len(lock)

    board = [[0] * (K*2 + L - 2) for _ in range(K*2 + L - 2)]
    
    # Lock을 board의 정중앙에 놓기
    for i in range(L):
        for j in range(L):
            board[K-1+i][K-1+j] = lock[i][j]
    
    # 90도 회전 4번 실행
    for _ in range(4):
        key = rotate(key)
        for row in range(K+L-1):
            for col in range(K+L-1):
                if check(board, key, row, col, K, L):
                    return True

    return False
    

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
rock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, rock))