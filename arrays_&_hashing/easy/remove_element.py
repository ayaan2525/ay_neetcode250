class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        first_pointer = 0
        initial_len = len(nums)

        for i in range(len(nums)):
            if nums[i] == val:
                continue
            else:
                nums[first_pointer] = nums[i]
                first_pointer += 1

        return first_pointer

"""
Question: https://leetcode.com/problems/remove-element/
Time Complexity: O(n), where n is the length of nums.
Space Complexity: O(1)
"""


