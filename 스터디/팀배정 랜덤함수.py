import random

members = ['river', 'Tommy_Kim', '누리', '박필', '코난', 'gogoodcode', '우영']
presentation = [
    'https://leetcode.com/problems/rotate-image/',
    'https://leetcode.com/problems/pascals-triangle/',
    'https://leetcode.com/problems/single-number/',
    'https://leetcode.com/problems/kth-smallest-element-in-a-bst/',
    'https://leetcode.com/problems/fizz-buzz/'
]

random.shuffle(members)
random.shuffle(presentation)
print(members)
print(presentation)
print(random.choice(members))  # 추가 문제 배분
