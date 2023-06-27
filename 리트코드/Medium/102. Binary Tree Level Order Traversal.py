'''
시간복잡도 O(n) why? 반복문이 중첩되어 있으나, 결국에는 모든 노드를 한번씩만 방문하는 것이기 때문이다.
공간복잡도 O(n) why? 공간복잡도는 '큐에 저장되는 노드의 수'에 의해 결정된다
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:  # Tree # Breadth-First Search # Binary Tree
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result, queue = [], deque([root])

        while queue:
            cur_level_vals = [] # 현재 레벨의 val 리스트
            for i in range(len(queue)):  # 현재 레벨의 노드 개수
                cur_node = queue.popleft()  # 큐에서 노드를 꺼냄
                cur_level_vals.append(cur_node.val)  # val 저장
                if cur_node.left:
                    queue.append(cur_node.left)  # left 노드 저장
                if cur_node.right:
                    queue.append(cur_node.right)  # right 노드 저장
            result.append(cur_level_vals)

        return result  # 레벨의 개수