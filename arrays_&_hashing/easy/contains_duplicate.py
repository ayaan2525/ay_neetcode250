class Solution:
    def hasDuplicate(Self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen:
                return True
            seen[num] = 1
        return False
    
"""
        Question: https://leetcode.com/problems/contains-duplicate/
        Time complexity: O(n)
        Space complexity: O(n)
"""
