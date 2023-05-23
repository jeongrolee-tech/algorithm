'''
https://leetcode.com/problems/single-number/
시간복잡도 O(n)
공간복잡도 O(1)
'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        compare_with_me = 0  # 만약 값이 바뀌면 그것이 유일한 수 그 자체

        for num in nums:
            compare_with_me ^= num

        return compare_with_me
