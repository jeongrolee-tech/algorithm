'''
https://school.programmers.co.kr/learn/courses/30/lessons/12987
# 숫자 게임 lv3

- 시간복잡도
    - n log n
        - sort 가 사용되었기 때문
- 공간복잡도
    - 1
        - 입력값의 크기와 무관하게 항상 동일한 변수 a_idx, b_idx, answer 3개만 증감연산만 수행하기 때문
'''

# 간결한 답안
# def solution(A, B):
#     A.sort()
#     B.sort()
#     i = 0
#     for b in B:
#         if A[i] < b:
#             i += 1
#     return i


def solution(A, B):
    A.sort()
    B.sort()

    a_idx, b_idx = 0, 0
    answer = 0

    # while a_idx < len(A) and b_idx < len(A):  # O
    while b_idx < len(B):
        if A[a_idx] < B[b_idx]:
            a_idx += 1
            b_idx += 1  # 간과한 부분
            answer += 1
        # elif A[a_idx] > B[b_idx]:  # 두 숫자가 같으면 안넘어가기 때문에 X
            # b_idx += 1
        else:
            b_idx += 1

    return answer
