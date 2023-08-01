import random

members = ['박필', '요한', 'gogoodcode', '새우', '지니', '잡아라', '김밥', 'ㅎㅇㄹ']
presentation = [
    'https://leetcode.com/problems/merge-two-sorted-lists/?envType=featured-list&envId=top-interview-questions',
    'https://leetcode.com/problems/unique-paths/?envType=featured-list&envId=top-interview-questions',
    'https://leetcode.com/problems/excel-sheet-column-number/?envType=featured-list&envId=top-interview-questions'
]

random.shuffle(members)
random.shuffle(presentation)
print(members)
print(presentation)
print(random.choice(members))  # 추가 문제 배분
