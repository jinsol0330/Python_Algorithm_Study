'''
안테나

모든 안테나의 거리를 하나하나 다 구했는데 시간초과가 떴다
최소값이 중앙값이라니 ㅋ
허탈하군뇨
'''

from sys import stdin

N = int(stdin.readline())
antennas = list(map(int, stdin.readline().split()))

antennas.sort()

print(antennas[(N-1) // 2])