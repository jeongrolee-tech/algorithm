import random

members = ['river', 'Tommy_Kim', '누리', '박필', '코난', 'gogoodcode', '우영', '자빔', 'kukuru', '김밥']
presentation = [
'https://leetcode.com/problems/group-anagrams/?envType=featured-list&envId=top-interview-questions',
'https://leetcode.com/problems/kth-largest-element-in-an-array/?envType=featured-list&envId=top-interview-questions',
'https://leetcode.com/problems/palindrome-partitioning/?envType=featured-list&envId=top-interview-questions',
'https://leetcode.com/problems/product-of-array-except-self/?envType=featured-list&envId=top-interview-questions',
'https://leetcode.com/problems/binary-tree-level-order-traversal/?envType=featured-list&envId=top-interview-questions'
]

random.shuffle(members)
random.shuffle(presentation)
print(members)
print(presentation)
print(random.choice(members))  # 추가 문제 배분
