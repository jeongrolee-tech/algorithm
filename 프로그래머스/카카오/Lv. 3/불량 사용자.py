'''
https://school.programmers.co.kr/learn/courses/30/lessons/64064
시간복잡도 O(n!)
공간복잡도 O(n!)
'''
import re
from itertools import permutations

# 풀이 1


def solution(user_id, banned_id):
    result_set = set()
    # comb = ("frodo", "fradi", "crodo")
    for comb in permutations(user_id, len(banned_id)):
        # zip(comb, banned_id) = [("frodo", "fr*d*"), ("fradi", "*rodo"), ("crodo", "......")]
        if all(re.fullmatch(b.replace('*', '.'), u) for b, u in zip(banned_id, comb)):
            result_set.add(tuple(sorted(comb)))
    return len(result_set)

# 풀이 2


def solution(user_id, banned_id):
    result_set = set()
    for comb in permutations(user_id, len(banned_id)):
        if all([all(b[i] == u[i] or b[i] == '*' for i in b) if len(u) == len(b) else False for u, b in zip(comb, banned_id)]):
            result_set.add(tuple(sorted(comb)))
    return len(result_set)
