'''
https://school.programmers.co.kr/learn/courses/30/lessons/67258
'''
# 투 포인터 # O(n)
from collections import defaultdict


def solution(gems):
    uni_gems = set(gems)  # 모든 보석 종류 목록
    counter = defaultdict(int)  # 보석 갯수 카운팅
    start, end = 0, 0  # 투 포인터
    shortest_start, shortest_val = 0, float('inf')  # 무한대(IEEE 754)

    while end < len(gems):
        counter[gems[end]] += 1  # 보석 담기
        end += 1

        while len(counter) == len(uni_gems):
            if end - start < shortest_val:  # '현재 범위' 와 '이전 범위' 비교 후 갱신
                shortest_val = end - start
                shortest_start = start
            if counter[gems[start]] == 1:  # 보석이 하나 남았을때
                break
            counter[gems[start]] -= 1
            start += 1

    return [shortest_start+1, shortest_start + shortest_val]
