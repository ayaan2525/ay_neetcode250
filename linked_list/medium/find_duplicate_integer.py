class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # Using the input list as a hash map to track visited integers
        # value at each index will be negative if that index has been visited
        # If we encounter a negative value, it means we've seen that index before, return it
        for i in range(len(nums)):

            n = abs(nums[i])            
            if nums[n] < 0:
                return n
            nums[n] = -1 * nums[n]
"""
Question: https://leetcode.com/problems/find-the-duplicate-number/
Time Complexity: O(n), where n is the length of the input list nums.
Space Complexity: O(1), no extra space is used.
"""