'''
course에 대한 루프: 이 루프는 course의 크기를 n이라 하면 O(n)의 시간 복잡도를 가집니다.
orders에 대한 루프: 이 루프는 orders의 크기를 m이라 하면 O(m)의 시간 복잡도를 가집니다.
combinations 함수: 이 함수는 최악의 경우, 문자열의 길이를 r이라 하면, O(r^c)의 시간 복잡도를 가집니다 (c는 코스 요리의 크기).
Counter 객체의 생성과 max 함수: 이 부분은 후보들의 갯수를 p라 하면 O(p)의 시간 복잡도를 가집니다.
전체 시간 복잡도 O(n * m * r^c * p)

candidates 리스트: 이 리스트는 모든 가능한 메뉴 조합을 저장합니다. 따라서 공간 복잡도는 모든 가능한 조합의 수, 즉 O(m * r^c)입니다.
counter Counter 객체: 이 객체는 candidates 리스트의 각 원소와 그 빈도수를 저장합니다. 따라서 공간 복잡도는 candidates 리스트와 같습니다.
공간복잡도 O(m * r^c)
'''
from itertools import combinations  # 조합을 구하기 위한 모듈
from collections import Counter  # 각 원소의 출현 빈도를 세기 위한 모듈


def solution(orders, course):
    answer = []

    for c in course:  # 각 코스 요리의 크기(메뉴의 갯수)에 대해
        candidates = []  # 해당 크기의 메뉴 조합을 저장할 리스트
        for order in orders:  # 각 주문에 대해
            for combination in combinations(sorted(order), c):  # 모든 가능한 조합을 찾아
                # 조합을 문자열로 변환하여 candidates에 추가
                candidates.append(''.join(combination))
        counter = Counter(candidates)  # 모든 조합의 출현 빈도를 세어
        if counter:  # 조합이 존재하는 경우
            max_value = max(list(counter.values()))  # 가장 많이 나온 조합의 빈도를 찾아
            if max_value > 1:  # 그 빈도가 1보다 큰 경우
                for k, v in counter.items():  # 모든 조합에 대해
                    if v == max_value:  # 가장 많이 나온 조합을 찾아
                        answer.append(k)  # 결과에 추가
    return sorted(answer)  # 결과를 사전 순으로 정렬하여 반환
