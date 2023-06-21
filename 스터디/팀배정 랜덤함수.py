import random

members = ['river', 'Tommy_Kim', '누리', '박필', '코난', 'gogoodcode', '우영']
presentation = [
    'https://school.programmers.co.kr/learn/courses/30/lessons/17683',
    'https://school.programmers.co.kr/learn/courses/30/lessons/60058',
    'https://school.programmers.co.kr/learn/courses/30/lessons/64062',
]

random.shuffle(members)
random.shuffle(presentation)
print(members)
print(presentation)
print(random.choice(members))  # 추가 문제 배분
