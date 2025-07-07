from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res = maxCount = 0

        for num in nums:
            count[num] += 1
            if maxCount < count[num]:
                res = num
                maxCount = count[num]
        return res
    
"""
Question: https://leetcode.com/problems/majority-element/
Time Complexity: O(n), where n is the length of nums.
Space Complexity: O(n), for the count dictionary."""