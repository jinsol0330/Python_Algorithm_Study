'''
회문
'''

from sys import stdin

N = int(stdin.readline())
words = [stdin.readline() for _ in range(N)]


def is_pseudo(word, left, right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


def is_palindrome(word):
    left = 0
    right = len(word) - 1
    while left < right:
        # left, right가 같은 경우라면 또 다른 비교를 위해 값 업데이트
        if word[left] == word[right]:
            left += 1
            right -= 1
        # left, right가 같지 않으면 유사회문인지 확인하는 과정 필요
        # 지운다고 생각하지 않고 좌, 우 각각 인덱스를 하나씩 늘려 비교해보면 유사회문인지 판단 가능
        else:
            left_p = is_pseudo(word, left + 1, right)
            right_p = is_pseudo(word, left, right - 1)
            # 둘 중 하나라도 유사회문이라면
            if left_p or right_p:
                return 1
            else:
                return 2
    return 0


for i in range(N):
    print(is_palindrome(words[i]))
