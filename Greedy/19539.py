'''
사과나무
- 물뿌리개 2개가 있음 
- 한 물뿌리개는 나무 하나를 1만큼 성장시키고, 다른 물뿌리개는 나무 하나를 2만큼 성장
- 이 물뿌리개들은 동시에 사용해야 하며, 물뿌리개를 나무가 없는 토양에 사용할 수는 없음 
- 두 물뿌리개를 한 나무에 사용하여 3만큼 키울 수도 있음
- 두 물뿌리개를 이용해 갊자가 알려준 사과나무의 배치를 만들 수 있는지의 여부를 판단
'''

from sys import stdin

N = int(stdin.readline())
apple_trees = list(map(int, stdin.readline().split()))

turn = sum(apple_trees) // 3

if sum(apple_trees) % 3 != 0:
    print('NO')
    
else:
    for apple in apple_trees:
        turn -= (apple // 2)
        
    if turn > 0:
        print('NO')
    else:
        print('YES')