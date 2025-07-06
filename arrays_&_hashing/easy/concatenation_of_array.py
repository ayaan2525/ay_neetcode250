class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        length = len(nums)
        result = [0] * 2*length

        for i in range(length):
            result[i] = nums[i]
            result[i+length] = nums[i]
        return result
    
"""
Question: https://leetcode.com/problems/concatenation-of-array/
Time complexity: O(n
Space complexity: O(n)
"""