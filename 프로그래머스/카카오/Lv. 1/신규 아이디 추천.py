'''
시간복잡도 O(n)
공간복잡도 O(n)  # 만약 list(자료구조) 를 사용했다면 O(1) 도 가능했을 것이지만, 문자열은 immutable(불변성) 이므로 O(n) 이다.
https://school.programmers.co.kr/learn/courses/30/lessons/72410

'''
import re


def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    # 2단계
    new_id = ''.join(re.findall(r'[0-9a-z-_.]', new_id))
    # 3단계
    new_id = re.sub(r'\.{2,}', '.', new_id)
    # 4단계
    new_id = re.sub(r'(^\.|\.$)', '', new_id)
    # 5단계
    if new_id == '':
        new_id = 'a'
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
    new_id = re.sub(r'\.$', '', new_id)
    # 7단계
    if len(new_id) <= 2:
        new_id = new_id.ljust(3, new_id[-1])

    return new_id
