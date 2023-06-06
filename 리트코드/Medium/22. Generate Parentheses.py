'''
https://leetcode.com/problems/generate-parentheses/description/
시간복잡도 O(2^2n * n)
공간복잡도 O(2^2n * n)
'''
from collections import deque


class Solution:  # String # Dynamic Programming # Backtracking
    def generateParenthesis(self, n: int) -> List[str]:

        # Approach 1: Brute Force
        def isValid(p_string):
            left_count = 0
            for p in p_string:
                if p == '(':
                    left_count += 1
                else:
                    left_count -= 1
                if left_count < 0:
                    return False
            return left_count == 0

        answer = []
        queue = deque([""])

        while queue:
            cur_string = queue.popleft()
            if len(cur_string) == 2 * n:
                if isValid(cur_string):
                    answer.append(cur_string)
                continue
            queue.append(cur_string + ")")
            queue.append(cur_string + "(")

        return answer
