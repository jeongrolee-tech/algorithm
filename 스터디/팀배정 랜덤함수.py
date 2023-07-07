import random

members = ['누리', '박필', '요한', 'gogoodcode', '새우', '지니', '잡아라', '김밥', 'ㅎㅇㄹ']
presentation = [
    'https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/?envType=featured-list&envId=top-interview-questions',
    'https://leetcode.com/problems/majority-element/?envType=featured-list&envId=top-interview-questions',
    'https://leetcode.com/problems/top-k-frequent-elements/?envType=featured-list&envId=top-interview-questions'
]

random.shuffle(members)
random.shuffle(presentation)
print(members)
print(presentation)
print(random.choice(members))  # 추가 문제 배분
