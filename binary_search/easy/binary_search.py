class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

        
"""
Question: https://leetcode.com/problems/binary-search/
Time complexity: O(log n), where n is the number of elements in nums
Space complexity: O(1), no extra space is used
"""