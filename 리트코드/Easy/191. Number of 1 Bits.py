'''
https://leetcode.com/problems/number-of-1-bits/
시간복잡도 방법1. O(Hamming Weight) 방법2. O(log n)
공간복잡도 O(1)
'''


class Solution:  # Divide and Conquer # Bit Manipulation
    def hammingWeight(self, n: int) -> int:
        # 방법1
        count = 0
        while n:
            n &= n-1
            count += 1
        return count

        # 방법2
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count
