class Solution:
    def twoSum(self, nums: list[int], target = int) -> list[int]:
        diff = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in diff:
                return diff[complement], i
            diff[num] = i
        return []
    """
        Question: https://leetcode.com/problems/two-sum/
        Time complexity: O(n)
        Space complexity: O(n)
    """