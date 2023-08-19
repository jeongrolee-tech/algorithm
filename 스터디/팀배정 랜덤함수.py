import random
substitutes = ['공부공부', '자빔', '우영', '잡아라', '요한', 'gogoodcode']
members = ['박필', '새우', '지니', '김밥']
presentation = [
    'https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/?envType=featured-list&envId=top-interview-questions',
    'https://leetcode.com/problems/flatten-nested-list-iterator/?envType=featured-list&envId=top-interview-questions',
]

random.shuffle(members)
random.shuffle(presentation)
print(members)
print(presentation)
print(random.choice(members))  # 추가 문제 배분
