'''
https://school.programmers.co.kr/learn/courses/30/lessons/118667
시간복잡도 O(n)
공간복잡도 O(n)
'''

# Greedy(탐욕법) # 투 포인터
# 상한 추정이 핵심
from collections import deque


def solution(queue1, queue2):
    answer = 0
    q1, q2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(q1), sum(q2)

    for i in range(len(q1) * 3):
        if sum1 == sum2:
            return i
        elif sum1 < sum2:
            q1.append(move := q2.popleft())
            sum2 -= move
            sum1 += move
        else:
            q2.append(move := q1.popleft())
            sum1 -= move
            sum2 += move

    return -1
