import random

members = ['박필', '요한', 'gogoodcode', '새우', '지니', '잡아라', '김밥', 'ㅎㅇㄹ']
presentation = [
'https://school.programmers.co.kr/learn/courses/30/lessons/72413',
'https://school.programmers.co.kr/learn/courses/30/lessons/67259',
'https://school.programmers.co.kr/learn/courses/30/lessons/60057'
]

random.shuffle(members)
random.shuffle(presentation)
print(members)
print(presentation)
print(random.choice(members))  # 추가 문제 배분
