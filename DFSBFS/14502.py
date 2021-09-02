'''
연구소
'''

from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]