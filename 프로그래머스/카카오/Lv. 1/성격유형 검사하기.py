'''
https://school.programmers.co.kr/learn/courses/30/lessons/118666
- 한줄평
    - 쉬운편에 속하는 구현 문제 같다
- 시간복잡도
    - O(n) - 입력값인 survey와 choice 의 길이만큼만 반복문을 수행하기 때문
- 공간복잡도
    - O(1) - 알고리즘을 실행할때 사용하는 메모리의 양이 **입력의 크기와 무관하게 일정**하기 때문
        1. **`cha_idx`**와 **`cho_idx`**는 고정된 크기의 딕셔너리입니다. 입력의 크기와 무관하게 이들의 크기는 변하지 않습니다.
        2. **`survey`**와 **`choices`**는 이미 주어진 입력으로, 이를 위한 추가적인 메모리가 할당되지 않습니다.
        3. 함수 **`final_decision`**과 **`type_decision`** 내에서 사용되는 임시 변수들은 상수 공간을 차지합니다.
        4. 이외에도 반복문에서 사용되는 변수 **`i`**와 **`type`**도 추가적인 공간을 차지하지 않습니다.
'''

def final_decision(cha_idx):
    one = 'R' if cha_idx['R'] >= cha_idx['T'] else 'T'
    two = 'C' if cha_idx['C'] >= cha_idx['F'] else 'F'
    three = 'J' if cha_idx['J'] >= cha_idx['M'] else 'M'
    four = 'A' if cha_idx['A'] >= cha_idx['N'] else 'N'
    return one+two+three+four
def type_decision(s, c):
    type_a, type_b = list(s)
    if c == 4: return min(type_a, type_b)
    elif c >= 5: return type_b
    elif c <= 3: return type_a
def solution(survey, choices):
    cha_idx = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0} # 성격 지표
    cho_idx = {1:3,2:2,3:1,4:0,5:1,6:2,7:3}  # choice 지표
    for i in range(len(survey)):
        type = type_decision(survey[i], choices[i])
        cha_idx[type] += cho_idx[choices[i]]
    return final_decision(cha_idx)