# 브루트포스 # 완전탐색
# 시간복잡도 O(n^2)
# 공간복잡도 O(n)
from itertools import permutations
import re
def solution(expression):
    answer = 0
    nums = list(map(int, re.split(r'\D', expression)))
    opers = re.findall(r'\D', expression)
    # '연산자 우선순위'의 모든 조합 구하기
    p_list = list(permutations(set(opers), len(set(opers))))
    # 연산자, 숫자 계산하면서 소거해 나가기 # 매번 소거하려면 연산자, 숫자 분리를 미리 해두고 복사해서 써야함
    for p in p_list:
        nums_c, opers_c = nums[:], opers[:]
        for o in p:
            while o in opers_c:
                idx = opers_c.index(o)
                nums_c[idx] = eval(f'{nums_c[idx]} {o} {nums_c.pop(idx+1)}')
                opers_c.pop(idx)
        # 해당 조합의 모든 계산이 끝나면 max_val 과 비교하기
        answer = max(abs(nums_c[0]), answer)
    return answer