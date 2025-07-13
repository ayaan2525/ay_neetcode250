class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            # When the target is not found, left ends up pointing to the position 
            # where the target should be inserted.
            return left
        
"""
Question: https://leetcode.com/problems/search-insert-position/
Time complexity: O(log n), binary search reduces the search space by half each time
Space complexity: O(1), no extra space is used
"""
