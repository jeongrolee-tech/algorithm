# 시간복잡도 O(n)
# 공간복잡도 O(n)
'''
https://school.programmers.co.kr/learn/courses/30/lessons/67256
numbers 배열의 크기는 1 이상 1,000 이하입니다.
numbers 배열 원소의 값은 0 이상 9 이하인 정수입니다.
'''


def solution(numbers, hand):
    answer = ''
    distance = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
        '*': (3, 0),
        0: (3, 1),
        '#': (3, 2)
    }
    left_pos = distance['*']  # (3,0)
    right_pos = distance['#']  # (3,2)

    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            answer += 'L'
            left_pos = distance[number]
        elif number == 3 or number == 6 or number == 9:
            answer += 'R'
            right_pos = distance[number]
        else:  # 거리계산
            left_distance = abs(
                left_pos[0]-distance[number][0]) + abs(left_pos[1]-distance[number][1])
            right_distance = abs(
                right_pos[0]-distance[number][0]) + abs(right_pos[1]-distance[number][1])
            if left_distance == right_distance:  # 거리가 같으면
                if hand == 'right':
                    answer += 'R'
                    right_pos = distance[number]  # 손위치 갱신
                else:
                    answer += 'L'
                    left_pos = distance[number]  # 손위치 갱신
            else:  # 거리가 다르면
                if left_distance < right_distance:
                    answer += 'L'
                    left_pos = distance[number]  # 손위치 갱신
                else:
                    answer += 'R'
                    right_pos = distance[number]  # 손위치 갱신
    return answer
