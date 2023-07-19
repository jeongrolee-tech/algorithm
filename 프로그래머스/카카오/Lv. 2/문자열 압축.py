'''
# 문자열 압축

- 풀이
    - 한줄평
        - 난이도 쉬움에 속하는 구현 문제인듯 하다
    - 접근방법
        - 키워드
            - 압축
            - 카운트
            - 문자열 분할
    - 시간복잡도
        - O(n^2)
            - 바깥쪽 for문은 절반만 순회하므로 O(n/2) 이고,
            - 안쪽 for문은 s의 전체길이를 순회하므로 O(n) 이다.
            - 따라서 O(n/2 * n) 이고
                - 빅오표기법에 의하면 상수는 무시되므로 O(n^2) 이 된다.
    - 공간복잡도
        - O(n)
            - 입력값인 s의 길이에 비례하여 `compressed` 변수의 공간복잡도도 비례하여 증가하므로 O(n) 이다.
- 코드
'''
'''
https://school.programmers.co.kr/learn/courses/30/lessons/60057
* 문자열의 길이의 '절반까지만' 단위를 증가시키며 반복합니다. 왜냐하면 문자열의 절반을 넘어가면 압축이 불가능하기 때문입니다.
* 잘라낸 문자열이 전에 잘라낸 문자열과 같으면 카운트를 증가시키고, 다르면 추가 한다
시간복잡도 O(n^2)
공간복잡도 O(n)
'''


def solution(s):
    answer = len(s)

    for step in range(1, answer//2 + 1):  # 각 단위 부분 문자열에 대해
        compressed = ''  # 압축 문자열
        prev = s[0:step]  # 부분 문자열
        count = 1  # 카운트

        for j in range(step, len(s), step):  # 반복되는 횟수 카운트 & 압축
            if prev == s[j:j+step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev  # 압축
                prev = s[j:j+step]  # prev 갱신
                count = 1  # 카운트 초기화

        compressed += str(count) + prev if count >= 2 else prev  # 압축
        answer = min(answer, len(compressed))

    return answer
